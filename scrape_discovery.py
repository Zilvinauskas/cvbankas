from camoufox.sync_api import Camoufox
from parsel import Selector

def main():

    # humanize=True makes mouse movement look real
    with Camoufox(headless=True, humanize=True) as browser:
        
        page = browser.new_page()
        page_number = 1
        title = 1
  
        while True:
            # open page
            print(f"Opening page {page_number}")
            requested_url = f"https://www.cvbankas.lt/?page={page_number}"
            page.goto(requested_url)
            
            # delay
            page.wait_for_load_state("networkidle")        

                
            # last page check
            if page.url != requested_url:
                print("\n done \n ------------------------\n")
                break
            
            #save htmls to html dir
            with open(f"htmls/file{title}.html", "w", encoding="utf-8") as file:
                file.write(page.content())

            page_number += 1
            title += 1
                 
        
if __name__ == "__main__":
    main()