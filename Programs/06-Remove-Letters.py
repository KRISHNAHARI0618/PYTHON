import time

start_time = time.time()
import random as rnd
import string as str

str.ascii_letters


s = rnd.choice(str.ascii_letters)
print(s)
s1 = ""
for i in s:
    if i == 'i' or i == 'y':
        continue
    else:
        s1 = s1 + i

print(s1)
end_time = time.time()

execution_time  = end_time - start_time
print(f"The Time taken is  {execution_time:.8f} seconds ")

stTime = time.time()

s= "hello world sdsd,mamnsdfjanfahdsjdsfbdnsavbadsbfvdsv"
s = s.replace("i", "ppp")
print(s)

endTime = time.time()
exTime  = endTime - stTime

print(f"The Execution time {exTime:.8f} seconds")

list1 =[4,6,8,10,12,45,67,32]
def func(x):
    return x % 2 == 0
s = filter(func,list1)
print(list(s))
