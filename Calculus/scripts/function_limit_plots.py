# Import libraries 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Createing vectors X and Y 
x = np.linspace(-3, 3, 100) 
y = x
  
fig = plt.figure(figsize = (12, 7))

# Setting plot limits
plt.xlim([-3, 3]) 

# Create the plot 
plt.plot(x, y, alpha = 0.8, label ='y = x', 
         color ='blue', 
         linewidth = 2,  
         markersize = 5) 
  
# Add a title 
plt.title('Some functions that tends to a limit') 
  
# Add X and y Label 
plt.xlabel('x') 
plt.ylabel('y') 
  
# Add a grid 
plt.grid(alpha =.6, linestyle ='--') 
# Add a Legend 
plt.legend() 
  
# Show the plot 
plt.show()

