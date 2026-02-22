Below is a **fully cleaned, properly formatted Markdown file** ready for direct paste into:

```
Active-Directory/Day-28-Domain-Trust-Issue.md
```

No broken backticks. No formatting conflicts. Clean GitHub rendering.

---

```markdown
# Day 28 — Domain Trust Relationship Failure

## Ticket Information

- **Category:** Active Directory / Authentication  
- **Priority:** P1 – Critical  
- **Impact:** User unable to log into domain workstation  
- **SLA Target:** 2 hours  
- **Resolution Time:** 1 hour 20 minutes  
- **Status:** Resolved  

---

## Scenario

**User Reported:**

> “This computer cannot connect to the domain.”

When attempting to log in using domain credentials, the following error was displayed:

    The trust relationship between this workstation and the primary domain failed.

The user was unable to authenticate using their domain account.

---

## Environment

- **Domain:** bpurple.com  
- **Domain Controller:** DC01 (192.168.10.10)  
- **Client Machine:** CLIENT01 (Domain-joined)  
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

On CLIENT01:

- Domain login failed  
- Local administrator login successful  
- Network connectivity to Domain Controller confirmed  

Connectivity validation:

    ping 192.168.10.10
    ping dc01.bpurple.com
    nslookup dc01.bpurple.com

Result: Successful  

This confirmed DNS and network communication were functioning properly.

---

## Business Impact

Without domain trust:

- User cannot authenticate to the domain  
- Group Policy Objects (GPOs) will not apply  
- Shared drives become inaccessible  
- Domain-dependent applications may fail  

This is considered a critical authentication issue in enterprise environments.

---

## Investigation Steps

### Step 1 — Validate Network and DNS

Executed:

    ipconfig /all
    ping dc01.bpurple.com
    nslookup dc01.bpurple.com

All tests were successful.

This eliminated DNS and network connectivity as possible root causes.

---

### Step 2 — Attempt Domain Login

Login attempt using:

    bpurple\john

Error received:

    The trust relationship between this workstation and the primary domain failed.

This indicated a broken secure channel between CLIENT01 and the domain controller.

---

### Step 3 — Verify Computer Account in Active Directory

On DC01:

Opened:

    Active Directory Users and Computers

Verified:

- CLIENT01 computer object exists  
- Account is enabled  
- No OU misconfiguration  

This confirmed the issue was related to secure channel synchronization.

---

## Root Cause

The secure channel password between CLIENT01 and the domain controller was out of sync.

This commonly occurs due to:

- Virtual machine snapshot restore  
- System restore  
- Machine account password mismatch  
- Prolonged disconnection from domain  
- Cloned virtual machines  

Although DNS and connectivity were functioning correctly, authentication failed due to a corrupted trust relationship.

---

## Resolution Steps

### Standard L1/L2 Method — Rejoin Domain

1. Logged into CLIENT01 using local administrator account.

2. Opened:

    System Properties → Computer Name → Change

3. Changed membership from:

    Domain: bpurple.com

   To:

    Workgroup: WORKGROUP

4. Restarted the computer.

5. Rejoined the domain:

    Domain: bpurple.com

6. Entered domain administrator credentials.

7. Restarted the computer again.

---

## Verification

- Domain login successful  
- No trust relationship error displayed  
- User logged in using:

    bpurple\john

- Shared folders accessible  
- Group Policy applied successfully  

Domain trust relationship restored.

---

## Alternative Advanced Resolution (PowerShell)

At L2 level, the secure channel can be repaired without removing the computer from the domain:

    Test-ComputerSecureChannel -Repair -Credential bpurple\Administrator

This method repairs the trust relationship without requiring domain rejoin.

---

## Skills Demonstrated

- Active Directory authentication troubleshooting  
- Secure channel concept understanding  
- Domain join and rejoin procedures  
- Root cause isolation (DNS vs authentication issues)  
- Structured L1/L2 troubleshooting workflow  
- Enterprise-grade documentation practices  

---

## Key Takeaway

A domain trust failure is not a DNS or network issue — it is an authentication mismatch between the workstation and the domain controller.

Effective troubleshooting requires:

1. Confirming connectivity  
2. Validating DNS functionality  
3. Identifying authentication failure  
4. Repairing the secure channel or rejoining the domain  

This scenario reflects a real-world enterprise authentication issue commonly handled by L1 and L2 IT Support teams.
```

---

This version avoids nested triple backticks inside GitHub Markdown (which can sometimes break rendering), making it safer and cleaner for portfolio presentation.

If you'd like, I can now standardize this exact structure into a reusable master template for all your remaining tickets.
