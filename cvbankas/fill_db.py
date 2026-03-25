import json
import pathlib

import psycopg

CONN_INFO = "dbname=cvbankas_db user=valdovas password=tusinukas host=localhost"
json_dir = pathlib.Path("./jsons")


def clean_data(data: dict) -> tuple[str, int]:
    # Join the description list
    desc = "\n".join(data.get("description", []))

    # Convert views to int
    views = int(data.get("seens", 0))

    return desc, views


with psycopg.connect(CONN_INFO) as conn, conn.cursor() as cur:
    rows = []
    # Loop through every JSON file
    for file_path in json_dir.glob("*.json"):
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        # clean
        desc, views = clean_data(data)

        rows.append(
            (
                data["job_id"],
                data["url"],
                data["title"],
                data["location"],
                data["company_name"],
                data["job_category"],
                views,
                desc,
                data["salary"],
                data["salary_type"],
                data["is_vip"],
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
