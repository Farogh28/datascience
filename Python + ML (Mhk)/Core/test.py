# .index method
# print (x.Index(p))

# Booleans - True / False
# used to check specific conditions
# print (5>10)


# LAMBDA function

def app(fx , val):
    return 4 + fx(val)


double = lambda x: x * 2

# print (double(6))

cube = lambda x : x * x * x 

# print(cube(7))

avg =lambda x , y : (x*y)/2

# print(avg(2,5))

# Lmbda function an also paas as a argument

print(app (cube, 9))