try:
    n=int(input("Enter numerator : "))
    m=int(input("Enter denomenator : "))
    print(n/m)
except (ValueError,ZeroDivisionError):
    print("Denominator should not be zero, string should not entered")