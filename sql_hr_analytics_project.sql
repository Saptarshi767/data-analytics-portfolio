-- HR Analytics SQL Project
-- Table schemas
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    gender VARCHAR(10),
    dept_id INT,
    salary DECIMAL(10,2),
    years_at_company INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE attrition (
    emp_id INT,
    attrition_date DATE,
    reason VARCHAR(100),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

-- Sample data
INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales');

INSERT INTO employees VALUES
(1, 'Asha', 'Female', 1, 50000, 3),
(2, 'Ravi', 'Male', 2, 70000, 5),
(3, 'Priya', 'Female', 3, 60000, 2),
(4, 'Vikram', 'Male', 2, 80000, 7),
(5, 'Neha', 'Female', 1, 52000, 4);

INSERT INTO attrition VALUES
(3, '2024-05-01', 'Resigned'),
(5, '2024-04-15', 'Retired');

-- Example queries
-- 1. Attrition rate
SELECT ROUND(COUNT(a.emp_id) * 100.0 / (SELECT COUNT(*) FROM employees), 2) AS attrition_rate_percent
FROM attrition a;

-- 2. Average salary by department
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- 3. Gender distribution
SELECT gender, COUNT(*) AS count
FROM employees
GROUP BY gender;

-- 4. Average years at company
SELECT AVG(years_at_company) AS avg_years
FROM employees; 