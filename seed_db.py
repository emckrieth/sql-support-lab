SELECT verification_id, delivery_status, COUNT(*) AS cnt
FROM webhooks
WHERE delivery_status = 'failed'
GROUP BY verification_id, delivery_status
HAVING COUNT(*) > 1;
