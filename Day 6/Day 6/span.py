
def getSpan(str1, ss):
    spans = []
    start = 0
    while start < len(str1):
        index = str1.find(ss, start)
        
        if index == -1:
            break

        spans.append((index, index + len(ss) - 1))
        start = index + 1
    return start, spans
 
if __name__ == "__main__":
    str1 = input("enter the string\n")
    substr = input("enter the sub_string\n")
    getSpan(str1, substr) 
