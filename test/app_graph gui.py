# Fenêtre graphique de graphique

# pip install matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np

# Générer des données fictives pour les statistiques
# Par exemple, des statistiques de vente mensuelle
mois = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ventes = np.random.randint(100, 500, size=len(mois))

# Créer un graphique
plt.figure(figsize=(10, 6))
plt.plot(mois, ventes, marker='o', linestyle='-', color='b', label='Ventes')

# Ajouter des titres et des labels
plt.title('Statistiques de Vente Mensuelle')
plt.xlabel('Mois')
plt.ylabel('Nombre de Ventes')
plt.legend()

# Afficher le graphique
plt.show()
