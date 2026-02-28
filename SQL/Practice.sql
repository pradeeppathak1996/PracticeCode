-- Duplicate email from users table --

SELECT email 
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- SECOND HIGHEST VALUE --

SELECT MAX(salary)
FROM emp
WHERE salary < (SELECT MAX(salary) FROM emp);

-- Duplicate Records Delete --

DELETE FROM emp
WHERE id NOT IN(
    SELECT MIN(id)
    FROM emp
    GROUP BY email 
    );

-- Employees with No Department --

SELECT emp.*
FROM emp
LEFT JOIN dept
ON emp.dept_id = dept.dept_id
WHERE dept.dept_id IS NULL;

-- Find employees earning more than average salary --

SELECT *
FROM emp
WHERE salary > (SELECT AVG(salary) FROM emp);

-- Salary same but different employees --

SELECT salary 
FROM emp
GROUP BY salary
HAVING COUNT (*) > 1

-- Fetch last 5 records --

SELECT *
FROM emp
ORDER BY id DESC
LIMIT 5;

------------------------ 2 TABLES RELATED QUERIES -----------------------

-- Employee with Department Name -- INNER JOIN --

SELECT d.dept_name , e.emp_name
FROM Employee e
INNER JOIN Department d
ON e.dept_id = d.dept_id;

-- Employees Without Department -- IMP.
-- Employees Whose Department Does Not Exist -- same question

SELECT d.emp_name
FROM Employee e
LEFT JOIN Department d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

--  Employees with Department (Including No Dept) --

SELECT e.emp_name , d.dept_name
FROM Employee
LEFT JOIN Department
ON e.dept_id = d.emp_id;

-- Count Employees in Each Department --

SELECT d.dept_name, COUNT(e.emp_name) AS total_emp
FROM Department e
LEFT JOIN Employee e
ON d.dept_id = e.dept_id
GROUP BY dept_name;

-- Departments Having More Than 3 Employees--

select d.dept_name
FROM Department d
JOIN Employee e
ON d.dept_id = e.dept_id
GROUP BY dept_name
HAVING COUNT (e.emp_id) > 3;

-- Employees Earning More Than Department Average --

SELECT emp_name, salary
FROM emp e
WHERE salary >
(
    SELECT AVG(salary)
    FROM emp
    WHERE dept_id = e.dept_id
);

-- Highest Salary in Each Department --

SELECT d.dept_name, MAX(e.salary) AS max_salary
FROM department d
JOIN employee e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- To get employee name also --

SELECT e.emp_name, e.salary, e.dept_id
FROM employee e
JOIN (
    SELECT dept_id, MAX(salary) AS max_salary
    FROM employee
    GROUP BY dept_id
) d
ON e.dept_id = d.dept_id AND e.salary = d.max_salary;

-- Employee with Highest Salary Overall + Dept Name --

SELECT e.emp_name, e.salary, d.dept_name
FROM employee e
JOIN department d
ON e.dept_id = d.dept_id
WHERE e.salary = (SELECT MAX(salary) FROM employee);

-- Delete Employees Without Department --

DELETE e
FROM employee e
LEFT JOIN department d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

-- Update Salary Based on Department --

UPDATE employee e
JOIN department d
ON e.dept_id = d.dept_id
SET e.salary = e.salary + 5000
WHERE d.dept_name = 'IT';

-- Fetch Employees from Same Department --

SELECT e1.emp_name, e2.emp_name
FROM employee e1
JOIN employee e2
ON e1.dept_id = e2.dept_id
AND e1.emp_id <> e2.emp_id;

-- 3 trasactions --

SELECT user_id, paid, transaction_date
FROM (
    SELECT
        user_id,
        paid,
        transaction_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY transaction_date
        ) AS rn
    FROM transactions
) t
WHERE rn = 3;