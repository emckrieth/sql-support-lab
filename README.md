# SQL Support Lab

A support-focused SQL investigation lab built to demonstrate how I approach data troubleshooting in a technical support environment.

This project simulates common production support scenarios such as:
- investigating failed verifications
- identifying duplicate user records
- tracing webhook delivery failures
- correlating incidents with underlying service behavior
- validating whether issues are caused by data, workflow, or application behavior

## Purpose

I built this lab to show practical SQL usage in a support engineering context rather than a pure analytics or database engineering context. The goal is to reflect the kind of investigation work involved in technical support roles where SQL helps confirm patterns, isolate impact, and speed up root cause analysis.

## Tech Stack

- Python
- SQLite
- SQL

## Project Structure

```text
sql-support-lab/
├── README.md
├── requirements.txt
├── db/
│   └── support_lab.db
├── queries/
│   ├── failed_verifications.sql
│   ├── duplicate_users.sql
│   ├── webhook_failures.sql
│   ├── incident_correlation.sql
│   └── latency_analysis.sql
└── scripts/
    └── seed_data.py
