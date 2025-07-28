-- This script creates a function `SafeDiv` that divides the first number
-- by the second number. If the second number is 0, it returns 0.

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END;
$$
DELIMITER ;