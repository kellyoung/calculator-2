def add(num_list):
    while len(num_list) > 1:
        num_list[0:2] = [num_list[0] + num_list[1]]
    
    return round(num_list[0], 2)

def subtract(num_list):
    while len(num_list) > 1:
        num_list[0:2] = [num_list[0] - num_list[1]]
    
    return round(num_list[0], 2)

def multiply(num_list):
    while len(num_list) > 1:
        num_list[0:2] = [num_list[0] * num_list[1]]
    
    return round(num_list[0], 2)

def divide(num_list):
    while len(num_list) > 1:
        num_list[0:2] = [float(num_list[0]) / num_list[1]]
    
    return round(num_list[0], 2)

def square(num_list):
    for item in range(len(num_list)):
        num_list[item] = round(num_list[item]**2, 2)
    return num_list

def cube(num_list):
    for item in range(len(num_list)):
        num_list[item] = round(num_list[item]**3, 2)
    return num_list

def power(num_list):
    while len(num_list) > 1:
        num_list[0:2] = [float(num_list[0]) ** num_list[1]]
    
    return round(num_list[0], 2)

def mod(num_list):
    while len(num_list) > 1:
        num_list[0:2] = [float(num_list[0]) % num_list[1]]
    
    return round(num_list[0], 2)


