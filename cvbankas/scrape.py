from camoufox.sync_api import Camoufox
from curl_cffi import requests
from parsel import Selector
from rnet import Impersonate, Client, Response
from patchright.sync_api import sync_playwright
from cvbankas.downloaders import CamoufoxDownloader, CffiDownloader, PlayrightDownloader
import time


def run_scrape(downloader_type) -> None:    

    all_links = []
    title = 1
    # set delay for opening new page
    delay = 5  
    with open("links.txt", "r") as my_file:
        all_links = my_file.readlines()
 

    if downloader_type == "cfox":  
        bot = CamoufoxDownloader()
         
    elif downloader_type == "cffi":
         bot = CffiDownloader()                   
          
    elif downloader_type == "playright":
        bot = PlayrightDownloader()     
    
    else:
        print(f"Unknown downloader: {downloader_type}. Supported: camoufox, cffi, rnet, playright")       
         
    print(downloader_type, "initialized")
    
    bot.start()
    
    for link in all_links:
        
        try:
            html_content = bot.get_html(link.strip())
            
            print(f"opening page: {link.strip()}")
            
            with open(f"jobhtmls/job_file{title}.html", "w", encoding="utf-8") as file:
                file.write(html_content)   
                
        except Exception as e:
            print(f"could not open {link}: {e}") 
                
        title += 1
        time.sleep(delay)       
    
    bot.stop()
    print("scraping finished, ", downloader_type, "stopped")        
            
if __name__ == "__main__":
    run_scrape() # type: ignore