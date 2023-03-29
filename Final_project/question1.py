temperature = float(input("Enter the temperature: "))


while True:
    choice = input("Convert to Celsius C or Fahrenheit F ")
    if choice == "C":
        converted_temp = (temperature - 32) * 5 / 9
        print(f"{temperature}°F is equivalent to {converted_temp}°C")
        break
    elif choice == "F":
        converted_temp = temperature * 9 / 5 + 32
        print(f"{temperature}°C is equivalent to {converted_temp}°F")
        break
    else:
        print("Invalid input. Please enter 'C' or 'F'")




