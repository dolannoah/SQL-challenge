-- List the frequency counts, in descending order, 
-- of all the employee last names (how many employees share each last name)

SELECT 
last_name,
COUNT(last_name) AS "name_count" 
FROM "Employees"
GROUP By last_name;