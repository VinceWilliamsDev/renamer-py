from os import scandir, rename
from pathlib import Path


def renamer(source=None, studio=None):
    list_of_files = set()
    number_modified = 0

    if source is None:
        directory = Path(r'')
    else:
        directory = Path(source)
    if studio is None:
        studio = ''

    """
    create list of file names to be modified
    this is important because scandir will detect files modified in place as new objects to be looped over again.
    If you aren't careful, and extend the names to be too large, the files could be corrupted.
    Alternatively you could relocate the files to a different directory and they would then be out of scope
    for the scan.
    """

    with scandir(directory) as it:
        for file in it:
            list_of_files.add(file.name)

    # print(list_of_files)

    with scandir(directory) as it:
        for file in it:

            if file.is_file() and file.name in list_of_files:
                parts = file.name.split(" - ", 1)
                file_extension = file.name[-4:]
                # last_dash should be the location of the last dash in the file name
                # if there is no last dash, truncate the file extension, to be appended later
                last_dash = -4

                # find the last dash in the file name
                for num in range(5, 8):
                    if file.name[-num] == '-':
                        last_dash = -num
                        break

                rename(file, f'{directory}\\{studio} - {parts[1][:last_dash]}{file_extension}')
                # rename(file, f'{directory}\\{studio} - {file.name}')
                number_modified += 1

                # print(file.name)
                # print(len(parts))
    print(f'Files modified: {number_modified}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    renamer()
