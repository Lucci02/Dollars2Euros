print("Dollars To Euro in Python")

dolr = float(input('Enter Dollar Value : '))

euros = dolr * 0.94540 

print("$" + str(dolr) + " " + "US Dollar is equivalent to " + str(euros) + " " +  "European Euros" )

yesono = input("Do you want to convert a number again?: (y/n)")

while yesono == "y":
    dolr = float(input('Enter US Dollar Value : '))
    euro = dolr *  0.94540 
    print("$" + str(dolr) + " " + "US Dollar is equivalent to " + str(euros) + " " +  "European Euros" )
    yesono = input("Do you want to convert a number again?: (y/n)")
    
    
