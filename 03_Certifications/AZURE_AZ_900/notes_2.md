# AZ-900 Module 2 — Azure Core Architectural Components

# Table of Contents

1. Introduction to Azure Architecture
2. Azure Global Infrastructure
3. Azure Regions
4. Azure Availability Zones
5. Azure Region Pairs
6. Azure Resource Groups
7. Azure Subscriptions
8. Azure Management Groups
9. Relationship Between Azure Components
10. Real-World Architecture Examples
11. Best Practices
12. Common Exam Confusions
13. AZ-900 Exam Tips
14. Memory Tricks
15. Practice Questions
16. Final Revision Notes

---

# 1. Introduction to Azure Architecture

Azure architecture is the foundation of all Microsoft Azure cloud services.

Before learning:

* Virtual Machines
* Networking
* Storage
* Databases
* AI Services

You must understand Azure architectural components.

These components help:

* organize resources
* manage billing
* improve availability
* support disaster recovery
* simplify administration

---

# Why Azure Architecture is Important

Every Azure service works inside this architecture.

Examples:

* Virtual Machines exist inside resource groups.
* Resource groups exist inside subscriptions.
* Subscriptions can exist inside management groups.

Without understanding architecture:

* Azure services become confusing.
* Networking concepts become difficult.
* Billing structure becomes unclear.

---

# Core Azure Architectural Components

The most important Azure architectural components are:

1. Regions
2. Availability Zones
3. Region Pairs
4. Resource Groups
5. Subscriptions
6. Management Groups

---

# Azure Infrastructure Hierarchy

```text
Management Groups
    ↓
Subscriptions
    ↓
Resource Groups
    ↓
Resources
```

Resources include:

* Virtual Machines
* Storage Accounts
* Databases
* Virtual Networks
* AI Services

---

# 2. Azure Global Infrastructure

# What is Azure Global Infrastructure?

Microsoft Azure operates a massive global cloud infrastructure.

This infrastructure consists of:

* datacenters
* networking systems
* power systems
* cooling systems
* physical security

Azure infrastructure exists worldwide.

---

# Why Global Infrastructure Exists

Cloud services must support users globally.

Users may exist in:

* India
* USA
* Europe
* Japan
* Australia
* Africa

Applications need:

* low latency
* high availability
* disaster recovery
* legal compliance

---

# Datacenters

A datacenter is a physical facility containing:

* servers
* storage systems
* networking hardware
* cooling systems

Microsoft owns and operates many datacenters worldwide.

---

# Benefits of Global Infrastructure

## Better Performance

Applications run closer to users.

## Lower Latency

Faster response times.

## Disaster Recovery

Services can recover from failures.

## Compliance

Supports local data residency laws.

---

# Azure Geography

Azure groups regions into geographies.

Examples:

* India Geography
* US Geography
* Europe Geography

Each geography usually contains multiple regions.

---

# Example

India Geography may contain:

* Central India
* South India
* West India

---

# 3. Azure Regions

# Definition

An Azure Region is:

> A geographical area containing one or more datacenters.

Each region contains:

* networking infrastructure
* power systems
* cooling systems
* physical security

---

# Examples of Azure Regions

Examples:

* Central India
* South India
* East US
* West Europe
* Japan East
* Southeast Asia

---

# Why Regions Exist

Regions exist to:

* reduce latency
* improve performance
* provide redundancy
* support legal compliance
* improve user experience

---

# Real-World Example

Suppose your users are mostly in India.

Best region choice:

* Central India
* South India

Because:
closer region = lower latency.

---

# Region Characteristics

## Regions Provide

* scalability
* redundancy
* high availability
* low latency
* disaster recovery support

---

# Region Selection Factors

When selecting a region, consider:

## 1. User Location

Choose closest region.

## 2. Compliance Requirements

Some data must stay within country.

## 3. Service Availability

Not all services exist in all regions.

## 4. Pricing

Pricing may differ across regions.

---

# Data Residency

Some organizations require:

* data to remain inside country boundaries.

Examples:

* banks
* government agencies
* healthcare systems

Regions help meet these requirements.

---

# Important AZ-900 Point

NOT all Azure services are available in every region.

Very important exam point.

---

# Region Benefits

## Improved Performance

Applications run closer to users.

## Better User Experience

Lower delays.

## Compliance Support

Supports legal regulations.

## Business Continuity

Supports backup and recovery.

---

# AZ-900 Example Question

Question:
A company wants minimum latency for users in India.

Best solution?

Answer:
Choose closest Azure region.

---

# 4. Azure Availability Zones

# Definition

Availability Zones are:

> Physically separate datacenters within the same Azure region.

Each availability zone has:

* separate power
* separate cooling
* separate networking

---

# Why Availability Zones Exist

Availability Zones protect applications from:

* datacenter failures
* power failures
* networking failures
* hardware failures

---

# Example

Region:
Central India

Inside region:

* Zone 1
* Zone 2
* Zone 3

If Zone 1 fails:
Zones 2 and 3 continue operating.

---

# Key Concept

Region = Geographic Area

Availability Zone = Separate Datacenter inside region

---

# Benefits of Availability Zones

## High Availability

Applications remain online.

## Fault Tolerance

Failures isolated to one zone.

## Improved Reliability

Better uptime.

## Disaster Isolation

Problems in one datacenter do not affect others.

---

# Real-World Example

Suppose an e-commerce application runs in:

* Zone 1
* Zone 2

If Zone 1 fails:
customers still access application from Zone 2.

---

# Availability Zone Architecture

```text
Azure Region

 ├── Zone 1
 ├── Zone 2
 └── Zone 3
```

---

# Important AZ-900 Point

Availability Zones protect against:

# Datacenter-level failures

NOT region-wide disasters.

---

# AZ-900 Example Question

Question:
Which Azure feature protects applications from datacenter failure?

Answer:
Availability Zones

---

# 5. Azure Region Pairs

# Definition

Each Azure region is paired with another Azure region within the same geography.

---

# Examples

* Central India ↔ South India
* East US ↔ West US
* North Europe ↔ West Europe

---

# Why Region Pairs Exist

Region pairs support:

* disaster recovery
* backup replication
* failover systems
* business continuity

---

# Key Concept

If an entire region becomes unavailable:
paired region can continue operations.

---

# Real-World Example

Suppose:
Central India region becomes unavailable.

Services can failover to:
South India.

---

# Region Pair Benefits

## Disaster Recovery

Supports recovery from regional outages.

## Replication

Data can replicate between paired regions.

## Planned Updates

Azure updates paired regions sequentially.

## Business Continuity

Applications remain available during disasters.

---

# Availability Zones vs Region Pairs

| Availability Zones    | Region Pairs        |
| --------------------- | ------------------- |
| Separate datacenters  | Separate regions    |
| Same region           | Different regions   |
| Datacenter protection | Regional protection |
| High availability     | Disaster recovery   |

---

# Important AZ-900 Point

Availability Zones:
Protect against datacenter failure.

Region Pairs:
Protect against regional disaster.

---

# AZ-900 Example Question

Question:
Which Azure feature helps recover from regional outage?

Answer:
Region Pairs

---

# 6. Azure Resource Groups

# Definition

A Resource Group is:

> A logical container for Azure resources.

Resources include:

* Virtual Machines
* Databases
* Storage Accounts
* VNets
* AI Services

---

# Why Resource Groups Exist

Resource groups help:

* organize resources
* simplify management
* control permissions
* monitor resources
* apply policies

---

# Real-World Example

Suppose company develops:

* website
* database
* storage

All related resources placed inside:

```text
RG-WebApplication
```

---

# Important Characteristics

## A Resource Belongs to Only One Resource Group

A resource cannot exist in multiple resource groups simultaneously.

---

## Resource Groups Can Contain Resources from Different Regions

Very important AZ-900 concept.

---

# Example

```text
RG-AI-Project
```

Contains:

* VM in Central India
* Storage in South India

This is allowed.

---

# Benefits of Resource Groups

## Better Organization

Resources grouped logically.

## Easier Administration

Manage related resources together.

## Cost Monitoring

Track costs by project.

## Access Management

Apply permissions to group.

## Simplified Deletion

Delete entire project resources together.

---

# Deleting Resource Groups

Deleting a resource group deletes:

# ALL resources inside it.

Very important exam point.

---

# Resource Group Example Structure

```text
Resource Group: RG-ERP-System

 ├── VM
 ├── Database
 ├── Storage Account
 └── Virtual Network
```

---

# Important AZ-900 Point

Resource Group:

* logical organization unit
* NOT billing boundary

---

# AZ-900 Example Question

Question:
Which Azure component logically groups resources?

Answer:
Resource Group

---

# 7. Azure Subscriptions

# Definition

An Azure Subscription is:

> A unit of management, billing, and access control.

---

# Main Purposes of Subscription

## Billing Boundary

Azure billing occurs at subscription level.

## Access Control

Permissions managed at subscription level.

## Resource Management

Resources organized under subscription.

## Usage Tracking

Monitor cloud usage.

---

# Real-World Example

Company creates separate subscriptions:

* Development Subscription
* Testing Subscription
* Production Subscription

---

# Benefits of Subscriptions

## Cost Separation

Separate billing for teams/projects.

## Better Security

Separate environments.

## Resource Isolation

Different workloads separated.

## Governance

Policies applied at subscription level.

---

# Azure Subscription Types

Examples:

* Free Trial
* Pay-As-You-Go
* Enterprise Agreement
* Student Subscription

---

# Important AZ-900 Point

Resource Groups exist INSIDE subscriptions.

---

# Subscription Hierarchy

```text
Subscription
    ↓
Resource Groups
        ↓
Resources
```

---

# Subscription Limits

Subscriptions may have:

* quotas
* service limits
* spending limits

---

# Example

Limits may exist for:

* number of VMs
* storage capacity
* networking resources

---

# AZ-900 Example Question

Question:
Which Azure component acts as billing boundary?

Answer:
Subscription

---

# 8. Azure Management Groups

# Definition

Management Groups help organize and manage multiple Azure subscriptions.

---

# Why Management Groups Exist

Large organizations may have:

* hundreds of subscriptions
* multiple departments
* multiple teams

Management Groups simplify administration.

---

# Example

Company departments:

* HR
* Finance
* AI Team
* Operations

Each department has subscriptions.

All subscriptions managed under:

```text
Company-ManagementGroup
```

---

# Benefits of Management Groups

## Centralized Policy Management

Apply policies across subscriptions.

## Centralized Access Control

Manage permissions centrally.

## Better Governance

Standardize cloud usage.

## Simplified Administration

Easier large-scale management.

---

# Management Group Hierarchy

```text
Management Group
    ↓
Subscriptions
    ↓
Resource Groups
    ↓
Resources
```

---

# Important AZ-900 Point

Management Groups sit ABOVE subscriptions.

---

# Example Structure

```text
Management Group: Enterprise

 ├── Production Subscription
 ├── Development Subscription
 └── Testing Subscription
```

---

# AZ-900 Example Question

Question:
Which Azure component organizes multiple subscriptions?

Answer:
Management Groups

---

# 9. Relationship Between Azure Components

# Full Azure Hierarchy

```text
Management Groups
    ↓
Subscriptions
    ↓
Resource Groups
    ↓
Resources
```

---

# Explanation

## Management Groups

Manage multiple subscriptions.

## Subscriptions

Billing and access boundary.

## Resource Groups

Logical grouping of resources.

## Resources

Actual Azure services.

---

# Complete Example

```text
Management Group: Company

    Subscription: Production

        Resource Group: RG-WebApp

            VM
            Database
            Storage

        Resource Group: RG-AI

            AI Services
            Blob Storage
```

---

# 10. Real-World Architecture Examples

# Example 1 — College ERP System

## Step 1 — Management Group

```text
DYPATIL-Management
```

---

## Step 2 — Subscriptions

```text
Development-Subscription
Production-Subscription
```

---

## Step 3 — Resource Groups

```text
RG-ERP
RG-AIChatbot
RG-StudentPortal
```

---

## Step 4 — Resources

Inside RG-AIChatbot:

* Azure VM
* Blob Storage
* Azure AI Service

---

# Example 2 — E-Commerce Platform

## Region

Central India

## Availability Zones

Zone 1 + Zone 2

## Resource Group

RG-ECommerce

## Resources

* Web App
* Database
* Load Balancer
* Storage Account

---

# 11. Best Practices

# Region Best Practices

* Choose nearest region to users.
* Check service availability.
* Consider compliance requirements.

---

# Availability Zone Best Practices

* Deploy critical applications across zones.
* Use redundancy for production systems.

---

# Resource Group Best Practices

* Group related resources together.
* Use naming conventions.
* Separate development and production.

---

# Subscription Best Practices

* Separate billing environments.
* Use separate subscriptions for production.

---

# Management Group Best Practices

* Organize subscriptions by department.
* Apply centralized governance.

---

# 12. Common Exam Confusions

# Region vs Availability Zone

| Region                 | Availability Zone   |
| ---------------------- | ------------------- |
| Geographic area        | Separate datacenter |
| Large scope            | Smaller scope       |
| Example: Central India | Zone 1              |

---

# Availability Zone vs Region Pair

| Availability Zone     | Region Pair         |
| --------------------- | ------------------- |
| Same region           | Different regions   |
| Datacenter protection | Regional protection |
| High availability     | Disaster recovery   |

---

# Resource Group vs Subscription

| Resource Group         | Subscription           |
| ---------------------- | ---------------------- |
| Organizes resources    | Billing boundary       |
| Logical container      | Account management     |
| Project-level grouping | Billing-level grouping |

---

# Management Group vs Subscription

| Management Group     | Subscription     |
| -------------------- | ---------------- |
| Groups subscriptions | Groups resources |
| Governance level     | Billing level    |

---

# 13. AZ-900 Exam Tips

# Microsoft Frequently Asks

## Resource Group Questions

Remember:

* logical grouping
* not billing boundary

---

## Availability Zone Questions

Protect against:

* datacenter failure

---

## Region Pair Questions

Protect against:

* regional disaster

---

## Subscription Questions

Used for:

* billing
* access control

---

## Management Group Questions

Used for:

* managing multiple subscriptions

---

# Exam Strategy

Read keywords carefully:

## Datacenter Failure

→ Availability Zones

## Regional Disaster

→ Region Pairs

## Billing Boundary

→ Subscription

## Logical Organization

→ Resource Group

## Multiple Subscriptions

→ Management Groups

---

# 14. Memory Tricks

# Resource Group

= Folder of resources

---

# Subscription

= Azure bill/account

---

# Management Group

= Group of subscriptions

---

# Availability Zone

= Separate datacenter

---

# Region Pair

= Disaster recovery partner

---

# Azure Hierarchy Memory Trick

Management Groups
→ Subscriptions
→ Resource Groups
→ Resources

---

# 15. Practice Questions

# Q1

Which Azure component is billing boundary?

Answer:
Subscription

---

# Q2

Which feature protects against datacenter failure?

Answer:
Availability Zones

---

# Q3

Which feature protects against regional disaster?

Answer:
Region Pairs

---

# Q4

Which Azure component logically groups resources?

Answer:
Resource Group

---

# Q5

Which Azure component manages multiple subscriptions?

Answer:
Management Groups

---

# Q6

Can resources from different regions exist in one Resource Group?

Answer:
Yes

---

# Q7

Deleting Resource Group deletes what?

Answer:
All resources inside it

---

# Q8

Which Azure component sits above subscriptions?

Answer:
Management Groups

---

# Q9

Which Azure component contains datacenters?

Answer:
Region

---

# Q10

Availability Zones exist inside what?

Answer:
Regions

---

# 16. Final Revision Notes

| Concept           | Key Idea                  |
| ----------------- | ------------------------- |
| Region            | Geographic area           |
| Availability Zone | Separate datacenter       |
| Region Pair       | Disaster recovery partner |
| Resource Group    | Logical container         |
| Subscription      | Billing boundary          |
| Management Group  | Organize subscriptions    |

---

# Most Important Exam Concepts

1. Region vs Availability Zone
2. Availability Zone vs Region Pair
3. Resource Group vs Subscription
4. Azure hierarchy
5. Billing boundaries
6. Disaster recovery concepts

---

# Quick Revision Table

| Component         | Purpose                           |
| ----------------- | --------------------------------- |
| Region            | Low latency and global deployment |
| Availability Zone | Datacenter-level fault tolerance  |
| Region Pair       | Regional disaster recovery        |
| Resource Group    | Organize resources                |
| Subscription      | Billing and access control        |
| Management Group  | Organize subscriptions            |

---

