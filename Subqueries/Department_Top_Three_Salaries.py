"""
SELECT 
    Department.name as Department, Employee.name as Employee, salary as Salary
FROM Employee
JOIN Department
ON Employee.departmentId = Department.id
WHERE (departmentId, salary) 
IN 
    (SELECT departmentId, salary
    FROM
        (SELECT departmentId, salary,
            DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS ranking
        FROM Employee) AS X
    WHERE
        ranking <= 3)
"""
