from camoufox.sync_api import Camoufox
from parsel import Selector

def main():

    # humanize=True makes mouse movement look real
    with Camoufox(headless=True, humanize=True) as browser:
        page = browser.new_page()
        jobs = []
        page_number = 1
        search = input("What job's do you want to scrape? ")
        
        while True:
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
            print(f"number of cards - {len(job_cards)}")
            
            # Extract stuff from job listing card
            for card in job_cards:
                item = {
                    "title": card.css("h3.list_h3::text").get(),
                    "link": card.css("::attr(href)").get()
                }               
                # go to job ad
                page.goto(item["link"])
                page.wait_for_load_state("networkidle")
                print(f"I am currently at: {page.url}")
                
                # get html for Parsel
                job_html = page.content()
                job_selector = Selector(text=job_html)
                
                #select description
                description = job_selector.css("#jobad_content_main *::text").getall()
                full_text = " ".join([text.strip() for text in description if text.strip()])             
                        
                # add to list to be printed
                if search.strip().lower() in full_text.lower():
                    jobs.append(item)

            # last page check
            if page.url != requested_url:
                print("\n done \n ------------------------\n")
                break
            
            # for testing purposes - only scan ads on first page of cvbankas
            if page_number >= 1:
                break

            page_number += 1
            
        for job in jobs:
            print(f"{job["title"]}, {job["link"]}\n")

if __name__ == "__main__":
    main()