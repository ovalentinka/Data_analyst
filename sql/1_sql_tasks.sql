---
SELECT COUNT(status)
FROM company
GROUP BY status 
HAVING status LIKE 'closed';

---
SELECT funding_total
FROM company
WHERE category_code LIKE 'news' 
   AND country_code LIKE 'USA'
ORDER BY funding_total DESC;

---
SELECT SUM(price_amount)
FROM acquisition
WHERE term_code LIKE 'cash'
   AND EXTRACT(YEAR from acquired_at) BETWEEN 2011 AND 2013
GROUP BY term_code;

---
SELECT first_name,
       last_name,
       twitter_username
FROM people
WHERE twitter_username LIKE 'Silver%';

---
SELECT *
FROM people
WHERE twitter_username LIKE '%money%'
   AND last_name LIKE 'K%';

---
SELECT country_code,
       SUM(funding_total)
FROM company
GROUP BY country_code
ORDER BY SUM(funding_total) DESC;

---
SELECT  funded_at,
        MIN(raised_amount),
        MAX(raised_amount)
FROM funding_round
GROUP BY  funded_at
HAVING MIN(raised_amount) NOT IN (0, MAX(raised_amount));

---
SELECT *,
   CASE 
       WHEN invested_companies >= 100 THEN 'high_activity'
       WHEN invested_companies BETWEEN 20 AND 99 THEN 'middle_activity'
       ELSE 'low_activity'
   END    
FROM fund;

---
SELECT CASE
           WHEN invested_companies>=100 THEN 'high_activity'
           WHEN invested_companies>=20 THEN 'middle_activity'
           ELSE 'low_activity'
       END AS activity, 
       ROUND(AVG(investment_rounds))
FROM fund
GROUP BY activity
ORDER BY ROUND(AVG(investment_rounds));

---
SELECT country_code,
       MIN(invested_companies),
       MAX(invested_companies),
       AVG(invested_companies)
FROM (SELECT *
      FROM fund
      WHERE EXTRACT(YEAR FROM founded_at) BETWEEN 2010 AND 2012) AS f
GROUP BY country_code
HAVING MIN(invested_companies) > 0
ORDER BY AVG(invested_companies) DESC
LIMIT 10;

---
SELECT p.first_name,
       p.last_name,
       e.instituition
FROM people AS p
LEFT JOIN education AS e ON p.id = e.person_id;

---
SELECT c.name, 
       COUNT(DISTINCT tab2.instituition)
FROM company AS c
LEFT JOIN 
         (SELECT tab1.instituition,
                 p.company_id
          FROM       
               (SELECT person_id,
                       instituition 
                FROM education 
                WHERE instituition  IS NOT NULL
               ) AS tab1
          INNER JOIN  people AS p ON p.id = tab1.person_id
         ) AS tab2 ON tab2.company_id = c.id
GROUP BY c.name
ORDER BY COUNT(DISTINCT tab2.instituition) DESC
LIMIT 5;

---
SELECT DISTINCT name
FROM company
WHERE status LIKE 'closed'
   AND id IN (SELECT company_id
              FROM funding_round
              WHERE is_first_round = 1 
                 AND is_last_round = 1);

---
SELECT DISTINCT p.id
FROM company AS c
INNER JOIN people AS p ON c.id = p.company_id
WHERE c.status LIKE 'closed'
   AND c.id IN (SELECT company_id
                FROM funding_round
                WHERE is_first_round = 1
                   AND is_last_round = 1);

---
SELECT DISTINCT p.id,
                e.instituition
FROM company AS c
INNER JOIN people AS p ON c.id = p.company_id
LEFT JOIN education AS e ON p.id = e.person_id
WHERE c.status LIKE 'closed'
   AND c.id IN (SELECT company_id
                FROM funding_round
                WHERE is_first_round = 1
                   AND is_last_round = 1)
   AND  e.instituition IS NOT NULL;


---
SELECT DISTINCT p.id,
                COUNT(e.instituition)
FROM company AS c
INNER JOIN people AS p ON c.id = p.company_id
LEFT JOIN education AS e ON p.id = e.person_id
WHERE c.status LIKE 'closed'
  AND c.id IN (SELECT company_id
               FROM funding_round
               WHERE is_first_round = 1
                  AND is_last_round = 1)
  AND  e.instituition IS NOT NULL
GROUP BY p.id;

---
SELECT AVG(tab1.count_in)
FROM (SELECT DISTINCT p.id,
             COUNT(e.instituition) AS count_in
      FROM company AS c
      INNER JOIN people AS p ON c.id = p.company_id
      LEFT JOIN education AS e ON p.id = e.person_id
      WHERE c.status LIKE 'closed'
        AND c.id IN (SELECT company_id
                     FROM funding_round
                     WHERE is_first_round = 1
                        AND is_last_round = 1)
        AND  e.instituition IS NOT NULL
      GROUP BY p.id) AS tab1;

---
SELECT AVG(tab1.count_in)
FROM (SELECT DISTINCT p.id,
             COUNT(e.instituition) AS count_in
      FROM company AS c
      INNER JOIN people AS p ON c.id = p.company_id
      LEFT JOIN education AS e ON p.id = e.person_id
      WHERE c.name LIKE 'Facebook'
         AND  e.instituition IS NOT NULL
      GROUP BY p.id
      ) AS tab1;

---
SELECT f.name AS name_of_fund, 
       C.name AS name_of_company, 
       fr.raised_amount AS amount
FROM investment AS i
JOIN company AS c ON i.company_id=c.id
JOIN fund AS f ON i.fund_id=f.id
JOIN funding_round AS fr ON i.funding_round_id = fr.id
WHERE EXTRACT(YEAR FROM fr.funded_at) BETWEEN 2012 AND 2013
   AND c.milestones > 6;

---
SELECT company.name AS acquiring_company,
       tab2.price_amount,
       tab2.acquired_company,
       tab2.funding_total,
       ROUND(tab2.price_amount / tab2.funding_total)
FROM
(
    SELECT c.name AS acquired_company,
           c.funding_total,
           tab1.acquiring_company_id,
           tab1.price_amount
    FROM company AS c
    RIGHT JOIN (
                SELECT acquiring_company_id,
                       acquired_company_id,
                       price_amount
                FROM acquisition
                WHERE price_amount > 0
               ) AS tab1 ON c.id = tab1.acquired_company_id
 ) AS tab2 LEFT JOIN company ON company.id  = tab2.acquiring_company_id
WHERE tab2.funding_total > 0
ORDER BY  tab2.price_amount DESC, tab2.acquired_company
LIMIT 10;

---
SELECT c.name,
       tab1.month
FROM company AS c
RIGHT JOIN (
             SELECT company_id,
             EXTRACT(MONTH FROM funded_at) AS month
             FROM funding_round
             WHERE EXTRACT(YEAR FROM funded_at) BETWEEN 2010 AND 2013
            ) AS tab1 ON c.id = tab1.company_id
WHERE c.category_code LIKE 'social';

---
WITH
-- выбираем месяц инвестиционных раундов в 2010-2013 гг
tab1 AS (SELECT EXTRACT(MONTH FROM funded_at) AS month,
                id AS funding_round_id
                FROM funding_round
         WHERE EXTRACT(YEAR FROM funded_at) BETWEEN 2010 AND 2013
         ),

-- считаем кол-во купленных и общую сумму по сделкам за 2010-2013 гг в разрезе месяца
tab2 AS (SELECT EXTRACT(MONTH FROM acquired_at) AS month,
                COUNT(acquired_company_id) AS count_acquired,
                SUM(price_amount) AS total_amount
         FROM acquisition
         WHERE EXTRACT(YEAR FROM acquired_at) BETWEEN 2010 AND 2013
         GROUP BY EXTRACT(MONTH FROM acquired_at)
        ),

-- ищем фонды из США
tab3 AS (SELECT i.funding_round_id,
                f.name
        FROM investment AS i
        JOIN fund AS f ON f.id = i.fund_id
        WHERE fund_id IN (SELECT id
                          FROM fund
                          WHERE country_code LIKE 'USA')
        ),

tab4 AS (SELECT month,
                COUNT(DISTINCT name) AS count_USA
         FROM tab1 
         LEFT JOIN tab3 ON tab1.funding_round_id = tab3.funding_round_id
         GROUP BY month)
         
SELECT tab4.month,
       tab4.count_USA,
       tab2.count_acquired,
       tab2.total_amount
FROM tab4 
LEFT JOIN tab2 ON tab4.month = tab2.month;


---
WITH

total_11 AS (SELECT AVG(funding_total) AS total_2011,
                      country_code
               FROM company
               GROUP BY country_code,
               EXTRACT(YEAR FROM founded_at)
               HAVING EXTRACT(YEAR FROM founded_at) = 2011),
               
total_12 AS (SELECT AVG(funding_total) AS total_2012,
                      country_code
               FROM company
               GROUP BY country_code,
               EXTRACT(YEAR FROM founded_at)
               HAVING EXTRACT(YEAR FROM founded_at) = 2012),

total_13 AS (SELECT AVG(funding_total) AS total_2013,
                      country_code
               FROM company
               GROUP BY country_code,
               EXTRACT(YEAR FROM founded_at)
               HAVING EXTRACT(YEAR FROM founded_at) = 2013)

SELECT total_11.country_code,
       total_11.total_2011,
       total_12.total_2012,
       total_13.total_2013
FROM total_11 
INNER JOIN total_12 ON total_11.country_code = total_12.country_code
INNER JOIN total_13 ON total_11.country_code = total_13.country_code
ORDER BY total_11.total_2011 DESC;
