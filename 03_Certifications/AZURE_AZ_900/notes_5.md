# AZ-900 Module 5 — Azure Storage Services

# Table of Contents

1. Introduction to Azure Storage Services
2. What is Cloud Storage?
3. Why Cloud Storage is Important
4. Benefits of Azure Storage
5. Azure Storage Account
6. Storage Account Types
7. Azure Blob Storage
8. Blob Types
9. Blob Storage Use Cases
10. Azure File Storage
11. Azure File Storage Architecture
12. Blob Storage vs File Storage
13. Azure Queue Storage
14. Queue Storage Architecture
15. Queue Storage Use Cases
16. Azure Table Storage
17. Table Storage Architecture
18. Table Storage Use Cases
19. Managed Disks
20. Managed Disk Types
21. Storage Redundancy
22. LRS (Locally Redundant Storage)
23. ZRS (Zone-Redundant Storage)
24. GRS (Geo-Redundant Storage)
25. GZRS (Geo-Zone-Redundant Storage)
26. Storage Access Tiers
27. Hot Tier
28. Cool Tier
29. Archive Tier
30. Comparing Storage Services
31. Real-World Storage Scenarios
32. Best Practices
33. Common AZ-900 Confusing Concepts
34. AZ-900 Exam Tips
35. Memory Tricks
36. Practice Questions
37. Final Revision Notes

---

# 1. Introduction to Azure Storage Services

Azure Storage Services provide scalable, durable, secure cloud storage for:

* files
* images
* videos
* backups
* databases
* logs
* AI datasets
* virtual machine disks

Storage is one of the core foundations of cloud computing.

Almost every cloud application needs storage.

---

# Why Storage is Important

Applications generate and use massive amounts of data.

Examples:

* AI training datasets
* user uploads
* backup files
* logs
* videos
* customer records

Cloud storage helps organizations:

* store massive data
* scale storage instantly
* improve durability
* support disaster recovery
* reduce infrastructure costs

---

# 2. What is Cloud Storage?

# Definition

Cloud storage means:

> Storing data in cloud infrastructure instead of local physical devices.

---

# Types of Data Stored

Cloud storage can store:

* documents
* images
* videos
* backups
* application logs
* databases
* AI datasets
* operating system disks

---

# Traditional Storage Problems

Traditional storage systems faced:

* limited scalability
* hardware failures
* expensive maintenance
* difficult backups
* disaster recovery issues

---

# Cloud Storage Advantages

Cloud storage provides:

* scalability
* availability
* durability
* redundancy
* global access

---

# 3. Why Cloud Storage is Important

# Key Benefits

## Scalability

Store petabytes of data.

## High Availability

Data remains accessible.

## Durability

Multiple copies protect data.

## Security

Encryption and access control.

## Disaster Recovery

Data replicated across regions.

## Global Access

Access data worldwide.

---

# Real-World Example

AI application stores:

* images
* videos
* trained models
* datasets

inside Azure Storage.

---

# 4. Benefits of Azure Storage

# Durability

Azure creates multiple copies of data.

---

# Scalability

Storage scales automatically.

---

# Security

Supports:

* encryption
* RBAC
* firewalls
* private endpoints

---

# Availability

Data accessible globally.

---

# Cost Optimization

Different pricing tiers available.

---

# Integration

Works with:

* VMs
* AI services
* Kubernetes
* databases

---

# 5. Azure Storage Account

# Definition

A Storage Account is:

> A container that provides access to Azure storage services.

It acts as the top-level namespace for Azure storage.

---

# Storage Account Can Contain

* Blob Storage
* File Shares
* Queues
* Tables

---

# Real-World Example

```text
storageaccount01
```

Contains:

* images
* videos
* logs
* backups

---

# Why Storage Accounts Exist

Storage accounts help:

* organize storage
* manage billing
* apply security
* monitor usage

---

# Important AZ-900 Point

You must create:

# Storage Account

before using Azure storage services.

---

# Storage Account Architecture

```text
Storage Account

 ├── Blob Containers
 ├── File Shares
 ├── Queues
 └── Tables
```

---

# 6. Storage Account Types

Azure supports different storage account types.

---

# General-Purpose v2 (GPv2)

Most commonly used.

Supports:

* blobs
* files
* queues
* tables

---

# Premium Storage Accounts

Optimized for:

* high-performance workloads
* SSD-based storage

---

# Blob Storage Accounts

Optimized for blob storage only.

---

# 7. Azure Blob Storage

# Definition

Blob Storage stores:

> Unstructured data.

---

# What is Unstructured Data?

Data without fixed schema.

Examples:

* images
* videos
* PDFs
* documents
* backups
* AI datasets

---

# Blob Meaning

Blob = Binary Large Object

---

# Blob Storage Benefits

## Massive Scalability

## High Durability

## Global Accessibility

## Cost-Effective

---

# Blob Storage Use Cases

## Media Storage

Store images and videos.

## AI/ML Datasets

Store training data.

## Backups

Store backup files.

## Static Website Hosting

Host static websites.

## Logging

Store application logs.

---

# Real-World Example

Deepfake detection project stores:

* videos
* datasets
* trained models

inside Blob Storage.

---

# Important AZ-900 Point

Blob Storage =

# Unstructured object storage

---

# 8. Blob Types

Azure Blob Storage supports:

---

# Block Blob

Most common blob type.

Best for:

* files
* media
* documents

---

# Append Blob

Optimized for appending data.

Best for:

* logs
* telemetry

---

# Page Blob

Optimized for random read/write.

Used for:

* VM disks

---

# Blob Type Comparison

| Blob Type   | Best Use        |
| ----------- | --------------- |
| Block Blob  | Files and media |
| Append Blob | Logs            |
| Page Blob   | VM disks        |

---

# 9. Blob Storage Use Cases

| Use Case        | Why Blob Storage?          |
| --------------- | -------------------------- |
| AI datasets     | Massive scalable storage   |
| Video streaming | Optimized media storage    |
| Website images  | Global access              |
| Backups         | Durable and cost-effective |

---

# 10. Azure File Storage

# Definition

Azure File Storage provides:

> Fully managed shared file storage.

---

# Protocol Used

Azure Files uses:

* SMB protocol

---

# Why Azure Files Exists

Organizations need:

* shared folders
* cloud-based file sharing
* hybrid file systems

---

# Real-World Example

Employees access:

```text
company-shared-folder
```

from:

* laptops
* VMs
* servers

---

# Azure File Storage Use Cases

## Shared Company Files

## Lift-and-Shift File Servers

## Hybrid Cloud Storage

---

# Important AZ-900 Point

Azure Files =

# Shared file storage

---

# 11. Azure File Storage Architecture

```text
Azure File Share

 ├── Shared Documents
 ├── Reports
 ├── Images
 └── Logs
```

---

# 12. Blob Storage vs File Storage

| Blob Storage           | File Storage          |
| ---------------------- | --------------------- |
| Object storage         | Shared file system    |
| Unstructured data      | Shared folders        |
| Internet/object access | SMB access            |
| Best for media         | Best for shared files |

---

# 13. Azure Queue Storage

# Definition

Queue Storage stores:

> Messages for asynchronous communication.

---

# Why Queue Storage Exists

Applications need:

* background processing
* workload buffering
* decoupled communication

---

# Real-World Example

E-commerce system:

* order placed
* queue message created
* payment system processes later

---

# Queue Storage Benefits

## Reliable Messaging

## Scalability

## Decoupled Systems

## Background Processing

---

# Queue Storage Use Cases

* order processing
* notification systems
* background jobs
* microservices communication

---

# Important AZ-900 Point

Queue Storage =

# Message storage service

---

# 14. Queue Storage Architecture

```text
Application A
    ↓
Queue Storage
    ↓
Application B
```

---

# 15. Queue Storage Use Cases

| Scenario      | Queue Storage Benefit   |
| ------------- | ----------------------- |
| Online orders | Asynchronous processing |
| Email systems | Message buffering       |
| AI pipelines  | Task scheduling         |

---

# 16. Azure Table Storage

# Definition

Table Storage is:

> NoSQL key-value data store.

---

# Characteristics

## Schema-less

## Fast Access

## Massive Scalability

## Flexible Structure

---

# Table Storage Use Cases

* IoT data
* telemetry
* user profiles
* metadata

---

# Real-World Example

IoT sensors generate telemetry data.

Stored inside Table Storage.

---

# Important AZ-900 Point

Table Storage =

# NoSQL structured data

---

# 17. Table Storage Architecture

```text
Table

 ├── Partition Key
 ├── Row Key
 └── Properties
```

---

# 18. Table Storage Use Cases

| Use Case      | Why Table Storage?  |
| ------------- | ------------------- |
| IoT telemetry | Fast NoSQL access   |
| User profiles | Flexible schema     |
| Metadata      | Lightweight storage |

---

# 19. Managed Disks

# Definition

Managed Disks are:

> Storage volumes used by Azure Virtual Machines.

---

# Why Managed Disks Exist

VMs require:

* operating system disks
* application disks
* data disks

Azure manages:

* availability
* scaling
* durability

---

# Important AZ-900 Point

Managed Disks =

# VM storage

---

# 20. Managed Disk Types

# Standard HDD

Low-cost storage.

Best for:

* backup
* dev/test

---

# Standard SSD

Better performance.

Best for:

* web servers
* business apps

---

# Premium SSD

High-performance storage.

Best for:

* databases
* enterprise apps
* AI workloads

---

# Disk Comparison

| Disk Type    | Best For                   |
| ------------ | -------------------------- |
| Standard HDD | Low-cost workloads         |
| Standard SSD | Balanced workloads         |
| Premium SSD  | High-performance workloads |

---

# 21. Storage Redundancy

VERY IMPORTANT AZ-900 TOPIC.

---

# Why Redundancy Exists

Redundancy protects data from:

* hardware failures
* datacenter failures
* regional disasters

---

# Types of Redundancy

| Type | Full Form                  |
| ---- | -------------------------- |
| LRS  | Locally Redundant Storage  |
| ZRS  | Zone-Redundant Storage     |
| GRS  | Geo-Redundant Storage      |
| GZRS | Geo-Zone-Redundant Storage |

---

# 22. LRS (Locally Redundant Storage)

# Definition

Stores:

# 3 copies

inside same datacenter.

---

# Benefits

## Low Cost

## Basic Hardware Protection

---

# Limitation

Does NOT protect against datacenter disaster.

---

# AZ-900 Important Point

LRS =

# Same datacenter redundancy

---

# 23. ZRS (Zone-Redundant Storage)

# Definition

Replicates data across:

# multiple availability zones.

---

# Benefits

## Datacenter Failure Protection

## Improved Availability

---

# Important AZ-900 Point

ZRS =

# Availability Zone protection

---

# 24. GRS (Geo-Redundant Storage)

# Definition

Replicates data to:

# secondary Azure region.

---

# Benefits

## Regional Disaster Recovery

## Geo Replication

---

# Important AZ-900 Point

GRS =

# Regional disaster protection

---

# 25. GZRS (Geo-Zone-Redundant Storage)

# Definition

Combines:

* ZRS
* GRS

---

# Benefits

## Zone Protection

## Regional Protection

## Maximum Availability

---

# Redundancy Comparison

| Redundancy Type | Protects Against        |
| --------------- | ----------------------- |
| LRS             | Hardware failure        |
| ZRS             | Datacenter failure      |
| GRS             | Regional disaster       |
| GZRS            | Zone + regional failure |

---

# 26. Storage Access Tiers

Azure Blob Storage supports:

* Hot Tier
* Cool Tier
* Archive Tier

---

# Why Access Tiers Exist

Different data has different access frequency.

Tiers optimize:

* storage cost
* access cost

---

# 27. Hot Tier

# Best For

Frequently accessed data.

Examples:

* active website images
* current application files

---

# Characteristics

* Higher storage cost
* Lower access cost

---

# 28. Cool Tier

# Best For

Infrequently accessed data.

Examples:

* monthly backups
* old reports

---

# Characteristics

* Lower storage cost
* Higher access cost

---

# 29. Archive Tier

# Best For

Rarely accessed data.

Examples:

* compliance records
* long-term archives

---

# Characteristics

* Lowest storage cost
* Highest retrieval cost
* Slow retrieval

---

# Tier Comparison

| Tier    | Best For              |
| ------- | --------------------- |
| Hot     | Frequently accessed   |
| Cool    | Occasionally accessed |
| Archive | Rarely accessed       |

---

# Important AZ-900 Point

Archive Tier =

# Cheapest storage tier

but:

* slow retrieval
* higher access latency

---

# 30. Comparing Storage Services

| Storage Service | Purpose             |
| --------------- | ------------------- |
| Blob Storage    | Unstructured data   |
| Azure Files     | Shared file storage |
| Queue Storage   | Messaging           |
| Table Storage   | NoSQL data          |
| Managed Disks   | VM storage          |

---

# 31. Real-World Storage Scenarios

# Scenario 1 — AI Dataset Storage

Need:

* images
* videos
* models

Best Solution:
Blob Storage

---

# Scenario 2 — Shared Office Files

Need:

* shared access

Best Solution:
Azure Files

---

# Scenario 3 — Order Processing System

Need:

* asynchronous messaging

Best Solution:
Queue Storage

---

# Scenario 4 — IoT Telemetry

Need:

* scalable NoSQL data

Best Solution:
Table Storage

---

# Scenario 5 — VM Storage

Need:

* operating system disk

Best Solution:
Managed Disks

---

# 32. Best Practices

# Blob Storage Best Practices

* Use for unstructured data.
* Use access tiers for cost optimization.

---

# Azure Files Best Practices

* Use for shared access.
* Secure with RBAC.

---

# Queue Storage Best Practices

* Use for decoupled systems.
* Avoid large message payloads.

---

# Redundancy Best Practices

* Use GRS for disaster recovery.
* Use ZRS for critical workloads.

---

# Access Tier Best Practices

* Hot for active data.
* Archive for compliance data.

---

# 33. Common AZ-900 Confusing Concepts

# Blob vs File Storage

| Blob                   | File               |
| ---------------------- | ------------------ |
| Object storage         | Shared file system |
| Unstructured data      | Shared folders     |
| Internet/object access | SMB access         |

---

# Queue vs Table Storage

| Queue         | Table                 |
| ------------- | --------------------- |
| Messages      | Structured NoSQL data |
| Communication | Storage               |

---

# ZRS vs GRS

| ZRS                | GRS                 |
| ------------------ | ------------------- |
| Zone protection    | Regional protection |
| Availability Zones | Region Pairs        |

---

# Hot vs Archive Tier

| Hot                 | Archive         |
| ------------------- | --------------- |
| Frequently accessed | Rarely accessed |
| Fast access         | Slow retrieval  |

---

# 34. AZ-900 Exam Tips

# Microsoft Frequently Asks

## Unstructured Data

→ Blob Storage

---

## Shared File Access

→ Azure Files

---

## Messaging

→ Queue Storage

---

## NoSQL Data

→ Table Storage

---

## VM Disk Storage

→ Managed Disks

---

## Datacenter Protection

→ ZRS

---

## Regional Disaster Protection

→ GRS

---

## Frequently Accessed Data

→ Hot Tier

---

## Rarely Accessed Data

→ Archive Tier

---

# Important Exam Strategy

Read keywords carefully:

| Keyword             | Likely Answer |
| ------------------- | ------------- |
| Unstructured files  | Blob Storage  |
| Shared folder       | Azure Files   |
| Messages            | Queue Storage |
| NoSQL               | Table Storage |
| Disaster recovery   | GRS           |
| Frequently accessed | Hot Tier      |

---

# 35. Memory Tricks

# Blob

= Big files

---

# Azure Files

= Shared folders

---

# Queue

= Messages waiting

---

# Table

= NoSQL structured data

---

# Hot Tier

= Frequently used

---

# Archive Tier

= Rarely used

---

# GRS

= Geographic redundancy

---

# 36. Practice Questions

# Q1

Which Azure storage service stores unstructured data?

Answer:
Blob Storage

---

# Q2

Which Azure storage service supports shared file access?

Answer:
Azure Files

---

# Q3

Which Azure storage service stores messages?

Answer:
Queue Storage

---

# Q4

Which Azure storage service supports NoSQL structured data?

Answer:
Table Storage

---

# Q5

Which storage type protects against regional disaster?

Answer:
GRS

---

# Q6

Which storage tier is cheapest?

Answer:
Archive Tier

---

# Q7

Which Azure storage type is used by VMs?

Answer:
Managed Disks

---

# Q8

Which redundancy type protects against datacenter failure?

Answer:
ZRS

---

# Q9

What does Blob stand for?

Answer:
Binary Large Object

---

# Q10

Which storage tier is best for active frequently used data?

Answer:
Hot Tier

---

# 37. Final Revision Notes

| Storage Service | Key Purpose        |
| --------------- | ------------------ |
| Blob Storage    | Unstructured data  |
| Azure Files     | Shared file system |
| Queue Storage   | Messaging          |
| Table Storage   | NoSQL data         |
| Managed Disks   | VM storage         |

---

# Redundancy Quick Revision

| Type | Protection            |
| ---- | --------------------- |
| LRS  | Hardware failure      |
| ZRS  | Datacenter failure    |
| GRS  | Regional disaster     |
| GZRS | Zone + region failure |

---

# Access Tier Quick Revision

| Tier    | Usage                 |
| ------- | --------------------- |
| Hot     | Frequently accessed   |
| Cool    | Occasionally accessed |
| Archive | Rarely accessed       |

---

# Most Important AZ-900 Concepts

1. Blob vs Azure Files
2. Queue vs Table Storage
3. Storage redundancy types
4. Hot/Cool/Archive tiers
5. Storage service selection
6. Disaster recovery concepts

---
