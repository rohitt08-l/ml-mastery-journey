# AZ-900 Module 6 — Azure Database Services

# Table of Contents

1. Introduction to Azure Databases
2. What is a Database?
3. Relational vs Non-Relational Databases
4. Azure SQL Database
5. Azure SQL Managed Instance
6. Azure Database for MySQL
7. Azure Database for PostgreSQL
8. Azure Cosmos DB
9. Database Service Selection
10. Real-World Use Cases
11. Best Practices
12. AZ-900 Exam Tips
13. Memory Tricks
14. Practice Questions
15. Final Revision Notes

---

# 1. Introduction to Azure Databases

Databases store, organize, and retrieve data efficiently.

Almost every application uses a database:
- Banking systems
- E-commerce websites
- ERP systems
- AI applications
- Mobile apps

---

# 2. What is a Database?

A database is an organized collection of data.

Examples:
- Student records
- Employee information
- Product catalogs
- Customer orders

Benefits:
- Fast retrieval
- Data consistency
- Security
- Scalability

---

# 3. Relational vs Non-Relational Databases

## Relational Databases (SQL)

Data is stored in tables.

Example:

| StudentID | Name |
|------------|--------|
| 101 | Rohit |
| 102 | Amit |

Characteristics:
- Tables
- Rows and columns
- SQL language
- Strong consistency

Examples:
- SQL Server
- MySQL
- PostgreSQL

---

## Non-Relational Databases (NoSQL)

Data is stored as:
- Documents
- Key-value pairs
- Graphs
- Column families

Characteristics:
- Flexible schema
- Massive scalability
- High performance

Example:
- Azure Cosmos DB

---

# 4. Azure SQL Database

## Definition

Azure SQL Database is a fully managed relational database service.

Service Type:
- PaaS

Azure manages:
- Backups
- Updates
- Patching
- Availability

Use Cases:
- Business applications
- ERP systems
- Web applications

AZ-900 Tip:
Azure SQL Database = Managed SQL Server in Azure.

---

# 5. Azure SQL Managed Instance

Provides near 100% SQL Server compatibility.

Best for:
- Migrating existing SQL Server workloads
- Enterprise applications

Advantages:
- Easier migration
- Managed by Azure
- Supports advanced SQL features

---

# 6. Azure Database for MySQL

Managed MySQL service in Azure.

Use Cases:
- WordPress
- Web applications
- Open-source applications

Benefits:
- Automatic backups
- High availability
- Security

---

# 7. Azure Database for PostgreSQL

Managed PostgreSQL service.

Best for:
- Modern web apps
- Analytics applications
- GIS workloads

Benefits:
- Open source
- Fully managed
- Scalable

---

# 8. Azure Cosmos DB

## Definition

Azure Cosmos DB is Microsoft's globally distributed NoSQL database.

Characteristics:
- Extremely fast
- Global distribution
- Low latency
- Massive scalability

Supports:
- Document data
- Key-value data
- Graph data

Use Cases:
- Gaming applications
- IoT platforms
- AI applications
- Global-scale apps

AZ-900 Tip:
Cosmos DB = NoSQL + Global Scale.

---

# 9. Database Service Selection

| Requirement | Service |
|-------------|---------|
| SQL Server workloads | Azure SQL Database |
| SQL migration | SQL Managed Instance |
| MySQL apps | Azure Database for MySQL |
| PostgreSQL apps | Azure Database for PostgreSQL |
| Global NoSQL workloads | Azure Cosmos DB |

---

# 10. Real-World Use Cases

## College ERP System
Azure SQL Database

## WordPress Website
Azure Database for MySQL

## Analytics Platform
Azure Database for PostgreSQL

## Global Gaming App
Azure Cosmos DB

---

# 11. Best Practices

- Use managed database services whenever possible.
- Choose relational databases for structured data.
- Choose Cosmos DB for globally distributed NoSQL workloads.
- Enable backups and monitoring.

---

# 12. AZ-900 Exam Tips

Microsoft frequently asks:

### Structured relational data
→ Azure SQL Database

### NoSQL database
→ Cosmos DB

### MySQL workloads
→ Azure Database for MySQL

### PostgreSQL workloads
→ Azure Database for PostgreSQL

### SQL Server migration
→ SQL Managed Instance

---

# 13. Memory Tricks

SQL Database = SQL in Azure

SQL Managed Instance = SQL Migration

MySQL = Open-source Web Apps

PostgreSQL = Analytics + Open Source

Cosmos DB = Global NoSQL

---

# 14. Practice Questions

Q1. Which Azure database is NoSQL?
Answer: Cosmos DB

Q2. Which Azure service is best for SQL Server workloads?
Answer: Azure SQL Database

Q3. Which database service supports global distribution?
Answer: Cosmos DB

Q4. Which Azure service is best for MySQL applications?
Answer: Azure Database for MySQL

Q5. Which Azure service is best for PostgreSQL applications?
Answer: Azure Database for PostgreSQL

---

# 15. Final Revision Notes

| Service | Key Idea |
|----------|----------|
| Azure SQL Database | Managed relational database |
| SQL Managed Instance | SQL migration |
| Azure Database for MySQL | Managed MySQL |
| Azure Database for PostgreSQL | Managed PostgreSQL |
| Cosmos DB | Globally distributed NoSQL |

---

# Most Important AZ-900 Concepts

1. Relational vs NoSQL
2. SQL Database vs Cosmos DB
3. MySQL vs PostgreSQL
4. SQL Managed Instance
5. Database service selection

