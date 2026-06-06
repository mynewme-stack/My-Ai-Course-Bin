import numpy as np
latitude,longitude = np.genfromtxt("Class-data-science/FastFoodRestaurants.csv", delimiter=",",usecols=(4,5),unpack=True,dtype= float,skip_header=1,invalid_raise=False)
print(latitude)
print(longitude)
print("Maximium Longitude = ", max(longitude))
print("Minimium Latitude = ", min(latitude))
print("Mean of Longitude = ", np.mean(longitude))
print("Average of longitude = ", np.average(longitude))
print("Standard longitude = ", np.std(longitude))
print("Median = " ,np.median(longitude))
print("Percentile of 50% = ", np.percentile(longitude, 50))
print("Percentile of 25% = ", np.percentile(longitude, 25))
# Math Operations
print("Square root of longitude = ", np.sqrt(longitude))
print("Square of longitude = ", np.square(longitude))
print("Power of longitude = ", np.power(longitude,0.5))
print("Absolute Value of longitude = ", np.abs(longitude))
# Arithmetic
print("Addition of longitude and latitude: ", longitude + latitude)
print("Subtraction of longitude and latitude: ", longitude - latitude)
print("Multiplication of longitude and latitude: ", longitude * latitude)
print("Division of longitude and latitude: ", longitude / latitude)
print("Floor Division of longitude and latitude: ", longitude // latitude)
# Trignometry
latpi = np.pi * latitude
print("Latitude multiply Pie = ", latpi)
print("Sine = ", np.sin(latpi))
print("Cosine = ", np.cos(latpi))
print("Tangent = ", np.tan(latpi))
normal = max(latitude)
print("Exponential values = ", np.exp(np.clip(latitude, None, 1)))
# Logarithm
print("Log :", np.log(latpi))
print("Base 10 Log :", np.log10(latpi))
# Hyperbolic
print("Sinh = ", np.sinh(latpi))
print("Cosh = ", np.cosh(latpi))
print("Tanh = ", np.tanh(latpi))
# Inverse hyperbolic
print("Inverse Sinh = ", np.arcsinh(latpi))
print("Inverse Cosh = ", np.arccosh(latpi))
print("Inverse Tanh = ", np.arctanh(latpi))
longlat_2d= np.array([latitude, longitude])
print("2D array: ",longlat_2d)
print("Dimesion of Longitude and Latitude: ",longlat_2d.ndim) 
print("Size : ", longlat_2d.size)
print("Shape : ", longlat_2d.shape)
print("Data Type : ", longlat_2d.dtype)
# Slicing
longlat_2d_slice = longlat_2d[1:2 , 2:5]
print("Sliced : ", longlat_2d_slice)
# IN dexing
longlat_2d_item = longlat_2d[1,0]
print("One item : ",longlat_2d_item)
for i in np.nditer(longlat_2d):
    print(i)
for index, i in np.ndenumerate(longlat_2d):
    print(index,i)
longlat_2d_re = np.reshape(longlat_2d, (2, -1 ))
print(longlat_2d_re)