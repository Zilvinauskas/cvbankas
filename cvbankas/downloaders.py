from camoufox.sync_api import Camoufox
from curl_cffi import requests
from rnet import Impersonate, Client, Response
from patchright.sync_api import sync_playwright

class Downloader:
    def __init__(self, headers = None):
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "Accept-Language": "en-US,en;q=0.9"
        }
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def get_url(self):
        pass
    
    def get_html(self, url: str) -> str:
        pass

class CamoufoxDownloader(Downloader):
    
    def __init__(self):
        self.browser = None
        self.page = None
        
    def start(self):
        self.browser = Camoufox(headless=True, humanize=True).start()
        self.page = self.browser.new_page()  
    
    def get_html(self, url: str) -> str:
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle") 
        return self.page.content()
    
    def get_url(self) -> str:
        if self.page:
            return self.page.url
        return "bot not started"

    def stop(self):
        if self.browser:
            self.browser.close()
            
class CffiDownloader(Downloader):

    def __init__(self):        
        self.session = None
        
    def start(self):        
        self.session = requests.Session()
        
    def get_html(self, url:str ) -> str:
        html = self.session.get(url, impersonate="chrome120")
        
        self.last_url = html.url
        return html.text

    def get_url(self) -> str:
        return self.last_url

    def stop(self):
        if self.session:
            self.session.close()

class PlayrightDownloader(Downloader):
    
    def __init__(self) -> None:        
        self.browser = None
        self.page = None
        
    def start(self) -> None:        
        self.pr = sync_playwright().start()
        self.browser = self.pr.chromium.launch()
        self.page = self.browser.new_page()
        
    def get_html(self, url: str) -> str:
        self.page.goto(url)
        html = self.page.content()
        return html 
    
    def get_url(self) -> str:
        if self.page:
            return self.page.url
        return "bot not started"

    def stop(self) -> None:
        if self.browser:
           self.browser.close()
        # stop pr engine
        if self.pr:
            self.pr.stop()

