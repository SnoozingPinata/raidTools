import texttable
import datetime
import pyperclip


def get_table(my_data: list[list]):
    table = texttable.Texttable()
    # table formatting
    table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]) # (l)eft, (r)ight, (c)enter
    table.set_cols_valign(["m", "m", "m", "m", "m", "m", "m", "m", "m", "m"]) # (t)op, (m)iddle, (b)ottom
    # set width of table
    table.set_max_width(0)
    # add rows here
    table.add_rows(my_data)
    return table.draw()


def get_output(table):
    return "```Thorim Assignments:\n" + \
    "\n" + \
    f"{table}\n" + \
    "```\n" #+ \
    #If this message has a :white_check_mark: reaction by Giskard, it is currently accurate."


if __name__ == "__main__":
    table_data = [
        [ "1", "2", "3", "4", "5", "6", "7", "orange", "green", "purple"],
        ["giskard", "healmut", "ephicus", "derasto", "senorfuego", "shel", "pyro", "flex", "stab", "octane"],
        ["gunnhaver", "riselyn", "dorkmistress", "lazz", "galfor", "shefth", "supus", "sordauq", "xinq", "sharkev"],
    ]

    table = get_table(table_data)
    output = get_output(table)

    print(output)
    pyperclip.copy(output)