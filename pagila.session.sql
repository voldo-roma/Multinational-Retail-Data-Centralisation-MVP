-- main sql commands and ordering
SELECT actor.first_name, COUNT(film_actor.film_id) as film_count
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id 
--WHERE first_name LIKE 'A%'
GROUP BY 1
HAVING COUNT(film_actor.film_id) > 31
ORDER BY first_name
