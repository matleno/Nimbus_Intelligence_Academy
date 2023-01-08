from random import randint

def random_number_generator():
    while True:
        A = randint(1, 9)
        B = randint(1, 9)
        C = A * B
        print(A, C)
        if C == 4:
            print('Success!')
            print('A = ', A ,'| B = ', B)
            break


random_number_generator()