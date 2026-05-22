# Azure AI-901 Preparation Notes
# Phase 1 — Build Azure + AI Basics

---

# Table of Contents

1. Introduction to Cloud Computing
2. Types of Cloud Computing
3. Cloud Deployment Models
4. Important Cloud Concepts
5. CapEx vs OpEx
6. Top Cloud Providers
7. Azure Regions
8. Availability Zones
9. Resource Groups
10. Subscriptions
11. Azure Portal
12. Azure Resource Manager (ARM)
13. Azure Storage
14. Azure Networking
15. Important Interview Questions

---

# 1. Introduction to Cloud Computing

## What is Cloud Computing?

Cloud computing means using computing services over the internet instead of managing physical hardware yourself.

These services include:
- Servers
- Storage
- Databases
- Networking
- Artificial Intelligence Services
- Virtual Machines
- Software Applications

Instead of buying expensive infrastructure, companies rent resources from cloud providers.

---

## Major Cloud Providers

| Company | Platform |
|---|---|
| Microsoft | Azure |
| Amazon | AWS |
| Google | GCP |

---

## Why Cloud Computing Became Popular

### 1. Cost Saving
No need to buy expensive hardware.

### 2. Scalability
Resources can increase or decrease based on demand.

### 3. Global Access
Applications become accessible worldwide.

### 4. Faster Development
Developers can deploy applications quickly.

### 5. Security and Backup
Cloud providers handle:
- Security
- Backups
- Disaster recovery

---

# 2. Types of Cloud Computing

---

# IaaS — Infrastructure as a Service

The cloud provider manages:
- Hardware
- Networking
- Storage

The user manages:
- Operating System
- Applications
- Runtime

## Examples
- Azure Virtual Machines
- AWS EC2

---

# PaaS — Platform as a Service

The cloud provider manages:
- Infrastructure
- Operating System
- Runtime

The user manages:
- Applications
- Data

## Example
Azure App Service

---

# SaaS — Software as a Service

Everything is managed by the provider.

Users simply use the software through the internet.

## Examples
- Microsoft 365
- Google Workspace
- Zoom

---

# Comparison Table

| Model | User Manages | Provider Manages |
|---|---|---|
| IaaS | OS, Applications | Hardware |
| PaaS | Applications | Platform + Hardware |
| SaaS | Almost Nothing | Everything |

---

# 3. Cloud Deployment Models

---

# Public Cloud

Services are available over the internet for everyone.

## Examples
- Azure
- AWS
- GCP

### Advantages
- Cost effective
- Highly scalable

---

# Private Cloud

Cloud dedicated to one organization.

### Advantages
- More control
- Better security

### Disadvantages
- Expensive

---

# Hybrid Cloud

Combination of:
- Public cloud
- Private cloud

Most companies use hybrid cloud architecture.

---

# 4. Important Cloud Concepts

---

# High Availability

The system remains operational even during failures.

---

# Scalability

Ability to increase or decrease resources.

## Types
- Vertical Scaling
- Horizontal Scaling

---

# Elasticity

Automatic scaling based on demand.

---

# Reliability

System performs consistently.

---

# Predictability

Performance and costs remain predictable.

---

# Security

Cloud providers offer:
- Encryption
- Firewalls
- Identity management

---

# Governance

Rules and policies for cloud resource usage.

---

# 5. CapEx vs OpEx

---

# CapEx — Capital Expenditure

Traditional IT model:
- Buy hardware upfront
- Large initial investment

---

# OpEx — Operational Expenditure

Cloud model:
- Pay as you use
- Monthly operational expense

Cloud computing mainly uses OpEx.

---

# 6. Azure Regions

---

# What is a Region?

An Azure Region is a geographical area containing one or more datacenters.

---

# Examples of Regions

| Region Name | Location |
|---|---|
| East US | Virginia |
| West Europe | Netherlands |
| Central India | Pune |
| South India | Chennai |

---

# Why Regions are Important

### Low Latency
Closer regions provide faster response.

### Compliance
Data can remain inside a specific country.

### Disaster Recovery
Backup regions help during failures.

---

# Region Pairs

Microsoft pairs regions for backup and recovery.

Example:
- Central India ↔ South India

---

# 7. Availability Zones

---

# What are Availability Zones?

Availability Zones are physically separate datacenters inside the same Azure region.

Each zone has:
- Independent power
- Cooling
- Networking

---

# Why Availability Zones are Important

If one datacenter fails:
- Other zones continue running applications.

This improves:
- Reliability
- Fault tolerance
- High availability

---

# Difference Between Region and Availability Zone

| Region | Availability Zone |
|---|---|
| Geographic area | Separate datacenter |
| Large scale | Small scale |
| Disaster recovery | Fault tolerance |

---

# 8. Resource Groups

---

# What is a Resource Group?

A Resource Group is a logical container for Azure resources.

---

# Resources Inside Resource Groups

Examples:
- Virtual Machines
- Databases
- Storage Accounts
- AI Services
- Networks

---

# Benefits of Resource Groups

### Organization
Keeps related resources together.

### Access Control
Permissions can be managed easily.

### Cost Management
Track spending for projects.

### Easy Deletion
Delete entire project resources together.

---

# Important Point

One resource belongs to only one Resource Group.

---

# 9. Subscriptions

---

# What is an Azure Subscription?

A Subscription is a billing and management boundary in Azure.

---

# Why Subscriptions are Important

### Billing Management
Tracks Azure costs.

### Access Control
Controls permissions.

### Resource Limits
Defines quotas.

---

# Hierarchy

```text
Subscription
   ↓
Resource Group
   ↓
Resources