-- #2
SELECT first_name,
last_name,
hire_date
FROM "Employees"
WHERE TO_CHAR(TO_DATE(hire_date, 'MM/DD/YYYY'), 'YYYY') = '1986';
