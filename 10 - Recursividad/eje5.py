


def es_palindromo(palabra: str):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


print(es_palindromo("caca"))

print(es_palindromo("uruguru"))
