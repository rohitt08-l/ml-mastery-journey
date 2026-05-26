# AZ-900 Module 3 — Azure Compute Services

# Table of Contents

1. Introduction to Azure Compute Services
2. What is Compute in Cloud Computing?
3. Why Compute Services are Important
4. Azure Compute Categories
5. Azure Virtual Machines (VMs)
6. Virtual Machine Components
7. VM Architecture
8. Types of Virtual Machines
9. VM Use Cases
10. VM Advantages and Disadvantages
11. Azure Virtual Machine Scale Sets (VMSS)
12. VMSS Architecture
13. VMSS Benefits
14. Containers
15. Container Architecture
16. Containers vs Virtual Machines
17. Docker Containers
18. Container Benefits and Limitations
19. Azure Kubernetes Service (AKS)
20. Kubernetes Concepts
21. AKS Architecture
22. AKS Benefits and Use Cases
23. Azure App Service
24. App Service Architecture
25. App Service Features
26. Azure Functions
27. Azure Functions Architecture
28. Serverless Computing
29. Event-Driven Architecture
30. Comparing Azure Compute Services
31. Real-World Compute Scenarios
32. Best Practices
33. Common AZ-900 Confusing Concepts
34. AZ-900 Exam Tips
35. Memory Tricks
36. Practice Questions
37. Final Revision Notes

---

# 1. Introduction to Azure Compute Services

Azure Compute Services provide the processing power required to run:

* applications
* operating systems
* AI models
* databases
* APIs
* websites
* enterprise systems

Compute is one of the core foundations of cloud computing.

Without compute resources:

* applications cannot run
* websites cannot function
* AI systems cannot process data

---

# Why Azure Compute Services are Important

Modern applications require:

* scalability
* flexibility
* high availability
* rapid deployment
* automation

Azure Compute Services help organizations:

* deploy applications quickly
* scale automatically
* reduce infrastructure management
* optimize costs

---

# Real-World Examples

Azure compute powers:

* AI chatbots
* streaming platforms
* banking applications
* hospital management systems
* ERP applications
* e-commerce platforms

---

# 2. What is Compute in Cloud Computing?

# Definition

Compute refers to:

> Processing resources used to execute applications and workloads.

Compute resources include:

* CPU
* RAM
* Operating Systems
* Runtime Environments
* Processing Power

---

# Compute in Traditional Datacenters

Organizations previously had to:

* buy physical servers
* install operating systems
* maintain hardware
* manage networking

Problems:

* expensive
* difficult scaling
* maintenance-heavy

---

# Compute in Cloud

Cloud providers supply compute resources on demand.

Organizations can:

* deploy servers instantly
* scale resources automatically
* pay only for usage

---

# 3. Why Compute Services are Important

# Benefits of Cloud Compute

## Scalability

Increase/decrease resources.

## Elasticity

Automatic scaling.

## High Availability

Applications remain online.

## Cost Optimization

Pay only for usage.

## Faster Deployment

Resources created in minutes.

## Global Reach

Deploy worldwide.

---

# 4. Azure Compute Categories

Azure compute services can be grouped into:

| Category           | Examples        |
| ------------------ | --------------- |
| Virtual Machines   | Azure VM, VMSS  |
| Container Services | Containers, AKS |
| PaaS Hosting       | App Service     |
| Serverless         | Azure Functions |

---

# 5. Azure Virtual Machines (VMs)

# Definition

Azure Virtual Machine (VM) is:

> A software-based computer running inside Azure.

A VM behaves like a physical computer.

---

# VM Includes

* CPU
* RAM
* Storage
* Networking
* Operating System

---

# Operating Systems Supported

Azure VMs support:

* Windows
* Linux

---

# Why VMs Exist

Organizations need:

* complete control
* custom configurations
* legacy application support

---

# Azure VM is Which Service Type?

Azure VM belongs to:

# Infrastructure as a Service (IaaS)

---

# Responsibilities in Azure VM

# Azure Manages

* physical hardware
* networking infrastructure
* datacenters

---

# Customer Manages

* operating system
* applications
* updates
* security patches
* configurations

---

# Real-World Example

Company migrates old ERP system to cloud.

Needs:

* custom OS
* custom software
* administrative control

Solution:
Azure Virtual Machines.

---

# VM Architecture

```text
Azure Infrastructure
    ↓
Hypervisor
    ↓
Virtual Machine
    ↓
Operating System
    ↓
Applications
```

---

# Hypervisor

A hypervisor creates and manages virtual machines.

It allows multiple VMs to run on one physical server.

---

# VM Advantages

## Full Control

Install any supported software.

## Flexibility

Supports many workloads.

## Custom Configurations

Configure networking and OS.

## Supports Legacy Applications

Useful for older enterprise systems.

---

# VM Disadvantages

## Requires Management

Customer manages updates.

## Higher Maintenance

OS and software maintenance required.

## Security Responsibility

Customer secures VM.

---

# VM Use Cases

* lift-and-shift migration
* development environments
* testing systems
* AI/ML workloads
* enterprise applications
* gaming servers

---

# Important AZ-900 Exam Point

If question says:

* full OS control
* install custom software
* custom networking

Answer often:

# Azure Virtual Machine

---

# 6. Virtual Machine Components

A virtual machine contains:

## Virtual CPU

Processes instructions.

## Virtual RAM

Temporary memory.

## Virtual Disk

Stores operating system and data.

## Network Interface

Provides connectivity.

## Operating System

Windows or Linux.

---

# 7. VM Architecture

# Azure VM Workflow

```text
User Request
    ↓
Azure Hypervisor
    ↓
VM Creation
    ↓
OS Installation
    ↓
Application Deployment
```

---

# 8. Types of Virtual Machines

Azure provides different VM families.

---

# General Purpose VMs

Balanced CPU and memory.

Best for:

* development
* testing
* small databases

---

# Compute Optimized VMs

High CPU power.

Best for:

* gaming
* analytics
* AI inference

---

# Memory Optimized VMs

High RAM capacity.

Best for:

* large databases
* SAP systems

---

# GPU VMs

Includes graphical processing units.

Best for:

* deep learning
* AI training
* image processing

---

# 9. VM Use Cases

# Enterprise Applications

Run old enterprise systems.

---

# AI/ML Workloads

Train machine learning models.

---

# Testing Environments

Create temporary testing systems.

---

# Development Servers

Host development environments.

---

# Disaster Recovery

Backup systems in cloud.

---

# 10. VM Advantages and Disadvantages

| Advantages              | Disadvantages              |
| ----------------------- | -------------------------- |
| Full control            | Requires maintenance       |
| Flexible                | Higher management overhead |
| Supports legacy apps    | OS management required     |
| Custom software support | Security responsibility    |

---

# 11. Azure Virtual Machine Scale Sets (VMSS)

# Definition

VMSS allows:

> Automatic deployment and management of multiple virtual machines.

---

# Why VMSS Exists

Managing many VMs manually is difficult.

VMSS automates:

* scaling
* deployment
* monitoring
* load balancing

---

# VMSS Features

## Automatic Scaling

Increase/decrease VMs automatically.

## High Availability

Multiple VM instances.

## Load Distribution

Traffic balanced across VMs.

## Cost Optimization

Scale based on demand.

---

# VMSS Architecture

```text
Load Balancer
    ↓
VM Instance 1
VM Instance 2
VM Instance 3
```

---

# Real-World Example

E-commerce platform during sale.

Traffic increases.

VMSS automatically creates more VMs.

---

# VMSS Use Cases

* scalable web applications
* enterprise platforms
* large APIs
* high-traffic applications

---

# Important AZ-900 Point

VMSS =

# Auto-scaling virtual machines

---

# 12. VMSS Benefits

## Scalability

Automatic growth.

## Reliability

Multiple VM instances.

## High Availability

Reduces downtime.

## Automation

Less manual management.

---

# 13. Containers

# Definition

A container is:

> A lightweight package containing application code and dependencies.

---

# Why Containers Exist

Traditional applications faced:

* dependency conflicts
* environment inconsistencies
* deployment problems

Containers solve these problems.

---

# Container Includes

* application code
* runtime
* libraries
* dependencies

---

# Container Architecture

```text
Host Operating System
    ↓
Container Runtime
    ↓
Container 1
Container 2
Container 3
```

---

# Containers vs Virtual Machines

| Virtual Machine       | Container            |
| --------------------- | -------------------- |
| Includes full OS      | Shares host OS       |
| Heavy                 | Lightweight          |
| Slow startup          | Fast startup         |
| Higher resource usage | Lower resource usage |
| Better isolation      | Faster portability   |

---

# Container Benefits

## Portability

Runs consistently everywhere.

## Fast Deployment

Starts quickly.

## Lightweight

Uses fewer resources.

## Scalability

Supports microservices.

---

# Container Limitations

## Shared OS

Less isolation than VMs.

## Complexity at Scale

Requires orchestration.

---

# 14. Docker Containers

# What is Docker?

Docker is the most popular container platform.

---

# Docker Components

## Docker Image

Blueprint/template.

## Docker Container

Running instance of image.

---

# Docker Workflow

```text
Docker Image
    ↓
Docker Container
    ↓
Application Running
```

---

# Real-World Example

AI chatbot packaged in Docker container.

Can run:

* locally
* on Azure
* on AWS
* on Kubernetes

---

# 15. Container Benefits and Limitations

| Benefits              | Limitations           |
| --------------------- | --------------------- |
| Lightweight           | Shared OS             |
| Portable              | Security concerns     |
| Fast startup          | Orchestration needed  |
| Consistent deployment | Networking complexity |

---

# 16. Azure Kubernetes Service (AKS)

# What is Kubernetes?

Kubernetes is:

> A container orchestration platform.

It manages:

* deployment
* scaling
* monitoring
* networking
* recovery

---

# Why Kubernetes Exists

Managing containers manually becomes difficult.

Kubernetes automates container management.

---

# Azure Kubernetes Service (AKS)

AKS is:

> Managed Kubernetes service provided by Azure.

---

# AKS Features

## Automatic Scaling

Scale containers automatically.

## Self-Healing

Restart failed containers.

## Load Balancing

Distribute traffic.

## Orchestration

Manage many containers.

---

# AKS Architecture

```text
AKS Cluster

 ├── Node 1
 │     ├── Container A
 │     └── Container B
 │
 ├── Node 2
 │     ├── Container C
 │     └── Container D
```

---

# Kubernetes Concepts

## Cluster

Group of nodes.

## Node

Machine running containers.

## Pod

Smallest deployable unit.

## Service

Networking abstraction.

---

# AKS Benefits

## Simplified Kubernetes Management

Azure manages infrastructure.

## Scalability

Handles large workloads.

## High Availability

Supports resilient applications.

## Automation

Automates deployments.

---

# AKS Use Cases

* microservices
* enterprise applications
* AI platforms
* large-scale APIs
* DevOps pipelines

---

# Important AZ-900 Point

AKS =

# Managed Kubernetes service

---

# 17. Azure App Service

# Definition

Azure App Service is:

> A fully managed platform for hosting web apps and APIs.

---

# Service Type

Azure App Service belongs to:

# Platform as a Service (PaaS)

---

# Why App Service Exists

Developers want to:

* focus on coding
* avoid infrastructure management

Azure manages:

* operating systems
* runtime
* patching
* scaling

---

# App Service Supports

* Python
* Java
* Node.js
* PHP
* .NET

---

# App Service Architecture

```text
Application Code
    ↓
Azure App Service Platform
    ↓
Azure Infrastructure
```

---

# App Service Features

## Automatic Scaling

## Managed Infrastructure

## SSL Support

## CI/CD Integration

## Built-in Security

---

# Real-World Example

Startup develops AI chatbot website.

Needs:

* quick deployment
* no OS management

Solution:
Azure App Service.

---

# App Service Advantages

## Faster Development

## Lower Maintenance

## Built-in Scaling

## Integrated Monitoring

---

# App Service Limitations

## Less Control

Compared to VMs.

## Platform Dependency

Application tied to platform.

---

# Important AZ-900 Point

If question says:

* host web app
* no server management
* focus on coding

Answer often:

# Azure App Service

---

# 18. Azure Functions

# Definition

Azure Functions is:

> Event-driven serverless compute service.

Code executes only when triggered.

---

# Trigger Examples

* HTTP request
* file upload
* database update
* timer event

---

# Why Functions Exist

Developers want:

* no server management
* lower costs
* event-driven automation

---

# Azure Functions Architecture

```text
Event Trigger
    ↓
Azure Function Executes
    ↓
Result Returned
```

---

# Azure Functions Benefits

## Pay Only When Running

## Automatic Scaling

## No Infrastructure Management

## Fast Development

---

# Azure Functions Use Cases

* automation
* notifications
* background jobs
* API triggers
* image processing

---

# Real-World Example

User uploads image.

Azure Function automatically:

* resizes image
* stores image
* sends notification

---

# Important AZ-900 Point

Azure Functions =

# Serverless compute

---

# 19. Serverless Computing

# Definition

Serverless computing means:

> Developers run code without managing servers.

Servers still exist.

Cloud provider manages them automatically.

---

# Serverless Characteristics

## Event-Driven

## Automatic Scaling

## Consumption-Based Billing

## No Server Management

---

# Azure Serverless Services

* Azure Functions
* Logic Apps
* Event Grid

---

# Benefits of Serverless

## Faster Development

## Lower Operational Cost

## High Scalability

## Better Productivity

---

# Serverless Limitations

## Cold Start Delay

## Less Infrastructure Control

## Runtime Limitations

---

# Important AZ-900 Point

Serverless =

# Focus only on code and business logic

---

# 20. Event-Driven Architecture

# Definition

Applications respond automatically to events.

---

# Examples of Events

* file upload
* user login
* payment completion
* database update

---

# Event Workflow

```text
Event Occurs
    ↓
Trigger Activated
    ↓
Azure Function Executes
    ↓
Action Completed
```

---

# 21. Comparing Azure Compute Services

| Service          | Type               | Control Level | Best Use Case           |
| ---------------- | ------------------ | ------------- | ----------------------- |
| Virtual Machines | IaaS               | High          | Full OS control         |
| VM Scale Sets    | IaaS               | High          | Auto-scaling VMs        |
| Containers       | Containerized      | Medium        | Portable apps           |
| AKS              | Managed Kubernetes | Medium        | Container orchestration |
| App Service      | PaaS               | Low-Medium    | Web apps/APIs           |
| Azure Functions  | Serverless         | Low           | Event-driven tasks      |

---

# 22. Real-World Compute Scenarios

# Scenario 1 — ERP Migration

Need:

* full OS control
* legacy application support

Solution:
Azure VM

---

# Scenario 2 — Shopping Website

Need:

* automatic scaling during sales

Solution:
VM Scale Sets

---

# Scenario 3 — AI Microservices

Need:

* portable scalable containers

Solution:
Containers + AKS

---

# Scenario 4 — Startup Website

Need:

* fast deployment
* no infrastructure management

Solution:
Azure App Service

---

# Scenario 5 — Background Automation

Need:

* event-triggered execution

Solution:
Azure Functions

---

# 23. Best Practices

# VM Best Practices

* Use for workloads needing control.
* Keep OS updated.

---

# Container Best Practices

* Keep images lightweight.
* Use orchestration for scale.

---

# AKS Best Practices

* Use monitoring tools.
* Deploy across multiple nodes.

---

# App Service Best Practices

* Use for modern web apps.
* Enable autoscaling.

---

# Azure Functions Best Practices

* Keep functions small.
* Use event-driven design.

---

# 24. Common AZ-900 Confusing Concepts

# VM vs Container

| VM             | Container      |
| -------------- | -------------- |
| Full OS        | Shared OS      |
| Heavy          | Lightweight    |
| Slower startup | Faster startup |

---

# VM vs App Service

| VM            | App Service        |
| ------------- | ------------------ |
| You manage OS | Azure manages OS   |
| More control  | Easier development |

---

# Containers vs AKS

Containers:
actual packaged applications.

AKS:
platform managing containers.

---

# Serverless vs PaaS

Serverless:
runs only when triggered.

PaaS:
application continuously hosted.

---

# 25. AZ-900 Exam Tips

# Microsoft Frequently Asks

## Full OS Control

→ Virtual Machines

---

## Auto-Scaling VMs

→ VMSS

---

## Portable Lightweight Apps

→ Containers

---

## Container Management at Scale

→ AKS

---

## Quick Web App Hosting

→ App Service

---

## Event-Driven Serverless Tasks

→ Azure Functions

---

# Important Exam Strategy

Read keywords carefully:

| Keyword         | Likely Answer   |
| --------------- | --------------- |
| Full control    | VM              |
| Portable        | Container       |
| Orchestration   | AKS             |
| Focus on coding | App Service     |
| Trigger-based   | Azure Functions |

---

# 26. Memory Tricks

# VM

= Full control

---

# VMSS

= Auto-scaling VMs

---

# Containers

= Lightweight portable apps

---

# AKS

= Container manager

---

# App Service

= Focus on coding

---

# Azure Functions

= Run on trigger

---

# 27. Practice Questions

# Q1

Which Azure compute service provides full OS control?

Answer:
Azure Virtual Machines

---

# Q2

Which Azure service automatically scales virtual machines?

Answer:
VM Scale Sets

---

# Q3

Which technology packages applications with dependencies?

Answer:
Containers

---

# Q4

Which Azure service manages containers at scale?

Answer:
AKS

---

# Q5

Which Azure service is best for hosting web applications quickly?

Answer:
Azure App Service

---

# Q6

Which Azure service is serverless?

Answer:
Azure Functions

---

# Q7

Containers are more lightweight than?

Answer:
Virtual Machines

---

# Q8

Which service belongs to PaaS?

Answer:
Azure App Service

---

# Q9

Which compute service is event-driven?

Answer:
Azure Functions

---

# Q10

AKS is based on which technology?

Answer:
Kubernetes

---

# 28. Final Revision Notes

| Service         | Key Idea                        |
| --------------- | ------------------------------- |
| VM              | Full OS control                 |
| VMSS            | Auto-scaling VMs                |
| Containers      | Lightweight portable apps       |
| AKS             | Container orchestration         |
| App Service     | Managed web hosting             |
| Azure Functions | Serverless event-driven compute |

---

# Most Important AZ-900 Concepts

1. VM vs App Service
2. Containers vs VMs
3. AKS purpose
4. Serverless computing
5. Compute service selection
6. PaaS vs IaaS compute

---

# Quick Revision Table

| Requirement               | Best Azure Service |
| ------------------------- | ------------------ |
| Full control              | VM                 |
| Auto-scaling VMs          | VMSS               |
| Lightweight portable apps | Containers         |
| Container orchestration   | AKS                |
| Fast web app hosting      | App Service        |
| Event-driven tasks        | Azure Functions    |

---