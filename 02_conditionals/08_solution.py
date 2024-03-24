password = "212ddsdg"


if len(password) < 6:
    critia = "weak"
elif len(password) < 10:
    critia = "Medium"
elif len(password) > 10:
    critia = "Strong"

print(critia)

