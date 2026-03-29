from abc import ABC, abstractmethod


class BaseDownloader(ABC):
    def __init__(self, headers: dict[str, str] | None = None) -> None:
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "Accept-Language": "en-US,en;q=0.9",
        }

    @abstractmethod
    def start_downloader(self) -> None:
        pass

    @abstractmethod
    def stop_downloader(self) -> None:
        pass

    @abstractmethod
    def get_current_url(self) -> str:
        pass

    @abstractmethod
    def make_request(self, url: str) -> str:
        pass
