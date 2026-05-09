# use of functions

def paint_wall(height,width,can=7):
    area = height*width 
    print(area)
    coverage_area = area/can
    print(f'the no of cans required to paint the wall are {int(coverage_area)+1}')

paint_wall(3,4)
paint_wall(25,15)
    
    