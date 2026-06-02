import os


def show_summary():

    folders = [
        "Images",
        "Documents",
        "PDFs",
        "Videos"
    ]

    print("\nSummary\n")

    for folder in folders:

        if os.path.exists(folder):

            count = len(
                os.listdir(folder)
            )

            print(
                f"{folder}: {count} files"
            )
