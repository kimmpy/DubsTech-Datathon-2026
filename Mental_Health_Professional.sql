CREATE TABLE nhis_clean AS
SELECT *
FROM nhis
WHERE flag IS NULL;

CREATE TABLE mental_health_counseling AS
SELECT *
FROM nhis_clean
WHERE topic = 'Counseled by a mental health professional'
  AND subgroup IN ('Health insurance coverage: Younger than 65 years',
                   'Health insurance coverage: Older than 65 years')
  AND time_period BETWEEN 2019 AND 2024;

CREATE TABLE mental_health_counseling_period AS
SELECT *,
       CASE
           WHEN time_period BETWEEN 2019 AND 2021 THEN 'Pre-COVID'
           WHEN time_period BETWEEN 2022 AND 2024 THEN 'COVID/Post-COVID'
       END AS covid_period
FROM mental_health_counseling;

CREATE TABLE mental_health_counseling_numeric AS
SELECT *,
       CAST(estimate AS REAL) AS estimate_real,
       CAST(estimate_lci AS REAL) AS estimate_lci_real,
       CAST(estimate_uci AS REAL) AS estimate_uci_real
FROM mental_health_counseling_period;

SELECT COUNT(*) AS total_rows FROM mental_health_counseling_numeric;
SELECT * FROM mental_health_counseling_numeric LIMIT 5;