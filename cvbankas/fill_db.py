import json
import pathlib

import psycopg

CONN_INFO = "dbname=cvbankas_db user=valdovas password=tusinukas host=localhost"
json_dir = pathlib.Path("./jsons")


def clean_data(data: dict) -> tuple[str, int]:
    # Join the description list
    description = "\n".join(data.get("description", []))

    # Convert views to int
    view_count = int(data.get("seens", 0))

    return description, view_count


with psycopg.connect(CONN_INFO) as conn, conn.cursor() as cur:
    rows = []
    # Loop through every JSON file
    for file_path in json_dir.glob("*.json"):
        with open(file_path, encoding="utf-8") as f:
            my_data = json.load(f)

        # clean
        desc, views = clean_data(my_data)

        rows.append(
            (
                my_data["job_id"],
                my_data["url"],
                my_data["title"],
                my_data["location"],
                my_data["company_name"],
                my_data["job_category"],
                views,
                desc,
                my_data["salary"],
                my_data["salary_type"],
                my_data["is_vip"],
            )
        )

        # add data to table
        cur.executemany(
            """
                INSERT INTO job_postings (
                    job_id, url, title, location, company_name,
                    job_category, views, description, salary, salary_type, is_vip
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (job_id) DO NOTHING;
            """,
            rows,
        )

        print(f"Finished processing {len(list(json_dir.glob('*.json')))} files!")
