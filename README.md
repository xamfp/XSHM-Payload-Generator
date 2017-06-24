# XSHM-Payload-Generator
XSHM-Payload-Generator is a tool used to generate Proof of Concept payloads by exploiting the Javascript functions ```history.go(-1)``` and ```history.back()```. I have found that this attack can be used to create a rather convincing phisher by chaining this attack with an open redirect and some URL tricks.
# Vulnerability Demonstration
Run ```./generate.py``` and navigate to http://127.0.0.1:5000/vulnerable.html

# What is XSHM?
Cross-Site History Manipulation (XSHM) is a SOP (Same Origin Policy) security breach. SOP is the most important security concept of modern browsers. SOP means that web pages from different origins by design cannot communicate with each other. Cross-Site History Manipulation breach is based on the fact that client-side browser history object is not properly partitioned on a per-site basis. Manipulating browser history may lead to SOP compromising, allow bi-directional CSRF and other exploitations such as: user privacy violation, login status detection, resources mapping, sensitive information inferring, users’ activity tracking and URL parameter stealing.

# References
https://www.owasp.org/index.php/Cross_Site_History_Manipulation_(XSHM)
