### **1. Concurrency & Locking**

**Question:**
"How does PostgreSQL handle concurrent writes to the same row? Explain how MVCC (Multi-Version Concurrency Control) prevents dirty reads and ensures consistency."

**Answer:**  
PostgreSQL uses **MVCC (Multi-Version Concurrency Control)** to handle concurrent writes. Instead of locking rows during updates, it creates new versions of the row (with a transaction ID). Older transactions see the old version, while newer ones see the updated version. This prevents dirty reads and ensures consistency without blocking most read/write operations.

**Example:**  
If two users update the same row simultaneously, PostgreSQL creates two row versions. Each transaction sees its own version until committed.

---

### **2. Indexing Strategies**

**Question:**
"When would you choose a BRIN index over a B-tree index? Give an example of a use case where BRIN significantly improves query performance."

**Answer:**  
**BRIN (Block Range Index)** is ideal for large, ordered datasets (e.g., timestamps or sensor data). It stores min/max values for data blocks, making it smaller and faster than B-tree for range queries.  
**B-tree** is better for high-cardinality data (e.g., unique IDs).

**Example:**  
Use BRIN for a `sensor_data` table with billions of timestamped rows. B-tree would be overkill and waste storage.

---

### **3. Query Optimization**

**Question:**
"A query with a `WHERE` clause on a timestamp column is slow despite an index. How would you diagnose and resolve this using `EXPLAIN ANALYZE`?"

**Answer:**  
Run `EXPLAIN ANALYZE` to check if the index is used. Common issues:

- The query isn’t sargable (e.g., `WHERE DATE(timestamp) = '2023-01-01'`). Rewrite to use indexed columns directly.
- Low selectivity (e.g., querying 90% of the table). Use a partial index or partitioning.

**Fix:**  
Change `DATE(timestamp)` to `timestamp >= '2023-01-01' AND timestamp < '2023-01-02'` to leverage the index.

---

### **4. Partitioning**

**Question:**
"How does table partitioning work in PostgreSQL? When would you use list partitioning vs. range partitioning? What are the trade-offs?"

**Answer:**  
Partitioning splits large tables into smaller chunks (partitions).

- **Range partitioning:** For ordered data (e.g., `sales` by month).
- **List partitioning:** For discrete values (e.g., `region`).

**Trade-offs:**

- Faster queries on partition keys but added complexity for writes and maintenance.

---

### **5. Replication & HA**

**Question:**
"Explain the difference between synchronous and asynchronous replication. How would you design a high-availability PostgreSQL setup for minimal downtime?"

**Answer:**

- **Synchronous replication:** Waits for all replicas to confirm writes. Ensures data consistency but slower.
- **Asynchronous replication:** Faster but risks data loss if the primary fails.

**HA Design:** Use synchronous replication for critical data + async for read replicas. Tools like Patroni automate failover.

---

### **6. Performance Tuning**

**Question:**
"How do you optimize `work_mem` and `shared_buffers` for a write-heavy workload? What metrics would you monitor to validate your configuration?"

**Answer:**

- **`shared_buffers`:** Set to ~25% of RAM for write-heavy workloads (caches frequently used data).
- **`work_mem`:** Increase for complex sorts/joins (e.g., 4MB–16MB).

**Monitor:** Cache hit ratio, lock contention, and buffer usage with `pg_stat_activity`.

---

### **7. JSONB & Advanced Data Types**

**Question:**
"When would you use `JSONB` over a traditional relational schema? How do you index a JSONB field for efficient querying?"
**Answer:**  
Use **`JSONB`** for semi-structured data (e.g., dynamic product attributes). Index with **GIN indexes** for fast searches on nested fields.

**Example:**  
`CREATE INDEX idx_product_tags ON products USING GIN (data->'tags');`

---

### **8. Transactions & Isolation Levels**

**Question:**
"Describe a scenario where using `REPEATABLE READ` isolation level would prevent a phantom read. How does PostgreSQL implement this under the hood?"

**Answer:**  
**`REPEATABLE READ`** takes a snapshot of the database at transaction start. Prevents phantom reads by ignoring new rows committed after the snapshot.

**Example:**  
If you run `SELECT SUM(sales)` twice in a transaction, new sales added by others won’t affect your result.

---

### **9. Vacuum & Maintenance**

**Question:**
"What’s the purpose of the `VACUUM` command? How does `autovacuum` work, and what happens if it’s misconfigured in a high-transaction system?"

**Answer:**

- **`VACUUM`:** Removes dead rows (from updates/deletes) to free space.
- **`autovacuum`:** Automates this but can lag in high-write systems. Misconfigured autovacuum leads to table bloat and slow queries.

**Fix:** Tune `autovacuum_vacuum_scale_factor` for large tables.

---

### **10. Extensions & Customization**

**Question**
"Have you used PostgreSQL extensions like `pg_partman`, `TimescaleDB`, or `PostGIS`? Explain how one of them solved a specific problem in your work."

**Answer:**  
**Example:** Used **TimescaleDB** (PostgreSQL extension) for time-series data. It automates partitioning by time and adds optimizations for aggregates (e.g., `avg()` over rolling windows).

---

### **Bonus Answers**

- **Replication lag:**
  "How would you troubleshoot replication lag in a read replica?"

Check network latency, replica load, and `pg_stat_replication`.

- **HOT updates:**
  "What’s the difference between a HOT (Heap-Only Tuple) update and a regular update?"

Updates that don’t modify indexes (saves I/O).

- **Row-level security:**
  "How do you enforce row-level security for multi-tenant applications?"
  Use `CREATE POLICY` to restrict access by tenant ID.

---

## PostgreSQL Commands

Here’s a concise **PostgreSQL Cheat Sheet** tailored for a back-end software engineer, covering commands for daily tasks, debugging, and optimization:

---

### **Database & Connection**

| **Command**                  | **Description**                           |
| ---------------------------- | ----------------------------------------- |
| `psql -U username -d dbname` | Connect to a database                     |
| `\l`                         | List all databases                        |
| `\c dbname`                  | Switch to a database                      |
| `\dt`                        | List tables in the current DB             |
| `\d table_name`              | Describe a table (columns, indexes, etc.) |

---

### **Table Operations**

| **Command** | **Description** |
| ----------- | --------------- |

| `CREATE TABLE users (  
  id SERIAL PRIMARY KEY,  
  name VARCHAR(50) NOT NULL,  
  email VARCHAR(100) UNIQUE  
);` | Create a table with constraints |
| `ALTER TABLE users ADD COLUMN age INT;` | Add a column |
| `ALTER TABLE users DROP COLUMN age;` | Drop a column |
| `DROP TABLE users;` | Delete a table |

---

### **CRUD Operations**

| **Command**                                                              | **Description**          |
| ------------------------------------------------------------------------ | ------------------------ |
| `INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');` | Insert a row             |
| `SELECT * FROM users WHERE name LIKE 'A%';`                              | Query data with a filter |
| `UPDATE users SET email = 'alice_new@example.com' WHERE id = 1;`         | Update a row             |
| `DELETE FROM users WHERE id = 1;`                                        | Delete a row             |

---

### **Querying & Joins**

| **Command** | **Description** |
| ----------- | --------------- |

| `SELECT u.name, o.total  
FROM users u  
JOIN orders o ON u.id = o.user_id  
WHERE o.total > 100;` | Inner join two tables |
| `SELECT COUNT(*) FROM users;` | Count rows |
| `SELECT name, SUM(total) FROM orders GROUP BY name;` | Aggregate with grouping |
| `SELECT * FROM users ORDER BY created_at DESC LIMIT 10;` | Pagination |

---

### **Indexes & Optimization**

| **Command**                                                             | **Description**                               |
| ----------------------------------------------------------------------- | --------------------------------------------- |
| `CREATE INDEX idx_users_email ON users(email);`                         | Create a B-tree index                         |
| `CREATE INDEX CONCURRENTLY idx_users_name ON users(name);`              | Non-blocking index creation                   |
| `EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';` | Debug query performance                       |
| `ANALYZE users;`                                                        | Update table statistics for the query planner |

---

### **Transactions**

| **Command**                                        | **Description**     |
| -------------------------------------------------- | ------------------- |
| `BEGIN;`                                           | Start a transaction |
| `COMMIT;`                                          | Save changes        |
| `ROLLBACK;`                                        | Discard changes     |
| `SAVEPOINT savepoint_name;`                        | Create a savepoint  |
| `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;` | Set isolation level |

---

### **JSON Operations**

| **Command**                                                                  | **Description**   |
| ---------------------------------------------------------------------------- | ----------------- |
| `SELECT data->>'field' FROM documents WHERE data @> '{"status": "active"}';` | Query JSONB field |
| `CREATE INDEX idx_data_status ON documents USING GIN ((data->'status'));`    | Index JSONB field |

---

### **User & Permissions**

| **Command**                                      | **Description**    |
| ------------------------------------------------ | ------------------ |
| `CREATE USER dev_user WITH PASSWORD 'password';` | Create a user      |
| `GRANT SELECT, INSERT ON users TO dev_user;`     | Grant permissions  |
| `REVOKE DELETE ON users FROM dev_user;`          | Revoke permissions |

---

### **Backup & Restore**

| **Command**                                | **Description**     |
| ------------------------------------------ | ------------------- |
| `pg_dump -U username dbname > backup.sql`  | Backup a database   |
| `psql -U username -d dbname -f backup.sql` | Restore a database  |
| `\copy users TO 'users.csv' CSV HEADER;`   | Export table to CSV |

---

### **Maintenance**

| **Command**                                               | **Description**              |
| --------------------------------------------------------- | ---------------------------- |
| `VACUUM FULL users;`                                      | Reclaim storage (aggressive) |
| `REINDEX TABLE users;`                                    | Rebuild corrupted indexes    |
| `SELECT pg_size_pretty(pg_total_relation_size('users'));` | Check table size             |

---

### **Useful Shortcuts (psql CLI)**

- `\x` : Toggle expanded display (for wide results).
- `\timing` : Toggle query execution time.
- `\e` : Open last command in a text editor.
- `\i script.sql` : Run SQL from a file.
- `\watch 5` : Rerun query every 5 seconds.

---

### **Common Gotchas**

- Use `ILIKE` for case-insensitive text searches.
- Prefer `text` over `varchar` (no performance difference, more flexible).
- Avoid `SELECT *` in production code (use explicit columns).
- Use `ON CONFLICT DO UPDATE` for upserts.

---

**Pro Tip:** Bookmark the [PostgreSQL Official Docs](https://www.postgresql.org/docs/) for quick syntax checks! Let me know if you want examples for a specific scenario.
