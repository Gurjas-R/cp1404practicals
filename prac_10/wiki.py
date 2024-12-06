"""
CP1404 Practical
Program gets data from Wikipedia using API
"""

import wikipedia


def main():
    """Get user input, then return data from Wikipedia page"""
    search_title = input("Enter page title: ")
    while search_title != "":
        try:
            page = wikipedia.page(search_title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as i:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(i.options)
        except wikipedia.exceptions.PageError:
            print(f"Page id {search_title} does not match any pages. Try another id!")
        search_title = input("Enter page title: ")
    print("Thank you.")


main()
