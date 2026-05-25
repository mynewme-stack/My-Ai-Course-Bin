mobile_list = {"Oppo f19", 50, 35000.05, "Oppo", True, "It is a phone."}
print(mobile_list)
print(type(mobile_list))
for i in mobile_list:
    print(i)
mobile_list.add(5.455)
print(mobile_list)
mobile_list.discard(50)
print(mobile_list)
mobile_list.remove("Oppo")
print(mobile_list)
mobile_list.pop(0)



