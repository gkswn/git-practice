def do_fizzbuzz():
    """
    fizzbuzz: print fizz buzz fizzbuzz
    3: fizz
    5: buzz
    15: fizzbuzz
    etc: num
    """
    for i in range(1,num+1):
        if i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        else:
            print(f'{i}')

    print('hello')


if __name__=='__main__':
    do_fizzbuzz(16)
