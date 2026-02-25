import json
from parsel import Selector

def main():
    
    count = 1
    
    while True:
        
        with open(f"jobhtmls/job_file{count}.html", "r") as file:
            html = file.read()
            
        selector = Selector(text=html)
        
        if count > 5:
            break
        
        # # title 
        # result = selector.xpath("//h1[@class='heading1']/text()")
        # title = result.get()
        # print(title)
        
        # # location
        # result = selector.xpath("//span[@itemprop='addressLocality']/text()")
        # location = result.get()
        # print(location)
        
        # # company_name
        # result = selector.xpath("//h2[@id='jobad_company_title']/text()")
        # company_name = result.get()
        # print(company_name)
        
        # # job_category
        # result = selector.xpath("//a[contains(@href, 'pasiulymai')]/text()")
        # job_category = result.get()
        # print(job_category)
        
        # # seens
        # result = selector.xpath("(//strong[@class='jobad_stat_value'])[1]/text()")
        # seens = result.get()
        # print(seens)
        
        # # candidate_count
        # result = selector.xpath("(//strong[@class='jobad_stat_value'])[2]/text()")
        # candidate_count = result.get()
        # print(candidate_count)
        
        # # description
        # result = selector.xpath("//section[@itemprop='description']/section[position() != last()]//text()")
        # description = result.getall()
        # for d in description:
        #     print(d.strip())
            
        # salary
        result = selector.xpath("//div[@class='label_component_body'][span[@class='data_tag_component_salary_amount']]//text()")
        salary = result.getall()
        for s in salary:
            print(s.strip(), end="")
        # is_company_vip
        result = selector.xpath("//div[@data-tooltip=jobadlist_article_vip_icon]//text()")
        isvip = result.getall()
        for i in isvip:
            print(i)??????????
        # employment_type   
        print("\n----------------------------------------------------------------")

            

        
        count += 1
    
    
    
if __name__ == "__main__":
    main()