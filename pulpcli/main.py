import click
import click_completion
import json
import urllib.parse as urlparse

from progress.spinner import Spinner

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import Terminal256Formatter

from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client

from time import sleep
from uuid import UUID


DOCUMENT_PATH = "file:///home/vagrant/.pulpcli/document.json"

click_completion.init()
app = App.create(DOCUMENT_PATH, strict=False)
auth = Security(app)

apiclient = Client(auth)


# Install for click-completion
def install_callback(ctx, attr, value):
    if not value or ctx.resilient_parsing:
        return value
    shell, path = click_completion.install()
    click.echo("%s completion installed in %s" % (shell, path))
    exit(0)


@click.group(invoke_without_command=True)
@click.option(
    "--install",
    is_flag=True,
    callback=install_callback,
    expose_value=False,
    help="Install completion for the current shell. Make sure to have psutil installed.",
)
@click.pass_context
def client(ctx):
    if ctx.invoked_subcommand is not None:
        return
    click.echo(ctx.get_help())


def is_uuid4(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False

    return val.hex == uuid_string


def echo_resp(response):
    try:
        body = json.dumps(obj=response, sort_keys=True, ensure_ascii=False, indent=4)
    except ValueError:
        click.secho(response, fg="green")
    else:
        click.echo(highlight(body, JsonLexer(), Terminal256Formatter()))


def apicall(*args, **kwargs):

    ctx = click.get_current_context()
    keys = ctx.command_path.split(" ")[1:]

    params = {k: v for k, v in kwargs.items() if v is not None}

    resp = apiclient.request(app.op[keys[0]]())
    echo_resp(resp.raw.decode('utf8'))

commands = {}
import ipdb; ipdb.set_trace()
for scope_key in app.op.keys():
    for scope in scope_key.split('!##!'):

        client.add_command(click.Command(scope, callback=apicall))




if __name__ == "__main__":
    client()
