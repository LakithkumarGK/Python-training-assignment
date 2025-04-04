def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)

try:

    n = int(input("Enter a number: "))
    if n <= 0:
        raise Exception("enter valid input")
    else:
        print(fact(n))
except Exception as e:
    print(f"Unexpected error:{e}")
else:
    print("No errors occurred!")
finally:
    print("Execution finished.")


