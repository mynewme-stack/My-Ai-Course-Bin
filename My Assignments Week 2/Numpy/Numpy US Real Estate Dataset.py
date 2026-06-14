import numpy as np
brokered_by, status, price, bed, bath,acre_lot, zip_code,house_size = np.genfromtxt('Datasets/RealEstate-USA.csv', delimiter=',', usecols= (0,1,2,3,4,6,9,10), unpack=True ,dtype= float, skip_header=1 )

# Output data

print(f'Brokered by: {brokered_by}')
print(f'Status: {status}')
print(f'Price: {price}')
print(f'Zipcode: {zip_code}')
print(f'Beds: {bed}')
print(f'Baths: {bath}')

# Maximum and Minimum value

print("Maximum price = ", max(price))
print("Minimum price = ", min(price))

# Basic Statistics

print("Mean of Price = ", np.mean(price))
print("Average of price = ", np.average(price))
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

print("Sine = ", np.sin(pricepi))
print("Cosine = ", np.cos(pricepi))
print("Tangent = ", np.tan(pricepi))

# Hyperbolic

print("Sinh = ", np.sinh(bed))
print("Cosh = ", np.cosh(bed))
print("Tanh = ", np.tanh(bed))

# Inverse hyperbolic

print("Inverse Sinh = ", np.arcsinh(pricepi))
print("Inverse Cosh = ", np.arccosh(pricepi))
print("Inverse Tanh = ", np.arctanh(pricepi))

# Exponential Value

print("Exponential value = ", np.exp(pricepi))

# Logarithm

print("Log :", np.log(pricepi))
print("Base 10 Log :", np.log10(pricepi))

# 2nd dimension

acre_size_2d = np.array([acre_lot, house_size])
print("2D array: ",acre_size_2d)

# Characteristics

print("Dimension of Acre lot: ",acre_size_2d.ndim) 
print("Size : ", acre_size_2d.size)
print("Shape : ", acre_size_2d.shape)
print("Data Type : ", acre_size_2d.dtype)

# Slicing

acre_size_2d_slice = acre_size_2d[0:1 , 1:5]
print("Sliced : ", acre_size_2d_slice)

# Indexing

acre_size_item = acre_size_2d_slice[0,1]
print("One item : ",acre_size_item)

# Ways of showing output

# 1. Without index

for i in np.nditer(acre_size_2d):
    print(i)

# 2. With Index

for index, i in np.ndenumerate(acre_size_2d):
    print(index,i)

# Reshaping

acre_size_2d_re = np.reshape(acre_size_2d, (2, -1))
print(acre_size_2d_re)
acre_size_2d_re = acre_size_2d_re[np.isfinite(acre_size_2d_re)]