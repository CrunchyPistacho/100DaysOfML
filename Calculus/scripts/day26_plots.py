# Import libraries 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Set custom color codes
color_codes = ['#1f77b4','#ff7f0e','#2ca02c',
               '#d62728','#9467bd','#8c564b','#e377c2',
               '#7f7f7f','#bcbd22','#17becf']

# plot 1
# Createing vectors X and Y 
x = np.linspace(2, 4.5, 100000) 


def y(x):
    return np.where( x != 0, x * np.sin(1/x), np.nan)

def y(x):
    return 1/x**2 + x* np.sin(x**2)

  
fig = plt.figure(figsize = (12, 7))

# Setting plot limits
plt.xlim([-1, 5]) 

# Create the plot 
plt.plot(x, y(x), alpha = 0.8, label ='y = 1/x**2 + x* np.sin(x**2)', 
         color =color_codes[0], 
         linewidth = 2,  
         markersize = 5) 
  
# Add hvlines
plt.axhline(y=0, color="black", linestyle ='-')
plt.axvline(x=0, color="black", linestyle ='-')

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


# plot 2
# Createing vectors X and Y 
x = np.linspace(2, 4, 100000) 

def y2(x):
    return 1/x + x* np.sin(x**2)

  
fig = plt.figure(figsize = (12, 7))

# Setting plot limits
plt.xlim([-1, 5]) 

# Create the plot 
plt.plot(x, y2(x), alpha = 0.8, label ='y = 1/x + x* np.sin(x**2)', 
         color =color_codes[0], 
         linewidth = 2,  
         markersize = 5) 
  
# Add hvlines
plt.axhline(y=0, color="black", linestyle ='-')
plt.axvline(x=0, color="black", linestyle ='-')
plt.axhline(y=4.1, color="grey", linestyle ='--')

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

# plot 3
# Createing vectors X and Y 
x = np.linspace(0, 3, 100000) 

def y3(x):
    return -x**2 +2*x -3

  
fig = plt.figure(figsize = (12, 7))

# Setting plot limits
plt.xlim([-1, 5]) 

# Create the plot 
plt.plot(x, y3(x), alpha = 0.8, label ='y = 1/x + x* np.sin(x**2)', 
         color =color_codes[0], 
         linewidth = 2,  
         markersize = 5) 
  
# Add hvlines
plt.axhline(y=0, color="black", linestyle ='-')
plt.axvline(x=0, color="black", linestyle ='-')
plt.axvline(x=1, color="grey", linestyle ='--')

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

