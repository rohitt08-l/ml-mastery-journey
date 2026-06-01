# AZ-900 Module 7 — Azure Identity, Access & Security

# Table of Contents

1. Introduction to Azure Security
2. Microsoft Entra ID
3. Authentication
4. Authorization
5. Authentication vs Authorization
6. Multi-Factor Authentication (MFA)
7. Single Sign-On (SSO)
8. Conditional Access
9. Role-Based Access Control (RBAC)
10. Zero Trust Security Model
11. Defense in Depth
12. Microsoft Defender for Cloud
13. Azure Firewall
14. Network Security Groups (NSGs)
15. Azure DDoS Protection
16. Security Best Practices
17. Real-World Security Scenarios
18. Common AZ-900 Confusions
19. AZ-900 Exam Tips
20. Memory Tricks
21. Practice Questions
22. Final Revision Notes

---

# 1. Introduction to Azure Security

Security is one of the most important pillars of cloud computing.

Organizations moving to Azure must secure:

- Users
- Applications
- Data
- Networks
- Infrastructure

Azure provides built-in services and tools to help organizations:

- Prevent attacks
- Detect threats
- Control access
- Monitor resources
- Meet compliance requirements

---

# Why Security Matters

Without proper security:

- Data breaches can occur
- Customer information may be stolen
- Systems may become unavailable
- Financial losses may occur
- Compliance violations may happen

Examples:

- Unauthorized access to databases
- Ransomware attacks
- Credential theft
- DDoS attacks

---

# Shared Responsibility Reminder

Remember the Shared Responsibility Model.

## Microsoft Secures

- Physical datacenters
- Hardware
- Network infrastructure
- Host operating systems

## Customer Secures

- User accounts
- Data
- Applications
- Permissions
- Operating systems in IaaS

---

# 2. Microsoft Entra ID

## Definition

Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's cloud-based Identity and Access Management (IAM) service.

It helps organizations:

- Manage identities
- Authenticate users
- Authorize access
- Enable Single Sign-On
- Apply security policies

---

# Key Components

## Users

People who access resources.

Examples:

- Employees
- Students
- Administrators

---

## Groups

Collection of users.

Benefits:

- Easier permission management
- Simplified administration

---

## Applications

Applications integrated with Entra ID.

Examples:

- Microsoft 365
- Azure Portal
- Teams
- Third-party applications

---

## Devices

Laptops, desktops, tablets, and mobile devices.

---

# Benefits of Entra ID

## Centralized Identity Management

Manage users from one location.

## Improved Security

Supports MFA and Conditional Access.

## Single Sign-On

One login for multiple applications.

## Scalability

Supports millions of users.

---

# Real-World Example

An employee logs into:

- Azure Portal
- Microsoft Teams
- Outlook
- Microsoft 365

using a single account.

This is managed by:

# Microsoft Entra ID

---

# AZ-900 Important Point

Entra ID is:

# Identity and Access Management Service

NOT a database service.

---

# 3. Authentication

## Definition

Authentication answers:

# "Who are you?"

It verifies the identity of a user, application, or device.

---

# Authentication Examples

- Username and Password
- Fingerprint
- Face Recognition
- Security Token
- One-Time Password (OTP)

---

# Authentication Factors

## Something You Know

- Password
- PIN

---

## Something You Have

- Mobile Phone
- Security Token

---

## Something You Are

- Fingerprint
- Face Scan

---

# Real-World Example

User enters:

- Username
- Password

Azure verifies credentials.

This process is:

# Authentication

---

# Important AZ-900 Point

Authentication happens BEFORE authorization.

---

# 4. Authorization

## Definition

Authorization answers:

# "What are you allowed to do?"

Authorization determines permissions after identity is verified.

---

# Examples

User may be allowed to:

- View resources
- Create virtual machines
- Delete storage accounts
- Manage subscriptions

---

# Real-World Example

Two users successfully log in.

User A:
- Can create VMs

User B:
- Can only view resources

Difference?

# Authorization

---

# Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Who are you? | What can you do? |
| Identity verification | Permission verification |
| Happens first | Happens second |

---

# Easy Memory Trick

Authentication = Identity

Authorization = Permissions

---

# 5. Multi-Factor Authentication (MFA)

## Definition

Multi-Factor Authentication requires two or more verification methods.

---

# Why MFA Exists

Passwords can be:

- Stolen
- Guessed
- Leaked

MFA significantly improves security.

---

# Example

User enters:

1. Password
2. Mobile OTP

Both must be verified.

---

# Benefits

## Stronger Security

Reduces unauthorized access.

## Identity Protection

Protects user accounts.

## Reduced Risk

Protects against password attacks.

---

# AZ-900 Exam Tip

If the question asks:

"How can login security be improved?"

The answer is often:

# MFA

---

# 6. Single Sign-On (SSO)

## Definition

Single Sign-On allows users to log in once and access multiple applications.

---

# Example

User logs in once and accesses:

- Azure Portal
- Teams
- Outlook
- Microsoft 365

without re-entering credentials.

---

# Benefits

## Better User Experience

Less password fatigue.

## Increased Productivity

Fewer login prompts.

## Simplified Management

Centralized authentication.

---

# AZ-900 Memory Trick

SSO =

One Login → Many Applications

---

# 7. Conditional Access

## Definition

Conditional Access applies security policies based on specific conditions.

---

# Examples

## Require MFA Outside Office

Employees working remotely must verify identity.

## Restrict Country Access

Allow access only from approved countries.

## Block Unknown Devices

Prevent risky device access.

## Block High-Risk Sign-ins

Protect against suspicious activity.

---

# Benefits

## Adaptive Security

Access rules change based on conditions.

## Risk Reduction

Protects sensitive resources.

## Compliance

Supports security policies.

---

# Real-World Example

Employee logs in from office:

Access granted.

Employee logs in from another country:

MFA required.

Conditional Access handles this automatically.

---

# 8. Role-Based Access Control (RBAC)

## Definition

RBAC controls access to Azure resources using roles.

---

# Why RBAC Exists

Not everyone should have full access.

Different users need different permissions.

---

# Common Roles

## Owner

Full access.

Can:

- Create resources
- Delete resources
- Assign permissions

---

## Contributor

Can manage resources.

Cannot assign permissions.

---

## Reader

Can view resources only.

Cannot make changes.

---

# Benefits

## Least Privilege Access

Users receive minimum permissions.

## Better Governance

Improves security control.

## Easier Administration

Role assignment simplifies management.

---

# Real-World Example

Administrator:
Owner

Developer:
Contributor

Manager:
Reader

---

# AZ-900 Important Point

RBAC is:

# Authorization Mechanism

---

# 9. Zero Trust Security Model

## Definition

Zero Trust follows:

# Never Trust, Always Verify

---

# Why Zero Trust Exists

Attackers may already be inside the network.

Therefore:

No user or device is automatically trusted.

---

# Core Principles

## Verify Explicitly

Authenticate every request.

---

## Use Least Privilege Access

Provide minimum permissions required.

---

## Assume Breach

Act as if attackers already exist.

---

# Real-World Example

Employee inside corporate network must still:

- Authenticate
- Pass MFA
- Meet access policies

---

# AZ-900 Memory Trick

Zero Trust =

Trust Nobody
Verify Everybody

---

# 10. Defense in Depth

## Definition

Defense in Depth uses multiple layers of security.

If one layer fails, others continue protection.

---

# Security Layers

## Physical Security

Datacenters and facilities.

---

## Identity Layer

Entra ID and MFA.

---

## Perimeter Layer

Firewalls.

---

## Network Layer

NSGs and network controls.

---

## Compute Layer

Virtual Machine security.

---

## Application Layer

Secure coding and application controls.

---

## Data Layer

Encryption and backups.

---

# Benefits

- Better protection
- Reduced attack success
- Improved resilience

---

# 11. Microsoft Defender for Cloud

## Definition

Microsoft Defender for Cloud is a Cloud Security Posture Management and Threat Protection service.

---

# Features

## Security Recommendations

Suggests improvements.

## Threat Detection

Identifies attacks.

## Compliance Monitoring

Checks compliance standards.

## Security Score

Measures security posture.

---

# Benefits

- Continuous monitoring
- Risk identification
- Compliance visibility

---

# Real-World Example

Defender identifies:

- Open ports
- Weak configurations
- Missing security updates

---

# 12. Azure Firewall

## Definition

Azure Firewall is a managed network security service.

---

# Purpose

Controls:

- Incoming traffic
- Outgoing traffic

---

# Features

## Centralized Security

Single security point.

## Traffic Filtering

Allow or deny traffic.

## Threat Intelligence

Blocks known malicious traffic.

---

# Real-World Example

Allow:

- HTTP
- HTTPS

Block:

- Unauthorized traffic

---

# 13. Network Security Groups (NSGs)

## Definition

NSGs filter network traffic to Azure resources.

---

# NSG Rules

Can:

- Allow traffic
- Deny traffic

Based on:

- IP address
- Port
- Protocol

---

# Example

Allow:

Port 80 (HTTP)

Block:

Port 22 (SSH)

---

# Benefits

- Improved security
- Traffic control
- Resource protection

---

# Firewall vs NSG

| Azure Firewall | NSG |
|---|---|
| Centralized protection | Resource-level filtering |
| Advanced inspection | Basic allow/deny rules |
| Organization-wide | VM/Subnet level |

---

# AZ-900 Tip

NSG = Network Traffic Filtering

---

# 14. Azure DDoS Protection

## Definition

Protects against:

# Distributed Denial of Service (DDoS) Attacks

---

# What is DDoS?

Attackers flood systems with massive traffic.

Goal:

Make applications unavailable.

---

# Azure DDoS Protection Benefits

## Automatic Detection

Identifies attacks.

## Automatic Mitigation

Reduces attack impact.

## Availability Protection

Keeps services online.

---

# Real-World Example

Online shopping website receives attack traffic.

Azure DDoS Protection absorbs and mitigates attack traffic.

---

# 15. Security Best Practices

- Enable MFA
- Use RBAC
- Apply Conditional Access
- Follow Least Privilege Principle
- Monitor with Defender for Cloud
- Enable DDoS Protection
- Review permissions regularly

---

# 16. Real-World Security Scenarios

## Secure Employee Login

Solution:
MFA

---

## Different User Permissions

Solution:
RBAC

---

## Monitor Security Risks

Solution:
Defender for Cloud

---

## Filter Network Traffic

Solution:
NSGs

---

## Protect Internet Traffic

Solution:
Azure Firewall

---

## Protect Against DDoS Attacks

Solution:
Azure DDoS Protection

---

# 17. Common AZ-900 Confusions

## Authentication vs Authorization

Authentication:
Who are you?

Authorization:
What can you do?

---

## RBAC vs Conditional Access

RBAC:
Permissions

Conditional Access:
Access Conditions

---

## Firewall vs NSG

Firewall:
Advanced centralized protection

NSG:
Basic network filtering

---

# 18. AZ-900 Exam Tips

Microsoft frequently asks:

- Authentication vs Authorization
- MFA
- RBAC
- Conditional Access
- Zero Trust
- Entra ID
- Defender for Cloud
- Firewall
- NSGs
- DDoS Protection

---

# 19. Memory Tricks

Authentication = Identity

Authorization = Permission

MFA = Multiple Checks

SSO = One Login

RBAC = Role Permissions

NSG = Network Filter

Firewall = Traffic Guard

DDoS = Attack Protection

Zero Trust = Never Trust

---

# 20. Practice Questions

### Q1
What service manages identities in Azure?

Answer:
Microsoft Entra ID

### Q2
What verifies user identity?

Answer:
Authentication

### Q3
What determines permissions?

Answer:
Authorization

### Q4
What provides role-based permissions?

Answer:
RBAC

### Q5
What filters network traffic?

Answer:
NSGs

### Q6
What protects against DDoS attacks?

Answer:
Azure DDoS Protection

### Q7
What security model says "Never trust, always verify"?

Answer:
Zero Trust

---

# 21. Final Revision Notes

| Concept | Key Idea |
|----------|----------|
| Entra ID | Identity Management |
| Authentication | Verify Identity |
| Authorization | Verify Permissions |
| MFA | Multiple Verification Methods |
| SSO | One Login |
| Conditional Access | Policy-Based Access |
| RBAC | Role-Based Permissions |
| Zero Trust | Never Trust, Always Verify |
| Defender for Cloud | Security Management |
| Azure Firewall | Network Protection |
| NSGs | Traffic Filtering |
| DDoS Protection | Attack Mitigation |

---

# Most Important AZ-900 Security Topics

1. Authentication vs Authorization
2. MFA
3. SSO
4. Conditional Access
5. RBAC
6. Zero Trust
7. Defense in Depth
8. Defender for Cloud
9. Firewall vs NSG
10. DDoS Protection