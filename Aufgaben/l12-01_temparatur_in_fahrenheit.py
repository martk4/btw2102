def to_fahrenheit(celcius):
    return(celcius * 1.8 + 32)



f_values = [14.0, 21.2, 28.4, 35.6, 42.8, 50.0, 57.2, 64.4]
for i in range(-10, 20, 4):
    assert to_fahrenheit(i) == f_values[int((i+10)/4)], str(i) + \
        "°C was wrongly calculated to °F!"
print('\nYour function works flawlessly.\n')