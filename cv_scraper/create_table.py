import psycopg

conn_info = "dbname=cvbankas_db user=USER password=PASSWORD host=localhost"

with psycopg.connect(conn_info) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS job_postings (
                id SERIAL PRIMARY KEY,
                job_id TEXT UNIQUE,
                url TEXT,
                title TEXT,
                location TEXT,
                company_name TEXT,
                job_category TEXT,
                views INTEGER,
                description TEXT,
                salary TEXT,
                salary_type TEXT,
                is_vip BOOLEAN,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)