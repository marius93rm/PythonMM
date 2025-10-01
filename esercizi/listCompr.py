# 1. Lista dei quadrati da 0 a 9
squares = [x**2 for x in range(10)]

# 2. Numeri pari da 0 a 20
evens = [x for x in range(21) if x % 2 == 0]

# 3. Lunghezze delle parole
words = ["ciao", "python", "studenti"]
lengths = [len(w) for w in words]

# 4. Caratteri maiuscoli in una stringa
text = "PyThOn"
upper_chars = [c for c in text if c.isupper()]

# 5. Prima lettera di ogni parola
first_letters = [w[0] for w in words]

# 6. Coppie (x, y) per una tabella 3x3
pairs = [(x, y) for x in range(3) for y in range(3)]

# 7. Lista piatta da lista di liste
matrix = [[1,2,3], [4,5,6]]
flat = [num for row in matrix for num in row]

# 8. Numeri divisibili per 3 e 5 fino a 50
div_3_5 = [x for x in range(51) if x % 3 == 0 and x % 5 == 0]

# 9. Stringhe con "!" aggiunto
shouts = [w + "!" for w in words]

# 10. Dizionario invertito → lista di tuple (valore, chiave)
d = {"a": 1, "b": 2, "c": 3}
inv = [(v, k) for k, v in d.items()]
