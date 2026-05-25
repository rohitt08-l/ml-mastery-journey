# AZ-900 Module 1 — Cloud Concepts Complete Guide

# Table of Contents

1. Introduction to Cloud Computing
2. What is Cloud Computing?
3. Evolution of Computing
4. Traditional IT vs Cloud Computing
5. Why Cloud Computing Exists
6. Characteristics of Cloud Computing
7. Shared Responsibility Model
8. Cloud Deployment Models

   * Public Cloud
   * Private Cloud
   * Hybrid Cloud
9. Use Cases of Cloud Models
10. Consumption-Based Model
11. Cloud Pricing Models
12. Serverless Computing
13. Benefits of Cloud Computing
14. High Availability
15. Scalability
16. Elasticity
17. Reliability
18. Predictability
19. Security
20. Governance
21. Manageability
22. Cloud Service Types
23. Infrastructure as a Service (IaaS)
24. Platform as a Service (PaaS)
25. Software as a Service (SaaS)
26. Comparison of IaaS, PaaS, SaaS
27. Real-World Use Cases
28. Important AZ-900 Exam Tips
29. Memory Tricks
30. Practice Questions
31. Final Revision Notes

---

# 1. Introduction to Cloud Computing

Cloud computing is one of the most important technologies in modern IT industries.

Today almost every company uses cloud services:

* Netflix
* Amazon
* Instagram
* Swiggy
* Zomato
* Banking systems
* AI platforms
* Healthcare systems

Cloud computing changed the way companies:

* build applications
* store data
* scale systems
* manage infrastructure
* deploy AI models

Before cloud computing, companies had to purchase expensive servers and maintain their own datacenters.

Now companies can rent computing resources from cloud providers.

Major cloud providers include:

* Microsoft Azure
* Amazon Web Services (AWS)
* Google Cloud Platform (GCP)

---

# 2. What is Cloud Computing?

## Definition

Cloud computing is the delivery of computing services over the internet.

These services include:

* Servers
* Storage
* Databases
* Networking
* Software
* Analytics
* Artificial Intelligence

Instead of owning physical infrastructure, organizations rent resources from cloud providers.

---

# Simple Explanation

Instead of:

* buying servers
* building datacenters
* managing hardware

Companies can:

* rent virtual resources
* pay only for usage
* scale instantly

---

# Real-Life Analogy

## Traditional IT

Like buying your own car.

You must manage:

* fuel
* maintenance
* repairs
* parking

## Cloud Computing

Like using Uber.

You:

* use service when needed
* pay for usage
* no maintenance responsibility

---

# Technical Definition

Cloud computing provides:

* on-demand access
* scalable resources
* internet-based delivery
* pay-as-you-go pricing

---

# 3. Evolution of Computing

## Phase 1 — Traditional Computing

Companies owned:

* physical servers
* networking devices
* storage systems

Problems:

* expensive
* difficult to scale
* maintenance-heavy
* downtime issues

---

## Phase 2 — Virtualization

One physical server could host multiple virtual machines.

Benefits:

* better hardware utilization
* reduced costs
* easier management

---

## Phase 3 — Cloud Computing

Resources delivered over internet.

Benefits:

* scalability
* flexibility
* global access
* cost optimization

---

# 4. Traditional IT vs Cloud Computing

| Traditional IT           | Cloud Computing                 |
| ------------------------ | ------------------------------- |
| Buy hardware             | Rent resources                  |
| Large upfront cost       | Pay-as-you-go                   |
| Manual scaling           | Automatic scaling               |
| Long deployment time     | Instant deployment              |
| Maintenance required     | Provider manages infrastructure |
| Limited flexibility      | Highly flexible                 |
| Hardware failures common | High availability               |

---

# 5. Why Cloud Computing Exists

Cloud computing exists because organizations faced several challenges:

## Problems with Traditional Infrastructure

### High Cost

Building datacenters is expensive.

### Maintenance Complexity

Servers require:

* updates
* cooling
* monitoring
* repairs

### Scaling Problems

During high traffic:

* systems crash
* performance decreases

### Disaster Recovery Issues

Hardware failures may cause:

* data loss
* downtime

### Global Access Problems

Serving worldwide users becomes difficult.

---

# Cloud Solves These Problems

Cloud providers offer:

* global infrastructure
* high availability
* scalability
* managed services
* security
* disaster recovery

---

# 6. Characteristics of Cloud Computing

## 1. On-Demand Self-Service

Users can create resources instantly.

Example:

* Create VM in minutes.

---

## 2. Broad Network Access

Services accessible through internet.

Example:

* Access Azure Portal from anywhere.

---

## 3. Resource Pooling

Resources shared among multiple users.

Example:

* Multiple companies use same datacenter.

---

## 4. Rapid Elasticity

Resources scale automatically.

Example:

* E-commerce traffic spikes.

---

## 5. Measured Service

Users pay only for usage.

Example:

* Hourly VM billing.

---

# 7. Shared Responsibility Model

This is one of the MOST IMPORTANT AZ-900 concepts.

Cloud security responsibilities are shared between:

* Cloud provider
* Customer

---

# Basic Principle

## Security OF the Cloud

Managed by cloud provider.

## Security IN the Cloud

Managed by customer.

---

# Microsoft Responsibilities

Microsoft manages:

* physical datacenters
* hardware
* cooling systems
* networking infrastructure
* physical security
* power systems

---

# Customer Responsibilities

Customer manages:

* user accounts
* passwords
* application settings
* access permissions
* data security
* operating systems (in some models)

---

# Shared Responsibility by Service Model

| Component         | On-Premises | IaaS     | PaaS     | SaaS     |
| ----------------- | ----------- | -------- | -------- | -------- |
| Physical Security | Customer    | Provider | Provider | Provider |
| Hardware          | Customer    | Provider | Provider | Provider |
| Networking        | Customer    | Provider | Provider | Provider |
| Operating System  | Customer    | Customer | Provider | Provider |
| Runtime           | Customer    | Customer | Provider | Provider |
| Applications      | Customer    | Customer | Customer | Provider |
| Data              | Customer    | Customer | Customer | Customer |
| Identity & Access | Customer    | Customer | Customer | Customer |

---

# Example

If your Azure Virtual Machine gets hacked due to weak password:

Responsibility = Customer

Because:

* password management
* access control
  are customer responsibilities.

---

# 8. Cloud Deployment Models

There are three major cloud deployment models:

1. Public Cloud
2. Private Cloud
3. Hybrid Cloud

---

# Public Cloud

## Definition

Resources are owned and operated by third-party cloud providers.

Services delivered over internet.

Examples:

* Microsoft Azure
* AWS
* Google Cloud

---

# Characteristics

* Shared infrastructure
* Pay-as-you-go
* Highly scalable
* Low cost
* Minimal maintenance

---

# Advantages

* Low investment
* Fast deployment
* Global access
* High scalability

---

# Disadvantages

* Less control
* Shared environment
* Internet dependency

---

# Private Cloud

## Definition

Cloud infrastructure dedicated to a single organization.

May exist:

* on-premises
* hosted by third-party

---

# Characteristics

* Dedicated resources
* High security
* More control
* Expensive

---

# Advantages

* Better control
* Strong security
* Custom configurations

---

# Disadvantages

* High cost
* Maintenance required
* Limited scalability

---

# Hybrid Cloud

## Definition

Combination of:

* public cloud
* private cloud

Allows data and applications to move between environments.

---

# Characteristics

* Flexible
* Balanced approach
* Supports legacy systems

---

# Advantages

* Better flexibility
* Improved security
* Cost optimization

---

# Disadvantages

* Complex management
* Integration challenges

---

# 9. Use Cases of Cloud Models

# Public Cloud Use Cases

Best for:

* startups
* web applications
* AI projects
* mobile apps
* development/testing

Example:
A startup launches AI chatbot using Azure.

---

# Private Cloud Use Cases

Best for:

* banking
* military
* government systems
* healthcare

Example:
Hospital stores sensitive patient data.

---

# Hybrid Cloud Use Cases

Best for:

* enterprises
* companies migrating to cloud
* organizations with compliance requirements

Example:
Bank stores customer records locally but hosts website on Azure.

---

# Comparison Table

| Feature     | Public  | Private   | Hybrid |
| ----------- | ------- | --------- | ------ |
| Cost        | Low     | High      | Medium |
| Scalability | High    | Medium    | High   |
| Security    | Good    | Very High | High   |
| Control     | Limited | High      | Medium |
| Maintenance | Minimal | High      | Medium |

---

# 10. Consumption-Based Model

Cloud follows a consumption-based pricing model.

Users:

* pay only for usage
* avoid large upfront investments

---

# Example

If you use:

* VM for 5 hours
* pay for 5 hours only

---

# Benefits

* Cost optimization
* Flexibility
* No overprovisioning
* Better budgeting

---

# Real-Life Analogy

Like electricity bill.

More usage = higher bill.

Less usage = lower bill.

---

# 11. Cloud Pricing Models

# CapEx (Capital Expenditure)

## Definition

Large upfront investment.

Example:

* Buying servers
* Building datacenter

---

# Characteristics

* Expensive initial setup
* Hardware ownership
* Maintenance responsibility

---

# OpEx (Operational Expenditure)

## Definition

Pay based on consumption.

Example:

* Monthly Azure bill

---

# Characteristics

* Flexible
* No hardware ownership
* Subscription/pay-as-you-go

---

# CapEx vs OpEx

| CapEx              | OpEx                 |
| ------------------ | -------------------- |
| Buy infrastructure | Rent services        |
| Upfront investment | Usage-based payment  |
| Traditional IT     | Cloud computing      |
| Long-term assets   | Operational expenses |

---

# Memory Trick

CapEx = BUY

OpEx = RENT

---

# 12. Serverless Computing

## Definition

Serverless allows developers to run code without managing servers.

Cloud provider automatically:

* provisions infrastructure
* scales resources
* manages servers

---

# Important Note

Servers still exist.

"Serverless" means:
Developers do not manage servers.

---

# Example

Azure Functions

Code executes only when triggered.

---

# Benefits

* No server management
* Automatic scaling
* Pay only when code runs
* Faster development

---

# Use Cases

* APIs
* automation
* event-driven apps
* chatbot backends

---

# Example Scenario

User uploads image.

Azure Function automatically:

* resizes image
* stores result
* sends notification

---

# 13. Benefits of Cloud Computing

Cloud provides many business and technical benefits.

Major benefits:

* High Availability
* Scalability
* Reliability
* Predictability
* Security
* Governance
* Manageability

---

# 14. High Availability

## Definition

Ability of system to remain operational for long periods.

---

# Goal

Minimize downtime.

---

# How Cloud Achieves High Availability

Using:

* redundancy
* failover systems
* multiple datacenters
* availability zones

---

# Example

Banking applications should work 24/7.

If one server fails:

* another server takes over.

---

# SLA (Service Level Agreement)

Cloud providers guarantee uptime percentages.

Example:
99.9% uptime.

---

# 15. Scalability

## Definition

Ability to increase or decrease resources based on demand.

---

# Types of Scaling

## Vertical Scaling

Increase power of existing machine.

Example:

* 4 GB RAM → 16 GB RAM

---

## Horizontal Scaling

Add more machines.

Example:

* 1 VM → 10 VMs

---

# Example

During IPL ticket booking:
traffic increases massively.

Cloud can scale resources.

---

# 16. Elasticity

## Definition

Automatic scaling based on workload.

---

# Difference Between Scalability and Elasticity

| Scalability               | Elasticity                    |
| ------------------------- | ----------------------------- |
| Manual or planned scaling | Automatic scaling             |
| Long-term growth          | Real-time adjustment          |
| Add resources manually    | Resources added automatically |

---

# Example

E-commerce website during sale:

* servers automatically increase
* servers reduce after sale

---

# 17. Reliability

## Definition

Ability of system to recover from failures.

---

# Cloud Reliability Features

* backup systems
* replication
* disaster recovery
* fault tolerance

---

# Example

If one datacenter fails:
services continue from another location.

---

# 18. Predictability

## Definition

Ability to predict:

* performance
* costs

---

# Achieved Through

* monitoring
* analytics
* AI-based recommendations
* cost management tools

---

# Example

Azure Cost Management predicts monthly expenses.

---

# 19. Security

## Definition

Cloud providers offer advanced security mechanisms.

---

# Security Features

* encryption
* firewalls
* identity management
* threat detection
* MFA
* DDoS protection

---

# Important Concept

Cloud provider secures infrastructure.

Customer still responsible for:

* passwords
* access control
* application security

---

# 20. Governance

## Definition

Governance ensures resources comply with company policies.

---

# Examples

Organizations may enforce:

* naming conventions
* allowed regions
* spending limits
* security standards

---

# Governance Tools in Azure

* Azure Policy
* Resource Locks
* Tags
* Blueprints

---

# 21. Manageability

## Definition

Ability to efficiently manage cloud resources.

---

# Management Methods

## Azure Portal

Web-based interface.

## Azure CLI

Command-line management.

## PowerShell

Automation scripting.

## ARM Templates

Infrastructure as code.

---

# Benefits

* automation
* centralized management
* remote access
* monitoring

---

# 22. Cloud Service Types

Three major cloud service types:

1. IaaS
2. PaaS
3. SaaS

These define how much responsibility belongs to:

* customer
* cloud provider

---

# 23. Infrastructure as a Service (IaaS)

## Definition

Cloud provider provides infrastructure.

Customer manages:

* operating systems
* applications
* configurations

---

# Provider Manages

* hardware
* networking
* storage
* virtualization

---

# Customer Manages

* operating systems
* applications
* middleware
* security settings

---

# Examples

* Azure Virtual Machines
* AWS EC2

---

# Real-Life Analogy

Like renting an empty apartment.

You arrange:

* furniture
* appliances
* decorations

---

# Advantages

* High control
* Flexible
* Custom configurations

---

# Disadvantages

* More management responsibility
* Requires technical expertise

---

# IaaS Use Cases

* lift-and-shift migration
* testing environments
* custom enterprise applications

---

# 24. Platform as a Service (PaaS)

## Definition

Cloud provider manages:

* infrastructure
* operating system
* runtime

Developers focus on:

* application development

---

# Provider Manages

* servers
* operating systems
* runtime
* scaling

---

# Customer Manages

* application code
* data

---

# Examples

* Azure App Service
* Azure SQL Database
* Google App Engine

---

# Real-Life Analogy

Like renting a fully furnished apartment.

You only focus on living.

---

# Advantages

* Faster development
* Less maintenance
* Automatic updates
* Easy scalability

---

# Disadvantages

* Less control
* Platform dependency

---

# PaaS Use Cases

* web applications
* mobile backends
* APIs
* AI applications

---

# 25. Software as a Service (SaaS)

## Definition

Complete software delivered over internet.

Users simply use the application.

---

# Provider Manages

Everything:

* infrastructure
* platform
* application

---

# Customer Responsibility

Minimal:

* user settings
* data

---

# Examples

* Gmail
* Microsoft 365
* Google Docs
* Salesforce

---

# Real-Life Analogy

Like staying in a hotel.

Everything managed for you.

---

# Advantages

* No maintenance
* Accessible anywhere
* Subscription-based
* Easy collaboration

---

# Disadvantages

* Limited customization
* Internet dependency

---

# SaaS Use Cases

* email systems
* collaboration tools
* CRM software
* online learning platforms

---

# 26. Comparison of IaaS, PaaS, SaaS

| Feature                | IaaS           | PaaS                      | SaaS          |
| ---------------------- | -------------- | ------------------------- | ------------- |
| Control Level          | High           | Medium                    | Low           |
| Provider Manages       | Infrastructure | Infrastructure + Platform | Everything    |
| Customer Focus         | OS & Apps      | Apps                      | Usage         |
| Technical Skill Needed | High           | Medium                    | Low           |
| Examples               | Azure VM       | Azure App Service         | Microsoft 365 |

---

# 27. Real-World Use Cases

# IaaS Example

Company migrates old ERP system to cloud.

Needs:

* custom OS
* full control

Uses Azure VMs.

---

# PaaS Example

Startup builds AI chatbot.

Developers only focus on:

* coding
* deployment

Uses Azure App Service.

---

# SaaS Example

Employees use Microsoft Teams.

No infrastructure management needed.

---

# 28. Important AZ-900 Exam Tips

Microsoft commonly asks:

* scenario-based questions
* responsibility questions
* cloud model comparisons
* service type selection

---

# Common Confusing Concepts

## Scalability vs Elasticity

Scalability:
manual/planned growth.

Elasticity:
automatic scaling.

---

## High Availability vs Reliability

High Availability:
system stays operational.

Reliability:
system recovers from failure.

---

## IaaS vs PaaS

IaaS:
manage OS.

PaaS:
focus only on applications.

---

# 29. Memory Tricks

# CapEx vs OpEx

CapEx = BUY

OpEx = RENT

---

# IaaS vs PaaS vs SaaS

IaaS = More Control

PaaS = Focus on Development

SaaS = Just Use Software

---

# Scalability vs Elasticity

Scalability = Manual Growth

Elasticity = Automatic Growth

---

# Shared Responsibility

Security OF cloud = Provider

Security IN cloud = Customer

---

# 30. Practice Questions

## Q1

Which cloud model combines public and private infrastructure?

Answer: Hybrid Cloud

---

## Q2

Which service model gives maximum control?

Answer: IaaS

---

## Q3

Which service model is Gmail?

Answer: SaaS

---

## Q4

Adding more servers is called?

Answer: Horizontal Scaling

---

## Q5

Who manages physical security in Azure?

Answer: Microsoft

---

## Q6

Increasing RAM on same VM is called?

Answer: Vertical Scaling

---

## Q7

Pay-as-you-go pricing is example of?

Answer: OpEx

---

## Q8

Which cloud model is best for startups?

Answer: Public Cloud

---

# 31. Final Revision Notes

# Important Definitions

Cloud Computing:
Delivery of computing services over internet.

---

High Availability:
System remains operational.

---

Scalability:
Ability to increase/decrease resources.

---

Elasticity:
Automatic scaling.

---

Reliability:
Recovery from failures.

---

IaaS:
Infrastructure provided by cloud provider.

---

PaaS:
Platform managed by provider.

---

SaaS:
Complete software delivered online.

---

# Most Important Exam Topics

1. Shared Responsibility Model
2. IaaS vs PaaS vs SaaS
3. Public vs Private vs Hybrid Cloud
4. Scalability vs Elasticity
5. CapEx vs OpEx
6. High Availability
7. Consumption-Based Model

---