from camoufox.sync_api import Camoufox
from parsel import Selector

def main():

    # humanize=True makes mouse movement look real
    with Camoufox(headless=True, humanize=True) as browser:
        
        page = browser.new_page()
        page_number = 1
        jobs = []
        title = 0
  
        while True:
            # open page
            print(f"Opening page {page_number}")
            requested_url = f"https://www.cvbankas.lt/?page={page_number}"
            page.goto(requested_url)
            
            # delay
            page.wait_for_load_state("networkidle")
            
            # give html to Parsel
            html = page.content()
            selector = Selector(text=html)
            
            # Extract data using CSS 
            job_cards = selector.css("a.list_a")
            
            # Extract stuff from job listing card
            for card in job_cards:
                item = {
                    "link": card.css("::attr(href)").get()
                }               
                # go to job ad
                page.goto(item["link"])
                page.wait_for_load_state("networkidle")
                print(f"I am currently at: {page.url}")
                
                # create and write file                
                with open(f"html/file{title}.html", "w", encoding="utf-8") as file:
                    file.write(page.content())
                
                #update title name
                title += 1               
                
            # last page check
            if page.url != requested_url:
                print("\n done \n ------------------------\n")
                break
            # for testing purposes - only scan ads on first page of cvbankas
            if page_number >= 1:
                break

            page_number += 1
                 
        
if __name__ == "__main__":
    main()