from contextlib import contextmanager


class Open_file():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_file('sample.txt', 'w') as f:
    f.write('Testing')


print(f.closed)



@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample1.txt', 'w') as f:
    f.write('My name is Saroj Shrestha.')

print(f.closed)