-- main sql commands and ordering
SELECT actor.first_name, COUNT(film_actor.film_id) as film_count FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
WHERE first_name LIKE 'A%'
GROUP BY actor.first_name
HAVING film_count > 31
ORDER BY first_name
LIMIT 3
-- to this, visually showing the order in which the statement will execute
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
WHERE first_name LIKE 'A%'
GROUP BY actor.first_name
HAVING film_count > 31
SELECT actor.first_name, COUNT(film_actor.film_id) as film_count
ORDER BY first_name
LIMIT 3