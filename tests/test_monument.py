from model.monument import Monument

# Création d'un monument
gare = Monument("Gare", 4)

# Vérification des informations
print("Nom :", gare.nom)
print("Coût :", gare.cout)
print("État initial :", gare.construit)

# Construction du monument
gare.construire()

# Vérification après construction
print("État après construction :", gare.construit)