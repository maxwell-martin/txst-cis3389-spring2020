# Q3

totalRainfall = 0

for i in range(1, 6):
    rainAmtInches = float(input("Enter the amount of rainfall for month " + str(i) + ": "))

    while rainAmtInches < 0:
        print("Rain amount cannot be negative. Try again.")
        rainAmtInches = float(input("Enter the amount of rainfall for month " + str(i) + ": "))

    totalRainfall += rainAmtInches

if totalRainfall < 0 or totalRainfall > 50:
    print("wrong inputs, please check.")
elif totalRainfall > 20:
    print("plenty rainfall")
elif totalRainfall >= 15 and totalRainfall <= 20:
    print("moderately high rainfall")
elif totalRainfall >= 10 and totalRainfall < 15:
    print("moderately low rainfall")
elif totalRainfall < 10:
    print("low rainfall")
