Width = float(input("How many width have your wall? "))
Height = float(input("How many height your wall? "))
Área_Total = Width * Height

print("Your wall have the dimension is {}x{} and your field is {}m²".format(Width, Height, Área_Total))

Tinta = Área_Total / 2
print("Para cada m² você precisará de {}L de tinta".format(Tinta))