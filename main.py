def retry(num=1):
    def decor(func):
        def inner(*args, **kwargs):
            print("Start")
            for i in range(num):
                try:
                    func()
                    break
                except Exception as e:
                    print(e)
                print("Finish")
        return inner
    return decor


@retry(10)
def fd():
    for i in range(10):
        print(i/0)


fd()
