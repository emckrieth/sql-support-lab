# Production Support Playbook

## Purpose

This playbook describes how I would use SQL during a production support investigation.

## 1. Define the Incident

- Confirm the customer impact and timeframe.
- Identify affected users, transactions, jobs, or verification records.
- Prioritize based on severity, urgency, and business impact.

## 2. Scope With SQL

- Filter by timestamp to determine when the issue started.
- Group by status or error signature to find the most common failure modes.
- Join related records to determine whether the issue is isolated or systemic.
- Look for duplicates, missing records, delayed webhooks, or incomplete workflow states.

## 3. Validate Root Cause Signals

- Compare failed records against successful records.
- Check whether failures cluster by provider, status, region, job run, or downstream dependency.
- Confirm whether data points to an application issue, ETL issue, provider issue, or user-input issue.

## 4. Escalate Clearly

Include:

- impact summary
- query used
- affected record count
- representative record IDs
- timeframe
- suspected failure domain
- recommended next action

## 5. Confirm Recovery

- Re-run the original query after remediation.
- Confirm failed counts decrease or workflow states complete.
- Document the final query result in the incident notes.

## Production Skills Represented

- SQL troubleshooting
- Database support
- ETL investigation patterns
- Incident and problem management
- Clear stakeholder communication
