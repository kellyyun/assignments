with open('name.txt', 'w') as f:
    my_name = f.read()


with open('output/hello.txt', 'w') as f:
    f.write('Hello, my name is ' + my_name)
    #second way-->   f.write(f'Hello, my name is {my_name}')