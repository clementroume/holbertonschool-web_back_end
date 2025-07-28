-- This script creates a stored procedure `ComputeAverageWeightedScoreForUser`
-- that computes and stores the average weighted score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN p_user_id INT) BEGIN DECLARE weighted_avg FLOAT;

-- Calculate the weighted average score for the specified user
SELECT
	SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg
FROM
	corrections AS c
	JOIN projects AS p ON c.project_id = p.id
WHERE
	c.user_id = p_user_id;

-- Update the user's average score in the 'users' table
UPDATE users
SET
	average_score = weighted_avg
WHERE
	id = p_user_id;

END;

$$ DELIMITER;
