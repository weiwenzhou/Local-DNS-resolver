# Local DNS resolver

A DNS resolver that takes a domain name and returns DNS information about the domain by querying servers starting at the root server level.

# Examples
```bash
$ python mydig.py www.google.com
QUESTION SECTION: 
www.google.com. IN A

ANSWER SECTION: 
www.google.com. 300 IN A 142.250.64.68

Query time: 63 msec
WHEN: 2021-02-27 02:19:59
```
# Installation
Dependencies:
- dnspython 
```bash
$ git clone https://github.com/weiwenzhou/CSE310-HW1.git DNS
$ cd DNS/
DNS$ pip install -r requirements.txt
```

# Usage
```bash
$ python mydig.py www.google.com
```