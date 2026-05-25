mobile_list = {"A":"Oppo f19","B": 50, "C": 35000.05,"D":  "Oppo","E" : True, "F": "It is a phone."}
print(mobile_list)
print(type(mobile_list))
for i in mobile_list:
    print(mobile_list[i])
mobile_list["A"] = 23
mobile_list["G"] = 90
print(type(mobile_list))
for i in mobile_list:
    print(mobile_list[i])
mobile_list.pop(0)
print(type(mobile_list))




