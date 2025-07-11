-- Power BI + SQL Integration Example Project
-- Table schemas
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100)
);

CREATE TABLE dates (
    date_id DATE PRIMARY KEY,
    month INT,
    year INT
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    date_id DATE,
    product_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (date_id) REFERENCES dates(date_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Sample data
INSERT INTO products VALUES
(1, 'Laptop'),
(2, 'Tablet');

INSERT INTO dates VALUES
('2024-01-01', 1, 2024),
('2024-02-01', 2, 2024),
('2024-03-01', 3, 2024);

INSERT INTO sales VALUES
(1, '2024-01-01', 1, 50000.00),
(2, '2024-01-01', 2, 20000.00),
(3, '2024-02-01', 1, 60000.00),
(4, '2024-03-01', 2, 25000.00);

-- Example queries
-- 1. Sales by month
SELECT d.month, d.year, SUM(s.amount) AS monthly_sales
FROM sales s
JOIN dates d ON s.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- 2. Sales by product
SELECT p.product_name, SUM(s.amount) AS total_sales
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name;

-- 3. Year-to-date (YTD) sales
SELECT d.year, SUM(s.amount) AS ytd_sales
FROM sales s
JOIN dates d ON s.date_id = d.date_id
GROUP BY d.year;

-- 4. Best month by sales
SELECT d.month, d.year, SUM(s.amount) AS monthly_sales
FROM sales s
JOIN dates d ON s.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY monthly_sales DESC
LIMIT 1; 