from thermo import Chemical

# Liste des molécules à étudier
molecules = {
    "Eau (H2O)": "water",
    "Méthanol": "methanol",
    "Éthanol": "ethanol",
    "Acétone": "acetone",
    "Hexane": "n-hexane",
    "Xylène": "o-xylene",
    "Benzène": "benzene"
}

print("\n==============================================")
print("   CALCUL DES TEMPÉRATURES D'ÉBULLITION")
print("==============================================")

for nom, identifiant in molecules.items():
    try:
        produit = Chemical(identifiant)

        # Température normale d'ébullition en kelvins
        temperature_K = produit.Tb

        if temperature_K is not None:
            temperature_C = temperature_K - 273.15
            print(f"{nom:<18} : {temperature_C:.2f} °C")
        else:
            print(f"{nom:<18} : valeur indisponible")

    except Exception as erreur:
        print(f"{nom:<18} : erreur - {erreur}")

print("==============================================")
print("             FIN DU CALCUL")
print("==============================================")