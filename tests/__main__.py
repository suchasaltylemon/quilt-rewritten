from loader.parsing import FileParser
from shsb import SHSB

FILE_PATH = "views/index.pyhtml"


def main():
    with FileParser(FILE_PATH) as parser:
        data = parser.parse()

        print


if __name__ == "__main__":
    shsb = SHSB()
    shsb.install_dependencies()

    main()
