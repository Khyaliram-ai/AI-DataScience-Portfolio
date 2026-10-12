create database sales_analysis;
use sales_analysis;

create table sales(
order_id int primary key,
customer_name varchar(50),
city varchar (50),
product varchar(50),
category varchar(50),
quantity int ,
price decimal(10,2),
sales_date DATE,
payment_method varchar(20)
);


INSERT INTO sales VALUES
(1001, 'Aman', 'Jaipur', 'Laptop', 'Electronics', 1, 55000, '2026-01-05', 'UPI'),
(1002, 'Priya', 'Delhi', 'Mouse', 'Electronics', 2, 800, '2026-01-06', 'Card'),
(1003, 'Ravi', 'Mumbai', 'Keyboard', 'Electronics', 1, 1500, '2026-01-07', 'UPI'),
(1004, 'Neha', 'Jaipur', 'Chair', 'Furniture', 2, 4500, '2026-01-08', 'Cash'),
(1005, 'Arjun', 'Delhi', 'Laptop', 'Electronics', 1, 62000, '2026-01-10', 'Card'),
(1006, 'Simran', 'Mumbai', 'Desk', 'Furniture', 1, 7000, '2026-01-11', 'UPI'),
(1007, 'Pooja', 'Jaipur', 'Headphones', 'Electronics', 3, 2000, '2026-01-12', 'UPI'),
(1008, 'Rahul', 'Bangalore', 'Monitor', 'Electronics', 2, 15000, '2026-01-14', 'Card'),
(1009, 'Anjali', 'Delhi', 'Chair', 'Furniture', 1, 5000, '2026-01-15', 'Cash'),
(1010, 'Vikas', 'Mumbai', 'Laptop', 'Electronics', 2, 58000, '2026-01-17', 'UPI'),
(1011, 'Kiran', 'Jaipur', 'Desk', 'Furniture', 2, 7500, '2026-01-18', 'Card'),
(1012, 'Mohit', 'Bangalore', 'Mouse', 'Electronics', 5, 750, '2026-01-20', 'UPI'),
(1013, 'Sneha', 'Delhi', 'Headphones', 'Electronics', 2, 2500, '2026-01-21', 'Card'),
(1014, 'Rohit', 'Jaipur', 'Monitor', 'Electronics', 1, 14000, '2026-01-23', 'UPI'),
(1015, 'Nisha', 'Mumbai', 'Chair', 'Furniture', 3, 4800, '2026-01-25', 'Cash'),
(1016, 'Aditya', 'Bangalore', 'Laptop', 'Electronics', 1, 60000, '2026-01-27', 'Card'),
(1017, 'Meena', 'Jaipur', 'Keyboard', 'Electronics', 2, 1800, '2026-01-28', 'UPI'),
(1018, 'Sahil', 'Delhi', 'Desk', 'Furniture', 1, 8000, '2026-01-29', 'Card'),
(1019, 'Komal', 'Mumbai', 'Mouse', 'Electronics', 4, 900, '2026-01-30', 'UPI'),
(1020, 'Varun', 'Bangalore', 'Monitor', 'Electronics', 2, 16000, '2026-01-31', 'Card');


-- Q1. Display all orders.
select *
from sales ;

-- Q2. Display only the customer name and product.
select customer_name ,product
from sales;

-- Q3. Find all orders from Jaipur.
select * 
from sales 
where city = "jaipur";

-- Q4. Find all orders where the price is greater than 10,000.
select *
from sales
where price > 10000;

-- Q5. Find all orders from the Electronics category.
select *
from sales
where category = "Electronics";

-- Q6. Find all Electronics orders from Jaipur.
select *
from sales 
where city = "jaipur"
and category = "Electronics" ;

-- Q7. Find all orders where the quantity is 2 or more.
select *
from sales 
where quantity >= 2;

-- Q8. Find all orders where the price is less than 5,000 OR the quantity is greater than 4.
select * 
from sales 
where price < 5000 OR quantity > 4;

-- Q9. Find all orders from Delhi where the payment method is Card.
select *
from sales 
where city = "Delhi" 
and payment_method = "card";

-- Q10. Find all Electronics orders where the price is greater than 50,000 .
select *
from sales 
where category = "Electronics" and price > 50000;

-- Q11. Find all orders from Jaipur or Delhi.
select * 
from sales 
where city ="Dehli" OR city ="Jaipur";

-- Q12. Find all orders where the price is between 5,000 and 20,000.
select *
from sales 
where price  between 5000.0 and 20000.0;

-- Q13. Find all orders where the city is Jaipur, the category is Electronics, and the quantity is 2 or more.
select *
from sales 
where city ="Jaipur" and category ="Electronics" and quantity > 2;

-- Q14. Find all Electronics orders from Mumbai where the price is greater than 1,000.
select * 
from sales 
where city ="Mumbai" and category ="Electronics" and price > 1000;

-- Q15. Find all orders where the city is Delhi or Mumbai, the category is Electronics, and the quantity is 2 or more.
select * 
from sales 
WHERE City in ('Delhi', 'Mumbai') 
and Category = 'Electronics' 
and Quantity >= 2;

-- 5 New Questions 
-- Q1. 
select * 
from sales 
where city ="jaipur" 
and category = "Furniture";

-- Q2.
select *
from sales 
where Quantity >= 3 
and payment = "UPI";

select * 
from sales 
where city in ("Delhi" ,"Banglore")
and category = "Electronics";

select * 
from sales 
where Quantity between 10000 and 60000;

select * 
from orders 
where (city = 'Jaipur' or city = 'Delhi')
  and category = 'Electronics'
  and quantity >= 2
  and price > 1500;

 
  
-- Day 2 : Practice 


-- Q1. Display all unique cities.
select distinct city
from sales ;  

-- Q2. Display all unique product names.
select distinct product
from sales;

-- Q3. Display all unique categories.
select distinct category 
from sales;

-- Q4. Display all unique payment methods.
select distinct payment_method 
from sales;


-- Ordered by close
select * 
from sales
order by  price ASC;

select * 
from sales 
order by price DESC;

-- Q5. Display all orders sorted by price from lowest to highest.
select * 
from sales 
order by price ASC;

-- Q6. Display all orders sorted by price from highest to lowest.
select * 
from sales 
order by price DESC;

-- Q7. Display all orders sorted by quantity from highest to lowest.
select * 
from sales 
order by quantity DESC;

-- Q8. Display all orders sorted by sales date from oldest to newest.
select * 
from sales 
order by sales_date ASC;


-- LIMIT questions practice 
select * 
from sales 
limit 5;

select * 
from sales 
order by price DESC
limit 5;

-- Q9. Display the top 5 orders with the highest price.
select *
from sales 
order by price DESC
limit 5;

-- Q10. Display the top 3 orders with the highest quantity.
select *
from sales 
order by quantity DESC
limit 3;

-- Q11. Display the 5 cheapest orders.
select* 
from sales 
order by price  ASC 
limit 5;


select city, count(order_id) 
from sales 
group by (city);

-- Q12. Find total orders and total revenue generated from each city, sorted by highest revenue.
select city, 
       COUNT(order_id) AS total_orders, 
       SUM(quantity * price) AS total_revenue
from sales
group by city
order by total_revenue DESC;
