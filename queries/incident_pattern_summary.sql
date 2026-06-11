SELECT error_signature,
       COUNT(*) AS incident_count,
       MIN(opened_at) AS first_seen,
       MAX(opened_at) AS last_seen
FROM incidents
GROUP BY error_signature
ORDER BY incident_count DESC;
