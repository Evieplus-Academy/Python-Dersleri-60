class FileManager:
    def __init__(self, file_name, mode="r"):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file_object = open(self.file_name, self.mode, encoding="utf-8")
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_object.close()


with FileManager("sample.txt") as file_object:
    text = file_object.read()
    print(text)