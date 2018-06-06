import argcomplete
import argparse
import json


DOCUMENT_PATH = "/home/vagrant/.coreapi/document.json"
commands = ["repositories", "tasks"]


def client():
    client = argparse.ArgumentParser()
    with open(DOCUMENT_PATH) as doc:
        doc = json.load(doc)
        add_command(client, doc)
    argcomplete.autocomplete(client)
    client.parse_args()


def add_command(parent_parser, metadata):
    subparsers = parent_parser.add_subparsers()

    for action, value in metadata.items():
        if "_" in action:
            continue
        if "_type" in value:
            subparser = subparsers.add_parser(action)

        else:
            subparser = subparsers.add_parser(action)
            add_command(subparser, value)


class CoreCLIAction(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super(CoreCLIAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print("%r %r %r" % (namespace, values, option_string))

        setattr(namespace, self.dest, values)


if __name__ == "__main__":
    client()
