# a = 0
# for i in range(19):
# print '2X'+ '' + '=' + ''

# for a in range(2, 10):
# 	for b in range(1, 10):
# 		print str(a) + "x" + str(b) + "=" + str(a*b)



# a= ""
# for i in range(5):
# 	a += "*"
# 	print a

# for i in range(1,6):
# 	print '*'*i




# s1 = 0
# s2 = 0
# for i in range(1, 101):
# 	s1 += i ** 2
# 	s2 += i
# s2 = s2 ** 2

# print abs(s2 - s1)



# def gcd(m, n):
# 	while n !=0:
# 		t=m%n
# 		(m, n) = (n, t)
# 	return abs(m)

# def lcm(m, n):
# 	g = gcd(m, n)
# 	return n * m / g

# numbers = range(1, 21)
# for i in range(1, 20):
# 	numbers[i] = lcm(numbers[i-1], numbers[i])
# print numbers[19]

# a = 0
# i = 1
# while 3 * i < 1000:
# 	a = a + i*3
# 	i = i + 1

# b = 0
# i = 1
# while 5 * i < 1000:
# 	b = b + i*5
# 	i = i + 1

# c = 0
# i = 1
# while 15 * i < 1000:
# 	c = c + i*15
# 	i = i + 1

# print a + b - c

# s = 0
# for i in range(1, 1000):
# 	if i % 3 == 0 or i % 5 == 0:
# 		s += i
# print s

# l = [1, 2]
# while True:
# 	l.append(l[len(l)-1]+l[len(l)-2])
# 	if l[len(l)-1] > 4000000:
# 		break
# s = 0
# for i in l:
# 	if i % 2 ==0:
# 		s = s + i

# print s


# fib_dict = {1: 1, 2: 2}
# def fib(n):
# 	if n in fib_dict:
# 		return fib_dict[n]
# 	else:
# 		fib_dict[n] = fib(n-2) + fib(n-1)
# 	    return fib_dict[n]




