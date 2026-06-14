import numpy as np
latitude,longitude = np.genfromtxt("Datasets/FastFoodRestaurants.csv", delimiter=",",usecols=(4,5),unpack=True,dtype= float,skip_header=1,invalid_raise=False)

# Displaying Output

print(f'Latitude:\n{latitude}')
print(f'Longitude:\n{longitude}')

# Arithmetic

print("Addition of Longitude and Latitude: ", longitude + latitude)
print("Subtraction of Longitude and Latitude: ", longitude - latitude)
print("Multiplication of Longitude and Latitude: ", longitude * latitude)
print("Division of Longitude and Latitude: ", longitude / latitude)
print("Floor Division of Longitude and Latitude: ", longitude // latitude)

# Math Operations

print("Square root of Longitude = ", np.sqrt(longitude))
print("Square of Longitude = ", np.square(longitude))
print("Power of Longitude = ", np.power(longitude,0.2))
print("Absolute Value of Longitude = ", np.abs(longitude))

# Basic Statistics

print("Maximum Longitude = ", max(longitude))
print("Minimum Latitude = ", min(latitude))
print("Mean of Longitude = ", np.mean(longitude))
print("Average of Longitude = ", np.average(longitude))
print("Standard Longitude = ", np.std(longitude))
print("Median of Longitude = " ,np.median(longitude))
print("Percentile of 50% = ", np.percentile(longitude, 50))
print("Percentile of 25% = ", np.percentile(longitude, 25))

# Trignometry

latpi = np.pi * latitude

print("Latitude multiply Pie = ", latpi)
print("Sine = ", np.sin(latpi))
print("Cosine = ", np.cos(latpi))
print("Tangent = ", np.tan(latpi))

# Hyperbolic

print("Sinh = ", np.sinh(latitude))
print("Cosh = ", np.cosh(latitude))
print("Tanh = ", np.tanh(latitude))

# Inverse hyperbolic

latpi_ratio = latpi/(latpi+1)                                # For taking value between 0 and 1 for tangent
print("Inverse Sinh = ", np.arcsinh(latitude))
print("Inverse Cosh = ", np.arccosh(latitude))
print("Inverse Tanh = ", np.arctanh(latpi_ratio))

# Exponential Value

print("Exponential values = ", np.exp(latpi))

# Logarithm

print("Log :", np.log(latpi))
print("Base 10 Log :", np.log10(latpi))

# 2nd Dimension

longlat_2d= np.array([latitude, longitude])
print("2D array: ",longlat_2d)

# Information of dimension

print("Dimension of Longitude and Latitude: ",longlat_2d.ndim) 
print("Size: ", longlat_2d.size)
print("Shape: ", longlat_2d.shape)
print("Data Type: ", longlat_2d.dtype)

# Slice

longlat_2d_slice = longlat_2d[1:2 , 2:5]
print("Sliced: ", longlat_2d_slice)

# Indexing
longlat_2d_item = longlat_2d[1,0]
print("One item: ",longlat_2d_item)

# Ways of showing output

for i in np.nditer(longlat_2d):                          # Without index
    print(i)
for index, i in np.ndenumerate(longlat_2d):             # With index
    print(index,i)

# Reshape

longlat_2d_re = np.reshape(longlat_2d, (2, -1 ))
print('Reshaped:\n',longlat_2d_re)