import texttable
import pyperclip


def get_thorim_p1_assignments_table_header():
    return [ "Tunnel Group"]


def get_table(my_data: list[list]):
    table = texttable.Texttable()
    # table formatting settings - one setting per column/row
    table.set_cols_align(["c"]) # (l)eft, (r)ight, (c)enter
    table.set_cols_valign(["m"]) # (t)op, (m)iddle, (b)ottom
    table.set_max_width(0)
    # add rows here
    table.add_rows(my_data)
    return table.draw()


def get_output(table):
    return "```Thorim P1 Assignments:\n" + \
    "\n" + \
    f"{table}\n" + \
    "```\n"


if __name__ == "__main__":
    table_data = [
        get_thorim_p1_assignments_table_header(),
        ["glasseater"],
        ["riselyn"],
        ["snowman"],
        ["bucs"],
        ["ephicus"],
        ["deepee"],
        ["drubot"],
        ["shefth"],
        ["cowboi"],
        ["derasto"],
    ]

    table = get_table(table_data)
    output = get_output(table)

    print(output)
    pyperclip.copy(output)