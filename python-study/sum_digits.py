digit = int(input("Enter the digit "))
num = digit
summ = 0
div = num
while(div != 0):
# use // as integer division
	div = num // 10 
	rem = num % 10
	summ = summ + rem
	num = div

print("Sum ", summ)
