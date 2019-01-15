def hanoi(n, i, k):
	if n == 1:
		print("Move Disk 1 From Pin {0} to {1}".format(i, k))
	else:
		tmp = 6 - i - k
		hanoi(n-1, i, tmp)
		print("Move Disk {0} From Pin {1} to {2}".format(n, i, k))
		hanoi(n-1, tmp, k)

hanoi(int(input("n=")), int(input("from (1): "), int(input("to (2): "))