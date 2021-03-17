with open('file02.txt', 'r') as f:
    content = f.readlines(5)
    print(content)
    content = f.readlines(5)
    print(content)
    content = f.readlines(100)
    print(content)
