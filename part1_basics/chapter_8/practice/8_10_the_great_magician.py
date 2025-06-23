def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]


magicians_1 = ["David Copperfield", "Harry Houdini", "Derren Brown"]
make_great(magicians_1)
show_magicians(magicians_1)
