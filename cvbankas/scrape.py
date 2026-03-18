from camoufox.sync_api import Camoufox
from curl_cffi import requests
from parsel import Selector
from rnet import Impersonate, Client, Response
from patchright.sync_api import sync_playwright
import asyncio
import time
import typer
import os

def run_scrape(downloader):    

    all_links = []
    # set delay for opening new page
    delay = 5  
    with open("links.txt", "r") as my_file:
        all_links = my_file.readlines()
    

              
    def camoufox(delay): 
        title = 1           
        with Camoufox(headless=True, humanize=True) as browser:
            page = browser.new_page()                 
                
            for link in all_links:
                # open link
                url = link.strip()
                print("going to: ", url)
                
                try:
                    page.goto(url)
                    page.wait_for_load_state("networkidle")
                    html = page.content()  
            
                    # save html to jobhtmls           
                    with open(f"jobhtmls/job_file{title}.html", "w", encoding="utf-8") as file:
                        file.write(html)
                
                except Exception as e:
                    print(f"could not open {url}: {e}") 
            
                title += 1
                time.sleep(delay)     
            
                       
    def cffi(delay):
        title = 1     
        with requests.Session() as s:
            for link in all_links:
                url = link.strip()
                print("going to: ", url)
                
                try: 
                    response = s.get(url, impersonate="chrome120", timeout=30)
                    
                    # raise exception if error
                    response.raise_for_status()
                    
                    html = response.text
                        
                    with open(f"jobhtmls/job_file{title}.html", "w", encoding="utf-8") as file:
                        file.write(html)
                                            
                except Exception as e:
                    print(f"could not open {url}: {e}")
                        
                title += 1
                time.sleep(delay)    
            
            
    def rnet(delay):
        title = 1     
        client = Client(impersonate = Impersonate.Chrome120)
        
        for link in all_links:
            url = link.strip()
            print("going to: ", url)
            
            try:
                response: Response = client.get(url)

                html = response.text
                with open(f"jobhtmls/job_file{title}.html", "w", encoding="utf-8") as file:
                    file.write(html)
                                            
            except Exception as e:
                print(f"could not open {url}: {e}") 
                
            title += 1
            time.sleep(delay)
        
         
    def playright(delay):
        title = 1 
        with sync_playwright() as pr:
            browser = pr.chromium.launch()
            page = browser.new_page()
            
            for link in all_links:
                url = link.strip()
                print("going to: ", url)
                try:
                    page.goto(url)
                    
                    html = page.content()
                    
                    with open(f"jobhtmls/job_file{title}.html", "w", encoding="utf-8") as file:
                        file.write(html)
                except Exception as e:
                    print(f"could not open {url}: {e}") 
                    
                title += 1
                time.sleep(delay)     
 
                    
    # open using camoufox
    if downloader == "cfox":  
        camoufox(delay)
     
    # open using curl_cffi            
    if downloader == "cffi":
        cffi(delay)
        
    # open using rnet
    if downloader == "rnet":
        rnet(delay)   
                     
    # open using playright             
    if downloader == "playright":
        playright(delay)  
    
    else:
        print(f"Unknown downloader: {downloader}. Supported: camoufox, cffi, rnet, playright")     
            
if __name__ == "__main__":
    run_scrape() # type: ignore