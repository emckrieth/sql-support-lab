# SQL Support Lab

A support-focused SQL investigation lab built to demonstrate how I approach data troubleshooting in a technical support environment.

This project simulates common production support scenarios such as:

- investigating failed verifications
- identifying duplicate user records
- tracing webhook delivery failures
- correlating incidents with underlying service behavior
- validating whether issues are caused by data, workflow, or application behavior

## Purpose

I built this lab to show practical SQL usage in a support engineering context rather than a pure analytics or database engineering context. The goal is to reflect investigation work where SQL helps confirm patterns, isolate impact, and speed up root cause analysis.

## Tech Stack

- Python
- SQLite
- SQL

## Quick Start

```bash
python scripts/seed_db.py
python scripts/report.py
```

The seed script creates `db/support_lab.db` with sample users, verifications, webhook deliveries, and incident records.

## Project Structure

```text
SQL-lab/
??? README.md
??? requirements.txt
??? db/
?   ??? .gitkeep
??? docs/
?   ??? sample_support_escalation.md
??? queries/
?   ??? duplicate_failed_webhooks.sql
?   ??? duplicate_users.sql
?   ??? failed_verifications.sql
?   ??? incident_pattern_summary.sql
?   ??? users_without_completed_verification.sql
??? scripts/
    ??? report.py
    ??? seed_db.py
```

## Queries Included

- `failed_verifications.sql`: recent failed verification attempts and failure reasons
- `duplicate_users.sql`: duplicate customer email records
- `users_without_completed_verification.sql`: users missing an approved verification
- `duplicate_failed_webhooks.sql`: repeated failed webhook deliveries
- `incident_pattern_summary.sql`: recurring incident signatures and timing

## Suggested GitHub Pin Description

SQL troubleshooting lab for support engineering investigations, failed verifications, webhook failures, and incident pattern analysis.
