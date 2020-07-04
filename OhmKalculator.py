import sys
print(sys.version)
print(" ")

print("Enter the values ​​you want to calculate. Set a value to 0 if you do not want to calculate it.")

V = 0
I = 0
R = 0

def V1():
    global V
    V = 0
    I = 0
    R = 0
    try:
        print(" ")
        V = float(input("Specify the Voltage: "))
        I1()
    except:
        print("You entered an invalid symbol. Use only numbers.")
        print(" ")
        V1()
        
def I1():
    global I
    try:
        I = float(input("Specify the Amperage: "))
        R1()
    except:
        print("You entered an invalid symbol. Use only numbers.")
        print(" ")
        I1()
        
def R1():
    global R
    try:
        R = int(input("Specify the Resistance: "))
    except:
        print("You entered an invalid symbol. Use only numbers.")
        print(" ")
        R1()
    pass
        
def again():
    print(" ")
    try:
        again1 = str(input("Do you want to calculate another set of y / n? "))
    except:
        print("You entered an invalid symbol. Use only numbers y or n.")
        print(" ")
        again()
    again1 = again1.lower()
    if again1 == "y":
        pass
        
    else:
        print("Exits...")
        exit()


while True:
    
    V1()
   
    if V > 0 and I > 0:
        print(" ")
        print("You specified {} Volt and {} Amp; Calculates the Resistance...".format(V, I))
        print(" ")
        R = int(V / I)
        print("{} Volt / {} Amp = {} Ohm".format(V, I, R))
        W = I*V
        print("Which results in {} Watt.".format(W))
        again()
        
    elif V > 0 and R > 0:
        print(" ")
        print("You specified {} Volt and {} Ohm; Calculating Current ...".format(V, R))
        print(" ")
        I = round(V / R, 2)
        if I > 1:
            print("{} Volt / {} Ohm = {} Amp".format(V, R, I))
        else:
            I1 = I * 100
            print("{} Volt / {} Ohm = {} MilliAmp".format(V, R, I1))
        W = I*V
        print(" ")
        print("Which results in {} Watt.".format(W))
        again()
        
    elif I > 0 and R > 0:
        print(" ")
        print("You specified {} Amp and {} Ohms; Calculating Voltage ...".format(I, R))
        print(" ")
        V = round(I * R, 2)
        if V > 1:
            print("{} Amp * {} Ohm = {} Volt".format(I, R, V))
        else:
            V = V * 100
            print("{} Amp * {} Ohm = {} MilliVolt".format(I, R, V))
        W = I * V
        print(" ")
        print("Which results in {} Watt.".format(W))
        again()

    else:
        print(" ")
        print("You did not enter enough values ​​to complete the equation. Enter two or more values.")
        V1()
        print(" ")