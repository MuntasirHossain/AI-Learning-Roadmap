def fibo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)


if __name__ == "__main__":
    n1 = input("Please enter your number: ")
    n1 = int(n1)
    print("The fibonacci sum is: ", fibo(n1))
