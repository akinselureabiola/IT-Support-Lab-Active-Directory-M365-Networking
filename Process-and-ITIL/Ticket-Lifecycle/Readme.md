# IT Support Ticket Lifecycle — End-to-End Incident Resolution

## Ticket Information

- **Category:** IT Operations / Service Desk / ITIL Process
- **Priority:** P3 – Medium
- **Impact:** Single user connectivity issue
- **SLA Target:** 4 hours (First response within 15 minutes)
- **Resolution Time:** 40 minutes
- **Status:** Resolved

---

## Scenario

In this lab, I simulated a real support ticket where a user reported:

> “Cannot connect to office Wi-Fi. Others are connected.”

Since other users were not affected, this indicated that the issue was likely isolated to the user’s device rather than a network-wide problem.

---

## Environment

- **Device:** Windows 10/11 Laptop
- **Network:** Corporate Wi-Fi (DHCP Enabled)
- **Authentication:** WPA2 Enterprise
- **User Account:** Standard Domain User
- **Support Model:** ITIL-based Service Desk Workflow

---

## Initial Symptoms

During initial assessment, I observed:

- Wi-Fi network was visible but not connecting  
- “No Internet, Secured” message displayed  
- Other users were connected successfully  

This confirmed that the issue was limited to a single device.

---

## 💼 Business Impact

In a real environment, this issue would prevent the user from accessing email, shared drives, and internal systems.

Even though the issue affected a single user, it still impacted productivity and required timely resolution within SLA.

---

## Ticket Lifecycle Process

### 1 — Ticket Received

The ticket was submitted through the service desk portal and categorized as a connectivity issue.

Priority was set to P3 based on impact, and the ticket was assigned for investigation.

---

### 2 — Triage and First Response

I acknowledged the ticket within SLA and gathered additional information to understand the issue:

- User’s current location  
- Whether others were affected  
- Recent changes to the device  
- Ability to connect to other networks  

Based on the responses, I confirmed the issue was isolated to the user’s device and updated the ticket status to:

In Progress

---

### 3 — Troubleshooting and Diagnosis

I followed a structured troubleshooting approach to identify the issue.

First, I verified that the wireless adapter was enabled and attempted to reconnect to the correct network.

Next, I checked the network configuration:

ipconfig  

I observed that no IPv4 address was assigned, indicating a DHCP issue.

To resolve this, I:

- Disabled and re-enabled the wireless adapter  
- Released and renewed the DHCP lease:

ipconfig /release  
ipconfig /renew  

After this, the device received a valid IP address from the DHCP server.

---

### 4 — Communication with User

Throughout the process, I kept the user informed about the steps being taken and what to expect.

I explained the issue in simple terms and ensured the user understood when testing was required on their side.

Regular updates were provided in the ticket to maintain transparency.

---

### 5 — Solution Applied

After restoring the network configuration:

- The wireless adapter was functioning correctly  
- A valid IP address was assigned  
- The device successfully connected to the corporate Wi-Fi  

The issue was resolved and the ticket was updated to:

Resolved — Pending User Confirmation

---

### 6 — User Validation

The user confirmed that:

- Internet access was restored  
- Shared drives were accessible  
- Email was functioning normally  

The ticket was then closed with final resolution notes documented.

---

## 🧠 Root Cause

The wireless adapter entered an unstable state and failed to obtain a DHCP lease.

Without a valid IP address, the device could not communicate with the network, resulting in loss of connectivity.

---

## ✅ Verification

- Valid IPv4 address assigned  
- Internet connectivity restored  
- Internal resources accessible  
- No further connection issues observed  
- User confirmed successful resolution  

---

## 🧑‍💻 Skills Demonstrated

- Managed an end-to-end IT support ticket using an ITIL-based workflow  
- Performed structured troubleshooting for network connectivity issues  
- Diagnosed DHCP-related problems using command-line tools  
- Restored connectivity by reconfiguring network settings  
- Communicated effectively with the user throughout the incident  
- Documented investigation, resolution, and closure within SLA  

---

## 🧠 Key Takeaway

This lab showed that effective IT support is not just about fixing technical issues, but also about managing the full ticket lifecycle.

Clear communication, structured troubleshooting, and proper documentation are just as important as the technical solution.