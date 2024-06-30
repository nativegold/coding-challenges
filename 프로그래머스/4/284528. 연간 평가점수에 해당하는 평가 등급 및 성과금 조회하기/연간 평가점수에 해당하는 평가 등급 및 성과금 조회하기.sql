SELECT s.EMP_NO AS EMP_NO,
    s.EMP_NAME AS EMP_NAME,
    s.GRADE AS GRADE,
    CASE
        WHEN s.GRADE = 'S'
        THEN s.SAL * 0.2
        WHEN s.GRADE = 'A'
        THEN s.SAL * 0.15
        WHEN s.GRADE = 'B'
        THEN s.SAL * 0.1
        ELSE 0
    END BONUS
FROM (
    SELECT e.EMP_NO AS EMP_NO, 
        e.EMP_NAME AS EMP_NAME,
        e.SAL AS SAL,
        CASE
            WHEN g.SCORE >= 96
            THEN 'S'
            WHEN g.SCORE >= 90
            THEN 'A'
            WHEN g.SCORE >= 80
            THEN 'B'
            ELSE 'C'
        END GRADE
    FROM HR_EMPLOYEES e, 
        (SELECT EMP_NO, AVG(SCORE) SCORE
         FROM HR_GRADE g 
         GROUP BY EMP_NO) g
    WHERE 1=1 
        AND e.EMP_NO = g.EMP_NO
) s