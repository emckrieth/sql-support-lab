# Sample Support Escalation

**Issue:** Customer reports repeated failed verification attempts.

**Steps performed:**

- Queried verification records for recent failures
- Confirmed repeated `provider timeout` failures
- Checked webhook records and found duplicate failed deliveries
- Compared the error signature against incident history

**Conclusion:**

Issue appears tied to repeated downstream provider timeouts rather than invalid user data.

**Recommended next step:**

Escalate to engineering with affected verification IDs, request timestamps, webhook delivery attempts, and the matching incident signature.
