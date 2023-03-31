from colorama import just_fix_windows_console, Fore, Style
from duckduckgo_search import ddg, ddg_answers
import sys


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


def format_results(results, max_length=60):
    for result in results:
        print(Fore.GREEN + result["title"])
        print(Fore.BLUE + result["href"])
        print(Style.RESET_ALL)
        print(text_to_lines(result["body"], max_length), "\n")


def format_instant(instant):
    print(Fore.RED + "Instant Answer:")
    print(Fore.BLUE + instant["url"])
    print(Fore.YELLOW)
    print(text_to_lines(instant["text"], 60), "\n")


def format_search(search, filter_websites):
    search += " ("
    for website in filter_websites:
        search += "site: " + website + " OR "
    search = search[:-4] + ")"
    return search


def main(search):
    just_fix_windows_console()
    filter_websites = ["wikipedia.org", "stackoverflow.com",
                       "github.com", "geeksforgeeks.com",
                       "reddit.com"]
#     search = format_search(search, filter_websites)
    print(search)
    results = ddg(search, max_results=10)
    instant = ddg_answers(search)
    if instant:
        format_instant(instant[0])
    format_results(results)


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]))
