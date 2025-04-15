import pandas as pd
import matplotlib.pyplot as plt


import numpy as np

# Excel dosyasını yükleyelim (Dosya adını kendi dosyana göre güncelle)
df = pd.read_excel("/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/TANKER/Tanker_Phase_5_EEDI2030.xlsx")

# Grafik boyutunu belirleyelim
plt.figure(figsize=(10, 6))

# DWT'ye göre Mevcut EEDI grafiği
plt.scatter(df['PME'], df['EEDI'], color='blue', alpha=0.5, label='Current EEDI')

# DWT'ye göre Tahmini EEDI (2030) grafiği
plt.scatter(df['PME'], df['Predicted_EEDI_2030'], color='red', alpha=0.5, label='Predicted EEDI 2030')


# Grafik başlık ve etiketleri
plt.title('TANKER')
plt.xlabel('DWT (Deadweight Tonnage)')
plt.ylabel('EEDI Values')

# Gösterge ekleyelim
plt.legend()

# Izgara ekleyelim
plt.grid(True, linestyle='--', alpha=0.7)

# Grafiği görüntüleyelim
plt.show()
