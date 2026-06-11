import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "db" / "support_lab.db"


def main() -> None:
    DB_PATH.parent.mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(
            """
            DROP TABLE IF EXISTS users;
            DROP TABLE IF EXISTS verifications;
            DROP TABLE IF EXISTS webhooks;
            DROP TABLE IF EXISTS incidents;

            CREATE TABLE users (
                user_id TEXT PRIMARY KEY,
                email TEXT NOT NULL,
                created_at TEXT NOT NULL
            );

            CREATE TABLE verifications (
                verification_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                status TEXT NOT NULL,
                failure_reason TEXT,
                provider_latency_ms INTEGER,
                created_at TEXT NOT NULL
            );

            CREATE TABLE webhooks (
                webhook_id TEXT PRIMARY KEY,
                verification_id TEXT NOT NULL,
                delivery_status TEXT NOT NULL,
                attempts INTEGER NOT NULL,
                last_error TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE incidents (
                incident_id TEXT PRIMARY KEY,
                error_signature TEXT NOT NULL,
                opened_at TEXT NOT NULL,
                status TEXT NOT NULL
            );
            """
        )

        conn.executemany(
            "INSERT INTO users VALUES (?, ?, ?)",
            [
                ("u1", "alex@example.com", "2026-06-01T10:00:00Z"),
                ("u2", "sam@example.com", "2026-06-01T10:15:00Z"),
                ("u3", "alex@example.com", "2026-06-02T11:00:00Z"),
                ("u4", "riley@example.com", "2026-06-02T12:00:00Z"),
            ],
        )
        conn.executemany(
            "INSERT INTO verifications VALUES (?, ?, ?, ?, ?, ?)",
            [
                ("v1", "u1", "approved", None, 320, "2026-06-03T09:00:00Z"),
                ("v2", "u2", "failed", "provider timeout", 8000, "2026-06-03T09:05:00Z"),
                ("v3", "u3", "failed", "document image quality too low", 410, "2026-06-03T09:10:00Z"),
            ],
        )
        conn.executemany(
            "INSERT INTO webhooks VALUES (?, ?, ?, ?, ?, ?)",
            [
                ("w1", "v1", "delivered", 1, None, "2026-06-03T09:01:00Z"),
                ("w2", "v2", "failed", 3, "502 Bad Gateway", "2026-06-03T09:06:00Z"),
                ("w3", "v2", "failed", 2, "502 Bad Gateway", "2026-06-03T09:07:00Z"),
            ],
        )
        conn.executemany(
            "INSERT INTO incidents VALUES (?, ?, ?, ?)",
            [
                ("i1", "provider_timeout", "2026-06-03T09:00:00Z", "open"),
                ("i2", "provider_timeout", "2026-06-04T09:00:00Z", "resolved"),
                ("i3", "webhook_delivery_failure", "2026-06-05T10:00:00Z", "open"),
            ],
        )

    print(f"Seeded {DB_PATH}")


if __name__ == "__main__":
    main()
