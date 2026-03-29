import sys
import time
from typing import Any

from downloaders.CamoufoxDownloader import CamoufoxDownloader
from downloaders.CffiDownloader import CffiDownloader
from downloaders.PlayrightDownloader import PlayrightDownloader


# pylint: disable=R0801
def run_scrape(downloader_type: str) -> None:

    all_links = []
    title = 1
    # set delay for opening new page
    delay = 5
    with open("links.txt", encoding="utf-8") as my_file:
        all_links = my_file.readlines()

    bot: Any

    if downloader_type == "cfox":
        bot = CamoufoxDownloader()

    elif downloader_type == "cffi":
        bot = CffiDownloader()

    elif downloader_type == "playright":
        bot = PlayrightDownloader()

    else:
        print(f"Unknown downloader: {downloader_type}. Supported: camoufox, cffi, rnet, playright")

    print(downloader_type, "initialized")

    bot.start_downloader()

    for link in all_links:
        try:
            html_content = bot.make_request(link.strip())

            print(f"opening page: {link.strip()}")

            with open(f"jobhtmls/job_file{title}.html", "w", encoding="utf-8") as file:
                file.write(html_content)

        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"could not open {link}: {e}")

        title += 1
        time.sleep(delay)

    bot.stop_downloader()
    print("scraping finished, ", downloader_type, "stopped")


if __name__ == "__main__":
    choice = sys.argv[2]
    run_scrape(choice)
