from patchright.sync_api import Browser, Page, Playwright, sync_playwright

from downloaders.base_downloader import BaseDownloader


class PlayrightDownloader(BaseDownloader):
    def __init__(self) -> None:
        super().__init__()
        self.browser: Browser | None = None
        self.page: Page | None = None
        self.pr: Playwright | None = None

    def start_downloader(self) -> None:
        self.pr = sync_playwright().start()
        self.browser = self.pr.chromium.launch()
        self.page = self.browser.new_page()

    def make_request(self, url: str) -> str:
        if self.page:
            self.page.goto(url)
            html = self.page.content()
            return html
        return "bot not started"

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
