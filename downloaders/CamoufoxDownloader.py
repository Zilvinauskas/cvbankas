from camoufox.sync_api import Camoufox

from downloaders.BaseDownloader import BaseDownloader


class CamoufoxDownloader(BaseDownloader):

    def __init__(self):
        self.browser = None
        self.page = None

    def start_downloader(self):
        self.browser = Camoufox(headless=True, humanize=True).start()
        self.page = self.browser.new_page()

    def make_request(self, url: str) -> str:
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
        return self.page.content()

    def get_current_url(self) -> str:
        if self.page:
            return self.page.url
        return "bot not started"

    def stop_downloader(self):
        if self.browser:
            self.browser.close()
