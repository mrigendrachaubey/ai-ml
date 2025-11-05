# function to calcluate sum of digits
def sum_of_digits(num):
	summ = 0
	div = num
	while(div != 0):
	# use // as integer division
		div = num // 10 
		rem = num % 10
		summ = summ + rem
		num = div
	return summ

digit = int(input("Enter the number: "))
print("sum of digits: ", sum_of_digits(digit))
