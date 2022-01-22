import sys

f = int(sys.stdin.readline())
for _ in range(f):
	n = int(sys.stdin.readline())
	number = [sys.stdin.readline().strip() for _ in range(n)]
	number.sort()
	say_yes = True
	for i in range(1, n):
		if number[i].startswith(number[i-1]):
			say_yes = False
			break
	if say_yes: print("YES")
	else: print("NO")