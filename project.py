from colorama import just_fix_windows_console, Fore, Style
from duckduckgo_search import ddg
from argparse import ArgumentParser


def list_to_string(list):
    list = [x.strip(" ") for x in list]
    return "\n".join(list)


def line_make(text, max_length):
    lines = []
    line = ""
    words = text.split(" ")
    for word in words:
        if len(line) + len(word) <= max_length:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)
    return lines


def text_to_lines(text, max_length):
    lines = line_make(text, max_length)
    return list_to_string(lines)


def format_results(results):
    for result in results:
        print(Fore.GREEN + result["title"])
        print(Style.RESET_ALL)
        print(Fore.BLUE + result["href"])
        print(Style.RESET_ALL)
        print(text_to_lines(result["body"], 60), "\n")


def main(search):
    just_fix_windows_console()
    results = ddg(search, max_results=5)
    format_results(results)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("search", help="Search query")
    args = parser.parse_args()
    main(args.search)
