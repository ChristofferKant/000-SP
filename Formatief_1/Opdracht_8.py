def compressie(file):
    infile = open(file)
    content = infile.read()
    infile.close()
    text_no_spaces = content.strip(" ")
    text_no_whitespace = text_no_spaces.replace("\n", "")
    compression = text_no_whitespace.replace("\t", "")
    words = compression.rstrip(" ")
    outfile = open('compressed.txt', 'w')
    outfile.write(words)
    outfile.close()

compressie("textfile.txt")