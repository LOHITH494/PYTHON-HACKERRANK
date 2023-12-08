def mutate_string(string, position, character):
    cl = list(string)
    cl[position]=character
    string=''.join(cl)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
