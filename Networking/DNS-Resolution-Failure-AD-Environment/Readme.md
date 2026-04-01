# 🔧 DNS Resolution Failure – Active Directory Troubleshooting Lab

This lab simulates a real-world IT support issue where a DNS misconfiguration prevented hostname resolution in an Active Directory environment.

The focus was to investigate the issue, identify the root cause, and restore proper name resolution.

## Ticket Information

- **Category:** Networking / Active Directory / DNS  
- **Priority:** P2 – High  
- **Impact:** Single user unable to access domain resources  
- **SLA Target:** 4 hours  
- **Resolution Time:** 45 minutes (within SLA)  
- **Status:** Resolved  

---

## Scenario

In this lab, I worked on a simulated support case where a user reported:

> “I can ping the server IP but not the server name.”

This indicated that network connectivity was working, but name resolution was failing.

---

## Environment

- **Domain:** bpurple.com  
- **Domain Controller:** DC01 (192.168.10.10)  
- **Client Machine:** CLIENT01 (Domain-joined)  
- **Virtualization:** VirtualBox (Internal Network + NAT)  
- **DNS Server:** 192.168.10.10  

---

## Network Architecture

![Architecture](./screenshots/ad-lab-network-architecture.png)

---

## Initial Symptoms

On CLIENT01, I tested connectivity and name resolution:

ping 192.168.10.10        → Successful  
ping dc01.bpurple.com     → Failed  
nslookup dc01             → Failed  

This confirmed that network connectivity was working, but DNS resolution was not functioning.

---

## Evidence — Issue Identification

### ❌ Hostname Resolution Failure
![DNS Failure](./screenshots/dns-failure.png)

### ❌ Incorrect DNS Configuration
![Wrong DNS](./screenshots/wrong-dns-config.png)

---

## Business Impact

- Domain authentication may fail  
- Group Policy processing may break  
- File shares may become inaccessible  
- Applications relying on hostname resolution may fail  

---

## 🔍 Investigation Process

I followed a structured troubleshooting approach, starting with connectivity checks and then focusing on DNS configuration.

### Step 1 — Validate Network Connectivity

```bash
ping 192.168.10.10
```

✅ Result: Successful  

---

### Step 2 — Test DNS Resolution

```bash
nslookup dc01.bpurple.com
```

❌ Result:

```
*** can't find dc01: Non-existent domain
```

This confirmed that the issue was related to DNS resolution, so I proceeded to check the client’s DNS configuration.

---

### Step 3 — Inspect DNS Configuration

```bash
ipconfig /all
```

Observed:

```
DNS Servers . . . . . . . : 8.8.8.8
```

📌 External DNS detected

---

## 🧠 Root Cause

The issue occurred because CLIENT01 was configured to use an external DNS server (8.8.8.8) instead of the domain controller.

Since external DNS servers do not contain Active Directory records, the client was unable to resolve internal hostnames.

## 🛠️ Resolution

To resolve the issue, I updated the client’s DNS configuration to point to the domain controller:

192.168.10.10  

I then flushed the DNS cache using:

ipconfig /flushdns  

This ensured the client used the correct DNS server for name resolution.

---

## 📸 Evidence — Resolution & Validation

### ✅ DNS Fixed
![DNS Fixed](./screenshots/dns-fixed.png)

### ✅ Successful Resolution
![DNS Success](./screenshots/dns-success.png)

---

## ✅ Verification

After updating the DNS configuration:

- Hostname resolution was successful  
- Ping to dc01.bpurple.com worked  
- Shared resources such as \\DC01\Finance-Share were accessible  

This confirmed that DNS functionality was restored and the issue was resolved.

---

## 💼 Business Impact

In a real environment, DNS issues like this can prevent users from logging into the domain, accessing shared resources, or receiving Group Policy updates.

Even though the issue affected a single user, it could significantly impact productivity if not resolved quickly.

---

## 🧑‍💻 Skills Demonstrated

- Diagnosed DNS resolution issues in an Active Directory environment  
- Differentiated between network connectivity and DNS problems  
- Used command-line tools (ping, nslookup, ipconfig) for troubleshooting  
- Identified incorrect DNS configuration on a client machine  
- Restored functionality by correcting DNS settings  
- Applied a structured approach to isolate and resolve the issue  

---

## 🧠 Key Takeaway

This lab reinforced how critical DNS is in an Active Directory environment.

Even when network connectivity is working, incorrect DNS configuration can prevent authentication, resource access, and normal system operations.  

---

## Conclusion

The issue was caused by incorrect DNS configuration on the client.

Updating the DNS server to point to the domain controller restored hostname resolution and full access to domain resources.

This scenario reflects a common real-world IT support issue and highlights the importance of proper DNS configuration in Active Directory environments.
