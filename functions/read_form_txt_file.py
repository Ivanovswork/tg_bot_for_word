def read_file():
    with open("./data/input.txt", 'r', encoding='UTF8') as f1:
        with open("./data/output.txt", 'w', encoding='UTF8') as f2:

            string = f1.readline()
            c = 0
            while(string):
                f2.write(string)
                string = f1.readline()
                c += 1
            print(c)