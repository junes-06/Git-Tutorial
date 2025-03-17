def get_radius(prompt):
    r=int(input(prompt))
    return r

radius = get_radius('넓이를 구하고자 하는  원의반지름은? ')

def get_circle_area() :
    s = radius**2*3.14
    return s

area = get_circle_area()


print('반지름',radius, '인 원의 넓이= 3.14 x',radius, "x", radius ,'=', area)
