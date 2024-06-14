import termgraph.termgraph as tg

# Données fictives pour les statistiques
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data = [[100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]]

# Options pour le graphique
args = {
    'filename': None,
    'title': 'Statistiques de Vente Mensuelle',
    'width': 50,
    'format': '{:<5.1f}',
    'suffix': '',
    'no_labels': False,
    'color': None,
    'vertical': False,
    'stacked': False,
    'different_scale': False,
    'calendar': False,
    'start_dt': None,
    'custom_tick': '',
    'delim': '',
    'verbose': False,
    'histogram': False,
    'no_values': False,
}

# Termgraph nécessite des couleurs, même si elles sont None
colors = [None]

# Affichage du graphique
tg.chart(colors, data, args, labels)
