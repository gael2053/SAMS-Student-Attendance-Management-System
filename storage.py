import os

from config import RECORDS_FILE
from UI import banner, clear_screen

records = []

FIELD_ORDER = ["id", "name", "section", "subject", "time", "status"]
DELIMITER = "|"


def load_records():
    records.clear()

    if not os.path.exists(RECORDS_FILE):
        return

    with open(RECORDS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(DELIMITER)
            if len(parts) != len(FIELD_ORDER):
                continue

            record = {}
            for i in range(len(FIELD_ORDER)):
                field_name = FIELD_ORDER[i]
                record[field_name] = parts[i]
            records.append(record)


def save_records():
    with open(RECORDS_FILE, "w") as f:
        for record in records:
            line = ""
            for i in range(len(FIELD_ORDER)):
                field_name = FIELD_ORDER[i]
                line = line + str(record[field_name])
                if i < len(FIELD_ORDER) - 1:
                    line = line + DELIMITER
            f.write(line + "\n")


def clear_saved_records():
    clear_screen()
    banner("CLEAR SAVED RECORDS")
    print("\nThis will permanently delete ALL saved attendance records.")
    confirm = input("Type CONFIRM to proceed, or press Enter to cancel: ").strip()

    if confirm == "CONFIRM":
        records.clear()
        if os.path.exists(RECORDS_FILE):
            os.remove(RECORDS_FILE)
        print("\nAll saved records have been deleted.")
    else:
        print("\nCancelled. No records were deleted.")

    input("\nPress Enter to return to the menu...")