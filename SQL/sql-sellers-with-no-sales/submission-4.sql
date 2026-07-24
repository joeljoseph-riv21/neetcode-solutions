/* using subqueries */
SELECT seller_name
FROM seller
WHERE seller_id NOT IN ( 
    SELECT seller_id
    FROM orders
    WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'  /* from orders table select(filter) the rows between the date and select sale_date from the filtered*/
    AND seller_id IS NOT NULL /* to prevent, if orders table has a single NULL value in seller_id column, the 'NOT IN' make entire query will return zero results.*/
) 
ORDER BY seller_name ASC