from datetime import datetime, timedelta

from config import SECTIONS, SUBJECTS
from UI import banner, print_record, print_table_header, print_record_row, print_table_border, clear_screen
from storage import records, save_records


def get_student_info():
    while True:
        clear_screen()
        banner("MARK ATTENDANCE")
        student_id = input("Enter your student ID: ").strip()
        if not student_id:
            print("Student ID cannot be empty. Try again please.\n")
            input("Press Enter to continue...")
            continue
        break

    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Student name cannot be empty. Try again please.\n")
            input("Press Enter to continue...")
            continue
        break

    return student_id, name


def choose_section():
    while True:
        clear_screen()
        banner("MARK ATTENDANCE")
        print("\nSelect your section: ")
        for key, value in SECTIONS.items():
            print(f" {key}. {value['name']}")
        choice = input("Section: ").strip()

        if choice in SECTIONS:
            return SECTIONS[choice]

        print("Invalid section choice. Try again.\n")
        input("Press Enter to continue...")


def choose_subject():
    while True:
        print("\nSelect your current subject:")
        for key, value in SUBJECTS.items():
            print(f" {key}. {value['name']} ({value['start_hour']:02d}:{value['start_minute']:02d})")
        choice = input("Subject: ").strip()

        if choice in SUBJECTS:
            return SUBJECTS[choice]

        print("Invalid subject choice. Try again.\n")
        input("Press Enter to continue...")


def get_status(check_time, subject):
    class_start = check_time.replace(
        hour=subject["start_hour"], minute=subject["start_minute"], second=0, microsecond=0
    )
    late_limit = class_start + timedelta(minutes=subject["grace_minutes"])
    if check_time <= class_start:
        return "Present"
    elif check_time <= late_limit:
        return "Late"
    else:
        return "Absent"


def mark_attendance():
    student_id, name = get_student_info()
    section = choose_section()
    subject = choose_subject()

    check_time = datetime.now()
    status = get_status(check_time, subject)
    record = {
        "id": student_id, "name": name, "section": section["name"],
        "subject": subject["name"], "time": check_time.strftime("%I:%M %p"),
        "status": status,
    }
    records.append(record)
    save_records()

    clear_screen()
    banner("ATTENDANCE REPORT")
    print_record(record)
    input("\nPress Enter to return to the menu...")


def view_full_report():
    clear_screen()

    if not records:
        print("\nNo attendance records found.\n")
        input("\nPress Enter to return to the menu...")
        return

    banner("ATTENDANCE RECORDS & SUMMARY")

    for key, subj in SUBJECTS.items():
        subj_name = subj["name"]
        subject_records = []
        for r in records:
            if r["subject"] == subj_name:
                subject_records.append(r)

        print(f"\n{subj_name}")
        print("-" * 38)

        if not subject_records:
            print(" No records yet.")
            continue

        print_table_header()
        counts = {"Present": 0, "Late": 0, "Absent": 0}
        for record in subject_records:
            print_record_row(record)
            counts[record["status"]] += 1
        print_table_border()

        print(f" Present: {counts['Present']} "
              f"Late: {counts['Late']}  "
              f"Absent: {counts['Absent']}")

    input("\nPress Enter to return to the menu...")