class Stall:
    
    def __init__(self, name=None, detail=None):
        self.__name = name
        self.__detail = detail


    def set_name(self, name : str):
        self.__name = name
    
    def set_detail(self, detail : str):
        self.__detail = detail
    
    def get_name(self) -> str:
        return self.__name
    
    def get_detail(self) -> str:
        return self.__detail

 
    def __str__(self) -> str:
        ans = f'''Details of the stall category:
Book Name : {self.__name}
Detail : {self.__detail}'''
        return ans
    


if __name__=="__main__":
    print("Enter book name")
    name = input()

    print("Enter book details")
    detail = input()

    print("Menu")
    print("1.Use Constructor to initialize")
    print("2.Use setters and getters")

    c = int(input())

    if c==1:
        print("Initializing and printing using parameterized Constructor and Str method")

        s = Stall(name, detail)
        print(s)

    else:
        print("Initializing and printing using default Constructor and Setters and Getters")

        s = Stall()
        s.set_name(name)
        s.set_detail(detail)
        ans = f'''Details of the stall category:
Book Name : {s.get_name()}
Detail : {s.get_detail()}'''
        

        print(ans)

