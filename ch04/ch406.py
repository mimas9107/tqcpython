h=1 ## height=1cm 
w=1 ## weight=1kg 
while(h>0 or w>0):
    h=eval(input()) ## 身高 in cm
    if(h==-9999): break 
    w=eval(input()) ## 體重 in kg
    if(w==-9999): break ## 確保在 w輸入時做保險,

    h=h/100
    bmi=w/(h)**2

    print(f"BMI: {bmi:.2f}")
    if(bmi<18.5): ## 過輕
        state="under weight" 
    elif(bmi<25): ## 正常
        state="normal"
    elif(bmi<30): ## 過重
        state="over weight"
    elif(bmi>=30): ## 肥胖
        state="fat" 
    else:
        pass

    print(f"State: {state}")
