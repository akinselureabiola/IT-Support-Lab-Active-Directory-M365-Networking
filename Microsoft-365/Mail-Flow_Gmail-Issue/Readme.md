
# 📧 Exchange Online Incident Investigation
## Mail Not Delivered from Gmail (Mail Flow Rule Misconfiguration)

---

# 🧾 Incident Summary

A user reported that emails sent from Gmail accounts were not being received in their Microsoft 365 mailbox. Internal emails were functioning normally.

Investigation revealed that a **transport (mail flow) rule** in Exchange Online was configured to **reject messages from the Gmail domain**, causing all Gmail messages to be blocked before reaching the mailbox.

The issue was resolved by **identifying and disabling the misconfigured mail flow rule**.

---

# 🎫 Ticket Information

| Field | Details |
|-----|-----|
| Incident ID | LAB-EXO-002 |
| Category | Microsoft 365 / Exchange Online |
| Subcategory | Mail Flow |
| Priority | P2 – High |
| Impact | External communication disruption |
| SLA Target | 4 Hours |
| Resolution Time | 1 Hour 10 Minutes |
| Status | Resolved |

---

# 🖥 Environment

| Component | Details |
|------|------|
| Platform | Microsoft 365 |
| Service | Exchange Online |
| Tenant Domain | daizsign.onmicrosoft.com |
| Mailbox Tested | ehisevans@daizsign.onmicrosoft.com |
| Admin Portals Used | Exchange Admin Center |
| Investigation Tools | Message Trace, Mail Flow Rules |
| Lab Setup | Microsoft 365 Admin Lab |

---

# 🚨 User Report

> “I’m not receiving emails from Gmail addresses.”

The user indicated that emails from Gmail accounts were not appearing in their mailbox.

---

# 🔎 Initial Symptoms

Observed behaviour:

✔ Internal emails delivered successfully  
✔ Microsoft 365 tenant operational  
❌ Emails from Gmail accounts not delivered  
❌ No messages in Inbox or Junk folder  

Test performed from external Gmail account:

```
Email Sent → No Delivery
```

---

# 💼 Business Impact

If unresolved, the issue could:

- Disrupt communication with Gmail users
- Delay client correspondence
- Impact business operations
- Cause missed deadlines

Because Gmail is a **major global email provider**, blocking Gmail senders can significantly affect business communication.

---

# 🧪 Investigation Process

## Step 1 — Confirm Mailbox Functionality

An internal test email was sent.

Result:

```
Email Delivered Successfully
```

This confirmed the mailbox itself was functioning correctly.

---

# Step 2 — Perform Message Trace

Navigated to:

```
Exchange Admin Center
→ Mail Flow
→ Message Trace
```

Filtered results by:

Sender: Gmail account  
Recipient: ehisevans@daizsign.onmicrosoft.com

Result:

```
Status: Not Delivered
Reason: Mail Flow Rule
```

This indicated the email was blocked **during transport processing**.

---

# Step 3 — Review Mail Flow Rules

Navigated to:

```
Exchange Admin Center
→ Mail Flow
→ Rules
```

Identified rule:

```
Rule Name: Block Gmail Test
```

### Rule Configuration

Condition

```
Sender domain = gmail.com
```

Action

```
Reject the message
```

The rule was **Enabled**, meaning Exchange Online rejected all Gmail messages.

---

# 🧠 Root Cause

A **transport rule** had been configured to block emails from the domain:

```
gmail.com
```

Because Gmail matched the rule condition, Exchange Online rejected the email during mail flow processing.

This was a **policy configuration issue**, not a mailbox problem.

---

# 🛠 Resolution

Steps taken:

1️⃣ Navigated to:

```
Exchange Admin Center
→ Mail Flow
→ Rules
```

2️⃣ Located rule

```
Block Gmail Test
```

3️⃣ Disabled the rule

4️⃣ Saved configuration changes

---

# ✅ Verification

A new test email was sent from a Gmail account.

Result:

✔ Email delivered successfully  
✔ Message visible in Inbox  
✔ Message trace status:

```
Status: Delivered
```

User confirmed successful receipt.

Mail flow restored.

---

# 🧠 Lessons Learned

Transport rules in Exchange Online can override normal mailbox delivery behaviour.

When users report missing external emails, administrators should:

1️⃣ Perform a **Message Trace**  
2️⃣ Review **Mail Flow Rules**  
3️⃣ Check **Anti-Spam Policies**  
4️⃣ Review **Quarantine**

Following a structured troubleshooting process helps identify configuration issues quickly.

---

# 🛠 Skills Demonstrated

- Exchange Online Administration
- Microsoft 365 Troubleshooting
- Mail Flow Investigation
- Message Trace Analysis
- Transport Rule Configuration
- IT Incident Handling
- Root Cause Analysis

---

# 📂 Screenshots

Evidence captured during investigation:

## Screenshots

### Gmail Bounce Back Error
![Bounce Back](screenshots/bounce-back-error.png)

### Mail Flow Rule Enabled
![Rule Enabled](screenshots/mail-flow-rule-enabled.png)

### Message Trace Failure
![Message Trace](screenshots/message-trace-delivery-failure.png)

### Mail Flow Rule Disabled
![Rule Disabled](screenshots/mail-flow-rule-disabled.png)
---

# 🔗 Related Skills

- Microsoft 365 Administration  
- Exchange Online  
- Cloud Infrastructure  
- Email Security  
- Enterprise Troubleshooting
