def my_name(func, question):
    print('What is your name?')
    func(question)
    print('Nice to meet you!')

def whatishisname(mainname):
    print(f'My name is {mainname}.')

my_name(whatishisname, 'Slava')