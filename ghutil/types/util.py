from   abc                 import ABCMeta, abstractmethod
import re
import click
from   ghutil.api.endpoint import GHEndpoint
from   ghutil.showing      import show_fields
from   ghutil.util         import cacheable

class Resource(GHEndpoint, metaclass=ABCMeta):
    """
    An abstract base class for endpoints for major API resource types,
    featuring convenience methods for constructing instances from URLs and
    command-line arguments, a `data` property that makes a GET request to the
    endpoint and caches the result, decorators for click arguments, and some
    other good stuff.

    Instances of concrete subclasses can be constructed from any of four
    different representations:

    - a URL — either a web interface URL, an API URL, or (if applicable) a
      ``git clone`` URL
    - a command-line argument (or "arg") — either a URL or an abbreviated
      representation like ``jwodder/ghutil``
    - a `dict` of the parameters (or "params") parsed from a URL or arg that
      are needed to construct the path to an API endpoint
    - a `dict` of raw data retrieved from the GitHub API

    Besides the abstract methods, concrete subclasses are expected to include
    the following:

    - A ``URL_REGEXES`` class attribute providing a list of regular expressions
      that together match all possible valid URLs for the resource type; each
      regex should contain named capture groups that will be used to extract
      params

    - An ``ARGUMENT_REGEXES`` class attribute providing a list of regular
      expressions that match non-URL args.  Some argument formats (e.g., those
      containing local repository paths) may require more than just regex
      matching in order to obtain the necessary params; these should be handled
      by overriding `parse_arg` in the subclasses.

    - A ``DISPLAY_FIELDS`` class attribute that will be passed to `show_fields`
      in order to non-verbosely JSONify instances

    - A `__str__` method that returns an object's "display name" for output

    - `cacheable` properties for the type's parameters that use the `data`
      attribute to fill in values that were not present in the constructor
      arguments (e.g., if a `Release` is constructed from a URL containing only
      a repository and a tag name, the ``id`` property can still be accessed to
      acquire the missing parameter)
    """

    def __init__(self, gh, params=None, data=None):
        """
        :param GitHub gh: the `GitHub` instance providing the underlying
            `requests.Session` object

        :param dict params: Parameters extracted from a URL or command-line
            argument, used to construct the path to the API endpoint.
            Non-`None` items in ``params`` will be copied to the new instance.

        :param dict data: Raw data retrieved from the GitHub API.  When
            non-`None`, ``data`` must contain a ``"url"`` key mapping to the
            resource's API URL, and the instance's `data` property will be
            initialized to ``data``.  If both ``params`` and ``data`` are
            non-`None`, ``params`` will be ignored.

        :raises TypeError: if both ``params`` and ``data`` are `None`
        """
        if data is not None:
            path = (data["url"],)
            self.data = data
        elif params is not None:
            path = self.params2path(gh, params)
            for k,v in params.items():
                if v is not None:  # Don't set unknown parameters
                    setattr(self, k, v)
        else:
            raise TypeError('At least one of data and params must be non-None')
        super().__init__(gh.session, *path)

    @cacheable
    def data(self):
        """
        The data returned by a GET request to the resource's API endpoint,
        fetched on demand and cached
        """
        return self.get()

    @classmethod
    @abstractmethod
    def params2path(cls, gh, params):
        """
        Convert a "params" dict to the sequence of URL path components for the
        API endpoint of the resource so described.

        This method may modify ``params`` in order to supply missing values
        (e.g., when only the name of a repository is specified, the owner may
        be set to the name of the current user).

        :type gh: GitHub
        :type params: dict
        :return: sequence of `str` and/or `int` values
        """
        pass

    @classmethod
    @abstractmethod
    def default_params(cls):
        """
        Returns a "params" dict for the resource type's default value (e.g.,
        for repositories, the GitHub remote for the current directory's
        repository).  Types which do not have a default value should set this
        method to `None`.

        :rtype: dict
        """
        pass

    @classmethod
    def parse_url(cls, url):
        """
        Convert a URL to a "params" dict by testing against each of the regular
        expressions in ``URL_REGEXES`` until one matches.

        :type url: str
        :rtype: dict
        :raises ValueError: if no regular expression matched
        """
        for rgx in cls.URL_REGEXES:
            d = typed_match(rgx, url)
            if d is not None:
                return d
        raise ValueError(url)

    @classmethod
    def parse_arg(cls, arg):
        """
        Convert a command-line argument to a "params" dict by testing against
        each of the regular expressions in ``ARGUMENT_REGEXES`` and then
        ``URL_REGEXES`` until one matches.

        :type arg: str
        :rtype: dict
        :raises ValueError: if no regular expression matched
        """
        for rgx in cls.ARGUMENT_REGEXES:
            d = typed_match(rgx, arg)
            if d is not None:
                return d
        return cls.parse_url(arg)

    @classmethod
    def from_url(cls, gh, url):
        """ Construct a resource instance from a `GitHub` instance and a URL """
        return cls.from_params(gh, cls.parse_url(url))

    @classmethod
    def from_arg(cls, gh, arg):
        """
        Construct a resource instance from a `GitHub` instance and a
        command-line argument
        """
        return cls.from_params(gh, cls.parse_arg(arg))

    @classmethod
    def from_params(cls, gh, params):
        """
        Construct a resource instance from a `GitHub` instance and a "params"
        dict
        """
        return cls(gh, params=params)

    @classmethod
    def from_data(cls, gh, data):
        """
        Construct a resource instance from a `GitHub` instance and a `dict` of
        raw data retrieved from the GitHub API
        """
        return cls(gh, data=data)

    @classmethod
    def default(cls, gh):
        """
        Construct the resource type's default value from a `GitHub` instance

        :raises TypeError: if `default_params` is `None`
        """
        return cls.from_params(gh, cls.default_params())

    @classmethod
    def argument(cls, name, implicit=True):
        """
        A `click.argument` decorator that converts command-line arguments to
        instances of the class.  If ``implicit`` is `True` and `default_params`
        is not `None`, the resource type's default value will be used as the
        argument's default value.
        """
        if implicit and cls.default_params is not None:
            return click.argument(
                name,
                type=ResourceParamType(cls),
                default=cls.default_params,
            )
        else:
            return click.argument(name, type=ResourceParamType(cls))

    @classmethod
    def argument_list(cls, name):
        """
        A `click.argument` decorator that accepts zero or more command-line
        arguments and converts them all to instances of the class.  If
        `default_params` is not `None`, an empty argument list will be
        defaulted to the resource type's default value.
        """
        if cls.default_params is not None:
            def callback(ctx, param, value):
                return value or [cls.default(ctx.obj)]
        else:
            callback = None
        return click.argument(
            name,
            'repos',
            type=ResourceParamType(cls),
            nargs=-1,
            callback=callback,
        )

    def for_json(self, verbose=False):
        """
        If ``verbose`` is true, return `data`; otherwise, return only those
        fields of `data` specified by `DISPLAY_FIELDS`.
        """
        if verbose:
            return self.data
        else:
            return show_fields(*self.DISPLAY_FIELDS)(self.data)


class ResourceParamType(click.ParamType):
    def __init__(self, resource_type):
        self.resource_type = resource_type
        ### TODO: Set `self.name`?

    def convert(self, value, param, ctx):
        if isinstance(value, str):
            try:
                return self.resource_type.from_arg(ctx.obj, value)
            except ValueError:
                self.fail(value, param, ctx)
        else:
            # `value` was returned by `default_params()`
            return self.resource_type.from_params(ctx.obj, value)


def typed_match(rgx, s):
    m = re.fullmatch(rgx, s)
    if not m:
        return None
    params = {}
    for k,v in m.groupdict().items():
        if k.startswith('i_'):
            params[k[2:]] = int(v)
        else:
            params[k] = v
    return params
