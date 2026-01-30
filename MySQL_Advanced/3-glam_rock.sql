-- This script lists all bands with 'Glam rock' as their main style,
-- ranked by their longevity.
-- The lifespan is calculated using the 'formed' and 'split' attributes.
-- For bands that have not split, 2024 is used as the reference year.

SELECT 
	band_name,
	(IFNULL(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
