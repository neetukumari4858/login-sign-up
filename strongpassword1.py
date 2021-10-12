pas=input("enter pass:-")
u,l,d,s=0,0,0,0
if len(pas)>=8:
    for check in pas:
        if (check.isupper()):
            u=1
        if (check.isdigit()):
            d=1
        if (check.islower()):
            l=1
        if(check=='@'or check=='$' or check=='_' or check=='#'):
            s=1
    total=u+d+l+s   
       
    if total==4:
        print("strong pass")

    else:
        print("use one cap,samll letter no and specail chr ")
else:
    print("pas is too short")