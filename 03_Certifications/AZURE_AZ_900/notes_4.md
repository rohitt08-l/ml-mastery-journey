# AZ-900 Module 4 — Azure Networking Services

# Table of Contents

1. Introduction to Azure Networking
2. What is Networking?
3. Importance of Networking in Cloud Computing
4. Azure Networking Overview
5. Azure Virtual Network (VNet)
6. VNet Architecture
7. VNet Features and Benefits
8. Subnets
9. Subnet Architecture
10. Public IP Addresses
11. Private IP Addresses
12. Public IP vs Private IP
13. DNS (Domain Name System)
14. Azure DNS
15. VPN Gateway
16. VPN Architecture
17. VPN Gateway Benefits and Use Cases
18. ExpressRoute
19. ExpressRoute Architecture
20. ExpressRoute Benefits and Use Cases
21. VPN Gateway vs ExpressRoute
22. Azure Load Balancer
23. Load Balancer Architecture
24. Load Balancer Benefits
25. Azure Application Gateway
26. Application Gateway Features
27. Load Balancer vs Application Gateway
28. Azure CDN (Content Delivery Network)
29. CDN Architecture
30. CDN Benefits and Use Cases
31. Network Security Groups (NSGs)
32. NSG Rules and Traffic Filtering
33. Real-World Networking Scenarios
34. Best Practices
35. Common AZ-900 Confusing Concepts
36. AZ-900 Exam Tips
37. Memory Tricks
38. Practice Questions
39. Final Revision Notes

---

# 1. Introduction to Azure Networking

Networking is one of the most important foundations of cloud computing.

Without networking:

* virtual machines cannot communicate
* applications cannot access databases
* users cannot access websites
* cloud resources cannot interact

Azure Networking Services help organizations:

* connect resources
* secure communication
* provide internet access
* connect on-premises networks to Azure
* distribute traffic efficiently

---

# Why Azure Networking is Important

Networking enables:

* communication between services
* internet connectivity
* secure cloud environments
* hybrid cloud architecture
* traffic routing
* scalability
* high availability

---

# Real-World Examples

Azure networking supports:

* banking systems
* AI platforms
* hospital management systems
* e-commerce websites
* cloud APIs
* enterprise ERP systems

---

# 2. What is Networking?

# Definition

Networking means:

> Connecting computers and devices so they can communicate and exchange data.

---

# Networking Components

Networking includes:

* IP addresses
* routers
* switches
* DNS
* firewalls
* communication protocols

---

# Real-World Analogy

Networking is like a road system.

* Roads = network paths
* Vehicles = data packets
* Traffic rules = security policies

---

# 3. Importance of Networking in Cloud Computing

Cloud networking enables:

## Resource Communication

VMs and databases communicate.

## Internet Connectivity

Users access applications online.

## Hybrid Cloud Connectivity

Connect local datacenters to cloud.

## Security

Protect data and resources.

## Scalability

Support large-scale applications.

---

# 4. Azure Networking Overview

Azure provides networking services for:

* connectivity
* security
* traffic management
* global content delivery

---

# Core Azure Networking Services

| Service             | Purpose                      |
| ------------------- | ---------------------------- |
| VNet                | Private network              |
| Subnet              | Smaller network inside VNet  |
| Public IP           | Internet communication       |
| Private IP          | Internal communication       |
| DNS                 | Name resolution              |
| VPN Gateway         | Secure internet connection   |
| ExpressRoute        | Private dedicated connection |
| Load Balancer       | Traffic distribution         |
| Application Gateway | Web traffic management       |
| CDN                 | Faster content delivery      |
| NSG                 | Traffic filtering            |

---

# 5. Azure Virtual Network (VNet)

# Definition

Azure Virtual Network (VNet) is:

> A private network inside Azure.

It allows Azure resources to communicate securely.

---

# Why VNets Exist

Organizations need:

* secure communication
* isolated environments
* hybrid cloud networking
* traffic control

---

# Real-World Analogy

VNet is like:

# Private office network in the cloud

Resources inside the office communicate securely.

---

# Resources Inside VNet

* Virtual Machines
* Databases
* Containers
* App Services
* AI Services

---

# VNet Features

## Isolation

Resources isolated from public internet.

## Secure Communication

Private communication between resources.

## Internet Connectivity

Can connect to internet if required.

## Hybrid Connectivity

Can connect on-premises systems.

---

# Example

```text
VNet-Production

 ├── Web Server
 ├── Database Server
 └── AI API Server
```

---

# VNet Benefits

## Better Security

## Easier Network Management

## Hybrid Cloud Support

## Traffic Isolation

---

# Important AZ-900 Point

VNet =

# Private Azure Network

---

# 6. VNet Architecture

```text
Azure Region
    ↓
Virtual Network (VNet)
    ↓
Subnets
    ↓
Resources
```

---

# Example Architecture

```text
VNet-Production

 ├── WebSubnet
 │      └── Web VM
 │
 ├── DatabaseSubnet
 │      └── SQL VM
 │
 └── AISubnet
        └── AI Service
```

---

# 7. VNet Features and Benefits

| Feature        | Benefit                  |
| -------------- | ------------------------ |
| Isolation      | Better security          |
| Private IPs    | Internal communication   |
| Subnets        | Better organization      |
| Connectivity   | Resource communication   |
| Hybrid Support | Connect local datacenter |

---

# 8. Subnets

# Definition

A subnet is:

> A smaller network inside a VNet.

---

# Why Subnets Exist

Subnets help:

* organize networks
* improve security
* isolate workloads
* manage traffic

---

# Real-World Analogy

Suppose a college building contains departments.

Entire building = VNet

Departments = Subnets

---

# Example

```text
VNet-Production

 ├── WebSubnet
 ├── DatabaseSubnet
 └── AISubnet
```

---

# Benefits of Subnets

## Better Organization

## Improved Security

## Traffic Isolation

## Easier Management

---

# Important AZ-900 Point

Subnet exists:

# INSIDE a VNet

---

# 9. Subnet Architecture

```text
Virtual Network

 ├── Subnet A
 │      └── VM
 │
 ├── Subnet B
 │      └── Database
 │
 └── Subnet C
        └── AI Services
```

---

# 10. Public IP Addresses

# Definition

A Public IP address is:

> An IP address accessible from the internet.

---

# Use Cases

* websites
* public APIs
* internet-facing applications

---

# Real-World Example

Google website uses public IP.

---

# Public IP Characteristics

## Internet Accessible

## External Communication

## Globally Reachable

---

# 11. Private IP Addresses

# Definition

A Private IP address is:

> An IP address used for internal communication only.

Not directly accessible from internet.

---

# Use Cases

* databases
* backend servers
* internal APIs

---

# Real-World Example

Application server communicates privately with database server.

---

# Private IP Characteristics

## Internal Communication

## More Secure

## Not Internet Accessible

---

# 12. Public IP vs Private IP

| Public IP              | Private IP             |
| ---------------------- | ---------------------- |
| Internet accessible    | Internal only          |
| External communication | Internal communication |
| Used by websites       | Used by databases      |
| Less secure            | More secure            |

---

# Important AZ-900 Point

Databases usually use:

# Private IPs

Websites often use:

# Public IPs

---

# 13. DNS (Domain Name System)

# Definition

DNS converts:

> Human-readable names into IP addresses.

---

# Example

Instead of:

```text
142.250.183.14
```

Users type:

```text
google.com
```

DNS translates name into IP.

---

# Why DNS Exists

Humans remember names easier than IP addresses.

---

# DNS Workflow

```text
User types website name
        ↓
DNS lookup occurs
        ↓
IP address returned
        ↓
Browser connects to server
```

---

# DNS Benefits

## Easier Website Access

## Simplified Networking

## Flexible Domain Management

---

# Important AZ-900 Point

DNS =

# Name-to-IP translation

---

# 14. Azure DNS

Azure DNS is:

> Azure service for hosting DNS domains.

---

# Azure DNS Benefits

## High Availability

## Scalability

## Azure Integration

## Security

---

# 15. VPN Gateway

# Definition

VPN Gateway:

> Connects on-premises networks to Azure securely over internet.

---

# VPN Meaning

VPN =

# Virtual Private Network

Creates encrypted communication tunnel.

---

# Why VPN Gateway Exists

Organizations need:

* secure cloud connectivity
* hybrid cloud communication

without dedicated private connection.

---

# VPN Architecture

```text
On-Premises Network
        ↓
Encrypted Internet Tunnel
        ↓
Azure VPN Gateway
        ↓
Azure VNet
```

---

# VPN Gateway Benefits

## Secure Communication

## Lower Cost

Compared to dedicated links.

## Hybrid Cloud Connectivity

## Encryption

---

# VPN Gateway Use Cases

* remote office connectivity
* hybrid cloud
* secure communication

---

# Important AZ-900 Point

VPN Gateway:

# Uses public internet

but communication is encrypted.

---

# 16. VPN Architecture

```text
Office Network
        ↓
Internet
        ↓
VPN Tunnel
        ↓
Azure VPN Gateway
        ↓
Azure Resources
```

---

# 17. VPN Gateway Benefits and Use Cases

| Benefit        | Description                        |
| -------------- | ---------------------------------- |
| Encryption     | Secure communication               |
| Cost Effective | Lower cost than private connection |
| Hybrid Support | Connect local systems to Azure     |
| Flexibility    | Works over internet                |

---

# 18. ExpressRoute

# Definition

ExpressRoute:

> Private dedicated connection between on-premises network and Azure.

---

# Why ExpressRoute Exists

Large enterprises need:

* lower latency
* higher security
* stable connectivity
* predictable performance

---

# ExpressRoute Characteristics

## Does NOT Use Public Internet

## Dedicated Private Connection

## High Reliability

## Low Latency

---

# Real-World Example

Bank connects private datacenter to Azure.

Uses:

# ExpressRoute

---

# 19. ExpressRoute Architecture

```text
On-Premises Datacenter
        ↓
Private Dedicated Connection
        ↓
ExpressRoute
        ↓
Azure Network
```

---

# 20. ExpressRoute Benefits and Use Cases

| Benefit         | Description            |
| --------------- | ---------------------- |
| Higher Security | No public internet     |
| Lower Latency   | Faster communication   |
| Reliability     | Stable connection      |
| Predictability  | Consistent performance |

---

# ExpressRoute Use Cases

* banking systems
* healthcare systems
* enterprise networking
* large hybrid cloud environments

---

# Important AZ-900 Point

ExpressRoute:

# Does NOT use public internet

Very important exam concept.

---

# 21. VPN Gateway vs ExpressRoute

| VPN Gateway       | ExpressRoute              |
| ----------------- | ------------------------- |
| Uses internet     | Private connection        |
| Lower cost        | Higher cost               |
| Encrypted traffic | Dedicated traffic         |
| More latency      | Lower latency             |
| Easier setup      | Enterprise-grade solution |

---

# 22. Azure Load Balancer

# Definition

Load Balancer:

> Distributes incoming traffic across multiple servers.

---

# Why Load Balancer Exists

Without load balancing:

* servers overload
* applications slow down
* downtime increases

---

# Load Balancer Architecture

```text
Users
   ↓
Load Balancer
   ↓
VM1   VM2   VM3
```

---

# Load Balancer Benefits

## High Availability

## Better Performance

## Scalability

## Fault Tolerance

---

# Load Balancer Use Cases

* web applications
* APIs
* scalable enterprise apps

---

# Important AZ-900 Point

Load Balancer =

# Traffic distribution service

---

# 23. Load Balancer Architecture

```text
Internet Traffic
        ↓
Load Balancer
        ↓
Server Pool

 VM1
 VM2
 VM3
```

---

# 24. Load Balancer Benefits

| Benefit      | Description          |
| ------------ | -------------------- |
| Availability | Multiple servers     |
| Scalability  | Handle large traffic |
| Reliability  | Reduce failures      |
| Performance  | Balanced workload    |

---

# 25. Azure Application Gateway

# Definition

Application Gateway:

> Web traffic load balancer operating at application layer.

---

# Why Application Gateway Exists

Web applications need:

* advanced routing
* SSL termination
* web application firewall

---

# Application Gateway Features

## HTTP/HTTPS Routing

## SSL Termination

## Web Application Firewall (WAF)

## URL-Based Routing

---

# Real-World Example

Large e-commerce website requiring:

* secure web traffic
* advanced routing

Uses:

# Application Gateway

---

# Important AZ-900 Point

Application Gateway =

# Web-specific load balancer

---

# 26. Application Gateway Features

| Feature         | Purpose                   |
| --------------- | ------------------------- |
| SSL Termination | Manage HTTPS              |
| WAF             | Web security              |
| URL Routing     | Smart traffic routing     |
| Layer 7 Routing | Web-level traffic control |

---

# 27. Load Balancer vs Application Gateway

| Load Balancer   | Application Gateway |
| --------------- | ------------------- |
| General traffic | Web traffic         |
| Layer 4         | Layer 7             |
| Basic balancing | Advanced routing    |
| Faster          | Web-aware           |

---

# Important AZ-900 Point

Application Gateway:

# Designed for web applications

---

# 28. Azure CDN (Content Delivery Network)

# Definition

CDN:

> Distributed network of servers delivering content closer to users.

---

# Why CDN Exists

Without CDN:

* distant users experience slow loading

CDN improves:

* speed
* performance
* user experience

---

# CDN Content Examples

* images
* videos
* CSS
* JavaScript
* static files

---

# Real-World Example

User in India accesses US website.

CDN delivers cached content from nearby server.

---

# 29. CDN Architecture

```text
Original Server
        ↓
CDN Edge Locations
        ↓
Users Worldwide
```

---

# 30. CDN Benefits and Use Cases

| Benefit             | Description        |
| ------------------- | ------------------ |
| Faster Delivery     | Lower latency      |
| Better Performance  | Faster loading     |
| Reduced Server Load | Cached content     |
| Global Reach        | Worldwide delivery |

---

# CDN Use Cases

* streaming platforms
* websites
* gaming platforms
* media applications

---

# Important AZ-900 Point

CDN =

# Faster global content delivery

---

# 31. Network Security Groups (NSGs)

# Definition

NSG:

> Security rules controlling network traffic.

---

# Why NSGs Exist

Organizations need to:

* allow approved traffic
* block unauthorized traffic
* secure Azure resources

---

# NSG Works Like

# Firewall for Azure resources

---

# Example Rules

Allow:

* HTTP (80)
* HTTPS (443)

Block:

* unauthorized ports

---

# NSG Features

## Inbound Rules

Control incoming traffic.

## Outbound Rules

Control outgoing traffic.

## Traffic Filtering

Allow or deny traffic.

---

# Real-World Example

Database subnet blocks public access using NSG.

---

# Important AZ-900 Point

NSG =

# Network traffic filtering

---

# 32. NSG Rules and Traffic Filtering

```text
Incoming Traffic
        ↓
NSG Rules
        ↓
Allow or Deny
        ↓
Azure Resource
```

---

# 33. Real-World Networking Scenarios

# Scenario 1 — Private Enterprise Network

Need:

* secure communication between VMs

Solution:
VNet + Subnets

---

# Scenario 2 — Public Website

Need:

* internet accessibility

Solution:
Public IP

---

# Scenario 3 — Secure Database

Need:

* internal-only communication

Solution:
Private IP + NSG

---

# Scenario 4 — Hybrid Cloud Connectivity

Need:

* secure connection to Azure

Solution:
VPN Gateway

---

# Scenario 5 — Enterprise Private Connection

Need:

* low latency and private communication

Solution:
ExpressRoute

---

# Scenario 6 — Scalable Web Application

Need:

* traffic distribution

Solution:
Load Balancer

---

# Scenario 7 — Advanced Web Traffic Routing

Need:

* WAF + SSL routing

Solution:
Application Gateway

---

# Scenario 8 — Faster Global Website Access

Need:

* lower latency worldwide

Solution:
CDN

---

# 34. Best Practices

# VNet Best Practices

* Use separate VNets for environments.
* Design proper subnet structure.

---

# Security Best Practices

* Use NSGs.
* Minimize public IP exposure.

---

# Connectivity Best Practices

* Use VPN Gateway for small hybrid environments.
* Use ExpressRoute for enterprises.

---

# Performance Best Practices

* Use CDN for global applications.
* Use Load Balancer for scalable systems.

---

# 35. Common AZ-900 Confusing Concepts

# VPN Gateway vs ExpressRoute

| VPN Gateway      | ExpressRoute         |
| ---------------- | -------------------- |
| Uses internet    | Private connection   |
| Lower cost       | Higher cost          |
| Encrypted tunnel | Dedicated connection |

---

# Load Balancer vs Application Gateway

| Load Balancer   | Application Gateway |
| --------------- | ------------------- |
| General traffic | Web traffic         |
| Layer 4         | Layer 7             |
| Basic balancing | Advanced routing    |

---

# Public IP vs Private IP

| Public IP       | Private IP    |
| --------------- | ------------- |
| Internet-facing | Internal only |
| Websites        | Databases     |

---

# VNet vs Subnet

| VNet                   | Subnet          |
| ---------------------- | --------------- |
| Entire private network | Smaller network |
| Larger scope           | Smaller scope   |

---

# 36. AZ-900 Exam Tips

# Microsoft Frequently Asks

## Private Azure Network

→ VNet

---

## Smaller Network Inside VNet

→ Subnet

---

## Secure Internet Connection to Azure

→ VPN Gateway

---

## Private Dedicated Connection

→ ExpressRoute

---

## Traffic Distribution

→ Load Balancer

---

## Web Traffic Routing

→ Application Gateway

---

## Faster Global Content Delivery

→ CDN

---

## Network Traffic Filtering

→ NSG

---

# Important Exam Strategy

Read keywords carefully:

| Keyword                   | Likely Answer       |
| ------------------------- | ------------------- |
| Private network           | VNet                |
| Internet accessible       | Public IP           |
| Internal communication    | Private IP          |
| Encrypted internet tunnel | VPN Gateway         |
| Dedicated connection      | ExpressRoute        |
| Web routing               | Application Gateway |
| Global content delivery   | CDN                 |
| Firewall rules            | NSG                 |

---

# 37. Memory Tricks

# VNet

= Private Azure network

---

# Subnet

= Smaller network inside VNet

---

# VPN Gateway

= Secure internet tunnel

---

# ExpressRoute

= Private Azure highway

---

# Load Balancer

= Traffic distributor

---

# Application Gateway

= Web traffic manager

---

# CDN

= Faster global delivery

---

# NSG

= Azure firewall rules

---

# 38. Practice Questions

# Q1

Which Azure service creates private network in Azure?

Answer:
VNet

---

# Q2

Which networking component exists inside VNet?

Answer:
Subnet

---

# Q3

Which IP type is internet accessible?

Answer:
Public IP

---

# Q4

Which Azure service translates names into IP addresses?

Answer:
DNS

---

# Q5

Which service securely connects on-premises network to Azure over internet?

Answer:
VPN Gateway

---

# Q6

Which service provides private dedicated Azure connection?

Answer:
ExpressRoute

---

# Q7

Which service distributes traffic across servers?

Answer:
Load Balancer

---

# Q8

Which service is designed specifically for web traffic routing?

Answer:
Application Gateway

---

# Q9

Which service improves global website performance?

Answer:
CDN

---

# Q10

Which service filters network traffic?

Answer:
NSG

---

# 39. Final Revision Notes

| Service             | Key Idea                     |
| ------------------- | ---------------------------- |
| VNet                | Private network              |
| Subnet              | Smaller network              |
| Public IP           | Internet communication       |
| Private IP          | Internal communication       |
| DNS                 | Name resolution              |
| VPN Gateway         | Secure internet connection   |
| ExpressRoute        | Private dedicated connection |
| Load Balancer       | Traffic distribution         |
| Application Gateway | Web traffic routing          |
| CDN                 | Faster content delivery      |
| NSG                 | Traffic filtering            |

---

# Most Important AZ-900 Networking Concepts

1. VNet and Subnets
2. Public vs Private IP
3. VPN Gateway vs ExpressRoute
4. Load Balancer vs Application Gateway
5. CDN functionality
6. NSG purpose

---

# Quick Revision Table

| Requirement                     | Best Azure Service  |
| ------------------------------- | ------------------- |
| Private network                 | VNet                |
| Internal segmentation           | Subnet              |
| Secure internet tunnel          | VPN Gateway         |
| Private dedicated connection    | ExpressRoute        |
| Traffic balancing               | Load Balancer       |
| Web application routing         | Application Gateway |
| Global performance optimization | CDN                 |
| Network filtering               | NSG                 |

----------
