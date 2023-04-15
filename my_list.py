class MyList:
    def __init__(self, *args):
        self.my_list = list(args)

    def __enter__(self):
        return self.my_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.my_list


with MyList(1, 2, 3, 4) as my_list:
    print(my_list)