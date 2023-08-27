from sum import primeSum

a = int(input())
b = int(input())

s = None
for i in range(b):
    if i==0:
        s = sum(primeSum(a))
    else:
        s = sum(primeSum(int(s)))

print(f"Sum:{s}")