
# 🏠 Estimateur Immobilier Intelligent - Maroc

Application professionnelle d'estimation de prix immobilier au Maroc, basée sur l'intelligence artificielle et l'analyse avancée de données.

---

## 🚀 Fonctionnalités Principales

- **Prédiction de prix en temps réel** : Estimation instantanée selon les caractéristiques du bien
- **Interface web intuitive** : Utilisation de Streamlit pour une expérience utilisateur optimale
- **Analyse comparative** : Visualisation des prix moyens par ville
- **Conseils personnalisés** : Suggestions pour augmenter la valeur de votre bien
- **Visualisations interactives** : Graphiques, heatmaps, boxplots, et rapports détaillés

---

## 🛠️ Installation & Démarrage

### Prérequis
- Python 3.7 ou plus récent
- pip (gestionnaire de paquets)

### Installation
```bash
git clone <repository-url>
cd gemini
pip install -r requirements.txt
```

### Génération du modèle (si nécessaire)
```bash
python test3.py
```

### Lancement de l'application
```bash
streamlit run streamlit_app.py
```
Ou double-cliquez sur `run_app.bat` (Windows).

---

## 📊 Utilisation

### Interface Utilisateur
- **Paramètres** : Sélection de la ville, surface, nombre de chambres, salles de bains, salons
- **Équipements** : Choix parmi 16 équipements (Ascenseur, Parking, Climatisation, etc.)
- **Estimation** : Cliquez sur "🔮 Estimer le Prix" pour obtenir une prédiction

### Exemple de Prédiction en Python
```python
import joblib
import pandas as pd

# Charger le modèle entraîné
model = joblib.load('model2.pkl')

# Exemple de données (adapter selon votre jeu de données)
sample_data = pd.DataFrame({
    'price_per_m2': [15000],
    'surface_area': [80],
    'nb_baths': [2],
    'nb_rooms': [3],
    'total_rooms': [4],
    'Ascenseur': [1],
    'Parking': [0],
    'Climatisation': [1],
    'Terrasse': [0],
    'Chauffage': [1],
    'Concierge': [0],
    'Balcon': [1]
})

# Prédiction
predictions = model.predict(sample_data)
print(f"Prix prédit : {predictions[0]:,.2f} MAD")
```

---

## 🔧 Fichiers Nécessaires

- `model2.pkl` : Modèle IA entraîné
- `appartements-data-db.csv` : Données d'entraînement
- (Autres fichiers .pkl selon la version du projet)

---

## 📈 Performance & Modélisation

- **Algorithmes** : Gradient Boosting, Random Forest, SVR, Régression Linéaire
- **Validation croisée** : R² > 0.70 sur 1400+ appartements
- **Features** : Sélection automatique et ingénierie de variables (price_per_m2, total_rooms, équipements...)
- **Traitement avancé** : Nettoyage, gestion des valeurs manquantes, outliers, encodage, normalisation

---

## 🏙️ Villes Supportées

- Casablanca, Rabat, Marrakech, Fès, Tanger, Agadir, Kénitra, Mohammedia, Salé, Temara, ...

## 🎯 Équipements Supportés

- Ascenseur, Parking, Climatisation, Terrasse, Balcon, Piscine, Sécurité, Concierge, Chauffage, Cuisine équipée, Jardin, Vue mer, Meublé, Garage, Cave, Interphone

---

## 🔍 Fonctionnalités Avancées

- Calculs automatiques : ratios, densité, interactions
- Catégorisation intelligente : surface, niveau de luxe, prix par ville
- Conseils personnalisés : suggestions d'amélioration et estimation d'impact

---

## 📱 Interface Responsive

Compatible desktop, tablette et mobile

---

## 🛡️ Sécurité & Confidentialité

- Données traitées localement
- Aucune donnée personnelle stockée
- Utilisation hors-ligne possible

---

## 🔄 Mise à Jour du Modèle

1. Ajoutez vos nouvelles données à `appartements-data-db.csv`
2. Exécutez `python test3.py` pour réentraîner
3. Relancez l'application

---

## 📞 Support & Questions

- Vérifiez la présence des fichiers .pkl
- Assurez-vous que Python 3.7+ et les dépendances sont installés

---

## 🌟 Roadmap & Fonctionnalités Futures

- [ ] Support maisons, villas
- [ ] Prédiction de tendances du marché
- [ ] Analyse de rentabilité locative
- [ ] Export PDF
- [ ] API REST

---

## 📄 Licence

Projet éducatif et démonstratif. Les estimations sont informatives et non contractuelles. Pour une expertise officielle, consultez un professionnel immobilier.
