def tokenize(filename):
    tokens = []

    with open(filename, "r") as file: # Öppna filen för läsning 

        for line in file: # Loopa igenom varje rad i filen
            currentword = "" # Skapa en variabel för det nuvarande ordet

            for char in line: # Loopar igenom varje tecken i ordet
                if char.isalpha() or char.isdigit(): # Om tecknet är en bokstav eller siffra, lägg till karaktären i currentword
                    currentword += char

                else:
                    if currentword != "": # Om nuvarande tecknet 
                        tokens.append(currentword)
                        currentword = ""

                    if not char.isspace():
                        tokens.append(char)

            if currentword != "":
                tokens.append(currentword)

    return tokens


print(tokenize("examples/article1.txt"))