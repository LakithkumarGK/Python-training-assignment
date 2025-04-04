

def getSpan(str1, ss):

    if ss == '':
        raise Exception("substring cannot be empty")
    else:
        spans = []
        start = 0
        while start < len(str1):
            index = str1.find(ss, start)
        
            if index == -1:
                break

            spans.append((index, index + len(ss) - 1))
            start = index + 1
        return spans

try:
    str1 = input("String:")
    ss = input("Substr:")

    getSpan(str1,ss)
    
except Exception as v:
    print(f"Unexpected error:{v}")
else:
    print("No errors occurred!")
finally:
    print("Execution finished.")
