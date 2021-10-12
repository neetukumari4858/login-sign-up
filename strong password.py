password=input("enter password:-")
cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklmnopqrstuvwxtz"
no="0123456789"
sc="@#$%&*!"
m=0
n=0
t=0
p=0
if len(password)>=8:
    for i in range(len(password)):
        
        if password[i] in cap:
            m=1
        elif password[i] in small:
            n=1
        elif password[i] in no:
            t=1
        elif password[i] in sc:
            p=1
        total=m+n+t+p
    if total==4:
        print("strong password")
    else:
        print("use one cap,samll letter no and specail chr ")
else:
    print("password is too shot")


