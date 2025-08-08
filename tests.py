from functions.write_file import write_file


def test():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))


if __name__ == "__main__":
    test()
