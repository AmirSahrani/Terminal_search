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


def format_results(results, max_length=70):
    for result in results:
        print(Fore.GREEN + result["title"])
        print(Fore.BLUE + result["href"])
        print(Style.RESET_ALL)
        print(text_to_lines(result["body"], max_length), "\n")


def format_instant(instant, max_length=70):
    print(Fore.RED + "Instant Answer:")
    print(Fore.BLUE + instant["url"])
    print(Fore.YELLOW)
    print(text_to_lines(instant["text"], 60), "\n")


def format_search(search, filter_websites):
    search += " ("
    for website in filter_websites:
        search += "site:" + website + " OR "
    search = search[:-4] + ")"
    return search


def main(search, filter_websites):
    just_fix_windows_console()
    prompt = search.split("-")[0]
    filter = search.split("-")
    try:
        filter = int(filter[1])-1
    except IndexError:
        filter = 0
    if filter:
        print("Filtered search")
        prompt = format_search(prompt, filter_websites[filter])

    results = ddg(prompt, max_results=5)
    instant = ddg_answers(prompt)
    max_length = 70

    if instant:
        format_instant(instant[0], max_length)
    format_results(results, max_length)


filter_websites = [["wikipedia.org", "stackoverflow.com",
                    "github.com", "geeksforgeeks.com",
                   "reddit.com"],
                   ["wikipedia.org", "youtube.com"]]

if __name__ == "__main__":
    main(" ".join(sys.argv[1:]), filter_websites)
