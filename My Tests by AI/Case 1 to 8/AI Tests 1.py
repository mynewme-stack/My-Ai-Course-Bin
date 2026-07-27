                                        # Costumer input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
product_name = input("Enter the product name: ")
price = float(input("Enter the price per unit: "))
quantity = int(input("Enter the quantity of the products: "))

#________________________________________________________________________________________________________________
 
                                        # Price calculations 
total_price = int(price * quantity)
tax = float(total_price * 0.10)
tax_total = int(total_price + tax)

#________________________________________________________________________________________________________________

                                        # Discount calculations
if (int(age) >= 50 or int(quantity) >= 5):
    discount = tax_total * 0.5
else:
    discount = tax_total * 0.05
net_total = int(tax_total - discount) 

#_____________________________________________________________________________________________________________
                                                 
                                          # Costumer Bill       
print("Costumer name: " + name)             
print("Costumer age: " + str(age))
print("Product name: " + product_name)
print("Price: " + str(price))
print("Quantity of products: " + str(quantity))
print("Total price without tax: " + str(total_price))
print("Tax: " + str(tax))
print("Total ammount: " +str(tax_total))
print("Net Total: " + str(net_total))

#________________________________________________________________________________________________________________

                                        # Discount Availabilty

if (int(age) >= 50 or int(quantity) >= 5):
    print("Senior Discount Applied!!")
else:
    print("Costumer is not applicable for discount.")

#________________________________________________________________________________________________________________

                                        # Payment Methods

payment = ["Cash", "Card", "Online"]
for i in payment:
    print(i)

#_________________________________________________________________________________________________________________
