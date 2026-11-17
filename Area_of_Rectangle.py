# Defining function to calculate area
def area_of_rectangle(l, w):
    return l * w 
    
    
length = float(input("Enter length: "))
width = float(input("Enter width: "))

result = area_of_rectangle(length, width)
print("The area of rectangle is ", result)
