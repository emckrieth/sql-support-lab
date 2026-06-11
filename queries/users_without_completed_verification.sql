SELECT u.user_id,
       u.email
FROM users u
LEFT JOIN verifications v
  ON u.user_id = v.user_id
 AND v.status = 'approved'
WHERE v.verification_id IS NULL;
