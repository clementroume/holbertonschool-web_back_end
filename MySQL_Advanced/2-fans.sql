-- This script ranks country origins of bands, ordered by the number of (non-unique) fans.
-- It calculates the total number of fans for each country and lists them in descending order.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
