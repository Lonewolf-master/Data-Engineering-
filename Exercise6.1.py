
# Exercise 6.1: Geometry Function
def GeometryFxn():
    print("Exercise 6.1: Geometry Function")

    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))

    def rectangle_area(length, width =0):
        print(f"Area = Length * Width: {length*width:.2f}")

    rectangle_area(length, width)

# Exercise 6.2: Temperature Converter
def TempCon():
    print("Exercise 6.2: Temperature Converter")
    unit = str(input("Enter the temperature(eg C or F): ")).upper()
    temp = float(input("Enter the unit of the temp(eg 35.93): "))

    def convert_temperature(temp, unit):
        if(temp):
            match(unit):
                case "C":
                    print("Converting to Fahrenheit,F: ")
                    return temp * (9/5) + 32
                case "F":
                    print("Converting to Celsius,C: ")
                    return (temp - 32) * (5/9)
                    
                case _:
                    return "Unknown temperature Unit please try again____"

    print(f"{unit}: {convert_temperature(temp, unit):.2f}")


# Exercise 6.3: The Global Counter
def globalCount():
    print("Exercise 6.3: The Global Counter")
    count = 0
    def update_counter(count):
        for _ in range(2):
            count += 1
    print(f"count:{count}")


GeometryFxn()
TempCon()
globalCount()