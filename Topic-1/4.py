if __name__=="__main__":
    name = input("Enter the Name :")
    creator = input("Enter the Creator Name :")
    purpose = input("Enter the Purpose :")
    mem = input("Memory Space :")
    speed = input("Speed :")

    ans = f'''
My Details :
I am the Robot named {name}.
I was created by {creator}.
I am created for the purpose of {purpose}.
My memory space is around {mem}Gb and my speed is {speed} Tb.'''
    
    print(ans)


