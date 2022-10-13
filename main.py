from rename_func import renamer


def main():
    source = input("Please enter the source directory: ")

    studio = input("Please enter the studio name: ")

    renamer(source, studio)


if __name__ == '__main__':
    main()
