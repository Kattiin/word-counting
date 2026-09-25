def tokenize(lines):
    tokens = []  # Lista som lagrar alla tokens

    for line in lines:  # Loopa igenom varje textrad
        current_word = ""
        current_type = ""

        for char in line:  # Loopa igenom varje tecken i raden

            if char.isalpha():
                # Om vi tidigare byggde ett tal, spara talet
                if current_type == "digit":
                    tokens.append(current_word)
                    current_word = ""

                current_word += char.lower()
                current_type = "alpha"

            elif char.isdigit():
                # Om vi tidigare byggde ett ord, spara ordet
                if current_type == "alpha":
                    tokens.append(current_word)
                    current_word = ""

                current_word += char
                current_type = "digit"

            else:
                # Om ett ord eller tal har byggts upp, spara det
                if current_word != "":
                    tokens.append(current_word)
                    current_word = ""
                    current_type = ""

                # Skiljetecken blir egna tokens
                if not char.isspace():
                    tokens.append(char)

        # Lägg till sista ordet/talet på raden
        if current_word != "":
            tokens.append(current_word)

    return tokens