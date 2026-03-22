# Outlook Email Sending Issue Troubleshooting Lab

🚀 This lab simulates a real-world IT support scenario where a user is unable to send emails in Microsoft 365.

The focus of this lab is not just setup, but **diagnosing, isolating, and resolving an email-related issue in a production-like environment**.

---

## 🧠 Scenario

A user reports:

> "I am unable to send emails from Outlook."

---

## 🔍 Investigation Steps

### 1. Verify User Account
- Navigated to Microsoft 365 Admin Center
- Confirmed user account exists and is active

---

### 2. Check License Assignment
- Opened **Licenses and Apps**
- Verified Microsoft 365 license is assigned

---

### 3. Verify Mailbox
- Accessed **Exchange Admin Center**
- Navigated to **Recipients → Mailboxes**
- Confirmed mailbox exists

---

### 4. Test Email via Outlook Web (OWA)
- Logged in via https://outlook.office.com
- Attempted to send email

---

## 💥 Issue Simulation

To simulate the issue:

- Disabled **Exchange Online** under the user’s license

Result:
- User was unable to send emails ❌

---

## 🧩 Root Cause

The issue was caused by **Exchange Online being disabled** in the user’s license.

Without Exchange Online:
- Mailbox functionality is restricted
- Sending and receiving emails is not possible

---

## 🛠️ Resolution

- Re-enabled **Exchange Online** in user license
- Waited for service to reapply
- Retested email functionality

Result:
- Email sending restored successfully ✅

---

## 🎯 Outcome

The issue was resolved by restoring the required service dependency.

---

## 💡 Key Learnings

- Email functionality depends on **Exchange Online**
- Licensing directly affects user access to services
- Outlook Web (OWA) is a powerful troubleshooting tool
- Always verify:
  - User account
  - License assignment
  - Service status
- Many issues are caused by **misconfiguration, not system failure**

---

## 🧑‍💻 Skills Demonstrated

- Microsoft 365 Administration  
- Exchange Online Management  
- Outlook Troubleshooting  
- License Management  
- Root Cause Analysis  
- IT Support Workflow  

---

## 📌 Tools Used

- Microsoft 365 Admin Center  
- Exchange Admin Center  
- Outlook Web (OWA)  

---

## 🔥 Real-World Insight

This is a very common IT support issue:

> “User cannot send email”

And in many cases, the root cause is not complex —  
it is simply a **missing or misconfigured service within the license**.

Understanding this helps reduce resolution time and improves user experience.