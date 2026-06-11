SELECT verification_id,
       user_id,
       failure_reason,
       provider_latency_ms,
       created_at
FROM verifications
WHERE status = 'failed'
  AND created_at >= NOW() - INTERVAL '24 hours'
ORDER BY created_at DESC;
