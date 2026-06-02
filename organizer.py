import os
import shutil

from categories import IMAGE_FILES
from categories import DOCUMENT_FILES
from categories import PDF_FILES
from categories import VIDEO_FILES

from folder_creator import create_folder


def organize_files(path):

    files = os.listdir(path)

    create_folder("Images")
    create_folder("Documents")
    create_folder("PDFs")
    create_folder("Videos")

    for file in files:

        source = os.path.join(path, file)

        if os.path.isdir(source):

            continue

        extension = os.path.splitext(file)[1]

        if extension in IMAGE_FILES:

            shutil.move(
                source,
                f"Images/{file}"
            )

        elif extension in DOCUMENT_FILES:

            shutil.move(
                source,
                f"Documents/{file}"
            )

        elif extension in PDF_FILES:

            shutil.move(
                source,
                f"PDFs/{file}"
            )

        elif extension in VIDEO_FILES:

            shutil.move(
                source,
                f"Videos/{file}"
            )
