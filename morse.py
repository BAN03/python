file = open("morse_code.txt", 'r')
read = file.read()
palabra = input("palabra a traducir: ")

# 36 lineas
# letter to index
index = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
    "1":27,
    "2":28,
    "3":29,
    "4":30,
    "5":31,
    "6":32,
    "7":33,
    "8":34,
    "9":35,
    "0":36,
    " ":37
}

def convertir(letra):
    x = 0
    for line in read.split('\n'):
        x += 1
        if x == index[letra]:
            print(line)

for letra in palabra:
    convertir(letra)
