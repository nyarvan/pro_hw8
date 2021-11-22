import os.path

def writter_str(cl):
    def wrapped(*args):
        if os.path.isfile(f"{cl.name.lower()}.txt"):
            name = cl.name.lower()
            file = open(f"{name}.txt", "a")
            file.write(cl(*args).__str__())
            file.close()
            return 1
        else:
            return None
    return wrapped

@writter_str
class Text:
    name = "Text"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Сумма чисел {self.a} и {self.b} равна {self.a + self.b}\n"