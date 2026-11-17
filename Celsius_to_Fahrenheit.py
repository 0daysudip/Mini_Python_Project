#Celsius to fahreneheit function 

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32 

#fahreneheit to Celsius function 

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

#Asking form which unti to convert. 

unit = input("Convert form (C for celsius /F for fahrenheit): ").strip().upper()

#Taking user input 
temp = float(input("Enter Temperature: "))

if unit == "C":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
elif unit == "F":
    print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
else:
    print("Invalid unit. Pleace enter C or F.")

