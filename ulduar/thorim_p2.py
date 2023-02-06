import texttable
import pyperclip


def get_thorim_p2_position_table_header():
    return [ "1", "2", "3", "4", "5", "6", "7", "orange", "green", "purple"]


def get_table(my_data: list[list]):
    table = texttable.Texttable()
    # table formatting settings - one setting per column/row
    table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]) # (l)eft, (r)ight, (c)enter
    table.set_cols_valign(["m", "m", "m", "m", "m", "m", "m", "m", "m", "m"]) # (t)op, (m)iddle, (b)ottom
    table.set_max_width(0)
    # add rows here
    table.add_rows(my_data)
    return table.draw()


def get_output(table):
    return "```Thorim P2 Position Assignments:\n" + \
    "\n" + \
    f"{table}\n" + \
    "```\n"


if __name__ == "__main__":
    table_data = [
        get_thorim_p2_position_table_header(),
        # 1, 2, 3, 4, 5, 6, 7, orange, green, purple
        ["shelarenda", "cowboi", "bucs", "beiric", "snowman", "shefth", "giskard", "sordauq", "xinc", "gardenslug"],
        ["ephicus", "healmut", "dorkmistress", "gunnhaver", "derasto", "drubot", "deepee", "flexecute", "stabthebussy", "dreadkill"],
        ["", "", "", "", "", "", "riselyn", "akamashifter", "", "unbrandable"]
    ]

    table = get_table(table_data)
    output = get_output(table)

    print(output)
    pyperclip.copy(output)