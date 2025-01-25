# i = 2
# j = 1
# while i <= 6:
#     result = 2 ** j * 1  
#     print(result)
#     i += 1
#     j += 1


i = 2
j = 1

while j <= 5:
    result = 2 ** j  # Powers of 2 for the result
    print(f"{i} * {j} = {result}")
    
    # Alternate between 2 and 3 for i
    if i == 2:
        i = 3
    else:
        i = 2
    
    j += 1