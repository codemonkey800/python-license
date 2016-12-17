import license.api as api
import click
import click_completion
import os
import os.path as path

from click_didyoumean import DYMGroup

click_completion.init()

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])



@click.group(context_settings=CONTEXT_SETTINGS, cls=DYMGroup)
@click.version_option(None, '-v', '--version')
def main():
    '''Retrieve or list open source licenses.'''

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    '--shell', '-s',
    type=str,
    help='Specify a shell manually.',
)
@click.option(
    '--install', '-i',
    help='Installs shell completions for your current shell.',
    is_flag=True,
)
def shell(shell, install):
    '''Installs or prints shell code for completions.'''
    try:
        if not shell:
            shell = click_completion.get_auto_shell(),
    except click.exceptions.UsageError as e:
        print(e.message)

    if install:
        click_completion.install(shell)
    else:
        click.echo(click_completion.get_code(shell))


@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument('pattern', required=False)
def list(pattern):
    '''Lists and filters all licenses for a match.'''
    lics = api.licenses(pattern)
    for lic in lics:
        print('{0:12} - {1}'.format(lic['key'], lic['name']))


@main.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    '--stdout', '-s',
    help='Print output to stdout',
    is_flag=True,
)
@click.option(
    '--output', '-o',
    type=str,
    help='Outputs into a different file',
    default='LICENSE.md'
)
@click.argument('name', required=False)
def get(name, stdout, output):
    '''Retrieve a license by key or name.'''
    lic = api.license(name)
    if stdout:
        click.echo(str(lic))
        return
    with open(output, 'w') as f:
        f.write(lic)


if __name__ == '__main__':
    main()
