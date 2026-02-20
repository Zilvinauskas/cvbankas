from camoufox.sync_api import Camoufox
from parsel import Selector

def main():    

    with open(f"links.txt", "r") as file:
        links = file.read()
        
    with Camoufox(headless=True, humanize=True) as browser:
        page = browser.new_page()
        
        while True:
             # open page
            # paselectinti link is listo
            requested_url = f"paselectintas link"
            page.goto(requested_url)
            
            # delay
            page.wait_for_load_state("networkidle")     
            
            # parse page
            html = page.content()
            selector = Selector(text=html)
            
            #istraukti data ir deti i dict
            item = {
                "title": card.css("h3.list_h3::text").get(),
                "link": card.css("::attr(href)").get()
            }   
                
    
    
    
if __name__ == "__main__":
    main()