from UI import banner, clear_screen
from auth import login
from attendance import mark_attendance, view_full_report
from storage import load_records, save_records, clear_saved_records


def main():
    load_records()

    banner(" STUDENT ATTENDANCE MANAGEMENT SYSTEM ")

    logged_in = False
    for attempt in range(3):
        if login():
            logged_in = True
            break
        print(f" Attempts remaining: {2 - attempt}\n")
    if not logged_in:
        print("Too many failed login attempts. Exiting the program.")
        return

    tasks = {
        "1": mark_attendance,
        "2": view_full_report,
        "3": clear_saved_records,
    }

    while True:
        banner("STUDENT ATTENDANCE MANAGEMENT SYSTEM")
        print("\nMenu: ")
        print("[1] Mark Attendance")
        print("[2] View Attendance Records & Summary")
        print("[3] Clear Saved Records")
        print("[4] Exit")
        choice = input("Select an option: ").strip()

        if choice == "4":
            save_records()
            print("\nExiting Student Attendance Management System. Byebye!")
            break
        elif choice in tasks:
            tasks[choice]()
            clear_screen()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()