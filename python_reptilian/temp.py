def main():
    string = '123123asdasd'
    boolean = True
    number = 345

    def inner():
        if not boolean:
            boolean = False
            print(string, boolean, number)

    inner()
