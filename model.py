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

    def __str__(self):
        return self.to_json()

    def to_json(self):
        examples = []
        for example in self.examples:
            examples.append({
                "command": example.command,
                "description": example.description,
            })

        arguments = []
        for argument in self.arguments:
            arguments.append({
                "argument": argument.argument,
                "description": argument.description,
            })

        entry = {
            "command": self.command,
            "description": self.description,
            "examples": examples,
            "arguments": arguments,
        }

        json_entry = json.dumps(entry, indent=2)

        return json_entry


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

