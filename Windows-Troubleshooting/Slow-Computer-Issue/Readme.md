# Slow Computer Performance — Windows 10/11 Optimization

## Ticket Information

- **Category:** Windows / Performance / Desktop Support
- **Priority:** P3 – Medium
- **Impact:** Single user experiencing degraded system performance
- **SLA Target:** 4 hours
- **Resolution Time:** 1 hour
- **Status:** Resolved

---

## 🧠 Scenario

In this lab, I worked through a common IT support issue where a user reported:

> “My computer is extremely slow and keeps freezing.”

From the description, it sounded like a performance issue rather than a system failure, so I approached it by checking what was consuming system resources and affecting responsiveness.

---

## Environment

- **Device:** Dell Laptop
- **Operating System:** Windows 10 / Windows 11
- **User Account:** Standard Employee Account
- **Network:** Home setup
- **Antivirus:** Microsoft Defender (Active)

---

## 🔍 Initial Symptoms

After logging into the system, I noticed:

- Slow response when opening applications  
- High memory usage immediately after startup  
- Multiple programs launching automatically  
- Occasional system freezing  

There were no error messages, which suggested the issue was likely caused by system load rather than hardware failure.

---

## 💼 Business Impact

Although this issue affected only one user, it still had a direct impact on productivity.

Tasks were taking longer to complete, and the system was unreliable, which could lead to delays in daily work if not resolved quickly.

---

## Investigation Steps

### Step 1 — Confirm the Issue

I first logged into the user’s account to experience the issue directly.

The system was clearly slow, so I opened Task Manager to see what was happening in the background.

I immediately noticed high memory usage and several processes running at startup.

![Task Manager - High Memory Usage](screenshots/CPU-and-memory-usage)

---

### Step 2 — Review Startup Programs

Next, I checked the Startup tab in Task Manager.

There were multiple applications set to launch automatically, including some that weren’t necessary.

I disabled the non-essential ones to reduce the load during login.

![Disable Unused Apps](screenshots/disabled-unused-apps.png)

---

### Step 3 — Clean Up Disk Space

I then ran Disk Cleanup to remove temporary files and cached data.

This helped free up space and reduce unnecessary system load.

![Disable Unused Apps](screenshots/disk-cleanup.png)

---

### Step 4 — Remove Unused Applications

I reviewed the installed applications and found several programs that were no longer needed.

I uninstalled these to reduce resource usage and improve overall performance.

![Resource Usage](screenshots/resource-usage.png)

---

### Step 5 — Check for Updates

Finally, I checked for pending Windows updates.

There were a few updates available, so I installed them and restarted the system to apply the changes.

---

## 🧠 Root Cause

The slowdown was mainly caused by too many applications running at startup, along with temporary files and outdated system updates.

All of these combined were putting unnecessary pressure on system resources.

---

## 🛠️ Resolution

To resolve the issue, I:

- Disabled unnecessary startup programs  
- Cleared temporary files using Disk Cleanup  
- Removed unused applications  
- Installed pending Windows updates  
- Restarted the system and tested performance  

---

## ✅ Verification

After making these changes, I checked the system again:

- Startup time improved noticeably  
- Applications opened faster  
- Memory usage was lower  
- No freezing or lag observed  

The user also confirmed that the system was running much smoother.

---

## 🧑‍💻 Skills Demonstrated

- Diagnosed a slow system by checking real-time resource usage  
- Identified unnecessary startup programs affecting performance  
- Performed system cleanup to improve responsiveness  
- Managed installed applications to reduce system load  
- Applied Windows updates to improve stability  
- Followed a structured approach to troubleshoot and resolve the issue  

---

## 🧠 Key Takeaway

This lab showed me that most slow computer issues aren’t caused by anything serious.

In many cases, it’s just a combination of too many startup programs, temporary files, and outdated updates.

Taking a simple, step-by-step approach can resolve the issue without needing to reinstall the system.
