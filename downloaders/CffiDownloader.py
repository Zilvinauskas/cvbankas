from curl_cffi import requests
from downloaders.BaseDownloader import BaseDownloader

class CffiDownloader(BaseDownloader):

    def __init__(self):        
        self.session = None
        
    def start_downloader(self):        
        self.session = requests.Session()
        
    def make_request(self, url:str ) -> str:
        html = self.session.get(url, impersonate="chrome120")
        
        self.last_url = html.url
        return html.text

    def get_current_url(self) -> str:
        return self.last_url

    def stop_downloader(self):
        if self.session:
            self.session.close()