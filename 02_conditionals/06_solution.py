distance = 3

if distance < 3:
    transportation = "Walk"
elif distance < 15:
    transportation = "Bike"
elif distance > 15:
    transportation = "Car"

print(transportation)