# This program is to demonstrate the usage of the decorator function 



def dec(func):
    def wrapper(**kwa):
        func(**kwa)
        for name,age in kwa.items():
            
            print(f"this is my name {name} and my age is {age} inside wrapper function .. :)")

    return wrapper

if __name__=="__main__":

    print("Inside main ..")

    @dec
    def original_func(**kwargs):
        for k,v in kwargs.items():
            print(k, v)
            print("inside original function ")

    original_func(name="vittal", age="22")
