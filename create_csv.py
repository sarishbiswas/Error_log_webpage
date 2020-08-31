#!/usr/bin/python
import re
import csv

pat = r"ticky: INFO (.+) \[(.*)\] \((.+)\)"
regex = r"ticky: ERROR (.+) \((.+)\)"

users={}
errors={}

f = open("syslog.log","r")

for line in f.readlines():
    res = re.search(regex,line.strip())
    if res is not None:
        error = res.group(1).strip()
        user = res.group(2).strip()
        if error not in errors:
            errors[error]=0
        errors[error]+=1
        if user not in users:
            users[user]={}
            users[user]["ERROR"]=0
            users[user]["INFO"]=0
        users[user]["ERROR"]+=1
    # print("ERROR: "+res.group(2)+": "+res.group(1))
    else:
        result = re.search(pat,line.strip())
        user = result.group(3).strip()
        if user not in users:
            users[user]={}
            users[user]["ERROR"]=0
            users[user]["INFO"]=0
        users[user]["INFO"]+=1
   # print("INFO: "+result.group(3)+": " +result.group(1))
f.close()
sort_errors = sorted(errors.items(), key=lambda x: x[1], reverse=True)
with open("error_message.csv","w") as f:
    f.write("%s,%s\n"%("Error","Count"))
    for key in sort_errors:
        f.write("%s,%s\n"%(key[0],key[1]))
with open("user_statistics.csv","w") as f:
    f.write("%s,%s,%s\n"%("Username","ERROR","INFO"))
    for key in sorted(users.keys()):
        f.write("%s,%s,%s\n"%(key,users[key]["ERROR"],users[key]["INFO"]))
