-- This script creates an index named `idx_name_first` on the `names` table.
-- The index is created only on the first letter of the `name` column
-- to optimize search queries based on the initial character.

CREATE INDEX idx_name_first ON names (name(1));
