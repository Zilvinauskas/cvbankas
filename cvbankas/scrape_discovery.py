from camoufox.sync_api import Camoufox
from curl_cffi import requests
from parsel import Selector
from rnet import Impersonate, Client, Response
from patchright.sync_api import sync_playwright
from cvbankas.downloaders import CamoufoxDownloader, CffiDownloader, PlayrightDownloader
import time



def run_scrape_discovery(downloader_type) -> None:       

    page_number = 1
    delay = 5
    
    if downloader_type == "cfox":  
        bot = CamoufoxDownloader()
        
    elif downloader_type == "cffi":
        bot = CffiDownloader()                   
        
    elif downloader_type == "playright":
        bot = PlayrightDownloader()       
    
    else:
        print(f"Unknown downloader: {downloader_type}. Supported: camoufox, cffi, playright") 
        
    bot.start()
    
    print(downloader_type, "initialized")
    
    while True:
        
        try:
            print(f"Opening page {page_number}")
            requested_url = f"https://www.cvbankas.lt/?page={page_number}"  
            
            
            html_content = bot.get_html(requested_url)        

            # last page check
            current_url = bot.get_url()
            if current_url != requested_url:
                print("done")
                break
                
            with open(f"htmls/file{page_number}.html", "w", encoding="utf-8") as file:
                file.write(html_content)
                
        except Exception as e:
            print(f"could not open: {requested_url}: {e}")
            
        page_number += 1
        time.sleep(delay)
            

        
if __name__ == "__main__":
    run_scrape_discovery()