import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except DisambiguationError as e:
             print(f"We need a more specific title. Try one of the following, or a new search:")
             print(e.options)

        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        title = input("\nEnter page title: ").strip()

    print("Thank you.")

main()
