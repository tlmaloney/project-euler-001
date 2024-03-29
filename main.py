'''

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

@author: Thomas Maloney
'''

sum = 0
for i in xrange(1,1000):
    if i % 15 == 0:
        sum = sum + i
    else:
        if i % 3 == 0:
            sum = sum + i

        if i % 5 == 0:
            sum = sum + i

print sum
