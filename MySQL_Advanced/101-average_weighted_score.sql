-- This script creates a stored procedure `ComputeAverageWeightedScoreForUsers`
-- that computes and stores the average weighted score for all students.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers () BEGIN
UPDATE users AS u
JOIN (
	SELECT
		c.user_id,
		SUM(c.score * p.weight) / SUM(p.weight) AS weighted_avg
	FROM
		corrections AS c
		JOIN projects AS p ON c.project_id = p.id
	GROUP BY
		c.user_id
) AS user_weighted_scores ON u.id = user_weighted_scores.user_id
SET
	u.average_score = user_weighted_scores.weighted_avg;

END;

$$ DELIMITER;
