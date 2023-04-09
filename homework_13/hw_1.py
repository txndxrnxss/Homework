def gen_func(file_path: str, letter: str):
    with open(file_path, mode = 'r') as file:
        for line in file:
            if line.startswith(letter):
                yield line

my_gen = gen_func('unsorted_names.txt', 'A')
for name in my_gen:
    print(name, end="")