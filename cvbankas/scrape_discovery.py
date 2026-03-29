import sys
import time
from typing import Any

from downloaders.CamoufoxDownloader import CamoufoxDownloader
from downloaders.CffiDownloader import CffiDownloader
from downloaders.PlayrightDownloader import PlayrightDownloader


# pylint: disable=R0801
def run_scrape_discovery(downloader_type: str) -> None:

    page_number = 1
    delay = 5

    bot: Any

    if downloader_type == "cfox":
        bot = CamoufoxDownloader()

    elif downloader_type == "cffi":
        bot = CffiDownloader()

    elif downloader_type == "playright":
        bot = PlayrightDownloader()
    else:
        print(f"Unknown downloader: {downloader_type}. Supported: camoufox, cffi, playright")

    bot.start_downloader()

    print(downloader_type, "initialized")

    while True:
        try:
            print(f"Opening page {page_number}")
            requested_url = f"https://www.cvbankas.lt/?page={page_number}"

            html_content = bot.make_request(requested_url)

            # last page check
            current_url = bot.get_current_url()
            if current_url != requested_url:
                print("done")
                break

            with open(f"htmls/file{page_number}.html", "w", encoding="utf-8") as file:
                file.write(html_content)

        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"could not open: {requested_url}: {e}")

        page_number += 1
        time.sleep(delay)

    bot.stop_downloader()


if __name__ == "__main__":
    choice = sys.argv[2]
    run_scrape_discovery(choice)
