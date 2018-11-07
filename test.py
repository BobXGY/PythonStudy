if __name__ == '__main__':
    def gen():
        i = 0
        while i < 20:
            i += 1
            yield i


    gen_obj = gen()
    while next(gen_obj):
        print(next(gen_obj))
