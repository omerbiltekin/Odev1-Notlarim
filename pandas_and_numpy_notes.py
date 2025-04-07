# -------------------------
# NUMPY ve PANDAS KULLANIMI
# -------------------------
import pandas as pd
import numpy as np

# -------------------------
# PANDAS KULLANIMLARI
# -------------------------

# CSV dosyasını okuma
df = pd.read_csv("ornek.csv")  # örnek dosya adı

# İlk 5 satırı görme
print(df.head())

# Veri yapısı hakkında bilgi
print(df.info())

# Sayısal özet
print(df.describe())

# Sütun seçimi
print(df["isim"])

# Birden fazla sütun seçimi
print(df[["isim", "yaş"]])

# Etikete göre seçim
print(df.loc[0, "isim"])

# Pozisyona göre seçim
print(df.iloc[0, 1])

# Eksik veri sayımı
print(df.isnull().sum())

# Eksik verileri silme
df_cleaned = df.dropna()

# Eksik verileri doldurma
df_filled = df.fillna("Bilinmiyor")

# Sıralama
df_sorted = df.sort_values("yaş", ascending=True)

# Gruplama ve ortalama alma
print(df.groupby("şehir").mean())

# Yeni sütun oluşturma
df["yaş_iki_kati"] = df["yaş"] * 2

# -------------------------
# NUMPY KULLANIMLARI
# -------------------------

# NumPy array oluşturma
arr = np.array([1, 2, 3, 4])

# Belirli aralıkta sayı üretme
aralik = np.arange(0, 10, 2)

# Sıfırlardan matris
zeros = np.zeros((3, 4))

# Birlerden matris
ones = np.ones((2, 2))

# Eşit aralıklı sayılar
linspace = np.linspace(0, 1, 5)

# Rastgele sayı matrisi
random_array = np.random.rand(3, 2)

# Ortalama, medyan, std
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))

# Şekil değiştirme
reshaped = arr.reshape((2, 2))

# İki array birleştirme
a = np.array([1, 2])
b = np.array([3, 4])
combined = np.concatenate([a, b])
