SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM PATIENT P, DOCTOR D, APPOINTMENT A
WHERE 1 = 1
    AND P.PT_NO = A.PT_NO 
    AND D.DR_ID = A.MDDR_ID
    AND A.MCDP_CD = 'CS'
    AND A.APNT_CNCL_YN = 'N'
    AND TO_CHAR(A.APNT_YMD, 'YYYYMMDD') = '20220413'
ORDER BY A.APNT_YMD;