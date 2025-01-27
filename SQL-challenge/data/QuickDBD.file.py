# -- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
# -- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE "Employees"(
    "emp_no" INT NOT NULL,
    "emp_title_id" INT NOT NULL,
    "birth_date" VARCHAR(50) NOT NULL,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(50) NOT NULL,
    "sex" VARCHAR(5) NOT NULL,
    "hire_date" DATE NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY ("emp_no")
);

CREATE TABLE "Departments"(
    "dept_no" VARCHAR(30) NOT NULL,
    "dept_name" VARCHAR(30) NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY ("dept_no")
);

CREATE TABLE "Titles"(
    "title_id" INT NOT NULL,
    "title" VARCHAR(50) NOT NULL,
    CONSTRAINT "pk_Titles" PRIMARY KEY ("title_id")
);

CREATE TABLE "Department_Employee"(
    "emp_no" INT NOT NULL,
    "dept_no" VARCHAR(30) NOT NULL,
    CONSTRAINT "pk_Department_Employee" PRIMARY KEY ("emp_no", "dept_no")
);

CREATE TABLE "Salary"(
    "emp_no" INT NOT NULL, 
    "salary" INT NOT NULL,
    CONSTRAINT "pk_Salary" PRIMARY KEY ("emp_no")
);

CREATE TABLE "Department_Manager"(
    "dept_no" VARCHAR(30) NOT NULL,
    "emp_no" INT NOT NULL,
    CONSTRAINT "pk_Department_Manager" PRIMARY KEY ("dept_no", "emp_no")
);

-- Foreign Key Constraints
ALTER TABLE "Employees" ADD CONSTRAINT "fk_Employees_employee_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "Titles" ("title_id");

ALTER TABLE "Department_Employee" ADD CONSTRAINT "fk_Department_Employee_department_number" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_no");

ALTER TABLE "Salary" ADD CONSTRAINT "fk_Salary_employee_number" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "Department_Manager" ADD CONSTRAINT "fk_Department_Manager_department_number" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_no");

ALTER TABLE "Department_Manager" ADD CONSTRAINT "fk_Department_Manager_employee_number" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

SELECT * FROM Departments;   ERROR:  relation "departments" does not exist
LINE 1: SELECT * FROM Departments;
                      ^ 

SQL state: 42P01
Character: 15