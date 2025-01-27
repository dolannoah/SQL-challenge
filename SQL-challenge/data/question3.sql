-- #3 List the manager of each department ("Employees with department manager")
-- along with their department number, ("Department_Manager")
-- department name, "Departments"
-- employee number, last name, and first name ("Employees")
SELECT e.emp_no,
e.first_name,
e.last_name,
m.emp_no,
d.dept_name,
d.dept_no
FROM "Employees" AS e
JOIN "Department_Manager" AS m ON e.emp_no = m.emp_no
JOIN "Departments" AS d ON d.dept_no = m.dept_no; 