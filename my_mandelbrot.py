from numpy import *

upper = 2
lower = -2
stride = .5

c = complex(-2,2)

x = arange(lower,upper+stride,stride) 
y = arange(lower,upper+stride,stride)

X,Y = meshgrid(x,y)

init_grid = flipud(X+1j*Y)
print init_grid.shape
final_grid = zeros(init_grid.shape)

colour_idx = where(init_grid == 0+1j*0)
# iter 1
grid_iter1 = zeros_like(init_grid)**2+init_grid
abs_iter1 = abs(grid_iter1)
abs_iter1[colour_idx] = 0
colour_idx = where (abs_iter1 >= upper)
final_grid[colour_idx] = 1

# iter 2


grid_iter2 = grid_iter1**2+init_grid
abs_iter2 = abs(grid_iter2)
abs_iter2[colour_idx] = 0
colour_idx = where (abs_iter2 >= upper)
final_grid[colour_idx] = 2


#print final_grid
#print abs_iter1
#grid_iter2 = zeros_like(init_grid)**2+init_grid


#print grid_iter1


#print X
#print Y

print final_grid

