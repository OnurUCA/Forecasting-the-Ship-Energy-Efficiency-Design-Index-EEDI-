import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score  # Performans skoru için eklendi

# Dosyanın yolunu belirtelim
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/CONTAINER/Phase_2.xlsx"

# Excel dosyasını oku
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Gerekli sütunları belirleyelim
selected_columns = [
    "Capacity (DWT)\n", "Year of delivery\n", "Required EEDI-Mandatory",
    "Required EEDI-Non-mandatory*", "Attained EEDI-Mandatory",
    "Attained EEDI-Non-mandatory", "Vref (knot)", "PME (kW)"
]
df = df[selected_columns]

# Vref ve PME sütunlarındaki sıfır değerleri NaN olarak değiştirelim
df["Vref (knot)"] = df["Vref (knot)"].replace(0, pd.NA)
df["PME (kW)"] = df["PME (kW)"].replace(0, pd.NA)

# Sayısal olmayan (hatalı) verileri NaN olarak değiştir
df.replace(["---", "NaN", "?", "", "None"], pd.NA, inplace=True)

# Tüm sütunları sayısal hale getirelim
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Bağımsız değişkenler (tahmin için kullanılacak sütunlar)
x_columns = [
    "Capacity (DWT)\n", "Year of delivery\n", "Required EEDI-Mandatory",
    "Required EEDI-Non-mandatory*", "Attained EEDI-Mandatory", "Attained EEDI-Non-mandatory"
]

# Eksik değerleri doldurmak için SimpleImputer kullanımı
imputer = SimpleImputer(strategy="mean")

# 📌 Vref (knot) için tahmin modeli ve performans skoru
df_vref_train = df.dropna(subset=["Vref (knot)"])
df_vref_missing = df[df["Vref (knot)"].isna()]

vref_r2_score = None

if not df_vref_missing.empty and not df_vref_train.empty:
    X_train, X_test, y_train, y_test = train_test_split(
        df_vref_train[x_columns], df_vref_train["Vref (knot)"], test_size=0.2, random_state=42
    )
    
    # Eksik değerleri doldur
    X_train = imputer.fit_transform(X_train)
    X_test = imputer.transform(X_test)
    
    model_vref = RandomForestRegressor(n_estimators=100, random_state=42)
    model_vref.fit(X_train, y_train)

    # Performans skoru hesapla
    y_pred = model_vref.predict(X_test)
    vref_r2_score = r2_score(y_test, y_pred)

    # Eksik değerleri doldur
    df.loc[df["Vref (knot)"].isna(), "Vref (knot)"] = model_vref.predict(imputer.transform(df_vref_missing[x_columns]))

# 📌 PME (kW) için tahmin modeli ve performans skoru
df_pme_train = df.dropna(subset=["PME (kW)"])
df_pme_missing = df[df["PME (kW)"].isna()]

pme_r2_score = None

if not df_pme_missing.empty and not df_pme_train.empty:
    X_train, X_test, y_train, y_test = train_test_split(
        df_pme_train[x_columns], df_pme_train["PME (kW)"], test_size=0.2, random_state=42
    )
    
    # Eksik değerleri doldur
    X_train = imputer.fit_transform(X_train)
    X_test = imputer.transform(X_test)
    
    model_pme = RandomForestRegressor(n_estimators=100, random_state=42)
    model_pme.fit(X_train, y_train)

    # Performans skoru hesapla
    y_pred = model_pme.predict(X_test)
    pme_r2_score = r2_score(y_test, y_pred)

    # Eksik değerleri doldur
    df.loc[df["PME (kW)"].isna(), "PME (kW)"] = model_pme.predict(imputer.transform(df_pme_missing[x_columns]))

# Temizlenmiş veriyi kaydet
filtered_file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/CONTAINER/Phase_2222.xlsx"
df.to_excel(filtered_file_path, index=False)

# 📢 Performans skorlarını ekrana yazdır
print(f"Tahmin edilen veri kaydedildi: {filtered_file_path}")
print(f"Vref (knot) R² Skoru: {vref_r2_score:.4f}" if vref_r2_score is not None else "Vref tahmini yapılamadı.")
print(f"PME (kW) R² Skoru: {pme_r2_score:.4f}" if pme_r2_score is not None else "PME tahmini yapılamadı.")
