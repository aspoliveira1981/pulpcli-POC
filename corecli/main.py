import click
import coreapi
import json



DOCUMENT_PATH = '/home/vagrant/.coreapi/document.json'
commands= ['repositories', 'tasks']


@click.group(invoke_without_command=True, help='Command line client for interacting with CoreAPI services.\n\nVisit http://www.coreapi.org for more information.')
@click.option('--version', is_flag=True, help='Display the package version number.')
@click.pass_context
def client(ctx, version):

    if ctx.invoked_subcommand is not None:
        return


    click.echo(ctx.get_help())


def add_command(parent_command, name, metadata):

    if '_type' in metadata:
        command = click.Command(name)
    else:
        command = click.Group(name)
        for action, value in metadata.items():
            #import ipdb; ipdb.set_trace()
            add_command(command, action, value)
    parent_command.add_command(command)

            #client.add_command(history)


with open(DOCUMENT_PATH) as doc:
    doc = json.load(doc)
    for action, value in doc.items():
        if not action.startswith('_'):
            add_command(client, action, value)

#for command in commands:
#    add_command(command)


if __name__ == '__main__':
    client()
