SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY TO_CHAR(DATETIME, 'HH24')
HAVING 1=1 
    AND TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) >= 9 
    AND TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) < 20
ORDER BY TO_NUMBER(TO_CHAR(DATETIME, 'HH24'));