def sub(a, b):
    print(a-b)

def smart_sub(func):

    def swap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return swap

sub = smart_sub(sub)

sub(2, 4)