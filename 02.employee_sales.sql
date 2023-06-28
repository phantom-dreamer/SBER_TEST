SELECT employee.id, employee.name, 
COUNT(sales.price) AS sales_c, 
rank() OVER (ORDER BY COUNT(sales.price) DESC) as sales_rank_c,
sum(sales.price) as sales_s, 
rank() OVER (ORDER BY sum(sales.price) DESC) as sales_rank_s
FROM employee INNER JOIN sales ON employee.id=sales.employee_id
group by employee.id;