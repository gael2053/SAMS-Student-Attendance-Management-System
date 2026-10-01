import os

def banner(title):
    line = "=" * 40
    print(f"\n{line}\n {title} \n{line}")


def print_record(record):
    fields = [
        ("Student ID", "id"), ("Student Name", "name"),
        ("Student Section", "section"), ("Subject", "subject"),
        ("Time", "time"), ("Status", "status"),
    ]
    for label, key in fields:
        print(f"{label}: ", record[key])


TABLE_COLUMNS = [
    ("ID", "id", 12),
    ("Name", "name", 18),
    ("Section", "section", 18),
    ("Time", "time", 10),
    ("Status", "status", 8),
]


def print_table_border():
    line = "+"
    for label, key, width in TABLE_COLUMNS:
        line = line + ("-" * (width + 2)) + "+"
    print(line)


def print_table_header():
    print_table_border()
    row = "|"
    for label, key, width in TABLE_COLUMNS:
        cell = " " + label.ljust(width) + " "
        row = row + cell + "|"
    print(row)
    print_table_border()


def print_record_row(record):
    row = "|"
    for label, key, width in TABLE_COLUMNS:
        value = str(record[key])
        cell = " " + value.ljust(width) + " "
        row = row + cell + "|"
    print(row)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")