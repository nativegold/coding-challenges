SELECT PRODUCT_CODE, PRICE * SALES_AMOUNT AS SALES
FROM PRODUCT p, 
    (
        SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS SALES_AMOUNT
        FROM OFFLINE_SALE
        GROUP BY PRODUCT_ID
    ) s
WHERE p.PRODUCT_ID = s.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE ASC
