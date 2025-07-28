-- This script creates a composite index named `idx_name_first_score`
-- on the `names` table. The index covers the first letter of the `name`
-- column and the entire `score` column to optimize search queries
-- that filter on both attributes.

CREATE INDEX idx_name_first_score ON names (name(1), score);