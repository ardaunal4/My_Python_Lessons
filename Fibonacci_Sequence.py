# Fibonacci sequence : 1, 1, 2, 3, 5, 8, 13, 21, ...

def Fibonacci(n):
    sequence = [1,1]
    if n >= 2:
        i = 2
        while 1:
            sequence.append(sequence[i-1]+sequence[i-2])
            i = i + 1
            if i == n:
                break
        print(sequence)
    elif n == 0:
        print(sequence[0])
    elif n == 1:
        print(sequence)
    else:
        print("This is not appropriate number for the sequence!")

if __name__ == "__main__":
    sequence_level = input("Enter sequence level in integer : ")
    Fibonacci(int(sequence_level))
