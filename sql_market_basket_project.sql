-- Market Basket Analysis SQL Project
-- Table schemas
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    transaction_date DATE
);

CREATE TABLE transaction_items (
    transaction_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Sample data
INSERT INTO products VALUES
(1, 'Milk'),
(2, 'Bread'),
(3, 'Eggs'),
(4, 'Butter');

INSERT INTO transactions VALUES
(1, 101, '2024-06-01'),
(2, 102, '2024-06-01'),
(3, 101, '2024-06-02');

INSERT INTO transaction_items VALUES
(1, 1, 1),
(1, 2, 1),
(1, 3, 1),
(2, 2, 2),
(2, 4, 1),
(3, 1, 1),
(3, 4, 1);

-- Example queries
-- 1. Top products by sales count
SELECT p.product_name, SUM(ti.quantity) AS total_sold
FROM transaction_items ti
JOIN products p ON ti.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

-- 2. Average basket size
SELECT AVG(item_count) AS avg_basket_size
FROM (
  SELECT transaction_id, SUM(quantity) AS item_count
  FROM transaction_items
  GROUP BY transaction_id
) sub;

-- 3. Frequent item pairs (simple co-occurrence)
SELECT p1.product_name AS item1, p2.product_name AS item2, COUNT(*) AS pair_count
FROM transaction_items ti1
JOIN transaction_items ti2 ON ti1.transaction_id = ti2.transaction_id AND ti1.product_id < ti2.product_id
JOIN products p1 ON ti1.product_id = p1.product_id
JOIN products p2 ON ti2.product_id = p2.product_id
GROUP BY item1, item2
ORDER BY pair_count DESC;

-- 4. Customer with most transactions
SELECT customer_id, COUNT(*) AS num_transactions
FROM transactions
GROUP BY customer_id
ORDER BY num_transactions DESC
LIMIT 1; 