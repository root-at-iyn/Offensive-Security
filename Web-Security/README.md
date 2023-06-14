# Web Application & API Hacking

## Offensive Web App Security

Web Application Security (Web App) Security is quite a big topic, and this is mainly due to each application being built slightly different. That being said, a lot of the fundamental things will remain the same. For instance an app will usually need: 

* A client or user interface for interaction
* Business logic which implements the apps purpose (the part that makes it useful to the user)
* Server-side logic to handle requests from clients
* Storage for persistant data which can be sent to or received from users.
* Network transport capabilities in order to communicate with other systems and the outside world 

These can be thought of as general requirements that most Web Apps or even APIs might need, and all of these requirements will need to be secured. The offensive side of Web App security explores looking at the app through the lens of a malicious attacker (or app user). The intended purpose is to reveal areas of weakness in the apps design or structure, that could be abused by a threat actor and ulitmately lead to the compromise of user data and control of the application or even the underlying system. 

## Resources

There's multiple resources available online to get started with Web App hacking / security testing, so I won't attempt to cover everything in this repo. The best place to get started would be:

### Books
- The [The Web Application Hacker’s Handbook: Finding and Exploiting Security Flaws](https://www.amazon.com/Web-Application-Hackers-Handbook-Exploiting/dp/1118026470/): This one's a classic and although it's dated, the sections on *application mapping*, *client side*, and *data store* attack vectors are still relevant.

### Labs
- [OWASP Vulnerable Web Applications Directory
](https://owasp.org/www-project-vulnerable-web-applications-directory/): These are easier to begin with and come with a mixture of guided labs or ctf style (less hand holding) labs. Some tried and tested apps that are well maintained are: 
    - [Damn Vulnerable Web Application - DVWA](https://github.com/digininja/DVWA) (PHP)
    - [NodeGoat](https://www.owasp.org/index.php/OWASP_Node_js_Goat_Project) (Node.js)
    - [OWASP Juice Shop](https://owasp-juice.shop/) (TypeScript, JavaScript, Angular, Node.js)
    - [WebGoat](https://owasp.org/www-project-webgoat/) (Java)
- [PortSwigger Web Security Accademy](https://portswigger.net/web-security): Probably has the best learning content with labs to practice, and is absolutely free :smirk:
- [HackTheBox](https://www.hackthebox.com/hacker): Most people have heard of this one by now, but they do ctf styled machines where you have to hack and compromise the system (box). You do have to pay to access archived machines, but it's worth it if you are preparing for exams like the **OSCP** or **OWSE**. For a list of HackTheBox machines that have a similarity to these exam labs, see [Vulnhub/Hackthebox OSWE-like VMs](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/edit#gid=665299979)

### Testing Guides
- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/latest/): This breaks down how to approach testing a Web App in the real world and what to look for. It is mainly used help guide security testing coverage.
- [The Burp Methodology](https://portswigger.net/support/the-burp-methodology): PortSwiggers guide and methodolgy to using BurpSuite for Web App testing. *Note: Parts of it may be out of date, but it's generally the same principle*

### Cheatsheets
- [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [Cross-site scripting (XSS) cheat sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#vuejs-reflected)
- [Obfuscating attacks using encodings
](https://portswigger.net/web-security/essential-skills/obfuscating-attacks-using-encodings#obfuscation-via-url-encoding)
- [MSSQL Injection Cheat Sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet)
- [Reverse Shell Cheat Sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
- [Web Shells](https://pentestmonkey.net/category/tools/web-shells)
- [0xn3va cheat-sheets - Web Application](https://0xn3va.gitbook.io/cheat-sheets/web-application/abusing-http-hop-by-hop-request-headers)

### Payloads and Lists
There are useful when fuzzing, brute forcing, or crafting payloads to send to an app:
- [Bug Bounty Cheat Sheet](https://github.com/EdOverflow/bugbounty-cheatsheet)
- [SecLists](https://github.com/danielmiessler/SecLists)
- [Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings)

In the `Web-Security` of this repo, it's mainly going to be writeups to challenges or labs. There's so much good content out there already, I won't be duplicating that :grin:

I hope this helps someone; have fun and happy hacking :sunglasses:
