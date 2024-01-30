ALTER TABLE payments_this_year
ALTER column payment_date  TYPE timestamp(0);

ALTER TABLE payments_this_year
DROP COLUMN payment_id;


UPDATE payments_this_year
SET staff_id =1
WHERE amount = 3.99 and customer_id IN (87, 137)
;
UPDATE payments_this_year
SET amount = amount + 0.50
WHERE payment_date > '2007-03-22';

ALTER TABLE payments_this_year
RENAME COLUMN amount TO total_payment_taken;

SELECT * 
FROM payments_this_year;