from menu import display_menu

from organizer import organize_files

from summary import show_summary


while True:

    display_menu()

    choice = input("Choose Option: ")

    if choice == "1":

        path = input(
            "Folder Path: "
        )

        organize_files(path)

        print(
            "Files Organized"
        )

    elif choice == "2":

        show_summary()

    elif choice == "3":

        print("Goodbye")

        break

    else:

        print("Invalid Option")
