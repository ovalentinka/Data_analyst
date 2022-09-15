---
SELECT COUNT(id)
FROM stackoverflow.posts
WHERE post_type_id=1 
   AND (score>300 OR favorites_count >= 100)
GROUP BY post_type_id;

---
SELECT ROUND(AVG(t.count),0)
FROM (
      SELECT COUNT(id),
             creation_date::date
      FROM stackoverflow.posts
      WHERE post_type_id = 1
      GROUP BY creation_date::date
      HAVING creation_date::date BETWEEN '2008-11-01' AND '2008-11-18') AS t;

---
SELECT COUNT(DISTINCT u.id)
FROM stackoverflow.badges AS b
JOIN stackoverflow.users AS u ON b.user_id=u.id
WHERE b.creation_date::date = u.creation_date::date;

---
SELECT COUNT(t.id)
FROM (
     SELECT p.id
     FROM stackoverflow.posts AS p
     JOIN stackoverflow.votes AS v ON p.id = v.post_id
     JOIN stackoverflow.users AS u ON p.user_id = u.id
     WHERE u.display_name LIKE 'Joel Coehoorn'
     GROUP BY p.id
     HAVING COUNT(v.id)>=1) as t;

---
SELECT *,
       ROW_NUMBER() OVER(ORDER BY id DESC) AS rank
FROM stackoverflow.vote_types
ORDER BY id;

---
SELECT *
FROM (
      SELECT v.user_id,
             COUNT(vt.id) AS cnt
      FROM stackoverflow.votes AS v
      JOIN stackoverflow.vote_types as vt ON vt.id = v.vote_type_id
      WHERE vt.name LIKE 'Close'
      GROUP BY v.user_id
      ORDER BY cnt DESC LIMIT 10
    ) AS t
ORDER BY t.cnt DESC, t.user_id DESC;

---
SELECT *,
      DENSE_RANK() OVER (ORDER BY t.cnt DESC) AS n
FROM (SELECT COUNT(id) AS  cnt,
             user_id
      FROM stackoverflow.badges
      WHERE creation_date::date BETWEEN '2008-11-15' AND '2008-12-15' 
      GROUP BY 2
      ORDER BY cnt DESC, user_id LIMIT 10) as t;

---
WITH t AS (
SELECT ROUND(AVG(score)) AS avg_score,
       user_id
FROM stackoverflow.posts
WHERE title IS NOT NULL 
   AND score <> 0
GROUP BY user_id
)

SELECT p.title,
       t.user_id,
       p.score,
       t.avg_score
FROM t 
JOIN stackoverflow.posts AS p ON t.user_id=p.user_id
WHERE p.title IS NOT NULL 
   AND p.score <> 0;   

---
SELECT title
FROM stackoverflow.posts
WHERE user_id IN (
                  SELECT user_id
                  FROM stackoverflow.badges
                  GROUP BY user_id
                  HAVING COUNT(id) >1000
                  )
  AND title IS NOT NULL;

---
SELECT id,
       views,
       CASE
          WHEN views>=350 THEN 1
          WHEN views<100 THEN 3
          ELSE 2
       END AS group
FROM stackoverflow.users
WHERE location LIKE '%United States%'
   AND views > 0;

---
WITH tab AS
(SELECT t.id,
        t.views,
        t.group,
        MAX(t.views) OVER (PARTITION BY t.group) AS max	
 FROM (SELECT id,
              views,
              CASE
                 WHEN views>=350 THEN 1
                 WHEN views<100 THEN 3
                 ELSE 2
              END AS group
       FROM stackoverflow.users
       WHERE location LIKE '%United States%'
          AND views > 0
          ) as t
  )
  
SELECT tab.id, 
       tab.views,  
       tab.group
FROM tab
WHERE tab.views = tab.max
ORDER BY tab.views DESC, tab.id;

---
SELECT *,
       SUM(t.cnt_id) OVER (ORDER BY t.days) as nn
FROM (
      SELECT EXTRACT(DAY FROM creation_date::date) AS days,
             COUNT(id) AS cnt_id
      FROM stackoverflow.users
      WHERE creation_date::date BETWEEN '2008-11-01' AND '2008-11-30'
      GROUP BY EXTRACT(DAY FROM creation_date::date)
      ) as t;
---
WITH p AS
(SELECT DISTINCT user_id,
        MIN(creation_date) OVER (PARTITION BY user_id) AS min_dt					
 FROM stackoverflow.posts
)

SELECT p.user_id,
       (p.min_dt - u.creation_date) AS diff
FROM stackoverflow.users AS u 
JOIN p ON  u.id = p.user_id;

---
SELECT SUM(views_count),
       DATE_TRUNC('month', creation_date)::date AS mnth
FROM stackoverflow.posts
GROUP BY DATE_TRUNC('month', creation_date)::date
ORDER BY SUM(views_count) DESC;

---
SELECT u.display_name,
       COUNT(DISTINCT p.user_id)
FROM stackoverflow.posts AS p
JOIN stackoverflow.users AS u ON p.user_id = u.id
JOIN stackoverflow.post_types AS pt ON pt.id = p.post_type_id
WHERE p.creation_date::date BETWEEN u.creation_date::date AND (u.creation_date::date + INTERVAL '1 month')
   AND pt.type LIKE '%Answer%'
GROUP BY u.display_name
HAVING COUNT(p.id) > 100
ORDER BY u.display_name;

---
WITH t AS (
           SELECT u.id
           FROM stackoverflow.posts AS p
           JOIN stackoverflow.users AS u ON p.user_id = u.id
           WHERE DATE_TRUNC('month', u.creation_date)::date = '2008-09-01'
              AND DATE_TRUNC('month', p.creation_date)::date = '2008-12-01'
           GROUP BY u.id
           HAVING COUNT(p.id)>0
          )

SELECT COUNT(p.id),
       DATE_TRUNC('month', p.creation_date)::date      
FROM stackoverflow.posts AS p
WHERE p.user_id IN (SELECT * FROM t)
   AND DATE_TRUNC('year', p.creation_date)::date = '2008-01-01'
GROUP BY DATE_TRUNC('month', p.creation_date)::date
ORDER BY DATE_TRUNC('month', p.creation_date)::date DESC;

---
SELECT user_id,
       creation_date,
       views_count,
       SUM(views_count) OVER (PARTITION BY user_id ORDER BY creation_date)						
FROM stackoverflow.posts;

---
SELECT ROUND(AVG(t.cnt))
FROM (
      SELECT user_id,
             COUNT(DISTINCT creation_date::date)  AS cnt
      FROM stackoverflow.posts
      WHERE creation_date::date BETWEEN '2008-12-01' AND '2008-12-07' 
      GROUP BY user_id
) AS t

---
WITH t AS (
SELECT EXTRACT(MONTH from creation_date::date) AS month,
       COUNT(DISTINCT id)    
FROM stackoverflow.posts
WHERE creation_date::date BETWEEN '2008-09-01' AND '2008-12-31'
GROUP BY month
)

SELECT *,
       ROUND(((count::numeric / LAG(count) OVER (ORDER BY month)) - 1) * 100,2) AS user_growth
FROM t;

---
WITH t AS (
SELECT user_id,
       COUNT(DISTINCT id) AS cnt
FROM stackoverflow.posts
GROUP BY user_id
ORDER BY cnt DESC
LIMIT 1),

     t1 AS (
SELECT p.user_id,
       p.creation_date,
       extract('week' from p.creation_date) AS week_number
FROM stackoverflow.posts AS p
JOIN t ON t.user_id = p.user_id
WHERE DATE_TRUNC('month', p.creation_date)::date = '2008-10-01'
           )

SELECT DISTINCT week_number::numeric,
       MAX(creation_date) OVER (PARTITION BY week_number)
FROM t1
ORDER BY week_number;
