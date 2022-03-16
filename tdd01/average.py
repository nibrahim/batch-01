def average(n1, n2):
    "Returns average of 2 arguments"
    return (n1 + n2)/2   # Logic

def test_average():
    for i in range(1, 100):
        for j in range(1, 100):
            assert average(i, j) == (i+j)/2


def average2():
    "Reads two numbers from the user and prints their average to standard output"
    n1 = int(input("Enter the first number "))   # Input
    n2 = int(input("Enter the second number "))  # inoput
    total = n1 + n2   # logic
    avrg = total/2    # logic
    print ("The average is ", avrg)  # output


def test_average2():
    ret = average2()
    assert ret == 4.5
