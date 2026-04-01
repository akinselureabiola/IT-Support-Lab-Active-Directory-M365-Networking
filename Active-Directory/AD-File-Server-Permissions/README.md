# Active Directory File Server Access Troubleshooting

## Enterprise Shared Folder Permissions Lab

In this lab, I worked through a real-world file server access issue in an Active Directory environment.

The scenario simulates a common IT support ticket where a user is unable to access a shared folder, and I investigated the issue step by step to identify the root cause and restore access.

The goal was to practice how shared folder permissions are handled using security groups and NTFS permissions, just like in a typical enterprise environment.

---

# Ticket Information

| Field | Value |
|------|------|
| Category | File Server / Access Management |
| Priority | P3 – Medium |
| Impact | User unable to access shared project files |
| SLA Target | 4 Hours |
| Resolution Time | ~45 Minutes |
| Status | Resolved |

---

# Scenario

## Incident Report

I simulated a scenario where a user reported they could not access the company Projects shared folder.

In a typical enterprise setup, shared folders are used to store project files, internal documents, and team resources, and access is usually controlled using Active Directory groups and NTFS permissions.

The goal here was to troubleshoot why the user was getting an access issue and resolve it using a structured approach.

---

# Environment

| System | Role | IP Address |
|------|------|------|
| DC01 | Domain Controller / File Server | 192.168.10.10 |
| CLIENT01 | Windows Domain Client | DHCP |

### Domain
bpurple.com

### Operating Systems
- Windows Server 2016 (Domain Controller)
- Windows 10 (Client Machine)

### Virtualization Platform
Oracle VirtualBox

### Network
Internal Network LABNET  
192.168.10.0/24

---

# Network Architecture

The diagram below illustrates the lab network topology.

- DC01 acts as both the Domain Controller and File Server  
- CLIENT01 is the domain joined workstation used to test access

![Lab Network Architecture](screenshots/lab-network-architecture.png)

---

# File Server Configuration

A shared folder was created on the Domain Controller to simulate a company file server used by employees to store and access project related files.

### Folder Path

C:\CompanyData\Projects

### Folder Structure

![Projects Folder Structure](screenshots/projects-folder.png)

---

# Share Configuration

The folder was shared on the network using the UNC path:

\\dc01\Projects

### Initial Share Permissions

Initially the share allowed **Everyone** access.

![Initial Share Permissions](screenshots/share-permissions-initial.png)

In enterprise environments this configuration is typically replaced with group based access control.

---

# Security Group Configuration

To follow enterprise access control best practices, permissions were assigned to a security group instead of individual users.

Security Group: **Project-Team**

![Project Team Security Group](screenshots/project-team-group.png)

Users requiring access to the Projects folder are added to this group.

---

# Group Membership

The user **Musa Ceesay** was assigned to the Project-Team group.

![Project Team Members](screenshots/project-team-members.png)

This allows administrators to manage access centrally without modifying folder permissions for individual users.

---

# NTFS Permission Configuration

NTFS permissions were configured on the Projects folder.

![NTFS Permissions](screenshots/ntfs-permissions.png)

| Group | Permission |
|------|------|
| SYSTEM | Full Control |
| Administrators | Full Control |
| Project-Team | Modify |
| CREATOR OWNER | Full Control |

Permission inheritance from the parent directory was disabled to ensure only authorized groups could access the folder.

---

# Simulated Incident

## Ticket Details

| Field | Value |
|------|------|
| Ticket ID | INC-1001 |
| User | musaceesay |
| Issue | Unable to access \\dc01\Projects |
| Category | File Server Access |
| Priority | Medium |

---

# Issue Reproduction

To simulate the incident, the user was removed from the Project-Team security group.

When the user attempted to access the shared folder from the client workstation:

\\dc01\Projects

Windows returned an **Access Denied error**.

![Access Denied Error](screenshots/access-denied.png)

---

# Investigation Process

To troubleshoot the issue, I followed a step-by-step approach similar to how I would handle a real support ticket.

## Step 1 — Verify Network Connectivity

I first checked if the client machine could communicate with the domain controller.

Command used:
ping dc01.bpurple.com

![Ping Test](screenshots/ping-test.png)

Result: Successful

This confirmed the issue was not related to network connectivity.

---

## Step 2 — Verify Shared Folder Access

Next, I tried accessing the shared folder directly using the UNC path:

\\dc01\Projects

Result: Access Denied

At this point, I knew the issue was likely related to permissions rather than connectivity.

---

## Step 3 — Check NTFS Permissions

I then checked the NTFS permissions on the Projects folder.

I noticed that access was controlled through the Project-Team security group rather than individual users.

---

## Step 4 — Review Group Membership

Finally, I reviewed the user's group membership in Active Directory.

I noticed the user was not part of the Project-Team group, which explains why access was denied.

This confirmed the root cause.

---

# Root Cause

The issue was caused by the user not being part of the Project-Team security group.

Since access to the folder was assigned to the group (and not directly to the user), removing the user from the group automatically removed their access.

---

# Resolution

To resolve the issue, I added the user back to the Project-Team security group.

I also verified that the share permissions were correctly configured for the group.

![Correct Share Permissions](screenshots/share-permissions-fixed.png)

---

# Verification

After adding the user back to the group, I logged into the client machine again and tested access:

\\dc01\Projects

![Acess Restored](screenshots/user-access-restored.png)

Result: Access successful

The user was able to open the shared folder without any issues.

---

# Troubleshooting Summary

| Check | Purpose |
|------|------|
| ping dc01 | Verify network connectivity |
| \\dc01\Projects | Confirm shared folder access |
| NTFS permissions | Verify authorized groups |
| AD group membership | Identify missing permissions |

---

# Business Impact

In a real environment, issues like this can prevent users from accessing important project files, which can delay work and impact productivity.

Using security groups instead of assigning permissions directly to users makes access easier to manage and reduces the risk of errors like this.

---

## 🧠 Skills Demonstrated

- Managed Active Directory users and security groups to control access to shared resources  
- Configured a Windows Server file share to simulate a company file server  
- Applied and reviewed NTFS permissions to manage folder access securely  
- Used security groups instead of individual users to simplify permission management  
- Investigated and resolved an “Access Denied” issue using a structured troubleshooting approach  
- Verified connectivity, permissions, and group membership to identify the root cause  

---

# Key Takeaway

This lab showed me how important group-based access control is in Active Directory.

Instead of assigning permissions directly to users, using security groups makes access easier to manage and troubleshoot.

It also reinforced a simple troubleshooting approach I can reuse:
1. Check connectivity  
2. Test access  
3. Review permissions  
4. Check group membership  

---

# Conclusion

In this lab, I investigated and resolved a shared folder access issue in an Active Directory environment.

The issue was caused by missing group membership, even though the share and NTFS permissions were configured correctly.

Working through this helped me better understand how file server access is managed through security groups and how to troubleshoot permission issues in a structured way.