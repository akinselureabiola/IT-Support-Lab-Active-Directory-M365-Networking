# Corrupt User Profile (Desktop and Files Missing)

## Ticket Information

- **Category:** Windows / User Profile / Active Directory  
- **Priority:** P2 – High  
- **Impact:** User unable to access personal desktop and profile data  
- **SLA Target:** 4 hours  
- **Resolution Time:** 1 hour 25 minutes  
- **Status:** Resolved  

---

## Scenario

**User Reported:**

> “I logged in and my desktop/files are missing.”

After logging into their domain workstation, the user noticed:

- Desktop icons were missing  
- Documents folder appeared empty  
- Personal settings were reset  
- Default Windows background displayed  

The user confirmed that files were previously present.

---

## Environment

- **Domain:** bpurple.com  
- **Domain Controller:** DC01 (192.168.10.10)  
- **Client Machine:** CLIENT01 (Domain-joined Windows 11)  
- **User Account:** john  
- **Virtualization:** VirtualBox (Internal Network + NAT)  
- **DNS Server:** 192.168.10.10  

---

## Network & Profile Architecture

The lab simulates a standard enterprise desktop environment:

- Active Directory Domain Services (AD DS) and DNS hosted on DC01  
- Client authentication via domain controller  
- Local profile stored under `C:\Users\john`  
- Registry-based profile mapping via SID under `ProfileList`  

*(Insert Architecture Diagram Screenshot Here)*

---

## Initial Symptoms

Upon login, Windows displayed a temporary profile behavior:

- Desktop appeared blank  
- User folders empty  
- Personalization settings reset  

System notification displayed:

> "You have been logged on with a temporary profile."

This indicated profile loading failure rather than authentication failure.

*(Insert Screenshot: Temporary Profile Notification)*

---

## Business Impact

If a user profile becomes corrupted:

- User cannot access business files  
- Productivity disrupted  
- Risk of perceived data loss  
- Increased IT support dependency  

Although domain authentication was successful, the user environment was unusable.

---

## Investigation Steps

### Step 1 — Verify Domain Authentication

User successfully logged in using: bpurple\john 


Confirmed domain authentication was functioning.

*(Insert Screenshot: Successful Domain Login)*

---

### Step 2 — Check User Profile Settings

Opened:

System Properties → Advanced → User Profiles → Settings

Observed multiple profile entries such as:

- john  
- TEMP.john  
- john.bpurple  

This indicated a profile loading issue.

*(Insert Screenshot: User Profiles Settings Window)*

---

### Step 3 — Inspect Registry ProfileList

Opened: regedit 


Navigated to:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList


Observed duplicate SID entries:

- One normal SID  
- One SID ending with `.bak`  

The `.bak` key indicated profile corruption and improper profile loading.

*(Insert Screenshot: Registry ProfileList Showing .bak SID Entry)*

---

## Root Cause

The user profile registry key became corrupted, causing Windows to load a temporary profile instead of the original profile directory.

This typically occurs due to:

- Improper shutdown  
- Disk write interruption  
- Profile locking during update  
- Antivirus interference  

Authentication succeeded, but profile initialization failed due to SID registry misalignment.

---

## Resolution Steps

1. Logged in with Domain Administrator account  
2. Backed up user profile folder: C:\Users\john

3. Opened Registry Editor: regedit

4. Located duplicate SID keys under `ProfileList`  
5. Renamed the SID with `.bak` by removing the extension  
6. Deleted incorrect temporary SID key  
7. Verified `ProfileImagePath` pointed to: C:\Users\john


8. Restarted CLIENT01  

*(Insert Screenshot: Corrected Registry SID Entry)*

---

## Verification

User logged back in.

Confirmed:

- Desktop icons restored  
- Documents folder intact  
- Personal settings restored  
- No temporary profile message  

*(Insert Screenshot: Restored Desktop Environment)*  

User confirmed files were accessible and environment restored.

---

## Skills Demonstrated

- Windows profile troubleshooting  
- Registry-level SID repair  
- SID identification and validation  
- Domain authentication validation  
- Data protection best practices (backup before modification)  
- Structured incident resolution workflow  

---

## Key Takeaway

Successful login does not guarantee successful profile loading.

When troubleshooting missing desktop or files:

1. Confirm the user is not logged into a temporary profile  
2. Check User Profile settings  
3. Inspect `ProfileList` registry entries  
4. Repair SID entries carefully  
5. Always back up user data before making changes  

Understanding Windows profile architecture and SID-to-profile mapping is critical for L1/L2 desktop support roles.


