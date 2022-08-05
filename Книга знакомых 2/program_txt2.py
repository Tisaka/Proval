from add2 import add_everything2 as ae2

def everything_program():
    with open('file.cvs', 'a') as file:
        file.write(f'{ae2()}\n')
    return
