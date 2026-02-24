from camoufox.sync_api import Camoufox
from parsel import Selector

def main():    

    all_links = []
    title = 1
    
    with open("links.txt", "r") as my_file:
        all_links = my_file.readlines()
        
    with Camoufox(headless=True, humanize=True) as browser:
        page = browser.new_page()      
            
        for link in all_links:
            # open link
            print("going to: ", link.strip())
            page.goto(link)
            page.wait_for_load_state("networkidle")  
    
            # save html to jobhtmls           
            with open(f"jobhtmls/job_file{title}.html", "w", encoding="utf-8") as file:
                file.write(page.content())
            
            title += 1
    
if __name__ == "__main__":
    main()