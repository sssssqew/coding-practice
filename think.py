#-*-coding:utf-8-*-
# def right_justify(s):
# 	s = " "*(70-len(s))+s
# 	print(s)

# right_justify("monty")
# ----------------------------------------------------
# def do_twice(f, s):
# 	f(s)
# 	f(s)

# def print_spam(s):
# 	print(s)

# def print_twice(bruce):
# 	print(bruce)
# 	print(bruce)

# def do_four(f, s):
# 	do_twice(f, s)
# 	do_twice(f, s)

# # do_twice(print_twice, 'twice')
# do_four(print_spam, 'spam')
# -----------------------------------------------------
# def print_once(s):
# 	print(s, end=' ')

# def do_once(f, s):
# 	f(s)

# def do_twice(f, s):
# 	f(s)
# 	f(s)

# def do_four(f, s):
# 	do_twice(f, s)
# 	do_twice(f, s)
	
# def draw_plus(s):
# 	do_once(print_once, '+')
# 	do_four(print_once, '-')

# def draw_poll(s):
# 	do_once(print_once, '|')
# 	do_four(print_once, ' ')

# def display_plus(s):
# 	do_four(draw_plus, '')
# 	do_once(print_once, '+')
# 	do_twice(print, '')

# def display_poll(s):
# 	do_four(draw_poll, '')
# 	do_once(print_once, '|')
# 	print()
# 	do_four(draw_poll, '')
# 	do_once(print_once, '|')
# 	print()
# 	print()

# def display():
# 	do_once(display_plus, '')
# 	do_four(display_poll, '')
# 	do_once(display_plus, '')
# 	do_four(display_poll, '')
# 	do_once(display_plus, '')
# 	do_four(display_poll, '')
# 	do_once(display_plus, '')
# 	do_four(display_poll, '')
# 	do_once(display_plus, '')

# display()
# -------------------------------------------------------
# import turtle
# import math

# bob = turtle.Turtle()

# def square(t, length):
# 	for i in range(4):
# 		t.fd(length)
# 		t.lt(90)

# def polygon(t, length, n):
# 	angle = 360/n
# 	polyline(t, length, n, angle)

# def polyline(t, length, n, angle):
# 	"""n개의 선분을 길이 length만큼, 
# 	선분 사이의 각도는 angle만큼 그린다. 
# 	"""
# 	for i in range(n):
# 		t.fd(length)
# 		t.lt(angle)	

# def circle(t, r):
# 	arc(t, r, 360)

# def arc(t, r, angle):
# 	# step_length는 3픽셀로 고정됨
# 	# 큰원이든 작은 원이든 step_length가 일정하기 때문에 
# 	# 모두 원의 형태를 유지함 
# 	# step_length가 원의 크기에 따라 변하면
# 	# 아주 큰 원인 경우에는 원처럼 보이지 않게 됨  
# 	arc_length = 2*math.pi*r*angle/360
# 	n = int(arc_length/3)+1 
# 	step_length = arc_length/n
# 	step_angle = angle / n
# 	polyline(t, step_length, n, step_angle)


# # square(bob, 50)
# # polygon(bob, 100, 6)
# # circle(bob, 50)
# arc(bob, 100, 270)
# turtle.mainloop()
# ---------------------------------------------------------
# import math
# import turtle


# def square(t, length):
#     """Draws a square with sides of the given length.

#     Returns the Turtle to the starting position and location.
#     """
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)


# def polyline(t, n, length, angle):
#     """Draws n line segments.

#     t: Turtle object
#     n: number of line segments
#     length: length of each segment
#     angle: degrees between segments
#     """
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)


# def polygon(t, n, length):
#     """Draws a polygon with n sides.

#     t: Turtle
#     n: number of sides
#     length: length of each side.
#     """
#     angle = 360.0/n
#     polyline(t, n, length, angle)


# def arc(t, r, angle):
#     """Draws an arc with the given radius and angle.

#     t: Turtle
#     r: radius
#     angle: angle subtended by the arc, in degrees
#     """
#     arc_length = 2 * math.pi * r * abs(angle) / 360
#     n = int(arc_length / 4) + 3
#     step_length = arc_length / n
#     step_angle = float(angle) / n

#     # making a slight left turn before starting reduces
#     # the error caused by the linear approximation of the arc
#     t.lt(step_angle/2)
#     polyline(t, n, step_length, step_angle)
#     t.rt(step_angle/2)


# def circle(t, r):
#     """Draws a circle with the given radius.

#     t: Turtle
#     r: radius
#     """
#     arc(t, r, 360)


# # the following condition checks whether we are
# # running as a script, in which case run the test code,
# # or being imported, in which case don't.

# if __name__ == '__main__':
#     bob = turtle.Turtle()

#     # draw a circle centered on the origin
#     radius = 100
#     bob.pu()
#     bob.fd(radius)
#     bob.lt(90)
#     bob.pd()
#     # circle(bob, radius)
#     arc(bob, radius, 270)
#     print(bob.xcor(), bob.ycor())

#     # wait for the user to close the window
#     turtle.mainloop()
# -------------------------------------------------------------------
# import math
# import turtle


# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# def polygon(t, n, length):
#     angle = 360.0/n
#     polyline(t, n, length, angle)

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * abs(angle) / 360
#     n = int(arc_length / 4) + 3
#     step_length = arc_length / n
#     step_angle = float(angle) / n

#     t.lt(step_angle/2)
#     polyline(t, n, step_length, step_angle)
#     t.rt(step_angle/2)

# def flower(t, r, angle, n):
# 	for i in range(n):
# 		arc(t, r, angle)
# 		t.lt(2*(360/n))
# 		print(2*(360/n))

# def pie(t, length, n):
# 	for i in range(n):
# 		polygon(t, 3, length)
# 		t.rt(360/n)

# bob = turtle.Turtle()
# # flower(bob, 100, 163, 7)
# pie(bob,100, 6)
# turtle.mainloop()
# ----------------------------------------------------------------------
# def print_n(s, n):
# 	if n <= 0:
# 		return
# 	print(s)
# 	print_n(s, n-1)

# def print_ham():
# 	print('sylee')

# def do_n(f, n):
# 	if n <=0:
# 		return
# 	f()
# 	do_n(f, n-1)

# # print_n("ham", 3)
# do_n(print_ham, 2)
# ----------------------------------------------------------------------
# import time

# day = 24 * 60 * 60
# days = int(time.time() // day)
# times = time.time() % day

# hours = int(times //  (60 * 60))
# times = times %  (60 * 60)

# mins = int(times // 60)
# seconds = int(times % 60)

# print("days: ",days)
# print("time {}:{}:{}".format(hours+9, mins, seconds))
# ---------------------------------------------------------------------
# def check_ferma(a, b, c, n):
# 	if n > 2 and (a**n+b**n == c**n):
# 		print("Holy smokes, Fermat was wrong!")
# 	else:
# 		print("No, that doesn’t work.")

# input = input("please type 4 values to check where true or not ferma's theorem...")
# values = input.split()
# check_ferma(int(values[0]), int(values[1]), int(values[2]), int(values[3]))
# ---------------------------------------------------------------------
# def recurse(n, s):
# 	"""Calculate the sum of 1 to n

# 	n: number range to sum up 
# 	s: total value 
# 	"""
# 	if n == 0:
# 		print(s)
# 	else:
# 		recurse(n-1, n+s)

# recurse(3, 0)
# --------------------------------------------------------------------
# import turtle

# def draw(t, length, n):
# 	if n==0:
# 		return
# 	angle = 20
# 	t.fd(length*n)
# 	t.lt(angle)
# 	draw(t, length, n-1)
# 	t.rt(2*angle)
# 	draw(t, length, n-1)
# 	t.lt(angle)
# 	t.bk(length*n)

# def Koch(t, x):
# 	if x < 3:
# 		t.fd(x)	
# 		return
# 	Koch(t, x/3)
# 	t.lt(60)
# 	Koch(t, x/3)
# 	t.rt(120)
# 	Koch(t, x/3)
# 	t.lt(60)
# 	Koch(t, x/3)

# def Koch2(t, x):
# 	if x < 4:
# 		t.fd(x)
# 		return
# 	Koch2(t, x/4)
# 	t.lt(90)
# 	Koch2(t, x/4)
# 	t.rt(90)
# 	Koch2(t, x/4)
# 	t.rt(90)
# 	Koch2(t, x/4)
# 	Koch2(t, x/4)
# 	t.lt(90)
# 	Koch2(t, x/4)
# 	t.lt(90)
# 	Koch2(t, x/4)
# 	t.rt(90)
# 	Koch2(t, x/4)

# def snowflake(t, x):
# 	for i in range(3):
# 		Koch(t, x)
# 		t.rt(360/3)

# def storm(t, x):
# 	for i in range(4):
# 		Koch2(t, x)
# 		t.rt(360/4)

# bob = turtle.Turtle()
# bob.speed(0)
# bob.pu()
# bob.bk(200)
# bob.pd()
# # draw(bob, 10, 7)
# # Koch(bob, 300)
# # snowflake(bob, 100)
# # Koch2(bob, 100)
# storm(bob, 200)

# turtle.mainloop()
# ---------------------------------------------------------------------
# def is_triangle(a, b, c):
# 	if a > b + c:
# 		print('no')
# 	elif b > a + c:
# 		print('no')
# 	elif c > a + b:
# 		print('no')
# 	else:
# 		print('yes')

# input = input("please type 3 values where or not to make triangle... ")
# values = input.split()
# is_triangle(int(values[0]), int(values[1]), int(values[2]))
# ----------------------------------------------------------------------
# def compare(x, y):
# 	if x > y:
# 		return 1
# 	elif x == y:
# 		return 0
# 	else:
# 		return -1

# input = input("type 2 values to compare...")
# values = input.split()
# re = compare(int(values[0]), int(values[1]))
# print(re)
# ----------------------------------------------------------------------
# import math

# def distance(x1, y1, x2, y2):
# 	dx = x2 - x1
# 	dy = y2 - y1
# 	dsquared = dx**2+dy**2
# 	result = math.sqrt(dsquared)
# 	return result

# print(distance(1, 2, 4, 6))
# ----------------------------------------------------------------------
# import math

# def hypotenuse(a, b):
# 	return math.sqrt(a**2+b**2)

# print(hypotenuse(3, 4))
# ----------------------------------------------------------------------
# import math

# def distance(x1, y1, x2, y2):
# 	dx = x2 - x1
# 	dy = y2 - y1
# 	dsquared = dx**2+dy**2
# 	result = math.sqrt(dsquared)
# 	return result

# def area(r):
# 	return math.pi*r**2

# def circle_area(xc, yc, xp, yp):
# 	return area(distance(xc, yc, xp, yp))

# print(circle_area(1, 2, 4, 6))
# ----------------------------------------------------------------------
# def is_divisible(x, y):
# 	return x % y == 0

# def is_between(x, y, z):
# 	return x <= y <= z

# if is_divisible(6, 3):
# 	print("6 is divisible by 3")

# if is_between(3, 4, 5):
# 	print("4 is between 3 and 5")
# ---------------------------------------------------------------------
# def fibonacci(n):
# 	if n==0:
# 		return 0
# 	elif n==1:
# 		return 1
# 	else:
# 		return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(7))
# ---------------------------------------------------------------------
# def factorial(n):
# 	if not isinstance(n, int):
# 		print('Factorial is only defined for integers.')
# 		return None
# 	elif n < 0:
# 		print('Factorial is not defined for negative integers.')
# 		return None
# 	elif n==0:
# 		return 1
# 	else:
# 		return n*factorial(n-1)

# print(factorial(3.5))
# print(factorial(-3))
# print(factorial(3))
# ---------------------------------------------------------------------
# def factorial(n):
# 	space = ' '*(2*n)
# 	print(space, 'factorial', n)
# 	if n==0:
# 		print(space, 'returning 1')
# 		return 1
# 	else:
# 		recurse = factorial(n-1)
# 		result = n*recurse
# 		print(space, 'returning', result)
# 		return result 

# factorial(4)
# --------------------------------------------------------------------
# def b(z):
# 	prod = a(z, z)
# 	print(z, prod)
# 	return prod

# def a(x, y):
# 	x = x + 1
# 	return x*y

# def c(x, y, z):
# 	total = x + y + z
# 	square = b(total)**2
# 	return square

# x = 1
# y = x + 1
# print(c(x, y+3, x+y))
# -----------------------------------------------------------------
# def ack(m, n):
# 	if m==0:
# 		return n+1
# 	elif m > 0 and n==0:
# 		return ack(m-1, 1)
# 	elif m > 0 and n > 0:
# 		return ack(m-1, ack(m, n-1))

# print(ack(3, 6))
# ----------------------------------------------------------------
# def first(s):
# 	return s[0]

# def last(s):
# 	return s[-1]

# def middle(s):
# 	return s[1:-1]

# def is_palindrome(s):
# 	"""처음과 끝 문자가 같고 중간단어도 대칭이면 True
# 		계속 처음과 끝 문자가 동일한 경우 결국 공백문자가 되므로 True
# 	"""
# 	if len(s)==0: return True
# 	return first(s)==last(s) and is_palindrome(middle(s))

# if is_palindrome('viltlie'):
# 	print("Yes, palindrome !!")
# else:
# 	print("No, It isn't")
# -----------------------------------------------------------------
# def is_power(a, b):
# 	if (a==b): return True
# 	if (b==0) or (b==1) or (a<b): return False

# 	return not (a % b) and is_power(a//b, b)

# print(is_power(0, 1))
# -----------------------------------------------------------------
# def gcd(a, b):
# 	if (b==0): return a
# 	return gcd(b, a%b)

# print(gcd(13, 6))
# -----------------------------------------------------------------
# def countdown(n):
# 	while n > 0:
# 		print(n)
# 		n = n - 1
# 	print('Blastoff!')

# countdown(3)
# -----------------------------------------------------------------
# def sequence(n):
# 	while n!=1:
# 		print(int(n))
# 		if n%2==0:
# 			n=n/2
# 		else:
# 			n=n*3+1

# sequence(3483)
# -----------------------------------------------------------------
# while True:
# 	line = input('>')
# 	if line=='done':
# 		break
# 	print(line)

# print('Done!')
# -----------------------------------------------------------------
# import math

# def mysqrt(a):
# 	epsilon = 0.000001
# 	x = 100
# 	while True:
# 		# print(x)
# 		y = (x + a/x)/2
# 		if abs(y -x)<epsilon:
# 			break
# 		x = y
# 	return y

# def test_square_root():
# 	print('a\tmysqrt(a)\t\tmath.sqrt(a)\t\tdiff')
# 	print('-\t---------\t\t------------\t\t----')
# 	for i in range(1, 10):
# 		re1 = mysqrt(i)
# 		re2 = math.sqrt(i)
# 		diff = abs(re1-re2)
# 		print('{}\t{:<20}\t{:<20}\t{}'.format(i, re1, re2, diff))

# test_square_root()
# ------------------------------------------------------------------
# def eval_loop():
# 	while True:
# 		ev = input('> ')
# 		if ev == 'done':
# 			break
# 		try:
# 			result = eval(ev)
# 		except:
# 			continue
# 		print(result)
# 	return result

# print(eval_loop())
# -------------------------------------------------------------------
# import math 

# def facto(n):
# 	if n==0:
# 		return 1
# 	return n*facto(n-1)

# def estimate_pi():
# 	"""s값이 수렴한다는 의미는 
# 		더해주는 term값이 0에 근접한다는 의미 
# 	"""
# 	k = 0
# 	s = 0
# 	c = 2*math.sqrt(2)/9801
# 	while True:
# 		num = facto(4*k)*(1103+26390*k)
# 		den = facto(k)**4*396**(4*k)
# 		term = c*(num)/(den)
# 		s += term
# 		k = k + 1
# 		if (term) < 10**(-15):
# 			break
# 	return 1/s

# print(estimate_pi())
# -----------------------------------------------------------------
# fruit = 'banana'
# index = len(fruit)-1
# while index >= 0:
# 	letter = fruit[index]
# 	print(letter)
# 	index = index - 1
# -----------------------------------------------------------------
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
# 	if letter=='O' or letter=='Q':
# 		letter += 'u'
# 	print(letter+suffix)
# -----------------------------------------------------------------
# def find(word, letter, start):
# 	index = start
# 	while index < len(word):
# 		if word[index] == letter:
# 			return index
# 		index = index + 1
# 	return -1

# print(find('banana', 'n', 3))
# -----------------------------------------------------------------
# def counter(word, ch):
# 	count = 0
# 	for letter in word:
# 		if letter == ch:
# 			count = count + 1
# 	return count 

# word = 'banana'
# print(counter(word, 'a'))
# -----------------------------------------------------------------
# def find(word, letter, start):
# 	index = start
# 	while index < len(word):
# 		if word[index] == letter:
# 			return index
# 		index = index + 1
# 	return -1

# def counter(word, letter, start):
# 	count = 0
# 	while True:
# 		index = find(word, letter, start)
# 		if index != -1:
# 			count = count + 1
# 			start = index + 1
# 		else:
# 			break
# 	return count

# word = 'banana'
# print(counter(word, 'b', 0))
# ----------------------------------------------------------------
# def in_both(word1, word2):
# 	for letter in word1:
# 		if letter in word2:
# 			print(letter)

# in_both('apples', 'oranges')
# ----------------------------------------------------------------
# word = input('> ')

# if word.lower() < 'banana':
# 	print('Your word, '+word+', comes before banana.')
# elif word.lower() > 'banana':
# 	print('Your word, '+word+', comes after banana.')
# else:
# 	print('All right, bananas.')
# ----------------------------------------------------------------
# def is_reverse(word1, word2):
# 	# guardian
# 	if len(word1) != len(word2):
# 		return False

# 	i = 0
# 	j = len(word2)-1

# 	while j > 0:
# 		if word1[i] != word2[j]:
# 			return False 
# 		i = i + 1
# 		j = j - 1

# 	return True 

# if is_reverse('banana', 'ananab'):
# 	print('Yeah, both words are the same !')
# else:
# 	print('No, two words are different...')
# ---------------------------------------------------------------
# word = 'banana'
# print(word.capitalize())
# print('Word'.casefold())
# print(word.center(len(word)+4))
# print(word.count('a'))
# print(word.encode('euc-kr'))
# print(word.endswith('na'))
# print('apple\tbanana\tjuice'. expandtabs())
# ---------------------------------------------------------------
# def is_palindrome(word):
# 	return word==word[::-1]

# print(is_palindrome('redivider'))
# ---------------------------------------------------------------
# def is_lowerfch(s):
# 	"""
# 	check if first character of given string is lowercase
# 	""" 
# 	for c in s:
# 		if c.islower():
# 			return True
# 		else:
# 			return False


# def is_lowerlch(s):
# 	"""
# 	check if last character of given string is lowercase
# 	""" 
# 	for c in s:
# 		flag = c.islower()
# 	return flag

# def is_loweranych(s):
# 	"""
# 	check if any character of given string is lowercase
# 	""" 
# 	flag = False
# 	for c in s:
# 		flag = flag or c.islower()
# 	return flag

# def is_lowerallch(s):
# 	"""
# 	check if all character of given string is lowercase
# 	""" 
# 	for c in s:
# 		if not c.islower():
# 			return False
# 	return True

# word = 'bAnanA'
# print(is_lowerfch(word))
# print(is_lowerlch(word))
# print(is_loweranych(word))
# print(is_lowerallch(word))
# ---------------------------------------------------------------------
# Caesar cipher
# def rotate_letter(ch, n, start):
# 	offset = ord(ch)-ord(start)
# 	pos = (offset + n) % 26 + ord(start)
# 	return chr(pos)

# def rotate_word(word, n):
# 	"""Rotates a word by n places.

# 	word: string
# 	n: integer

# 	Returns: string
# 	"""
# 	s = ''
# 	for ch in word:
# 		if ch.islower():
# 			s += rotate_letter(ch, n, 'a')
# 		elif ch.isupper():
# 			s += rotate_letter(ch, n, 'A')
# 		else:
# 			s += ch
# 	return s 	

# s1 = '“N zna, n cyna, n pnany: Cnanzn!”'
# s2 = '“Gur dhvpx oebja sbk whzcrq bire gur ynml qbtf.”'
# print(rotate_word('Cheer', 7))
# print(rotate_word('Melon', -10))
# print(rotate_word('HAL', 1))
# print(rotate_word(s1, -13))
# print(rotate_word(s2, -13))
# ----------------------------------------------------------------
# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	if len(word) >= 20:
# 		print(word)
# ----------------------------------------------------------------
# def has_no_e(word):
# 	return not 'e' in word

# total = 0
# cnt = 0
# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	if has_no_e(word):
# 		# print(word)
# 		cnt = cnt + 1
# 	total = total + 1

# print(cnt/total*100)
# ----------------------------------------------------------------
# def avoids(word, avs):
# 	for c in avs:
# 		if c in word:
# 			return False
# 	return True

# def counter(avs):
# 	cnt = 0
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		if avoids(word, avs):
# 			cnt = cnt + 1
# 	return cnt

# # print(cnt/total*100)
# counts = {}
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for i in alphabet:
# 	counts[i] = counter(i)

# freq = sorted(counts, key=lambda k:counts[k], reverse=True)[0:5]
# print("".join(freq))
# print(counter("".join(freq)))
# ----------------------------------------------------------------
# def uses_only(word, onlys):
# 	for ch in word:
# 		if ch not in onlys:
# 			return False 
# 	return True

# cnt = 0
# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	if uses_only(word, 'acefhlo'):
# 		print(word)
# 		cnt = cnt + 1

# print(cnt)
# print(uses_only('felao', 'acefhlo'))
# ----------------------------------------------------------------
# def uses_all(word, needs):
# 	for need in needs:
# 		if need not in word:
# 			return False
# 	return True

# cnt1 = 0
# cnt2 = 0
# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	if uses_all(word, 'aeiou'):
# 		cnt1 = cnt1 + 1
# 	if uses_all(word, 'aeiouy'):
# 		cnt2 = cnt2 + 1

# print('aeiou:',cnt1)
# print('aeiouy:',cnt2)
# ----------------------------------------------------------------
# def is_abecedarian(word):
# 	return word=="".join(sorted(word))

# def is_abecedarian(word):
# 	for i in range(len(word)-1):
# 		if word[i] > word[i+1]:
# 			return False
# 	return True

# def is_abecedarian(word):
# 	previous = word[0]
# 	for c in word:
# 		if c < previous:
# 			return False
# 		previous = c
# 	return True

# def is_abecedarian(word):
# 	if len(word) < 2:
# 		return True
# 	if word[0] > word[1:]:
# 		return False
# 	return is_abecedarian(word[1:])

# cnt = 0
# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	if is_abecedarian(word):
# 		# print(word)
# 		cnt = cnt + 1

# print("count:",cnt)
# -------------------------------------------------------------
# def is_palindrome(word):
# 	i = 0
# 	j = len(word) - 1
# 	while i < j:
# 		if word[i] != word[j]:
# 			return False
# 		i = i + 1
# 		j = j -1
# 	return True

# def is_reverse(word1, word2):
# 	if len(word1) != len(word2):
# 		return False
# 	i = 0
# 	j = len(word2)-1
# 	while j > 0:
# 		if word1[i] != word2[j]:
# 			return False
# 		i = i + 1
# 		j = j - 1
# 	return True

# def is_palindrome(word):
# 	return is_reverse(word, word)

# print(is_palindrome('allill'))
# --------------------------------------------------------------
# def is_sequence(word):
# 	if len(word) < 6:
# 		return False

# 	cnt = 0
# 	i = 0
# 	while i < len(word)-1:
# 		if word[i] == word[i+1]:
# 			cnt = cnt + 1
# 			if cnt == 3:
# 				return True
# 			i = i + 2
# 		else:
# 			cnt = 0
# 			i = i + 1

# 	return False

# # print(is_sequence('commttee'))
# # print(is_sequence('Missssppi'))

# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	if is_sequence(word):
# 		print(word)
# ------------------------------------------------------------
# def is_reverse(word1, word2):
# 	if len(word1) != len(word2):
# 		return False

# 	i = 0
# 	j = len(word2)-1
# 	while j > 0:
# 		if word1[i] != word2[j]:
# 			return False 
# 		i = i + 1
# 		j = j- 1
# 	return True 

# def is_palindrome(word):
# 	return is_reverse(word, word)

# for i in range(10**6):
# 	word = str(i).zfill(6)[-6:]
# 	if is_palindrome(word[-4:]):
# 		word = str(i+1).zfill(6)[-6:]
# 		if is_palindrome(word[-5:]):
# 			word = str(i+2).zfill(6)[-6:]
# 			if is_palindrome(word[-5:-1]):
# 				word = str(i+3).zfill(6)[-6:]
# 				if is_palindrome(word):
# 					print(str(i).zfill(6)[-6:])
# -----------------------------------------------------------
# def has_palindrome(i, start, length):
# 	s = str(i)[start:start+length]
# 	return s[::-1]==s

# def check(i):
# 	return (has_palindrome(i, 2, 4) and
# 					has_palindrome(i+1, 1, 5) and
# 					has_palindrome(i+2, 1, 4) and
# 					has_palindrome(i+3, 0, 6))

# def check_all():
# 	i = 100000
# 	while i <= 999996:
# 		if check(i):
# 			print(i)
# 		i = i + 1

# check_all()
# ----------------------------------------------------------
# classify = {}
# for i in range(100):
# 	myage = str(i).zfill(2)
# 	momage = myage[::-1] 
# 	if myage < momage:
# 		diff = int(momage)-int(myage)
# 		if diff == 18:
# 			print(myage)
# 			print(momage)
# 			print()

# 		if diff in classify:
# 			classify[diff] += 1
# 		else:
# 			classify[diff] = 1

# 57
# print(classify) 
# ---------------------------------------------------------
# def count_reverse(ageDiff):
# 	cnt = 0
# 	age = 0
# 	for i in range(100):
# 		myage = str(i).zfill(2)
# 		momage = str(i + ageDiff).zfill(2)
# 		if myage[::-1] == momage:
# 			cnt = cnt + 1
# 			if cnt == 6:
# 				age = i

# 	return cnt, age 

# for i in range(10, 60):
# 	cnt, age = count_reverse(i)
# 	if cnt == 8: 
# 		print('Current my age:',age)
# ---------------------------------------------------------
# def str_fill(i, n):
#     """Returns i as a string with at least n digits.
#     i: int
#     n: int length
#     returns: string
#     """
#     return str(i).zfill(n)


# def are_reversed(i, j):
#     """Checks if i and j are the reverse of each other.
#     i: int
#     j: int
#     returns:bool
#     """
#     return str_fill(i, 2) == str_fill(j, 2)[::-1]


# def num_instances(diff, flag=False):
#     """Counts the number of palindromic ages.
#     Returns the number of times the mother and daughter have
#     palindromic ages in their lives, given the difference in age.
#     diff: int difference in ages
#     flag: bool, if True, prints the details
#     """
#     daughter = 0
#     count = 0
#     while True:
#         mother = daughter + diff

#         # assuming that mother and daughter don't have the same birthday,
#         # they have two chances per year to have palindromic ages.
#         if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
#             count = count + 1
#             if flag:
#                 print(daughter, mother)
#         if mother > 120:
#             break
#         daughter = daughter + 1
#     return count
    

# def check_diffs():
#     """Finds age differences that satisfy the problem.
#     Enumerates the possible differences in age between mother
#     and daughter, and for each difference, counts the number of times
#     over their lives they will have ages that are the reverse of
#     each other.
#     """
#     diff = 10
#     while diff < 70:
#         n = num_instances(diff)
#         if n > 0:
#             print(diff, n)
#         diff = diff + 1

# print('diff  #instances')
# check_diffs()

# print()
# print('daughter  mother')
# num_instances(18, True)
# ---------------------------------------------------------
# for x in []:
# 	print("This never happens.")
# ---------------------------------------------------------
# 리스트 복제 
# t = [1, 2, 3]
# print(t[1:])
# t[1:] = [4, 5]
# print(t)
# t.extend([7, 8])
# print(t)
# t.sort()
# ---------------------------------------------------------
# def capitalize_all(t):
# 	res = []
# 	for s in t:
# 		res.append(s.capitalize())
# 	return res

# fruits = ['apple', 'banana', 'orange', 'pinapple', 'strawberry']
# print(capitalize_all(fruits))
# ---------------------------------------------------------
# def nested_sum(t):
# 	total = 0
# 	for item in t:
# 		total += sum(item)
# 	return total

# t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))
# ---------------------------------------------------------
# def cumsum(t):
# 	res = []
# 	total = 0
# 	for v in t:
# 		total += v
# 		res.append(total)
# 	return res

# t = [1, 2, 3]
# print(cumsum(t))
# ---------------------------------------------------------
# def middle(t):
# 	return t[1:-1]

# t = [1, 2, 3, 4]
# print(middle(t))
# ---------------------------------------------------------
# def chop(t):
# 	del t[0]
# 	del t[-1]

# t = [1, 2, 3, 4]
# chop(t)
# print(t)
# ---------------------------------------------------------
# def is_sorted(t):
# 	for i in range(len(t)-1):
# 		if t[i] > t[i+1]:
# 			return False
# 	return True 

# t = [1, 2, 2]
# print(is_sorted(t))

# t = ['b', 'c', 'a']
# print(is_sorted(t))
# ----------------------------------------------------------
# def is_anagram(s1, s2):
# 	if len(s1) != len(s2):
# 		return False

# 	s1 = sorted(s1)
# 	s2 = sorted(s2)

# 	return s1==s2

# print(is_anagram('spam', 'pams'))
# ----------------------------------------------------------
# def has_duplicates(t):
# 	t2 = t[:]
# 	t2.sort()
# 	for i in range(len(t2)-1):
# 		if t2[i]==t2[i+1]:
# 			return True
# 	return False

# t = [3, 1, 3, 5, 2, 1, 1, 6, 9, 7, 8, 10, 7, 6]
# print(has_duplicates(t))

# t = [6, 3, 2, 9, 5, 7]
# print(has_duplicates(t))
# ----------------------------------------------------------
# def has_duplicates(t):
# 	res = []
# 	for v in t:
# 		if v not in res:
# 			res.append(v)
# 		else:
# 			return True 
# 	return False 

# t = [3, 1, 3, 5, 2, 1, 1, 6, 9, 7, 8, 10, 7, 6]
# print(has_duplicates(t))

# t = [6, 3, 2, 9, 5, 7]
# print(has_duplicates(t))
# print(t)
# ---------------------------------------------------------
# import random 

# def has_duplicates(t):
# 	s = t[:]
# 	s.sort()
# 	for i in range(len(s)-1):
# 		if s[i]==s[i+1]:
# 			return True
# 	return False 

# def create_randlist(n):
# 	res = []
# 	for i in range(n):
# 		birthday = random.randint(1, 365)
# 		res.append(birthday)
# 	return res

# def counter(num_students, num_simulations):
# 	cnt = 0
# 	for i in range(num_simulations):
# 		t = create_randlist(num_students)
# 		if has_duplicates(t):
# 			cnt += 1
# 	return cnt 

# simulations = 1000
# class_nums = [1, 5, 10, 20, 23, 30, 40, 50, 60, 70, 100]
# print('students  possibility')
# for n in class_nums:
# 	cnt = counter(n, simulations)
# 	p = cnt / simulations * 100
# 	print('{:<10}{:.1f}'.format(n, p))
# -------------------------------------------------------
# import time 

# def make_wordlist1():
# 	res = []
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		res.append(word)
# 	return res 

# # 단어마다 리스트를 생성해야 되어서 오래 걸림 
# def make_wordlist2():
# 	res = []
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		res = res + [word]
# 	return res 

# def get_exectime(f):
# 	start = time.time()
# 	res = f()
# 	print(res[:10])
# 	exec_time = time.time()-start
# 	return exec_time

# print(get_exectime(make_wordlist1))
# print(get_exectime(make_wordlist2))
# -------------------------------------------------------
# import bisect 

# def in_bisect(wordlist, word):
# 	if len(wordlist)==0:
# 		return False 

# 	i = len(wordlist) // 2
# 	if wordlist[i] == word:
# 		return True

# 	if wordlist[i] > word:
# 		return in_bisect(wordlist[:i], word)
# 	else:
# 		return in_bisect(wordlist[i+1:], word)

# def in_bisect_cheat(word_list, word):
#     """Checks whether a word is in a list using bisection search.
#     Precondition: the words in the list are sorted
#     word_list: list of strings
#     word: string
#     """
#     i = bisect.bisect_left(word_list, word)
#     # 리스트 인덱스를 벗어남 
#     if i == len(word_list):
#         return False

#     return word_list[i] == word

# def create_wordlist():
# 	wordlist = []
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		wordlist.append(word)
# 	return wordlist 

# wordlist = create_wordlist()

# for word in ['aa', 'alien', 'allen', 'zymurgy']:
# 	print(word, 'in list', in_bisect(wordlist, word))

# for word in ['aa', 'alien', 'allen', 'zymurgy']:
# 	print(word, 'in list', in_bisect_cheat(wordlist, word))
# -------------------------------------------------------
# import time 

# # 이진탐색 구현 (wordlist는 알파벳 순으로 정렬되어 있어야 함)
# def search_bisec(wordlist, word):
# 	if len(wordlist) == 0:
# 		return False

# 	i = len(wordlist) // 2
# 	if wordlist[i] == word:
# 		return True 

# 	if wordlist[i] >  word:
# 		return search_bisec(wordlist[:i], word)
# 	else:
# 		return search_bisec(wordlist[i+1:], word)

# def create_wordlist():
# 	wordlist = []
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		wordlist.append(word)
# 	return wordlist 

# start = time.time()
# cnt = 0
# wordlist = create_wordlist()
# for word in wordlist:
# 	revword = word[::-1]
# 	if search_bisec(wordlist, revword):
# 		print(word, revword)
# 		cnt = cnt + 1

# exec_time = time.time()-start
# print(cnt)
# print(exec_time)
# ------------------------------------------------------
# import time 

# def make_word_list():
#     """Reads lines from a file and builds a list using append.
#     returns: list of strings
#     """
#     word_list = []
#     fin = open('words.txt')
#     for line in fin:
#         word = line.strip()
#         word_list.append(word)
#     return word_list


# def in_bisect(word_list, word):
#     """Checks whether a word is in a list using bisection search.
#     Precondition: the words in the list are sorted
#     word_list: list of strings
#     word: string
#     returns: True if the word is in the list; False otherwise
#     """
#     if len(word_list) == 0:
#         return False

#     i = len(word_list) // 2
#     if word_list[i] == word:
#         return True

#     if word_list[i] > word:
#         # search the first half
#         return in_bisect(word_list[:i], word)
#     else:
#         # search the second half
#         return in_bisect(word_list[i+1:], word)

# def reverse_pair(word_list, word):
#     """Checks whether a reversed word appears in word_list.
#     word_list: list of strings
#     word: string
#     """
#     rev_word = word[::-1]
#     return in_bisect(word_list, rev_word)
        

# if __name__ == '__main__':
# 	start = time.time()
# 	cnt = 0
# 	word_list = make_word_list()
	
# 	for word in word_list:
# 		if reverse_pair(word_list, word):
# 			print(word, word[::-1])
# 			cnt = cnt + 1

# 	exec_time = time.time()-start
# 	print(cnt)
# 	print(exec_time)
# -----------------------------------------------------------
# import time 

# # 이진탐색 구현 (wordlist는 알파벳 순으로 정렬되어 있어야 함)
# def search_bisec(wordlist, word):
# 	if len(wordlist) == 0:
# 		return False

# 	i = len(wordlist) // 2
# 	if wordlist[i] == word:
# 		return True 

# 	if wordlist[i] >  word:
# 		return search_bisec(wordlist[:i], word)
# 	else:
# 		return search_bisec(wordlist[i+1:], word)

# def create_wordlist():
# 	wordlist = []
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		wordlist.append(word)
# 	return wordlist 

# def interlock(wordlist, word):
# 	evens = word[::2]
# 	odds = word[1::2]
# 	return search_bisec(wordlist, evens) and \
# 				search_bisec(wordlist, odds)

# def interlock_general(wordlist, word, n=3):
# 	for i in range(n):
# 		if not search_bisec(wordlist, word[i::n]):
# 			return False
# 	return True 


# wordlist = create_wordlist()

# print('word1\tword2\tword')
# for word in wordlist:
# 	if interlock(wordlist, word):
# 		print('{:<8}{:<8}{:<8}'.format(word[::2], word[1::2], word))

# print('word1\tword2\tword3\tword')
# for word in wordlist:
# 	if interlock_general(wordlist, word, 3):
# 		print('{:<8}{:<8}{:<8}{:<8}'.format(word[::3], word[1::3], word[2::3], word))
# ------------------------------------------------------------
# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		if c not in d:
# 			d[c] = 1
# 		else:
# 			d[c] += 1
# 	return d 

# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		d[c] = d.get(c, 0) + 1
# 	return d

# h = histogram('brontosaurus')
# print(h)
# -----------------------------------------------------------
# def print_hist(h):
# 	for c in sorted(h):
# 		print(c, h[c])

# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		d[c] = d.get(c, 0) + 1
# 	return d

# h = histogram('brontosaurus')
# print_hist(h)
# ---------------------------------------------------------
# def reverse_lookup(d, v):
# 	for k in d:
# 		if d[k] == v:
# 			return k 
# 	raise LookupError('value does not appear in the dict...')

# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		d[c] = d.get(c, 0) + 1
# 	return d

# h = histogram('parrot')
# k = reverse_lookup(h, 2)
# print(k)
# k = reverse_lookup(h, 3)
# print(k)
# ----------------------------------------------------------
# def invert_dict(d):
# 	inverse = dict()
# 	for key in d:
# 		val = d[key]
# 		if val not in inverse:
# 			inverse[val] = [key]
# 		else:
# 			inverse[val].append(key)
# 	return inverse

# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		d[c] = d.get(c, 0) + 1
# 	return d

# hist = histogram('parrot')
# print(hist)
# inverse = invert_dict(hist)
# print(inverse)
# ---------------------------------------------------------
# # 메모화 (memo) 
# # 이미 계산한 값을 사전에 저장해 두었다가 나중에 재활용함 
# import time 

# # 가장 성능이 좋음 
# def fibonacci0(n):
# 	a, b = 0, 1
# 	for i in range(n):
# 		a, b = b, a+b
# 	return a

# # cach 사용과 유사함 
# def fibonacci1(n):
# 	if n in known:
# 		return known[n]
# 	res = fibonacci1(n-1)+fibonacci1(n-2)
# 	known[n] = res
# 	return res

# def fibonacci2(n):
# 	if n<=1:
# 		return n
# 	res = fibonacci2(n-1)+fibonacci2(n-2)
# 	return res 

# print('-'*40)
# start = time.time()
# res = fibonacci0(40)
# exec_time = time.time()-start
# print(res)
# print('fibonacci 0:{:.10f}'.format(exec_time))

# print('-'*40)
# known = {0:0, 1:1}
# start = time.time()
# res = fibonacci1(40)
# exec_time = time.time()-start
# print(res)
# print('fibonacci 1:{:.10f}'.format(exec_time))

# print('-'*40)
# start = time.time()
# res = fibonacci2(40)
# exec_time = time.time()-start
# print(res)
# print('fibonacci 2:{:.10f}'.format(exec_time))
# -------------------------------------------------------------------
# 가장 성능이 좋은 피보나치 수열 
# import time 

# def mult(x, y):
# 	"""
# 	행렬에 대한 곱셈 함수 
# 	x, y = list형태의 매트릭스 
# 	"""
# 	if(len(y)==2):
# 		a = x[0]*y[0]+x[1]*y[1]
# 		b = x[2]*y[0]+x[3]*y[1]
# 		return [a, b]
# 	a = x[0]*y[0]+x[1]*y[2]
# 	b = x[0]*y[1]+x[1]*y[3]
# 	c = x[2]*y[0]+x[3]*y[2]
# 	d = x[2]*y[1]+x[3]*y[3]
# 	return [a, b, c, d]

# def matrix_power(x, n):
# 	"""
# 	행렬 지수 함수
# 	"""
# 	if(n==1):
# 		return x
# 	if(n%2==0):
# 		return matrix_power(mult(x,x), n//2)
# 	return mult(x, matrix_power(mult(x,x), n//2))

# A = [1, 1, 1, 0]
# v = [1, 0]

# def fibonacci_best(n):
# 	return mult(matrix_power(A, n-1), v)[0]

# start = time.time()
# print(fibonacci_best(40))
# exec_time = time.time()-start
# print('fibonacci_best:{:.10f}'.format(exec_time))
# ----------------------------------------------------------
# import pprint 

# def word_dict():
# 	dictionary = dict()
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		if word not in dictionary:
# 			dictionary[word] = 0
# 		dictionary[word] += 1
# 	return dictionary

# print('-'*50)
# pprint.pprint(word_dict(), width=20, indent=4)
# -----------------------------------------------------------
# setdefault 
# 키가 없으면 default 값 리턴 
# 키가 있으면 값을 리턴 
# def invert_dict(d):
# 	inverse = dict()
# 	for key in d:
# 		val = d[key]
# 		v_list = inverse.setdefault(val, list())
# 		v_list.append(key)
# 	return inverse

# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		d[c] = d.get(c, 0) + 1
# 	return d

# hist = histogram('parrot')
# print(hist)
# inverse = invert_dict(hist)
# print(inverse)
# ----------------------------------------------------------
# 아커만 메모화 버전 
# def int2str(m, n):
# 	return str(m)+str(n)

# def ack(m, n):
# 	key = int2str(m, n)
# 	if key in known:
# 		return known[key]
# 	if m==0:
# 		known[key] = n+1
# 	if m > 0 and n==0:
# 		known[key] = ack(m-1, 1)
# 	if m > 0 and n > 0:
# 		known[key] = ack(m-1, ack(m, n-1))
# 	return known[key]

# known = dict()
# print(ack(3, 4))
# ---------------------------------------------------------
# def has_duplicates(t):
# 	d = dict()
# 	for item in t:
# 		if item in d:
# 			return True 
# 		d[item] = 0
# 	return False 

# t = [1, 2, 3]
# print(has_duplicates(t))
# t.append(1)
# print(has_duplicates(t))
# --------------------------------------------------------
# import pprint 
# import time 

# # 검색시 사전을 사용하면 해시함수 때문에 빠름 
# # 그러므로 항목이 늘어나도 속도는 동일함 

# def rotate_char(c, n):
# 	if c.isupper():
# 		offset = ord('A')
# 	elif c.islower():
# 		offset = ord('a')
# 	else:
# 		return c 

# 	code = ord(c)-offset
# 	code = (code + n) % 26 + offset
# 	return chr(code)

# def rotate_word(word, n):
# 	s = ''
# 	for c in word:
# 		s += rotate_char(c, n)
# 	return s

# def find_rotates(wordlist, word):
# 	cnt = 0
# 	pairs = dict()
# 	pairs[word] = []
	
# 	for i in range(1, 26):
# 		rot_word = rotate_word(word, i)
# 		if rot_word in wordlist:
# 			pairs[word].append(rot_word)
# 			cnt = cnt + 1

# 	if cnt > 0:
# 		print('cnt:', cnt) 
# 		pprint.pprint(pairs, width=20, indent=2)
# 		print('-'*30)

# def get_wordlist():
# 	d = dict()
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip().lower()
# 		d[word] = None
# 	return d 

# start = time.time()
# wordlist = get_wordlist()
# for word in wordlist:
# 	find_rotates(wordlist, word)
# exec_time = time.time()-start 
# print('execution time:{:.10f} s'.format(exec_time))
# ----------------------------------------------------------

