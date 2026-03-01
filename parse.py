import json
from parsel import Selector

def main():
    
    count = 1
    
    all_data = []
    
    while True:
        
        try:
            with open(f"jobhtmls/job_file{count}.html", "r") as file:
                html = file.read()
                
            selector = Selector(text=html)
            
            # title 
            title = selector.xpath("//h1[@class='heading1']/text()").get()        
            # location
            location = selector.xpath("//span[@itemprop='addressLocality']/text()").get()        
            # company_name
            company_name = selector.xpath("//h2[@id='jobad_company_title']/text()").get()        
            # job_category
            job_category = selector.xpath("//a[contains(@href, 'pasiulymai')]/text()").get()        
            # seens
            seens = selector.xpath("(//strong[@class='jobad_stat_value'])[1]/text()").get()        
            # candidate_count
            candidate_count = selector.xpath("(//strong[@class='jobad_stat_value'])[2]/text()").get()        
            # description
            description_parts = selector.xpath("//section[@itemprop='description']/section[position() != last()]//text()").getall()
            description_full = []
            for d in description_parts:
                description_full.append(d.strip() + "\n")
            # salary
            salary = selector.xpath("//div[@class='label_component_body'][span[@class='data_tag_component_salary_amount']]//text()").getall()
            salary_full = []
            for s in salary:       
                if not s.isspace():                
                    salary_full.append(s.strip() + "\n")                
            # is_company_vip        
            is_vip = bool(selector.xpath('//div[contains(@class,"jobadlist_article_vip_icon")]'))
            
            jobs = {
                "title": title,
                "location": location,
                "company_name": company_name,
                "job_category": job_category,
                "seens": seens,
                "candidate_count": candidate_count,
                "description": description_full,
                "salary": salary,
                "is_vip": is_vip            
            }
            
            all_data.append(jobs)
            
            count += 1
        
        except FileNotFoundError:
            break

    with open(f"jobs.json", "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file, ensure_ascii=False, indent=4)    
    
    print("Files parsed: ", count)              

    
if __name__ == "__main__":
    main()