#Attempt One
"""
height_in_centimetres = float(input("Height (cms): "))
if height_in_centimetres >= 0:
    inch_calculation = height_in_centimetres / 2.54190
    feet_floor_value = round(inch_calculation // 12)
    inch_value = inch_calculation - 12 * feet_floor_value
    print(str(round(height_in_centimetres)) + "cms is " + str(feet_floor_value) + "'" + str(inch_value) + '"')
else:
    print("Invalid input")
"""

centimetre_input = int(input("Height (cms): "))
if centimetre_input >= 0:
    initial_inches = centimetre_input / 2.54
    feet_value = initial_inches // 12
    remaining_feet = (initial_inches / 12) - feet_value
    inch_value = remaining_feet * 12
    print(str(round(centimetre_input)) + "cms is " + str(round(feet_value)) + "'" + str(round(inch_value)) + '"')
else:
    print("Invalid input")


