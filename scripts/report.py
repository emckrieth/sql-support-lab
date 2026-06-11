import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "db" / "support_lab.db"

queries = {
    "failed_verifications": """
        SELECT verification_id, user_id, failure_reason, provider_latency_ms
        FROM verifications
        WHERE status = 'failed';
    """,
    "duplicate_user_emails": """
        SELECT email, COUNT(*) AS cnt
        FROM users
        GROUP BY email
        HAVING COUNT(*) > 1;
    """,
    "incident_signatures": """
        SELECT error_signature, COUNT(*) AS cnt
        FROM incidents
        GROUP BY error_signature
        ORDER BY cnt DESC;
    """,
}


def main() -> None:
    if not DB_PATH.exists():
        raise SystemExit("Database not found. Run `python scripts/seed_db.py` first.")

    with sqlite3.connect(DB_PATH) as conn:
        for title, query in queries.items():
            print(f"\n## {title}")
            rows = conn.execute(query).fetchall()
            for row in rows:
                print(row)


if __name__ == "__main__":
    main()
