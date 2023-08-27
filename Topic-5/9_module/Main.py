import operator as op


# from Minimum
if __name__=="__main__":
    menu = '''Menu
1.Arithmetic Operators
2.Comparison Operators
3.Logical Operations
4.Bitwise Operators
Enter the choice'''

    while True:
        print(menu)

        c = int(input())

        if c==1:
            a = int(input("Enter the value of a\n"))
            b = int(input("Enter the value of b\n"))
            c = int(input("Enter the value of c\n"))
            d = int(input("Enter the value of d\n"))

            ans = f'''add(a, b) : {op.add(a,b)}
sub(b, a) : {op.sub(b,a)}
mul(a, b) : {op.mul(a,b)}
floordiv(a, b) : {op.floordiv(a,b)}
floordiv(d, c) : {op.floordiv(d,c)}
truediv(a, b) : {op.truediv(a, b)}
truediv(d, c) : {op.truediv(d,c)}
mod(a, b) : {op.mod(a, b)}
pow(c, d) : {op.pow(c,d)}'''
            
            print(ans)
            
        elif c == 2:
            a = int(input("Enter the value of a\n"))
            b = int(input("Enter the value of b\n"))
            ans = f'''a = {a}
b = {b}
lt(a, b) : {op.lt(a, b)}
le(a, b) : {op.le(a,b)}
eq(a, b) : {op.eq(a, b)}
ne(a, b) : {op.ne(a, b)}
ge(a, b) : {op.ge(a, b)}
gt(a, b) : {op.gt(a, b)}'''
            print(ans)
        elif c==3:
            a = int(input("Enter the value of a\n"))
            b = int(input("Enter the value of b\n"))
            
            ans = f'''a = {a}
b = {b}
not_(a) : {op.not_(a)}
truth(a) : {op.truth(a)}
is_(a, b) : {op.is_(a, b)}
is_not(a, b) : {op.is_not(a, b)}'''
            print(ans)

        elif c == 4:
            a = int(input("Enter the value of a\n"))
            b = int(input("Enter the value of b\n"))

            ans = f'''and_(c, d) : {op.and_(a,b)}
invert(c) : {op.invert(a)}
lshift(c, d) : {op.lshift(a, b)}
or_(c, d) : {op.or_(a, b)}
rshift(d, c) : {op.rshift(b, a)}
xor(c, d) : {op.xor(a, b)}'''
            print(ans)

        else:
            print("Invalid Choice")

            exit(0)