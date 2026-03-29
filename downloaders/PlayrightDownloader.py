from patchright.sync_api import sync_playwright

from downloaders.BaseDownloader import BaseDownloader


class PlayrightDownloader(BaseDownloader):

    def __init__(self) -> None:
        self.browser = None
        self.page = None

    def start_downloader(self) -> None:
        self.pr = sync_playwright().start()
        self.browser = self.pr.chromium.launch()
        self.page = self.browser.new_page()

    def make_request(self, url: str) -> str:
        self.page.goto(url)
        html = self.page.content()
        return html

    def get_current_url(self) -> str:
        if self.page:
            return self.page.url
        return "bot not started"

    def stop_downloader(self) -> None:
        if self.browser:
           self.browser.close()
        # stop pr engine
        if self.pr:
            self.pr.stop()
