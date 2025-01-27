-- #4 List the department number for each employee along with that employee’s employee number 
-- (all of Department_Employee)
-- last name, first name (Employees), 
-- and department name(Departments.department_name).

SELECT 
de.dept_no,
e.emp_no,
e.last_name,
e.first_name,
d.dept_name
FROM "Department_Employee" AS de
JOIN "Employees" AS e ON e.emp_no = de.emp_no
JOIN "Departments" AS d on d.dept_no = de.dept_no;

SELECT * FROM "Departments";

SELECT * FROM "Department_Employee";

SELECT * FROM "Employees";

