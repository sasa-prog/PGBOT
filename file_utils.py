def read_token():
    bottoken = ""
    with open("Token.0","r",encoding="utf-8") as f:
        bottoken = f.read()

    return bottoken

def read_colors():
    lines = []
    with open("Colors.0","r",encoding="utf-8") as color_file:
        lines = color_file.readLines()
        for line in lines:
            line = line.rstrip("\n")
            if line != "":
                colors.append(line)
    return lines
