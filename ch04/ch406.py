h=-9998 # height=0cm
while(h!=-9999):
    h=eval(input()) ## 身高 in cm
    if(h==-9999): break
    w=eval(input()) ## 體重 in kg

    h=h/100
    bmi=w/(h)**2

    print(f"BMI: {bmi:.2f}")
    if(bmi<18.5):
        state="under weight"
    elif(bmi<25):
        state="normal"
    elif(bmi<30):
        state="over weight"
    elif(bmi>=30):
        state="fat"
    else:
        pass

    print(f"State: {state}")
