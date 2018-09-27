def findpalindrome(str):
    revstr="".join(reversed(str))
    if str==revstr:
        print str," is a Palindrome!"
    else:
        print str," is not a Palindrome!"

str = raw_input("Enter the string: ").lower()
findpalindrome(str)

