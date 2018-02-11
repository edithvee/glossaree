from pathlib import Path

import click

from make_entry_interactive import display_entry
from model import Entry, Argument, Example


def make_entry(command, description):

    arguments = []
    add_arg = click.confirm('add argument and description?')
    while add_arg:
        arg = click.prompt('give argument')
        desc = click.prompt('give description')
        arguments.append(Argument(arg, desc))
        add_arg = click.confirm('add another argument and description?')

    examples = []
    add_ex = click.confirm('add example and description?')
    while add_ex:
        ex = click.prompt('give example')
        desc = click.prompt('give description')
        examples.append(Example(ex, desc))
        add_ex = click.confirm('add another example and description?')

    entry = Entry(command, description, arguments=arguments, examples=examples)

    return entry


def save_entry(entry, file_name):
    # hard code! hard code!
    directory = Path("/home/edith/PycharmProjects/glossaree!/dictionary")
    directory.mkdir(exist_ok=True)
    path = directory / file_name
    if path.exists():
        save_prompt = 'overwrite existing entry?'
    else:
        save_prompt = 'save entry?'

    if not click.confirm(save_prompt, default=False):
        click.secho('\nnot saved\n', fg='yellow', bold=True)
        return

    path.write_text(entry.to_json())

    print(f'\nsaved to {path}\n')


@click.command()
@click.argument('command')
@click.argument('description')
@click.option('-f', '--filename', help='file name when saving entry')
def main(command: str, description, filename):
    """Creates glossaree entry in json format.

    Asks whether to add argument/s or example/s.
    Checks whether entry already exists and asks whether to save (or overwrite existing)."""
    entry = make_entry(command, description)
    display_entry(entry)

    if not filename:
        filename = command.replace(' ', '_') + '.json'

    save_entry(entry, filename)


if __name__ == '__main__':
    main()
