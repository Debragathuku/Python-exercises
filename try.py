try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("file not found!")
finally:
    print("clossing the file.")