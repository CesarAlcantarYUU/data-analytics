# Description: The script tests various numeric conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print(a, type(a))
print(a, type(b))
print(c,type(c))
print(d, type(d))

#print(int(a)) = ValueError because you cannot convert decimal string into a integer.
#print(int(b)) = 55
#print(int(c)) = ValueError because it contains text
#print(int(d)) = valueError because it contains text

print(float(a)) # = 101.1
print(float(b)) # = 55.0
# print(float(c)) = ValueError
# print(float(d)) = valueError

print(int(float(a))) # = 101

c_number = int(c[0:3])
print(c_number) # = 402

d_number = int(d[7:8])
print(d_number) # = 5

print(a.strip())
print(d.strip())