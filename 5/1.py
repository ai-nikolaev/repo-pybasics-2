with open("with_abc.txt") as in_file:
    with open("without_abc.txt", "w") as out_file:
        for in_line in in_file:
            out_file.write(in_line.replace("abc", ""))
