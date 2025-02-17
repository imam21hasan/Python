try:
    list = [10, 20, 0]
    rslt = list[0]/list[2]
    print(rslt)
    print("Result print successfully")
except ZeroDivisionError:
    print("Mathematical error !!!")
