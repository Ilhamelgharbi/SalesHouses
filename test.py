import unittest
import joblib
import pandas as pd

class TestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = joblib.load('models/model.pkl')

    def test_model_load(self):
        self.assertIsNotNone(self.model)

    def test_prediction(self):
        # Utiliser l'ordre exact des features utilisé lors de l'entraînement
        # Test avec plusieurs exemples d'appartements
        data = pd.DataFrame({
            'price_per_m2': [15000, 12000, 18000, 10000, 20000],
            'surface_area': [80, 120, 60, 100, 50],
            'nb_baths': [2, 3, 1, 2, 1],
            'total_rooms': [4, 5, 3, 4, 2],
            'nb_rooms': [3, 4, 2, 3, 1],
            'Ascenseur': [1, 1, 0, 1, 1],
            'Parking': [1, 1, 0, 1, 0],
            'Climatisation': [1, 1, 1, 0, 1],
            'Terrasse': [0, 1, 0, 1, 0],
            'Chauffage': [1, 1, 0, 1, 1],
            'Concierge': [0, 1, 0, 0, 1],
            'Balcon': [1, 1, 1, 0, 1]
        })
        pred = self.model.predict(data)
        
        # Prix estimés réels pour chaque appartement (exemples)
        real_prices = [1200000, 1440000, 1080000, 1000000, 1000000]  # MAD
        
        print(f"\n🏠 Test de prédiction sur {len(data)} appartements :")
        print("-" * 60)
        
        for i in range(len(data)):
            difference = abs(pred[i] - real_prices[i])
            percentage_diff = (difference / real_prices[i]) * 100
            
            print(f"\n📋 Appartement {i+1}:")
            print(f"   Surface: {data.iloc[i]['surface_area']}m² | Chambres: {data.iloc[i]['nb_rooms']} | SDB: {data.iloc[i]['nb_baths']}")
            print(f"   Prix prédit : {pred[i]:,.2f} MAD")
            print(f"   Prix réel estimé : {real_prices[i]:,.2f} MAD")
            print(f"   Différence : {difference:,.2f} MAD ({percentage_diff:.1f}%)")
            
            if percentage_diff <= 10:
                print("   ✅ Prédiction excellente (≤10% d'écart)")
            elif percentage_diff <= 20:
                print("   🟡 Prédiction acceptable (≤20% d'écart)")
            else:
                print("   ❌ Prédiction à améliorer (>20% d'écart)")
        
        # Statistiques globales
        avg_diff = sum(abs(pred[i] - real_prices[i]) for i in range(len(data))) / len(data)
        avg_percentage = sum(abs(pred[i] - real_prices[i]) / real_prices[i] * 100 for i in range(len(data))) / len(data)
        
        print(f"\n📊 Statistiques globales :")
        print(f"   Écart moyen : {avg_diff:,.2f} MAD ({avg_percentage:.1f}%)")
        
        self.assertEqual(pred.shape, (len(data),))
        self.assertTrue(all(isinstance(p, float) for p in pred))

if __name__ == '__main__':
    unittest.main()
