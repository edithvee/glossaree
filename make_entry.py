from pathlib import Path

from model import Example, Argument, Entry


def make_entry():
    """"""
    command = input("command: ")
    description = input("description: ")
    
    examples = []
    examples_yesorno = input("add example? y or n: ")
    while examples_yesorno == "y":
        example_command = input("command: ")
        example_description = input("description: ")
        examples.append(Example(example_command, example_description))
        examples_yesorno = input("add another example? y or n: ")
        
    arguments = []
    arguments_yesorno = input("add argument? y or n: ")
    while arguments_yesorno == "y":
        argument = input("argument: ")
        argument_description = input("description: ")
        arguments.append(Argument(argument, argument_description))
        arguments_yesorno = input("add another argument? y or n: ")

    entry = Entry(command, description, examples=examples, arguments=arguments)

    return entry


def display_entry(entry):
    print("Your pretty entry looks as follows:\n")
    print(entry)


def save_entry(entry):
    save_or_not = input("would you like to save this to file? (y or n) ")
    if save_or_not != "y":
        return

    file_name = input("give a file name: ")
    # hard code! hard code!
    directory = Path("/home/edith/PycharmProjects/glossaree!/dictionary")
    directory.mkdir(exist_ok=True)
    path = directory / file_name
    # newfangled:
    path.write_text(entry.to_json())
    # old-school, verbose:
    # f = open(str(path), 'w')
    # try:
    #     f.write(entry.to_json())
    # except Exception:
    #     pass
    # finally:
    #     f.close()
    #
    # standard, less verbose:
    # with open(str(path), 'w') as f:
    #     f.write(entry.to_json())
    print(f"your pretty entry has been saved to:\n{path}")






# def import_entry(tsv_line):
#     return 1
#
#
# if __name__ == "__main__":
#     with open('exampls.tsv') as f:
#         tsv_lines = [line.rstrip() for line in f]
#
#     for line in tsv_lines[0:2]:
#         entry = import_entry(line)
#         print(entry)


if __name__ == "__main__":
    entry = make_entry()
    display_entry(entry)
    save_entry(entry)
