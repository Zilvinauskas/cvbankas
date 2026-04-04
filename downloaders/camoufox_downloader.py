from typing import cast

from camoufox.sync_api import Camoufox
from playwright.sync_api import Browser, Page

from downloaders.base_downloader import BaseDownloader


class CamoufoxDownloader(BaseDownloader):
    def __init__(self) -> None:
        super().__init__()
        self.browser: Browser | None = None
        self.page: Page | None = None

    def start_downloader(self) -> None:
        if self.browser is None:
            self.browser = cast(Browser, Camoufox(headless=True, humanize=True).start())
        if self.browser:
            self.page = self.browser.new_page()

    def make_request(self, url: str) -> str:
        if self.page:
            self.page.goto(url)
            self.page.wait_for_load_state("networkidle")
            return self.page.content()
        return "bot not started"

    def get_current_url(self) -> str:
        if self.page:
            return self.page.url
        return "bot not started"

    def stop_downloader(self) -> None:
        if self.browser:
            self.browser.close()
