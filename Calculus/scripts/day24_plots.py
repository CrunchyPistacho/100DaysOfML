# Import libraries 
import matplotlib.pyplot as plt 
import numpy as np 

# Set custom color codes
color_codes = ['#1f77b4','#ff7f0e','#2ca02c',
               '#d62728','#9467bd','#8c564b','#e377c2',
               '#7f7f7f','#bcbd22','#17becf']
  
# Createing vectors X and Y 
x = np.linspace(-3, 3, 100) 

#define functions to plot
def y1(x):
    return x


def y2(x):
    return x**2

def y3_1(x):
    return np.where(x <= 1.5, x**2, np.nan)

def y3_2(x):
    return np.where(x > 1.5, x, np.nan)


# Define the figure options
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)  
fig = plt.figure(figsize = (12, 7))

# Add a title 
plt.title('Some functions that tends to a limit') 

# first plot
# Create the plot 
ax1.plot(x, y1(x), alpha = 0.8, label ='y = x', 
         color = color_codes[1], 
         linewidth = 2,  
         markersize = 5) 

# Setting plot limits
ax1.axis(xmin=-2,xmax=2)
    
# Add X and y Label 
ax1.set_xlabel('x') 
ax1.set_ylabel('y') 
  
# Add a grid 
ax1.grid(alpha =.6, linestyle ='--') 

# Add hvlines
ax1.axhline(y=1.5, color="gray", linestyle ='--')
ax1.axvline(x=1.5, color="gray", linestyle ='--')

# Add a Legend 
ax1.legend() 

# second plot
# Create the plot 
ax2.plot(x, y2(x), alpha = 0.8, label ='y = x**2', 
         color = color_codes[1], 
         linewidth = 2,  
         markersize = 5) 

# Add and arrow
# ax2.arrow(1, y2(1), 1.1, y2(1.1), head_width=0.2, head_length=0.15, color = color_codes[1])

# Setting plot limits
ax2.axis(xmin=-3,xmax=3)
  
# Add X and y Label 
ax2.set_xlabel('x') 
ax2.set_ylabel('y') 
  
# Add a grid 
ax2.grid(alpha =.6, linestyle ='--') 

# Add hvlines
ax2.axhline(y=1.5**2, color="gray", linestyle ='--')
ax2.axvline(x=1.5, color="gray", linestyle ='--')


# Add a Legend 
ax2.legend() 

# third plot
# Create the plot 
ax3.plot(x, y3_1(x), alpha = 0.8, label ='y = x**2 if x < 2 \n x if x >= 2', 
         color = color_codes[1], 
         linewidth = 2,  
         markersize = 5) 

ax3.plot(x, y3_2(x), alpha = 0.8,
         color = color_codes[1], 
         linewidth = 2,  
         markersize = 5) 

# Add and arrow
# ax2.arrow(1, y2(1), 1.1, y2(1.1), head_width=0.2, head_length=0.15, color = color_codes[1])

# Setting plot limits
ax3.axis(xmin=-3,xmax=3)
  
# Add X and y Label 
ax3.set_xlabel('x') 
ax3.set_ylabel('y') 
  
# Add a grid 
ax3.grid(alpha =.6, linestyle ='--') 

# Add hvlines
ax3.axhline(y=1.5**2, color="gray", linestyle ='--')
ax3.axhline(y=1.5, color="gray", linestyle ='--')
ax3.axvline(x=1.5, color="gray", linestyle ='--')

# Add a Legend 
ax3.legend() 
  
# Show the plot 
plt.show()