filename = '../alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        # 二是给参数encoding指定了值，在系统的默认编码与要读取文件使用的编码不一致时，必须这样做
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()  # 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
