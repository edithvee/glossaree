import json


class Entry:
    def __init__(self, command, description, *, examples=None, arguments=None):
        self.command = command
        self.description = description

        if examples is not None:
            self.examples = examples
        else:
            self.examples = []

        if arguments is not None:
            self.arguments = arguments
        else:
            self.arguments = []

    def to_json(self):
        return json.dumps(self, indent=2, cls=EntryEncoder)

    def __str__(self):
        return self.to_json()


class EntryEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Entry, Argument, Example)):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Example:
    def __init__(self, command, description):
        self.command = command
        self.description = description


class Argument:
    def __init__(self, argument, description):
        self.argument = argument
        self.description = description

    def __str__(self):
        return f"Argument({self.argument!r}, {self.description!r})"


if __name__ == "__main__":
    entry1 = Entry("git branch -d nm", "delete branch 'nm' (just the label, not the history)")
    print(entry1)

    entry2 = Entry(
        "git diff", "diffs between staging area and working directory",
        arguments=[
            Argument("--staged", "diffs between staging area and repository"),
            Argument("git diff id_a id_b", "diffs between commits (id_a and _b)"),
        ]
    )
    print(entry2)

    for i, arg in enumerate(entry2.arguments):
        print(f'\t{i}:', arg)

    print(entry2.to_json())

