from typing import Any, Optional

from curl_cffi import requests

from downloaders.BaseDownloader import BaseDownloader


class CffiDownloader(BaseDownloader):

    def __init__(self) -> None:
        self.session: Optional[Any] = None
        self.last_url: str = ""

    def start_downloader(self) -> None:
        self.session = requests.Session()

    def make_request(self, url: str) -> str:
        html = self.session.get(url, impersonate="chrome120")  # type: ignore[union-attr]

        self.last_url = html.url
        return html.text  # type: ignore[no-any-return]

    def get_current_url(self) -> str:
        return self.last_url

    def stop_downloader(self) -> None:
        if self.session:
            self.session.close()
