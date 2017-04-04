import click

class GHRepo(click.ParamType):
    name = 'repository'

    def convert(self, value, param, ctx):
        try:
            return ctx.obj.repository(value)
        except ValueError:
            self.fail('Invalid GitHub URL: ' + value, param, ctx)
