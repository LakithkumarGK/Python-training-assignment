'''Session 1: [45]
---------------------------------------------------------------------------------------------------------
1. Create a module called strops
2. Create a function to get the span of substrings
3. Create a setup file 
4. Test in a virtual environment
    4.1 Install the module in virtual environment
    4.2 Create a program to input a string and substring. Diplay the span of the substrings'''

str1 = "mississippi"
ss = 'ss'

def getSpan(str1, ss):
    index = str1.find(ss)
    print(index)    
