#Calculate Profit or Loss Input cost price and selling price. Display either: Profit and amount, or Loss and amount, or No Profit No Loss

cost_price = int(input("Enter Cost Price: "))           
selling_price = int(input("Enter Selling Price: "))     

if selling_price > cost_price:                          
    profit = selling_price - cost_price                 
    print(f"Profit is {profit}.")                       
elif selling_price < cost_price:                        
    loss = cost_price - selling_price                   
    print(f"Loss is {loss}.")                                                       
else:                                                   
    print("No Profit and Loss.")                        