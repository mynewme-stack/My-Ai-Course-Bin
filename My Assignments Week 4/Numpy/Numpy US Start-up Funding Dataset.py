import numpy as np
investment,valuation = np.genfromtxt("Datasets/startup_growth_investment_data.csv", delimiter=",", usecols=(3,4), dtype=float, skip_header=1, unpack= True, encoding= None)

# Output

print(f'Investment:\n{investment}')
print(f'Valuation:\n{valuation}')

# Math Operations

print("Square root of Investment = ", np.sqrt(investment))
print("Square of Investment = ", np.square(investment))
print("Power of Investment = ", np.power(investment,0.4))
print("Absolute Value of Investment = ", np.abs(investment))

# Arithmetic

print("Addition of Investment and Valuation: ", investment + valuation)
print("Subtraction of Investment and Valuation: ",investment - valuation)
print("Multiplication of Investment and Valuation: ", investment * valuation)
print("Division of Investment and Valuation: ",investment / valuation)
print("Floor Division of Investment and Valuation: ", investment // valuation)

# Trignometry

valpi = np.pi * valuation
print("Valuation multiply Pie = ", valpi)

print("Sine = ", np.sin(valpi))
print("Cosine = ", np.cos(valpi))
print("Tangent = ", np.tan(valpi))

# Hyperbolic

val_ratio = valpi/(valpi+1)

print("Sinh = ", np.sinh(valuation))
print("Cosh = ", np.cosh(valuation))
print("Tanh = ", np.tanh(valuation))

# Inverse hyperbolic

print("Inverse Sinh = ", np.arcsinh(valuation))
print("Inverse Cosh = ", np.arccosh(valuation))
print("Inverse Tanh = ", np.arctanh(val_ratio))

# Exponential Value

print("Exponential values = ", np.exp(val_ratio))

# Logarithm

print("Log :", np.log(investment))
print("Base 10 Log :", np.log10(investment))

# 2nd Dimension

invval_2d= np.array([investment, valuation])
print("2D array: ",invval_2d)

# Qualities of 2nd Dimension Array

print("Dimension of Investment and Valuation: ",invval_2d.ndim) 
print("Size : ", invval_2d.size)
print("Shape : ", invval_2d.shape)
print("Data Type : ", invval_2d.dtype)

# Slicing

invval_2d_slice = invval_2d[1:2 , 2:5]
print("Sliced : ", invval_2d_slice)

# Indexing

invval_2d_item = invval_2d[1,0]
print("One item : ",invval_2d_item)

# Showing data

for i in np.nditer(invval_2d):                # Without index
    print(i)
for index, i in np.ndenumerate(invval_2d):      # With index
    print(index,i)

# Statistics

print("Maximum Investment = ", max(investment))
print("Minimum Investment = ", min(investment))
print("Maximum Valuation = ", max(valuation))
print("Minimum Valuation = ", min(valuation))
print("Mean of Investment = ", np.mean(investment))
print("Average of Investment = ", np.average(investment))
print("Standard Investment = ", np.std(investment))
print("Median = " ,np.median(investment))
print("Percentile of 70% = ", np.percentile(investment, 70))
print("Percentile of 15% = ", np.percentile(investment, 15))

# Reshaped

invval_2d_re = np.reshape(invval_2d, (2, -1 ))
print('Reshaped:\n',invval_2d_re)