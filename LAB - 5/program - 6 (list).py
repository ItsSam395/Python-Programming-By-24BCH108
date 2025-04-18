temp = input("Enter Temperature in Fahrenheit : ")
fahrenheit_temps=[]

for item in temp.split():
    fahrenheit_temps.append(float(item))
    
print("Temperatures in Fahrenheit: ", fahrenheit_temps)

celsius_temps=[]

for temp in fahrenheit_temps:
    celsius_temps.append((5/9) * (temp - 32))

print("Equivalent temperatures in Celsius: ", celsius_temps)
