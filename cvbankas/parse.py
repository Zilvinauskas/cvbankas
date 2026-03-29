import json
from pathlib import Path

from parsel import Selector


def run_parse() -> None:  # pylint: disable=too-many-locals, R0801

    count = 0

    folder_path = Path("jobhtmls/")

    for file in folder_path.glob("*.html"):
        with open(file, encoding="utf-8") as f:
            html = f.read()

        selector = Selector(text=html)

        url = selector.xpath("//link[@rel='canonical']/@href").get() or ""
        job_id = url.split("/")[-1] if url else "0"
        title = selector.xpath("//h1[@class='heading1']/text()").get()
        location = selector.xpath("//span[@itemprop='addressLocality']/text()").get()
        company_name = selector.xpath("//h2[@id='jobad_company_title']/text()").get()
        job_category = selector.xpath("//a[contains(@href, 'pasiulymai')]/text()").get()
        seens = selector.xpath("(//strong[@class='jobad_stat_value'])[1]/text()").get()
        candidate_count = selector.xpath("(//strong[@class='jobad_stat_value'])[2]/text()").get()
        is_vip = bool(selector.xpath('//div[contains(@class,"jobadlist_article_vip_icon")]'))

        description_parts = selector.xpath("//section[@itemprop='description']//text()").getall()
        description_full = []
        for d in description_parts:
            description_full.append(d.strip() + "\n")

        salary = selector.xpath(
            "//div[@class='label_component_body']"
            "[span[@class='data_tag_component_salary_amount']]"
            "/span[@class='data_tag_component_salary_amount']/text()"
        ).get()

        # find out if after_tax and salary type
        parts = selector.xpath(
            "//div[@class='label_component']"
            "[div[@class='label_component_body']]"
            "/div[@class='label_component_body']/text()"
        ).getall()
        joined_parts = "".join(parts).strip()
        after_tax = "rankas" in joined_parts

        salary_type = "hourly" if "val." in joined_parts else "monthly"

        # json file
        job_details = {
            "url": url,
            "job_id": job_id,
            "title": title,
            "location": location,
            "company_name": company_name,
            "job_category": job_category,
            "seens": seens,
            "candidate_count": candidate_count,
            "description": description_full,
            "salary": salary,
            "salary_type": salary_type,
            "after_tax": after_tax,
            "is_vip": is_vip,
        }

        # save json
        name = file.name.split("/")[-1].split(".")[0]
        with open(f"jsons/{name}.json", "w", encoding="utf-8") as json_file:
            json.dump(job_details, json_file, indent=4, ensure_ascii=False)
        count += 1

    print("Files parsed: ", count)


if __name__ == "__main__":
    run_parse()
