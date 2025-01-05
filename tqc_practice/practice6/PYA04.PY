#406
# BMI=kg/m^2
while(True):
    height=eval(input())
    if(height == -9999): break
    kg=eval(input())
    if(kg == -9999): break    
    BMI=kg/(height/100)**2
    print(f"BMI: {BMI:.2f}")
    if(BMI>=30):
        print("State: fat")
    elif(BMI<30):
        print("State: over weight")
    elif(BMI<25):
        print("State: normal")
    elif(BMI<18.5):
        print("State: under weight")
