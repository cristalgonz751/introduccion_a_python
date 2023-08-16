def multisuma(num1,num2):
    acu=0
    if abs(num1)<abs(num2):
        acu=num1
        num1=num2
        num2=acu
        acu=0
    if num1<0:
        num1neg=-1
        num1*=-1
    else:num1neg=1
    if num2<0:
        num2neg=-1
        num2*=-1
    else:num2neg=1
    for elemento in range (1,num2+1,1):
        acu=num1+acu
    return acu*num1neg*num2neg
print(multisuma(1,1))
print(multisuma(1,-100))
print(multisuma(-21,2))
print(multisuma(100,5))
        
        
