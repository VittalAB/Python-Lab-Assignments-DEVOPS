# program to find palindrome

if __name__=="__main__":
    s = input("Enter a string\n")
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
