def prime(n):
    if n <= 0:
        return False
    for i in range ( 2, n):
        if n % i == 0:
            return False
    return True
print(("True") if prime( 11) else print("False"))