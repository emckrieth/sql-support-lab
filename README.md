import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "support_lab.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

schema = """
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS verifications;
DROP TABLE IF EXISTS incidents;
DROP TABLE IF EXISTS webhooks;

CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    country TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE verifications (
    verification_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    status TEXT NOT NULL,
    failure_reason TEXT,
    provider_latency_ms INTEGER,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE incidents (
    incident_id TEXT PRIMARY KEY,
    service_name TEXT NOT NULL,
    severity TEXT NOT NULL,
    error_signature TEXT NOT NULL,
    opened_at TEXT NOT NULL
);

CREATE TABLE webhooks (
    webhook_id TEXT PRIMARY KEY,
    verification_id TEXT NOT NULL,
    delivery_status TEXT NOT NULL,
    delivered_at TEXT NOT NULL,
    FOREIGN KEY (verification_id) REFERENCES verifications(verification_id)
);
"""

users = [
    ("u100", "a@example.com", "US", "2026-06-01T10:00:00Z"),
    ("u101", "b@example.com", "US", "2026-06-01T11:00:00Z"),
    ("u102", "c@example.com", "GB", "2026-06-01T12:00:00Z"),
    ("u103", "a@example.com", "US", "2026-06-02T09:00:00Z")
]

verifications = [
    ("v100", "u100", "approved", None, 210, "2026-06-09T10:01:00Z"),
    ("v101", "u101", "failed", "provider timeout", 9000, "2026-06-09T10:02:00Z"),
    ("v102", "u102", "review", None, 450, "2026-06-09T10:03:00Z"),
    ("v103", "u101", "failed", "provider timeout", 8700, "2026-06-09T10:04:00Z")
]

incidents = [
    ("i100", "verification-api", "SEV2", "provider timeout", "2026-06-09T10:05:00Z"),
    ("i101", "verification-api", "SEV3", "provider timeout", "2026-06-09T10:10:00Z"),
    ("i102", "webhook-delivery", "SEV3", "duplicate delivery", "2026-06-09T10:20:00Z")
]

webhooks = [
    ("w100", "v100", "delivered", "2026-06-09T10:06:00Z"),
    ("w101", "v101", "failed", "2026-06-09T10:06:30Z"),
    ("w102", "v101", "failed", "2026-06-09T10:06:45Z"),
    ("w103", "v103", "failed", "2026-06-09T10:07:00Z")
]

with sqlite3.connect(DB_PATH) as conn:
    conn.executescript(schema)
    conn.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", users)
    conn.executemany("INSERT INTO verifications VALUES (?, ?, ?, ?, ?, ?)", verifications)
    conn.executemany("INSERT INTO incidents VALUES (?, ?, ?, ?, ?)", incidents)
    conn.executemany("INSERT INTO webhooks VALUES (?, ?, ?, ?)", webhooks)
    conn.commit()

print(f"Seeded database at {DB_PATH}")
