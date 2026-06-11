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

## How This Maps to Production Support

This lab demonstrates how SQL can support production incident investigation:

- identify failed transactions or verifications by status, timestamp, and failure reason
- detect duplicate user records that may create workflow or customer-impact issues
- find users missing a completed verification
- investigate repeated webhook delivery failures
- summarize recurring incident signatures for problem management

The sample database uses SQLite so the project is easy to run locally. The same query patterns translate to PostgreSQL and other production relational databases commonly used in cloud environments.

## ITIL-Style Support Practices Reflected

- **Incident management:** quickly isolate affected records and failure patterns.
- **Problem management:** group recurring error signatures to identify repeat issues.
- **Change validation:** rerun queries after remediation to confirm the data state improved.
- **Knowledge management:** document the support workflow and escalation summary.

## PostgreSQL Notes

Most queries in this lab use portable SQL. In PostgreSQL, the same investigations would typically run against production tables with indexed timestamp, status, and foreign-key columns. For larger datasets, I would add time-window filters, inspect query plans with `EXPLAIN`, and validate join behavior before using query results in an escalation.

## Project Structure

```text
SQL-lab/
|-- README.md
|-- requirements.txt
|-- db/
|   `-- .gitkeep
|-- docs/
|   |-- production_support_playbook.md
|   `-- sample_support_escalation.md
|-- queries/
|   |-- duplicate_failed_webhooks.sql
|   |-- duplicate_users.sql
|   |-- failed_verifications.sql
|   |-- incident_pattern_summary.sql
|   |-- postgres_recent_failures.sql
|   `-- users_without_completed_verification.sql
`-- scripts/
    |-- report.py
    `-- seed_db.py
```

## Queries Included

- `failed_verifications.sql`: recent failed verification attempts and failure reasons
- `duplicate_users.sql`: duplicate customer email records
- `users_without_completed_verification.sql`: users missing an approved verification
- `duplicate_failed_webhooks.sql`: repeated failed webhook deliveries
- `incident_pattern_summary.sql`: recurring incident signatures and timing
- `postgres_recent_failures.sql`: PostgreSQL-style recent failure analysis with a time window

## Suggested GitHub Pin Description

SQL troubleshooting lab for support engineering investigations, failed verifications, webhook failures, and incident pattern analysis.
