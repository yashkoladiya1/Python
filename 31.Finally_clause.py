def func1():
    try:
        l = [1,2,3,4]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("some Error")
        return 0
    finally:
        print("I am always executed")

x = func1()