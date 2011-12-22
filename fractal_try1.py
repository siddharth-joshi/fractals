from numpy import *
import Image
import ImageDraw

upper = 2
lower = -2
stride = .005

MAX_ITER = 255

x = arange(lower,upper+stride,stride) 
y = arange(lower,upper+stride,stride)

X,Y = meshgrid(x,y)

init_grid = flipud(X+1j*Y)
print init_grid.shape
final_grid = zeros(init_grid.shape)

colour_idx = where(init_grid == 0+1j*0)
grid_iter = zeros_like(init_grid)


#img = Image.new("RGB",(len(x),len(y)),"#FFFFFF")
#draw = ImageDraw.Draw(img)
#final_Image = ImageDraw.Draw(img)

# iterator
for idx in xrange(0,MAX_ITER):
#	print idx
	grid_iter = square(grid_iter)+init_grid
	abs_iter = abs(grid_iter)
	abs_iter[colour_idx] = 0
	colour_idx = where (abs_iter >= upper)
	final_grid[colour_idx] = MAX_ITER - idx
#	final_Image.point(colour_idx,MAX_ITER-idx)

im = Image.fromarray(uint8(final_grid))
im.show()
#print final_grid
#image.save(r,"fractal.png","PNG")
