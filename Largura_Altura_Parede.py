Largura = float(input("How many width have your wall? "))
Altura = float(input("How many higth haver your wall? "))

Área_Total = Largura * Altura

print("Your wall have dimensions of {}x{} and your field is {}m²".format(Largura, Altura, Área_Total))

Tinta = Área_Total / 2
print("For to paint this wall you need of {}L to ink".format(Tinta))