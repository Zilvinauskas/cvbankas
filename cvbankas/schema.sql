CREATE TABLE job_postings (
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