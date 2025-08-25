
# exceptions : Value Error , Type Error , IndexOutofBound Error
#    try - except - finally

try:
    print(5/0)
    print(int("Python"))
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception as e:
    print(e)
finally:
    print("Job Done!")
