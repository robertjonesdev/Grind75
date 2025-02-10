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
