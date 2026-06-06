import numpy as np
assessed , sale, sale_ratio  = np.genfromtxt("Class-data-science/Real_Estate_Sales_2001-2022_GL-Short.csv", delimiter=",", usecols=(5,6,7), skip_header= 1, unpack=True,dtype=float, invalid_raise= False)
print(f"Assessed Value: {assessed}")
print(f"Sale Ammount: {sale}")
print(f"Sale ratio: {sale_ratio}")
print("Maximium sale = ", max(sale))
print("Minimium sale = ", min(sale))
print("Mean of sale = ", np.mean(sale))
print("Average of sale = ", np.average(sale))
print("Standard Deviation = ", np.std(sale))
print("Median = " ,np.median(sale))
print("Percentile of 50% = ", np.percentile(sale, 50))
print("Percentile of 25% = ", np.percentile(sale, 25))
# Math Operations
print("Square root of sale = ", np.sqrt(sale))
print("Square of sale = ", np.square(sale))
print("Power of sale = ", np.power(sale,0.5))
print("Absolute Value of sale = ", np.abs(sale))
# Arithmetic
print("Addition of sale and sale_ratio: ", sale+sale_ratio)
print("Subtraction of sale and sale_ratio: ",sale - sale_ratio)
print("Multiplication of sale and sale_ratio: ", sale * sale_ratio)
print("Division of sale and sale_ratio: ",sale / sale_ratio)
print("Floor Division of sale and sale_ratio: ", sale // sale_ratio)
# Trignometry
salpi = np.pi * sale_ratio
print("Latitude multiply Pie = ", salpi)
print("Sine = ", np.sin(salpi))
print("Cosine = ", np.cos(salpi))
print("Tangent = ", np.tan(salpi))
normal = max(sale)
print("Exponential values = ", np.exp(np.clip(sale, None, 1)))
# Logarithm
print("Log :", np.log(sale))
print("Base 10 Log :", np.log10(sale))
# Hyperbolic
print("Sinh = ", np.sinh(salpi))
print("Cosh = ", np.cosh(salpi))
print("Tanh = ", np.tanh(salpi))
# Inverse hyperbolic
print("Inverse Sinh = ", np.arcsinh(salpi))
print("Inverse Cosh = ", np.arccosh(salpi))
print("Inverse Tanh = ", np.arctanh(sale_ratio))
salrat_2d= np.array([sale, sale_ratio])
print("2D array: ",salrat_2d)
print("Dimesion of sale and sale ratio: ",salrat_2d.ndim) 
print("Size : ", salrat_2d.size)
print("Shape : ", salrat_2d.shape)
print("Data Type : ", salrat_2d.dtype)
# Slicing
salrat_2d_slice = salrat_2d[1:2 , 2:5]
print("Sliced : ", salrat_2d_slice)
# IN dexing
salrat_2d_item = salrat_2d[1,0]
print("One item : ",salrat_2d_item)
for i in np.nditer(salrat_2d):
    print(i)
for index, i in np.ndenumerate(salrat_2d):
    print(index,i)
salrat_2d_re = np.reshape(salrat_2d, (2, 139))
print(f"Reshaped: {salrat_2d_re}")