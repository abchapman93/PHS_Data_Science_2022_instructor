
USE PHS;
SELECT * FROM PHS.value_set;
SELECT * FROM PHS.value_set_value;

CREATE TEMPORARY TABLE pna_dx
SELECT 
	dx.subject_id
    ,dx.hadm_id
    ,dx.code
    ,dx.description
FROM PHS.value_set_value val
	INNER JOIN PHS.value_set vs
		ON val.value_set_id = vs.value_set_id
	INNER JOIN mimic2.icd9 dx 
		ON val.code_value = dx.code
WHERE vs.value_set_name = 'icd9_pneumonia';

SELECT 
	a.subject_id
    ,a.hadm_id
    ,disch_dt
    ,dod
    ,p.sex
    ,d.ethnicity_descr
    ,DATEDIFF(disch_dt, dob) / 365 age_at_discharge
    ,CASE 
		WHEN CAST(DATEDIFF(disch_dt, dob) / 365 AS SIGNED) < 18 THEN '<18'
        WHEN CAST(DATEDIFF(disch_dt, dob) / 365 AS SIGNED) BETWEEN 18 AND 35 THEN '18-35'
        WHEN CAST(DATEDIFF(disch_dt, dob) / 365 AS SIGNED) BETWEEN 36 AND 65 THEN '36-65'
        WHEN CAST(DATEDIFF(disch_dt, dob) / 365 AS SIGNED) BETWEEN 66 AND 90 THEN '66-90'
        ELSE '91+'
    END AS age_at_discharge_binned
    ,CASE WHEN pna.hadm_id IS NULL THEN 0 ELSE 1 END AS pna
    ,DATEDIFF(dod, disch_dt) time_to_death
    ,CASE WHEN CAST(DATEDIFF(dod, disch_dt) AS SIGNED) <= 30 THEN 1 ELSE 0 END AS mortality_30_day
    FROM mimic2.admissions a
    LEFT OUTER JOIN (
        SELECT DISTINCT
        dx.hadm_id
    FROM PHS.value_set_value val
        INNER JOIN PHS.value_set vs
            ON val.value_set_id = vs.value_set_id
        INNER JOIN mimic2.icd9 dx 
            ON val.code_value = dx.code
    WHERE vs.value_set_name = 'icd9_pneumonia'
    ) pna
		ON a.hadm_id = pna.hadm_id
	INNER JOIN mimic2.d_patients p
		ON a.subject_id = p.subject_id
	INNER JOIN mimic2.demographic_detail d
		ON p.subject_id = d.subject_id
WHERE disch_dt != dod
	AND a.hadm_id = 26649;

SELECT *
FROM mimic2.admissions
WHERE hadm_id = 26649;

SELECT DISTINCT
	dx.hadm_id
FROM PHS.value_set_value val
	INNER JOIN PHS.value_set vs
		ON val.value_set_id = vs.value_set_id
	INNER JOIN mimic2.icd9 dx 
		ON val.code_value = dx.code
WHERE vs.value_set_name = 'icd9_pneumonia'
AND hadm_id = 26649;

