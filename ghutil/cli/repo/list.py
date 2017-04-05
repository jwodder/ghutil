import click

@click.command()
@click.pass_obj
def cli(gh):
    """ List your GitHub repositories """
    for repo in gh.user.repos.get():
        print(repo["full_name"])
