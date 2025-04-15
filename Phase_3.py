import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Dosyanın yolunu belirtelim
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/TANKER/Phase_2.xlsx"

# Excel dosyasını oku
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Gerekli sütunları belirleyelim
selected_columns = [
    "Capacity\n(DWT)", "Year of delivery", "Required EEDI-Mandatory",
    "Required EEDI-Non-mandatory*", "Attained EEDI-Mandatory",
    "Attained EEDI-Non-mandatory", "Vref (knot)", "PME (kW)"
]
df = df[selected_columns]

# Vref ve PME sütunlarındaki sıfır değerleri NaN olarak değiştirelim
df["Vref (knot)"] = df["Vref (knot)"].replace(0, pd.NA)
df["PME (kW)"] = df["PME (kW)"].replace(0, pd.NA)

# Bağımsız değişkenler (tahmin için kullanılacak sütunlar)
x_columns = [
    "Capacity\n(DWT)", "Year of delivery", "Required EEDI-Mandatory",
    "Required EEDI-Non-mandatory*", "Attained EEDI-Mandatory", "Attained EEDI-Non-mandatory"
]

# Vref (knot) için tahmin modeli
df_vref_train = df.dropna(subset=["Vref (knot)"])
df_vref_missing = df[df["Vref (knot)"].isna()]

if not df_vref_missing.empty:
    X_train, X_test, y_train, y_test = train_test_split(df_vref_train[x_columns], df_vref_train["Vref (knot)"], test_size=0.2, random_state=42)
    model_vref = RandomForestRegressor(n_estimators=100, random_state=42)
    model_vref.fit(X_train, y_train)
    df.loc[df["Vref (knot)"].isna(), "Vref (knot)"] = model_vref.predict(df_vref_missing[x_columns])

# PME (kW) için tahmin modeli
df_pme_train = df.dropna(subset=["PME (kW)"])
df_pme_missing = df[df["PME (kW)"].isna()]

if not df_pme_missing.empty:
    X_train, X_test, y_train, y_test = train_test_split(df_pme_train[x_columns], df_pme_train["PME (kW)"], test_size=0.2, random_state=42)
    model_pme = RandomForestRegressor(n_estimators=100, random_state=42)
    model_pme.fit(X_train, y_train)
    df.loc[df["PME (kW)"].isna(), "PME (kW)"] = model_pme.predict(df_pme_missing[x_columns])

# Temizlenmiş veriyi kaydet
filtered_file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/TANKER/Phase_3.xlsx"
df.to_excel(filtered_file_path, index=False)

print(f"Tahmin edilen veri kaydedildi: {filtered_file_path}")
