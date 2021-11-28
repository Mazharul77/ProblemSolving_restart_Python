s = input("Enter any word(String): ")
l = len(s)
# rs = s[-1:-l-1:-1]
rs = s[::-1]
print(l)
print("reverse: ", rs)


#also using function
def palindrome(s):
    revS = s[::-1]
    if s==revS:
        print(s, " is palindrome")
        return 1
    else:
        print(s, " is Not Palindrome")
        return 0

pd = palindrome(s)

print("......", pd)
