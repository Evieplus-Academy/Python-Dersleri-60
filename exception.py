class SampleClass:
    def __init__(self, sample_data):
        print("__init__ çalıştı")
        self.sample_data = sample_data

    def __enter__(self):
        print("__enter__ çalıştı")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is ValueError:
            print("ValueError exception catched.", exc_value, traceback)
            return True
        print("__exit__ çalıştı")

    def print_sample_data(self):
        print(self.sample_data)


with SampleClass("Merhaba") as my_sample_class:
    my_sample_class.print_sample_data()
    raise ValueError("Örnek Hata")

print("Programın sonu")