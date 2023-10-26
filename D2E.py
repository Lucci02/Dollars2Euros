
print("US Dollar To Euro in Python")

us_dollar = float(input('Enter US Dollar Value : '))

euro = us_dollar *  0.94540 

print("$" + str(us_dollar) + " " + "US Dollar is equivalent to " + str(euro) + " " +  "European Euros" )

YON = input("Do you want to convert a number again?: (y/n)")

while YON == "y":
    us_dollar = float(input('Enter US Dollar Value : '))
    euro = us_dollar *  0.94540 
    print("$" + str(us_dollar) + " " + "US Dollar is equivalent to " + str(euro) + " " +  "European Euros" )
    YON = input("Do you want to convert a number again?: (y/n)")
    