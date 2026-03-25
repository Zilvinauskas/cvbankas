from parsel import Selector


def run_parse_discovery() -> None:

    title = 1
    links = []

    while True:
        try:
            # open html
            with open(f"htmls/file{title}.html", encoding="utf-8") as file:
                print(f"Opening file no:{title}")
                html = file.read()

            # select data
            selector = Selector(text=html)
            job_cards = selector.css("a.list_a")

            # append links to list
            for card in job_cards:
                # if get() is None, use "" instead
                links.append(card.css("::attr(href)").get() or "")

            title += 1

        # catch exception with last html file
        except FileNotFoundError:
            print("done")
            break

    # create txt and paste all links from list
    with open("links.txt", "w", encoding="utf-8") as file:
        for link in links:
            file.write(link.strip() + "\n")


if __name__ == "__main__":
    run_parse_discovery()
