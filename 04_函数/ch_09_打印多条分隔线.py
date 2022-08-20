def print_line(char, times):

    print(char * times)


def print_lines(c, t):

    i = 0
    while i < 5:
        print_line(c, t)
        i += 1


print_lines("U", 20)
