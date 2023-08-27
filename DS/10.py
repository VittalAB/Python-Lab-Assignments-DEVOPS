# shallow vs deep copy
import copy

if __name__=="__main__":
    

    menu = '''1.Deep copy
2.Shallow copy'''

    print(menu)
    c = int(input())

    if c==1:
        # for deep copy

        n = int(input())
        m = int(input())
        m1 = []
        for i in range(n):
            t = []
            for i in range(m):
                t.append(int(input()))

            m1.append(t)
        
        print(m1)
        
        i1 = int(input())
        i2 = int(input())
        val = int(input())

        m2 = copy.deepcopy(m1)
        
        m1[i1][i2] = val
        

        print(m2)
        print(m1)
    else:
        n = int(input())
        m = int(input())
        m1 = []
        for i in range(n):
            t = []
            for i in range(m):
                t.append(int(input()))

            m1.append(t)
        
        print(m1)
        
        i1 = int(input())
        i2 = int(input())
        val = int(input())

        m2 = m1.copy()
        
        m1[i1][i2] = val
        

        print(m2)
        print(m1)
