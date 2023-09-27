
codes = {'A': '%', 'a': 9, 'B': '@', 'b': '#', "C": 1, "d": 3, "D": "$", "E": 5, "e": "^",  "f": "&",  "g": "*",  "h": "_", "I": "()", "i": "+",  "k": ",",  "l": ">",
         "m": "|", "n": "/", "O": "=", "o": ";",  "p": "[]", "R": "`", "r": 4, "S": 8, "s": 0, "T": ":", "t": "?", "U": "{}", "u": "<", "V": ".", "v": "-", "w": 7,
         "x": 6, "y": 2, "z": "~"}


info_security = open("info_security.txt", "r")
encrypted_text = open("encrypted_text", "w")

for word in info_security:
    for letter in word:
        if letter in codes:
            encrypt = codes[letter]
            encrypted_text.write(f"{encrypt}")  # what about periods?
        else:
            encrypted_text.write(f"{letter}")


info_security.close()
encrypted_text.close()
