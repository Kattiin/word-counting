def tokenize(filename):
    tokens = []  # Lista som lagrar alla tokens

    with open(filename, "r") as file:  # Öppna filen för läsning

        for line in file:  # Loopa igenom varje rad i filen

            current_word = ""  # Skapa en variabel för ordet som byggs upp

            for char in line:  # Loopa igenom varje tecken i raden

                if char.isalpha() or char.isdigit():
                    # Om tecknet är en bokstav eller siffra läggs det till i current_word
                    current_word += char.lower()

                else:
                    if current_word != "":
                        # Om ett ord har byggts upp läggs det till i tokens
                        tokens.append(current_word)

                        current_word = ""  # Nollställer current_word

                    if not char.isspace():
                        # Om tecknet inte är ett mellanslag läggs det till som en egen token
                        tokens.append(char)

            if current_word != "":
                # Lägg till sista ordet på raden om det fortfarande finns ett ord kvar
                tokens.append(current_word)

    return tokens  # Returnera listan med alla tokens


print(tokenize("examples/article1.txt"))