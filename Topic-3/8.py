# String util

if __name__=="__main__":
    s1 = input()
    s2 = input()
    
    print(f'The length of the first string is {len(s1)}')
    print(f'The length of the second string is {len(s2)}')
    print(f'The reverse of the first string is {s1[::-1]}')
    print(f'The reverse of the second string is {s2[::-1]}')
    print(f'The concatenated string is {s1+s2}')

    if s1<s2:
        print(f"{s1} appears before {s2}")
    elif s1>s2:
        print(f"{s2} appears before {s1}")
    else:
        print(f"Both input strings are the same")
