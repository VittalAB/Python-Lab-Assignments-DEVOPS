# Match blood group

if __name__=="__main__":
    details = {}

    n = int(input("Enter the no donors available\n"))

    for i in range(n):
        print(f"Enter the details of donor {i+1}")

        name = input()
        email = input()
        phone = input()
        grp = input()

        details[phone] = [name, email, grp]

    req = input("Enter the required blood group\n")
    matched = 0

    for k,v in details.items():
        if req in v:
            print("Details of matched donor")
            matched = 1
            print(v[0])
            print(v[1])
            print(k)
            print(v[2])
    else:
        if not matched:
            print("No donor with required blood group")
           
    
