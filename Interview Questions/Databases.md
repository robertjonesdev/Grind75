### 1. **What are the differences between SQL and NoSQL databases?**

- **Explanation:** SQL databases are relational, table-based, and use structured query language (e.g., MySQL, PostgreSQL). NoSQL databases are non-relational and can be document-based (e.g., MongoDB), key-value (e.g., Redis), column-based (e.g., Cassandra), or graph-based (e.g., Neo4j).
- **Follow-up:** Discuss scenarios where you would choose SQL over NoSQL and vice versa.

---

### 2. **What is database normalization, and why is it important?**

- **Explanation:** Normalization is the process of organizing data to reduce redundancy and improve data integrity. It involves dividing tables into smaller, related tables and defining relationships between them (e.g., 1NF, 2NF, 3NF).
- **Follow-up:** Provide an example of normalization and explain its benefits and trade-offs (e.g., performance impact).

---

### 3. **What are indexes, and how do they improve database performance?**

- **Explanation:** Indexes are data structures that improve the speed of data retrieval operations by providing quick access to rows in a table. Common types include B-tree, hash, and composite indexes.
- **Follow-up:** Discuss the trade-offs of using indexes (e.g., increased storage and slower write operations).

---

### 4. **What is a transaction, and what are the ACID properties?**

- **Explanation:** A transaction is a sequence of database operations performed as a single unit. ACID stands for:
  - **Atomicity:** All operations succeed or fail together.
  - **Consistency:** The database remains in a valid state.
  - **Isolation:** Transactions are executed independently.
  - **Durability:** Committed changes are permanent.
- **Follow-up:** Explain how you handle transactions in your applications.

---

### 5. **What is the difference between inner join, left join, right join, and full outer join?**

- **Explanation:**
  - **Inner Join:** Returns only matching rows from both tables.
  - **Left Join:** Returns all rows from the left table and matching rows from the right table.
  - **Right Join:** Returns all rows from the right table and matching rows from the left table.
  - **Full Outer Join:** Returns all rows when there is a match in either table.
- **Follow-up:** Provide an example query for each type of join.

---

### 6. **What is database sharding, and how does it work?**

- **Explanation:** Sharding is a technique for horizontally partitioning data across multiple databases or servers to improve scalability and performance. Each shard contains a subset of the data.
- **Follow-up:** Discuss the challenges of sharding (e.g., data distribution, query complexity).

---

### 7. **How do you optimize a slow-running query?**

- **Explanation:** Techniques include:
  - Adding indexes to columns used in `WHERE`, `JOIN`, and `ORDER BY` clauses.
  - Rewriting the query to avoid subqueries or unnecessary joins.
  - Analyzing the query execution plan to identify bottlenecks.
- **Follow-up:** Share an example of a query you optimized and the steps you took.

---

### 8. **What is a deadlock, and how do you prevent it?**

- **Explanation:** A deadlock occurs when two or more transactions block each other by holding locks on resources that the other transactions need. Prevention techniques include:
  - Using consistent transaction ordering.
  - Reducing transaction time.
  - Using timeouts or deadlock detection mechanisms.
- **Follow-up:** Provide an example of a deadlock scenario and how you resolved it.

---

### 9. **What is the difference between clustered and non-clustered indexes?**

- **Explanation:**
  - **Clustered Index:** Determines the physical order of data in a table. A table can have only one clustered index.
  - **Non-Clustered Index:** Stores a separate data structure that points to the actual data. A table can have multiple non-clustered indexes.
- **Follow-up:** Discuss when to use each type of index.

---

### 10. **How do you handle database backups and recovery?**

- **Explanation:** Database backups can be full, incremental, or differential. Recovery involves restoring data from backups and applying transaction logs to bring the database to a consistent state.
- **Follow-up:** Share your experience with backup strategies (e.g., automated backups, cloud storage) and disaster recovery plans.

---

### Bonus Questions:

1. **What is database replication, and why is it used?**

   - **Explanation:** Replication involves copying data from one database to another to improve availability, fault tolerance, and read scalability.
   - **Follow-up:** Discuss different replication strategies (e.g., master-slave, master-master).

2. **What is the CAP theorem, and how does it apply to databases?**

   - **Explanation:** The CAP theorem states that a distributed system can only guarantee two of the following: Consistency, Availability, and Partition Tolerance. For example, SQL databases prioritize Consistency and Availability, while NoSQL databases often prioritize Availability and Partition Tolerance.
   - **Follow-up:** Provide examples of databases that align with each CAP combination.

3. **How do you handle database migrations in a production environment?**
   - **Explanation:** Database migrations involve updating the schema or data in a live database. Tools like Flyway or Liquibase can automate this process.
   - **Follow-up:** Discuss best practices for zero-downtime migrations.

---

### Tips for Answering:

- Use **real-world examples** to demonstrate your experience.
- Showcase your ability to **balance performance, scalability, and maintainability**.
- Be prepared to write **SQL queries** or explain **database design decisions**.
