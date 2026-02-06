def torre(li, ci, lf, cf):
    return li == lf or ci == cf


def bispo(li, ci, lf, cf):
    return abs(li - lf) == abs(ci - cf)


def rainha(li, ci, lf, cf):
    return torre(li, ci, lf, cf) or bispo(li, ci, lf, cf)


def cavalo(li, ci, lf, cf):
    return (abs(li - lf) == 2 and abs(ci - cf) == 1) or \
           (abs(li - lf) == 1 and abs(ci - cf) == 2)


def rei(li, ci, lf, cf):
    return abs(li - lf) <= 1 and abs(ci - cf) <= 1


print("Peças: torre | bispo | rainha | cavalo | rei")
peca = input("Escolha a peça: ").lower()

li = int(input("Linha inicial (0 a 7): "))
ci = int(input("Coluna inicial (0 a 7): "))
lf = int(input("Linha final (0 a 7): "))
cf = int(input("Coluna final (0 a 7): "))

movimento_valido = False

if peca == "torre":
    movimento_valido = torre(li, ci, lf, cf)
elif peca == "bispo":
    movimento_valido = bispo(li, ci, lf, cf)
elif peca == "rainha":
    movimento_valido = rainha(li, ci, lf, cf)
elif peca == "cavalo":
    movimento_valido = cavalo(li, ci, lf, cf)
elif peca == "rei":
    movimento_valido = rei(li, ci, lf, cf)
else:
    print("Peça inválida")

if movimento_valido:
    print("✅ Movimento válido")
else:
    print("❌ Movimento inválido")
