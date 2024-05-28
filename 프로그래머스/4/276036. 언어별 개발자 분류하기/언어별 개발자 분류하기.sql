SELECT
    (CASE #
        WHEN SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End')
            AND SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') 
            THEN 'A'
        WHEN SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') 
            THEN 'B'
        WHEN SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End')
            THEN 'C'
        ELSE NULL
     END) AS GRADE,
    d.ID, 
    d.EMAIL
FROM DEVELOPERS d
GROUP BY GRADE, ID, EMAIL
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID;