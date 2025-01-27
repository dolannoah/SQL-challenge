-- #6 List each employee in the Sales department, 
-- including their employee number, last name, and first name

SELECT 
e.emp_no, 
e.last_name, 
e.first_name,
d.dept_name
FROM 
"Employees" AS e
JOIN 
"Department_Employee" AS de ON e.emp_no = de.emp_no
JOIN 
"Departments" AS d ON de.dept_no = d.dept_no
WHERE 
d.dept_name = 'Sales';
