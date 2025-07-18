


# 🏠 Estimateur Immobilier Marocain - SalesHouses

Outil d'estimation automatique du prix des appartements au Maroc, basé sur le machine learning et conçu pour la plateforme SalesHouses.

---

## 📌 Contexte

Dans un marché immobilier en constante évolution, l’estimation précise des prix est essentielle pour les acheteurs, vendeurs et agences. Ce projet propose un simulateur intelligent permettant d’obtenir une estimation rapide et fiable du prix de vente d’un appartement marocain, à partir de ses caractéristiques principales.

---

## 🚀 Fonctionnalités

- Chargement et analyse exploratoire des données (EDA)
- Nettoyage, transformation et préparation des variables
- Détection et gestion des valeurs manquantes et aberrantes
- Feature engineering et sélection des variables explicatives
- Entraînement, validation et optimisation de plusieurs modèles de régression
- Sélection et sauvegarde du meilleur modèle (model.pkl)
- Documentation claire et reproductible

---

## 🧱 Pipeline de traitement

1. **Chargement des données**
   - Importation des bibliothèques (pandas, numpy)
   - Lecture du fichier CSV (appartements-data-db.csv)
   - Aperçu et structure des données (df.head(), df.info())
2. **Analyse exploratoire (EDA)**
   - Dimensions, types, valeurs manquantes, doublons
   - Statistiques descriptives, histogrammes, corrélations
   - Visualisation des relations avec le prix
3. **Prétraitement**
   - Transformation de `equipment` en variables booléennes
   - Nettoyage de la colonne `price` (conversion en float)
   - Suppression des colonnes inutiles
   - Uniformisation de `city_name` (arabe ➝ français)
   - Gestion des valeurs manquantes (suppression, imputation)
   - Feature engineering : `price_per_m2`, `total_rooms`, `log_price`
   - Détection et traitement des outliers (IQR, capping)
   - Encodage des variables catégorielles (LabelEncoder)
   - Mise à l’échelle des variables numériques (StandardScaler)
4. **Sélection des variables explicatives**
   - Corrélation avec la cible, filtrage et vérification des redondances
5. **Séparation des données**
   - Définition de la cible `y` et des features `X`
   - Split entraînement/test (80/20)
6. **Entraînement des modèles**
   - Régression Linéaire, Random Forest, SVR, Gradient Boosting
   - Évaluation (MAE, RMSE, R²), validation croisée (5-fold, 10-fold)
   - Optimisation des hyperparamètres (GridSearchCV, RandomizedSearchCV)
   - Sélection et sauvegarde du meilleur modèle

---

## 📂 Structure du projet

```
/saleshouse
│
├── data/
│   └── appartements-data-db.csv
│
├── notebooks/
│   └── analyse_immobiliere_complete.ipynb
│
├── models/
│   └── model.pkl
│
└── README.md│
└──requirements.txt 
```

---

## ⚙️ Installation

1. Cloner le projet
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

---

## 📝 Utilisation

- Ouvrir et exécuter le notebook `analyse_immobiliere_complete.ipynb` pour suivre le pipeline complet
- Exemple de prédiction Python :

```python
import joblib
import pandas as pd

model = joblib.load('models/model.pkl')


    'surface_area': [80],
    'nb_rooms': [3],
    'nb_baths': [2],
    'price_per_m2': [15000],
    # Ajouter les colonnes équipements (0 ou 1)
})

prix = model.predict(data)
print(f"Prix estimé : {prix[0]:,.2f} MAD")
```

---

## 🔄 Mise à jour du modèle

- Ajouter de nouvelles données dans `data/appartements-data-db.csv`
- Relancer l’entraînement dans le notebook
- Remplacer le fichier `models/model.pkl`

---

##  Auteur

ILHAM EL GHARBI
