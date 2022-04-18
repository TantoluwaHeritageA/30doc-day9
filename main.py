def check_if_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            return"prime number"


print(check_if_prime(int(input("enter a number: "))))
