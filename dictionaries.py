from traceback import print_tb

# dictionary

d1 = {
    "Language":"Python",
    "number":10,
    1:"Training",
    10:"Training"
     }

print(d1.keys())
print(d1.values())
print(d1.items())
print(d1)
print(dir(dict))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values'

d2 = d1.copy()
print(d2)
print(d1.get("Language"))
d1.pop("Language")
print(d1)
d1.popitem()
print(d1)
print(d2)
d1.update(d2)
print(d1)
print(d1.setdefault(1))

# adding , updating and deleting

del d1["Language"]
print(d1)

d1["number"] = 50
print(d1)

d1["name"] = "Ankit"
print(d1)

if "name" in d1.values():
    print("It is present")
else:
    print("Not present")

for i in d1:
    print(f"Key is {i}")
    print(f"Value is {d1[i]}")
    print(d1.get(i))


#json

ankit = {
           "personal_info":
               {
               "name":"XYZ",
               "age":35,
               "sex":"male"
               },
            "career_info":
               {
                "degree":"btech",
                "branch":"IT",
                "company":"abc"
               }
        }

print(ankit["career_info"]["degree"])