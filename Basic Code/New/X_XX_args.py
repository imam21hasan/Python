def xFun(*args):    # x argument
    print(args)
    # print(args[0])

xFun(10)
xFun(20, 30)
xFun(40, "Python", 50)
print("\n")


def xFun2(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

xFun2(10)
xFun2(20, 30)
xFun2(40, 50, 60)
print("\n")


def info(**args):   # xx argument
    print(args)
    print(args["name"])
    print(args["num"])

info(name="Python",num=28)
info(name="SHAWON",num=21,val=2003)