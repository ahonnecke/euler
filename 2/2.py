# coding: utf-8

total = 0
upper = 4000000
#upper = 100
num = 1
last = 1
laster = 0

while (num < upper):
    laster = last
    last = num
    num = laster + last
    #this print makes fibonacci numbers
    #print num
    if(num <= upper and num % 2 == 0):
        total += num
#        print num

print(total);

#✔ 11:24 ~/Code/euler [master|✚ 2…4] $ python 2.py
#4613732
