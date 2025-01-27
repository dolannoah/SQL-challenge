-- #1
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
From "Employees" AS e
JOIN "Salary" AS s on e.emp_no = s.emp_no;