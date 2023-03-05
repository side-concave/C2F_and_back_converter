def F_to_C(F):
    C = 5/9*(F - 32)
    return C

def C_to_F(C):
    F = (9/5)*C + 32
    return F

choice = int(input('Do you want to convert C to F [1] or F to C [2]?\n'))

if choice == 1:
    C = float(input('What is the temperature in Celcius?\n'))
    print('It is now '+str(C_to_F(C))+' degrees Farenheit.')

elif choice == 2:
    F = float(input('What is the temperature in Farenheit?\n'))
    print('It is now '+str(F_to_C(F))+' degrees Celcius.')