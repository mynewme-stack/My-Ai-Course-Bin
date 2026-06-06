import numpy as np
investment,valuation = np.genfromtxt("Class-data-science/startup_growth_investment_data.csv", delimiter=",", usecols=(3,4), dtype=float, skip_header=1, unpack= True, encoding= None)
print(investment)
print(valuation)
print("Maximium Investment = ", max(investment))
print("Minimium Valuation = ", min(valuation))
print("Maximium Investment = ", max(investment))
print("Minimium Valuation = ", min(valuation))
print("Mean of Investment = ", np.mean(investment))
print("Average of Investment = ", np.average(investment))
print("Standard Investment = ", np.std(investment))
print("Median = " ,np.median(investment))
print("Percentile of 50% = ", np.percentile(investment, 50))
print("Percentile of 25% = ", np.percentile(investment, 25))
# Math Operations
print("Square root of Investment = ", np.sqrt(investment))
print("Square of investment = ", np.square(investment))
print("Power of investment = ", np.power(investment,0.5))
print("Absolute Value of investment = ", np.abs(investment))
# Arithmetic
print("Addition of investment and valuation: ", investment+valuation)
print("Subtraction of investment and valuation: ",investment - valuation)
print("Multiplication of investment and valuation: ", investment * valuation)
print("Division of investment and valuation: ",investment / valuation)
print("Floor Division of investment and valuation: ", investment // valuation)
# Trignometry
valpi = np.pi * valuation
print("Latitude multiply Pie = ", valpi)
print("Sine = ", np.sin(valpi))
print("Cosine = ", np.cos(valpi))
print("Tangent = ", np.tan(valpi))
normal = max(investment)
print("Exponential values = ", np.exp(np.clip(investment, None, 1)))
# Logarithm
print("Log :", np.log(investment))
print("Base 10 Log :", np.log10(investment))
# Hyperbolic
print("Sinh = ", np.sinh(valpi))
print("Cosh = ", np.cosh(valpi))
print("Tanh = ", np.tanh(valpi))
# Inverse hyperbolic
print("Inverse Sinh = ", np.arcsinh(valpi))
print("Inverse Cosh = ", np.arccosh(valpi))
print("Inverse Tanh = ", np.arctanh(valpi))
invval_2d= np.array([investment, valuation])
print("2D array: ",invval_2d)
print("Dimesion of Longitude and Latitude: ",invval_2d.ndim) 
print("Size : ", invval_2d.size)
print("Shape : ", invval_2d.shape)
print("Data Type : ", invval_2d.dtype)
# Slicing
invval_2d_slice = invval_2d[1:2 , 2:5]
print("Sliced : ", invval_2d_slice)
# IN dexing
invval_2d_item = invval_2d[1,0]
print("One item : ",invval_2d_item)
for i in np.nditer(invval_2d):
    print(i)
for index, i in np.ndenumerate(invval_2d):
    print(index,i)
invval_2d_re = np.reshape(invval_2d, (2, -1 ))
print(invval_2d_re)