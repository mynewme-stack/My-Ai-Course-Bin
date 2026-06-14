import numpy as np
brokered_by, status, price, bed, bath,acre_lot, zip_code,house_size = np.genfromtxt('Datasets/RealEstate-USA.csv', delimiter=',', usecols= (0,1,2,3,4,6,9,10), unpack=True ,dtype= None, skip_header=1 )

# Output data

print(f'Brokered by: {brokered_by}')
print(f'Status: {status}')
print(f'Price: {price}')
print(f'Zipcode: {zip_code}')
print(f'Beds: {bed}')
print(f'Baths: {bath}')

# Maximum and Minimum value

print("Maximium price = ", max(price))
print("Minimium price = ", min(price))

# Basic Statistics

print("Mean of Price = ", np.mean(price))
print("Average of price = ", np.average(price))
print("Standard Deviation= ", np.std(price))
print("Median= " ,np.median(price))
print("Percentile of 10% = ", np.percentile(price, 10))
print("Percentile of 5% = ", np.percentile(price, 5))
print("Standard Deviation = ", np.std(price))

# Math Operations

print("Square root = ", np.sqrt(price))
print("Square = ", np.square(price))
print("Power = ", np.power(price,0.5))
print("Absolute Value = ", np.abs(price))

# Arithmetic

print("Addition of Bedrooms and Bathrooms: ", bed + bath)
print("Subtraction of Bedrooms and Bathrooms: ", bed - bath)
print("Multiplication of Bedrooms and Bathrooms: ", bed * bath)
print("Division of Bedrooms and Bathrooms: ", bed / bath)
print("Floor Division of Bedrooms and Bathrooms: ", bed // bath)

# Trignometry

pricepi = np.pi * price
print("Price Pie = ", pricepi)

print("Sine = ", np.sin(price))
print("Cosine = ", np.cos(price))
print("Tangent = ", np.tan(price))

# Hyperbolic

print("Sinh = ", np.sinh(price))
print("Cosh = ", np.cosh(pricepi))
print("Tanh = ", np.tanh(price))

# Inverse hyperbolic

print("Inverse Sinh = ", np.arcsinh(price))
print("Inverse Cosh = ", np.arccosh(price))
print("Inverse Tanh = ", np.arctanh(price))

# Exponential Value

print("Exponential values = ", np.exp(np.clip(pricepi, None, 1)))

# Logarithm

print("Log :", np.log(pricepi))
print("Base 10 Log :", np.log10(pricepi))

acre_size_2d = np.array([acre_lot, house_size])
print("2D array: ",acre_size_2d)
print("Dimesion of Acre lot: ",acre_size_2d.ndim) 
print("Size : ", acre_size_2d.size)
print("Shape : ", acre_size_2d.shape)
print("Data Type : ", acre_size_2d.dtype)
# Slicing
acre_size_2d_slice_1 = acre_size_2d[0:1 , 1:5]
print("Sliced : ", acre_size_2d_slice_1)
# IN dexing
acre_size_item = acre_size_2d_slice_1[0,1]
print("One item : ",acre_size_item)
for i in np.nditer(acre_size_2d):
    print(i)
for index, i in np.ndenumerate(acre_size_2d):
    print(index,i)
acre_size_2d_re = np.reshape(acre_size_2d, (2, 200))
print(acre_size_2d_re)
clean_arr = price[~np.isnan(price)]

print(clean_arr)