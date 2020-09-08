# Import libraries 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Set custom color codes
color_codes = ['#1f77b4','#ff7f0e','#2ca02c',
               '#d62728','#9467bd','#8c564b','#e377c2',
               '#7f7f7f','#bcbd22','#17becf']

# Createing vectors X and Y 
x = np.linspace(-0.1, 0.1, 100000) 


def y(x):
    return np.where( x != 0, x * np.sin(1/x), np.nan)

  
fig = plt.figure(figsize = (12, 7))

# Setting plot limits
plt.xlim([-0.1, 0.1]) 

# Create the plot 
plt.plot(x, y(x), alpha = 0.8, label ='y = x * np.sin(1/x)', 
         color =color_codes[0], 
         linewidth = 2,  
         markersize = 5) 
  
# Add a title 
plt.title('') 
  
# Add X and y Label 
plt.xlabel('x') 
plt.ylabel('y') 
  
# Add a grid 
plt.grid(alpha =.6, linestyle ='--') 
# Add a Legend 
plt.legend() 
  
# Show the plot 
plt.show()

