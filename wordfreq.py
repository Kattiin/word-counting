# FIXA SÅ ATT INTE +=

def tokenize(lines):
    words = []  # Lista som lagrar alla tokens

    for line in lines:  # Loopa igenom varje textrad
        current_word = ""
        current_type = ""

        for char in line:  # Loopa igenom varje tecken i raden

            if char.isalpha():
                # Om vi tidigare byggde ett tal, spara talet
                if current_type == "digit":
                    words.append(current_word)
                    current_word = ""

                current_word += char.lower()
                current_type = "alpha"

            elif char.isdigit():
                # Om vi tidigare byggde ett ord, spara ordet
                if current_type == "alpha":
                    words.append(current_word)
                    current_word = ""

                current_word += char
                current_type = "digit"

            else:
                # Om ett ord eller tal har byggts upp, spara det
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
                    current_type = ""

                # Skiljetecken blir egna tokens
                if not char.isspace():
                    words.append(char)

        # Lägg till sista ordet/talet på raden
        if current_word != "":
            words.append(current_word)

    return words

def countWords(words, stopwords): 
    frequencies = {} # Skapa en dictionary för att lagra vilka ord samt hur många gånger de förekommer

    for word in words: # Loopar igenom alla ord 
        if word not in stopwords: # Om ordet inte finns i stopwords, räkna med det 

            if word in frequencies: # Om ordet redan förekommit, öka antal gånger det förekommit
                frequencies[word] += 1
            else: # Om ordet inte förekommit, lägg till det i dictionariyt med antal 1
                frequencies[word] = 1

    return frequencies # Returnera dictionaryt med räknade ord

def printTopMost(frequencies, n):
    pass