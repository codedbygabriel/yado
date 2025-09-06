from utils import dir


def main():
    print("Welcome to YADO - Yet Another Directory Organizer!")
    print("Know Issues: Doesn't handle files with spaces well.\n")

    res: str = input("Insert custom path [presume it already has /home/your_user] or leave it empty for default: ")
    dir.entry_point(res)


if __name__ == "__main__":
    main()
