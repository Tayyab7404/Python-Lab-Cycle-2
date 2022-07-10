def sum_of_devisors(n):
    sum=0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum

def check_amicable_numbers(n1, n2):
    if n1==sum_of_devisors(n2) and n2==sum_of_devisors(n1):
        return True
    return False

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if check_amicable_numbers(n1, n2):
    print(f"\'{n1}\' and \'{n2}\' are amicable number pair")

else:
    print(f"\'{n1}\' and \'{n2}\' are not amicable number pair")