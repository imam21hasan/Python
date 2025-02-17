try:
    list = [10, 20, 0]
    rslt = list[0]/list[5]
    print(rslt)
    print("Result print successfully")
except IndexError:
    print("Index error !!!")
print("Exception Handling")
