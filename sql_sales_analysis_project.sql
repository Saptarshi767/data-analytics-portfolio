-- Sales Data Analysis SQL Project
-- Table schemas
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Sample data
INSERT INTO customers VALUES
(1, 'Amit Sharma', 'North'),
(2, 'Priya Singh', 'West'),
(3, 'Rahul Verma', 'South');

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics'),
(2, 'Desk Chair', 'Furniture'),
(3, 'Notebook', 'Stationery');

INSERT INTO sales VALUES
(1, '2024-06-01', 1, 1, 2, 120000.00),
(2, '2024-06-02', 2, 2, 5, 15000.00),
(3, '2024-06-03', 3, 3, 10, 500.00),
(4, '2024-06-04', 1, 2, 1, 3000.00),
(5, '2024-06-05', 2, 1, 1, 60000.00);

-- Example queries
-- 1. Total sales amount
SELECT SUM(amount) AS total_sales FROM sales;

-- 2. Top selling products
SELECT p.product_name, SUM(s.quantity) AS total_quantity
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC;

-- 3. Sales by region
SELECT c.region, SUM(s.amount) AS region_sales
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.region;

-- 4. Monthly sales trend
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(amount) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month; 