-- E-commerce Customer Segmentation SQL Project
-- Table schemas
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE segments (
    segment_id INT PRIMARY KEY,
    segment_name VARCHAR(50)
);

CREATE TABLE customer_segments (
    customer_id INT,
    segment_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (segment_id) REFERENCES segments(segment_id)
);

-- Sample data
INSERT INTO customers VALUES
(1, 'Amit', 'amit@email.com'),
(2, 'Priya', 'priya@email.com'),
(3, 'Rahul', 'rahul@email.com');

INSERT INTO orders VALUES
(1, 1, '2024-06-01', 5000.00),
(2, 1, '2024-06-10', 7000.00),
(3, 2, '2024-06-05', 2000.00),
(4, 3, '2024-06-07', 15000.00);

INSERT INTO segments VALUES
(1, 'Premium'),
(2, 'Regular'),
(3, 'Occasional');

INSERT INTO customer_segments VALUES
(1, 1),
(2, 2),
(3, 1);

-- Example queries
-- 1. List customers with their segment
SELECT c.customer_name, s.segment_name
FROM customers c
JOIN customer_segments cs ON c.customer_id = cs.customer_id
JOIN segments s ON cs.segment_id = s.segment_id;

-- 2. Order count by segment
SELECT s.segment_name, COUNT(o.order_id) AS order_count
FROM orders o
JOIN customer_segments cs ON o.customer_id = cs.customer_id
JOIN segments s ON cs.segment_id = s.segment_id
GROUP BY s.segment_name;

-- 3. Average order value by segment
SELECT s.segment_name, AVG(o.order_amount) AS avg_order_value
FROM orders o
JOIN customer_segments cs ON o.customer_id = cs.customer_id
JOIN segments s ON cs.segment_id = s.segment_id
GROUP BY s.segment_name;

-- 4. Top segment by total order value
SELECT s.segment_name, SUM(o.order_amount) AS total_value
FROM orders o
JOIN customer_segments cs ON o.customer_id = cs.customer_id
JOIN segments s ON cs.segment_id = s.segment_id
GROUP BY s.segment_name
ORDER BY total_value DESC
LIMIT 1; 