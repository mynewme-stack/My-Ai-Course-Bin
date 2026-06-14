import numpy as np
assessed , sale, sale_ratio  = np.genfromtxt("Datasets/Real_Estate_Sales_2001-2022_GL-Short.csv", delimiter=",", usecols=(5,6,7), skip_header= 1, unpack=True,dtype=float, invalid_raise= False)

# Output

print(f"Assessed Value: {assessed}")
print(f"Sale Amount: {sale}")
print(f"Sale ratio: {sale_ratio}")

# Basic Operations

print("Maximum Sale = ", max(sale))

print("Minimum Sale = ", min(sale))

print("Mean of Sale = ", np.mean(sale))

print("Median = " ,np.median(sale))

print("Average of Sale = ", np.average(sale))

print("Standard Deviation = ", np.std(sale))       # Standard Deviation

print("Percentile of 50% = ", np.percentile(sale, 50))
print("Percentile of 25% = ", np.percentile(sale, 25))

# Math Operations
print("Square root of Sale = ", np.sqrt(sale))
print("Square of Sale = ", np.square(sale))
print("Power of Sale = ", np.power(sale,0.5))
print("Absolute Value of Sale = ", np.abs(sale))

# Arithmetic
print("Addition of sale and sale_ratio: ", sale+sale_ratio)

print("Subtraction of sale and sale_ratio: ",sale - sale_ratio)

print("Multiplication of sale and sale_ratio: ", sale * sale_ratio)

print("Division of sale and sale_ratio: ",sale / sale_ratio)

print("Floor Division of sale and sale_ratio: ", sale // sale_ratio)

# Trignometry

salpi = np.pi * sale_ratio
print("Sale ratio multiply by Pie = ", salpi)

print("Sine = ", np.sin(salpi))
print("Cosine = ", np.cos(salpi))
print("Tangent = ", np.tan(salpi))

# Hyperbolic

print("Sinh = ", np.sinh(salpi))
print("Cosh = ", np.cosh(salpi))
print("Tanh = ", np.tanh(salpi))

# Inverse hyperbolic

print("Inverse Sinh = ", np.arcsinh(salpi))
print("Inverse Cosh = ", np.arccosh(np.clip(salpi,1,None)))
print("Inverse Tanh = ", np.arctanh(sale_ratio))

# Exponential value 

print("Exponential values = ", np.exp(salpi))

# Logarithm

print("Log :", np.log(sale))
print("Base 10 Log :", np.log10(sale))

# 2nd Dimension

salrat_2d= np.array([sale, sale_ratio])
print("2D array: ",salrat_2d)

# Characteristics 

print("Dimension of sale and sale ratio: ",salrat_2d.ndim) # Number of dimensions
print("Size : ", salrat_2d.size)  
print("Shape : ", salrat_2d.shape)
print("Data Type : ", salrat_2d.dtype)

# Slicing

salrat_2d_slice = salrat_2d[1:2 , 2:5]
print("Sliced : ", salrat_2d_slice)

# Indexing

salrat_2d_item = salrat_2d[1,0]
print("One item : ",salrat_2d_item)

# Output

print("Nditer:\n")
for i in np.nditer(salrat_2d):                         # Only values
    print(i)

print("Ndenumerate:\n")
for index, i in np.ndenumerate(salrat_2d):               # Index,Value
    print(index,i)

# Reshaping

salrat_2d_re = np.reshape(salrat_2d, (2, -1))            #
print(f"Reshaped: {salrat_2d_re}")