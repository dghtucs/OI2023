import problem
import json
ci = open("l7.txt","r")
text = ci.read()
co = open("co.json","a")

str = text.split('V')
print(str)



import sys
sys.stdout = co

for s in str:
    print(problem.api_request(s)[0])


# with open('co.json', 'w') as f:
#     for s in str:
#         json.dump(problem.api_request(s)[0], f)