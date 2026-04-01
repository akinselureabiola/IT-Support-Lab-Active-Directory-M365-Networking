
# Windows Server Deployment – Active Directory Infrastructure Build

## Ticket Information

- **Category:** Windows Infrastructure / Server Deployment  
- **Priority:** P2 – High  
- **Impact:** Infrastructure setup required for Active Directory lab environment  
- **SLA Target:** 1 Business Day  
- **Resolution Time:** 2 hours  
- **Status:** Completed  

---

## Scenario

In this lab, I simulated a real-world infrastructure task where I was required to deploy a Windows Server environment to support an Active Directory domain.

The goal was to build a functional domain environment that could support:

- User authentication  
- DNS resolution  
- Domain-joined client communication  

This type of setup forms the foundation of most enterprise IT environments.

---

## 🎯 Objectives

- Deploy a Windows Server environment for Active Directory  
- Configure static IP addressing for infrastructure stability  
- Install and configure AD DS and DNS roles  
- Promote the server to a Domain Controller  
- Join a client machine to the domain  
- Validate authentication and network communication  

---

## 🖥️ Environment

- Domain: bpurple.com  
- Domain Controller: DC01 (192.168.10.10)  
- Client Machine: CLIENT01 (192.168.10.20)  
- Server OS: Windows Server 2016 (Desktop Experience)  
- Client OS: Windows 10  
- Virtualization: Oracle VirtualBox (Internal Network)  
- Network Range: 192.168.10.0/24  

---

# Network Architecture

The lab environment consists of a Windows Server Domain Controller and a Windows client machine connected through a VirtualBox internal network.

![Lab Architecture](./screenshots/lab-architecture.png)

---

## 🏗️ Infrastructure Overview

The lab environment consists of a Domain Controller and a client machine configured within the same network to simulate a typical enterprise setup.

### Domain Controller

DC01  
Windows Server 2016  
192.168.10.10  
Roles: AD DS / DNS  
Domain: bpurple.com  

Responsibilities:

- Active Directory authentication
- DNS resolution
- Directory management

---

### Client Machine

CLIENT01  
Windows 10  
Domain Joined  

Responsibilities:

- Domain authentication
- User login testing
- Network communication validation

---

# Server Deployment

## Windows Server Installation

A Windows Server 2016 virtual machine was created using Oracle VirtualBox.

The **Desktop Experience edition** was selected to allow graphical server management.

![Server Installation](./screenshots/server-installation.png)

---

## Server Identity Configuration

The server hostname was configured using enterprise naming standards.

Computer Name: DC01  
Domain: bpurple.com  

This naming convention is commonly used in enterprise infrastructure environments where domain controllers follow the format:

DC01  
DC02  

![Server System Properties](./screenshots/server-system-properties.png)

---

## ⚙️ Static IP Configuration

I configured a static IP address on the server to ensure consistent availability of critical services such as DNS and Active Directory.

Using DHCP for a Domain Controller can lead to service disruptions, so static addressing is required in enterprise environments.

IP Address: 192.168.10.10  
Subnet Mask: 255.255.255.0  
Default Gateway: 192.168.10.1  
DNS Server: 192.168.10.10  

Configuration validation command:

ipconfig /all

![Server IP Configuration](./screenshots/server-ipconfig.png)

---

## 🧩 Server Roles Installed

I installed the following roles to support enterprise identity services:

- Active Directory Domain Services (AD DS)  
- DNS Server  

These roles enable:

- Centralized authentication  
- Directory management  
- Name resolution within the domain  

![Server Manager](./screenshots/server-manager.png)

---

## 🚀 Domain Controller Promotion

I promoted the server to a Domain Controller for the domain:

bpurple.com

This process configured:

- Active Directory Domain Services  
- Integrated DNS  
- Domain authentication infrastructure  

After promotion, the server became the central authority for authentication and directory services in the environment.

---

# Client Machine Deployment

## 💻 Client Machine Deployment

I configured a  Windows 10 client machine was within the same network and joined it to the domain.

This allowed validation of:

- Domain authentication  
- DNS resolution  
- Network communication with the Domain Controller  

![Client Domain Join](./screenshots/client-domain-joined.png)

---

# Client IP Configuration

Host Name . . . . . . . . : CLIENT01
Primary DNS Suffix . . . : bpurple.com

IPv4 Address . . . . . . : 192.168.10.20
Subnet Mask . . . . . .  : 255.255.255.0
Default Gateway . . . .  : 192.168.10.1

DNS Servers . . . . . .  : 192.168.10.10

Configuration validation command:

ipconfig /all

![Client IP Configuration](./screenshots/client-ipconfig.png)

---

## 🔐 Domain Authentication Validation

To verify the environment, I created  and tested a domain user account.

Example user:

bpurple\john  

The user successfully logged in from CLIENT01.

This confirmed:

- Domain authentication was working  
- DNS resolution was functional  
- Communication with the Domain Controller was successful  

---

## ✅ Verification

I ensured the following checks were performed to validate the deployment:

Server:
- Domain Controller operational  
- DNS service running  
- Domain reachable (DC01.bpurple.com)  

Client:
- Successfully joined to domain  
- Domain login successful  
- DNS resolution working  

Connectivity Test:

ping dc01.bpurple.com  

Result:

Reply from 192.168.10.10  

---

# Evidence — Lab Screenshots

### Virtual Lab Environment

![VirtualBox Lab](./screenshots/virtualbox-lab-environment.png)

---

### Server System Properties

![Server System Properties](./screenshots/server-system-properties.png)

---

### Static IP Configuration

![Server IP Config](./screenshots/server-ipconfig.png)

---

### Server Manager Roles

![Server Manager](./screenshots/server-manager.png)

---

### Client Domain Join

![Client Domain Join](./screenshots/client-domain-joined.png)

---

## 💼 Business Impact

In a real environment, this infrastructure would serve as the foundation for:

- User authentication  
- Access to shared resources  
- Group Policy enforcement  
- Network service management  

Without a properly configured Domain Controller, users would be unable to log in, access resources, or operate within the corporate network.

---

## 🧑‍💻 Skills Demonstrated

- Set up a Windows Server from scratch and prepared it for an Active Directory environment  
- Configured a static IP to ensure the server remained stable and reachable  
- Installed and configured Active Directory Domain Services (AD DS) and DNS  
- Promoted the server to a Domain Controller  
- Joined a Windows client machine to the domain  
- Tested and confirmed that authentication and DNS were working properly  
- Built a complete lab environment that can be used for further troubleshooting and simulations  

---

## 🧠 Key Takeaway

One thing this lab reinforced for me is that you can’t troubleshoot Active Directory or network issues without having a solid foundation in place.

Setting up a proper Domain Controller with DNS is what everything else depends on. If this part isn’t configured correctly, nothing else in the environment will work as expected.

---

## 🧠 Conclusion

In this lab, I set up a Windows Server and configured it as the Domain Controller for the bpurple.com environment.

I validated the setup by joining a client machine to the domain and confirming that authentication and DNS were working correctly.

This environment now serves as the foundation for all the other labs I’ve built, including troubleshooting Active Directory, DNS, DHCP, and access-related issues.

Overall, this gave me a clearer understanding of how enterprise environments are structured and how everything connects together.