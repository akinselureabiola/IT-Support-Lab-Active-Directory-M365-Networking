# Security Group Access (Shared Folder Permission Issue)

## Ticket Information

- **Category:** Active Directory / File Server / Access Control  
- **Priority:** P3 – Medium  
- **Impact:** Single user unable to access shared company folder  
- **SLA Target:** 4 hours  
- **Resolution Time:** 50 minutes  
- **Status:** Resolved  

---

## Scenario

In this lab, I simulated a support ticket where a user reported they could not access a shared company folder.

When the user tried to open the folder, they received an **Access Denied** error, while other users were able to access it without any issues.

This is a common access control issue in Active Directory environments, usually related to permissions or group membership.

---

## Environment

- **Domain:** bpurple.com  
- **Domain Controller:** DC01 (192.168.10.10)  
- **Client Machine:** CLIENT01 (Domain-joined)  
- **Shared Folder Path:** \\DC01\Finance-Share  
- **Security Group:** Finance-Access  
- **Virtualization:** VirtualBox (Internal Network + NAT)  
- **DNS Server:** 192.168.10.10  

---

## Network Architecture Diagram

![Active Directory Lab Network Architecture](ad-lab-network-architecture.png)

---

**Configuration Notes:**

- Adapter 1 → Internal Network (intnet)  
- Adapter 2 → NAT (Internet access)  
- DNS Server → 192.168.10.10  
- Domain → bpurple.com  

---

## Initial Symptoms

On CLIENT01, I tried accessing the shared folder:

\\DC01\Finance-Share  

Result: Access Denied  

![Access Denied Error](File-access-denied.png) 

To rule out network or DNS issues, I tested connectivity:

ping 192.168.10.10  
ping dc01.bpurple.com  

Both tests were successful, confirming the issue was not related to connectivity.

![Successful Connectivity Test](Successful-network-connectivity.png)

---

## Business Impact

From a support perspective, issues like this can slow down a user’s ability to work, especially if the folder contains important department files.

In this case, the user was unable to access the finance shared folder, which could delay tasks and require additional support time to resolve.

Even though the issue affected only one user, it still impacted productivity and needed to be resolved within SLA.

---

## Investigation Steps

I followed a step-by-step approach to isolate the issue, starting from basic checks and moving toward access control validation.

### Step 1 — Validate Network Connectivity

I executed:

    ping 192.168.10.10

Result: Successful  

![Successful Connectivity Test](Successful-network-connectivity.png)

Confirmed network communication with Domain Controller.

---

### Step 2 — Validate Share Availability

Accessed shared folder from another user account.

Result: Successful  

I confirmed that the shared folder and server were operational.

![Access Working for Other User](File-Access-granted.png)

---

### Step 3 — Review Share and NTFS Permissions

On DC01:

Opened:

    C:\Finance → Properties → Sharing → Advanced Sharing
    Security Tab → NTFS Permissions

Verified:

- Share permissions assigned to: Finance-Access (Modify)
- NTFS permissions assigned to: Finance-Access (Modify)
- No direct user permissions configured

Everything looked correct at the permission level, so I moved on to check group membership.

---

### Step 4 — Verify Group Membership

Opened:

    Active Directory Users and Computers

Navigated to:

    Finance-Access Security Group

Checked membership.

![User Not in Security Group](No-Group-Access.png)

I noticed that the user was not listed as a member of the Finance-Access group.

At this point, the root cause became clear.

---

## Root Cause

The issue occurred because the user was not part of the Finance-Access security group, which controls access to the shared folder.

Even though the permissions were correctly configured, the user could not access the folder because they were missing the required group membership.

---

## Resolution

To fix the issue, I added the user to the Finance-Access security group in Active Directory.

After making the change, I asked the user to log off and log back in so their access token could refresh.

![User Added to Security Group](Group-Access-granted.png)

---

## Verification

After the user logged back in, I tested access again:

\\DC01\Finance-Share  

![Access Restored](File-Access-granted.png)

The folder opened successfully without any errors.

This confirmed that the issue was resolved and access was restored.

---

## Skills Demonstrated

- Managed Active Directory users and security groups to control access to shared folders  
- Compared and verified Share and NTFS permissions to understand access behavior  
- Used security group-based access control instead of assigning permissions directly to users  
- Investigated and resolved an “Access Denied” issue using a structured troubleshooting approach  
- Verified network connectivity, permissions, and group membership to identify the root cause  
- Applied understanding of authentication and group membership updates during troubleshooting  

---

## Key Takeaway

This lab reinforced how important security groups are in managing access within an Active Directory environment.

It also showed me that when troubleshooting access issues, it’s important to follow a structured approach — starting from connectivity checks and moving toward permissions and group membership.

In many cases, the issue is not the permissions themselves, but whether the user is actually part of the group that grants access.
