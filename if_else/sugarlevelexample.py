sugarlevel = int(input("enter your sugar level: "))

if sugarlevel < 80:
    print("your sugar level is low")
elif sugarlevel >= 80 and sugarlevel <= 100:
    print("your sugar level is normal")
elif sugarlevel > 100:
    print("your sugar level is too high")