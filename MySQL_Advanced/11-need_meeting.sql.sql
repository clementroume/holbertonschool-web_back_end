-- This script creates a view named `need_meeting` that lists all students
-- who have a score strictly under 80 and either have no `last_meeting` date
-- or their last meeting was more than one month ago.
CREATE VIEW
	need_meeting AS
SELECT
	name
FROM
	students
WHERE
	score < 80
	AND (
		last_meeting IS NULL
		OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
	);