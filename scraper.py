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
            job_titles = selector.css("h3.list_h3::text").getall()
            
            #links = selector.css("a.list_a::attr(href)").getall()
            
            # Copy jobs from list to master list
            jobs.extend(job_titles + links)

            if page.url != requested_url:
                print("done")
                break

            if page_number > 20:
                break

            page_number += 1
            
        for job in jobs:
            if search in job.lower():
                print(f"- {job.strip()}")

if __name__ == "__main__":
    main()