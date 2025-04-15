import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Dosya yolu ve veri yükleme
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/TANKER/Phase_5.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name="Original Data")

# Yıllara göre ortalama EEDI değerlerini hesaplayalım
eedi_trend = df.groupby("Year")["EEDI"].mean()

# Grafiği oluşturalım
plt.figure(figsize=(10, 5))
plt.plot(eedi_trend.index, eedi_trend.values, marker='o', linestyle='-', label="EEDI Trend")

# 2030'a kadar tahmini bir eğilim çizgisi ekleyelim (lineer regresyon)
years = eedi_trend.index.values.reshape(-1, 1)
eedi_values = eedi_trend.values

# Lineer regresyon modeli oluştur ve eğit
model = LinearRegression()
model.fit(years, eedi_values)

# 2030'a kadar tahmin edelim
future_years = np.arange(min(years), 2031).reshape(-1, 1)
future_eedi = model.predict(future_years)

# Tahmini çizgiyi ekleyelim
plt.plot(future_years, future_eedi, linestyle="dashed", color="red", label="Projection to 2030")

# Grafik başlık ve etiketler
plt.xlabel("Year")
plt.ylabel("EEDI Value")
plt.title("TANKER EEDI Temporal Trend (with Projection to 2030)")
plt.legend()
plt.grid(True)

# Grafiği göster
plt.show()