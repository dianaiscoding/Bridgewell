import psycopg2

from db import get_pg_connection


def fetch_country_rows():
    print("Opening PostgreSQL connection...", flush=True)
    conn = get_pg_connection()
    print("PostgreSQL connected", flush=True)

    sql = """
    SELECT
        eg.country,
        eg.total_respondents,
        eg.avg_stress,
        eg.avg_work_life_balance,
        eg.avg_job_satisfaction,
        eg.avg_symptom_score,
        eg.pct_lacking_support,
        lr.avg_sleep_hours,
        lr.avg_screen_time,
        lr.caffeine,
        lr.count_no_exercise,
        lr.count_poor_diet,
        lr.count_smokers,
        lr.count_freq_drinkers,
        tg.diagnosed_count,
        tg.untreated_count,
        tg.pct_untreated
    FROM employer_gap_by_country eg
    LEFT JOIN lifestyle_risk_by_country lr
        ON eg.country = lr.country
    LEFT JOIN treatment_gap_by_country tg
        ON eg.country = tg.country
    ORDER BY eg.country
    """

    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            print("Running aggregate query...", flush=True)
            cur.execute(sql)
            print("Query finished, fetching rows...", flush=True)
            rows = [dict(row) for row in cur.fetchall()]
            print(f"Fetched {len(rows)} rows", flush=True)
            return rows
    finally:
        conn.close()
        print("PostgreSQL connection closed", flush=True)