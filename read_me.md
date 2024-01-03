# `iloc` Metodu

**Açıklama:**
`iloc` metodu, Pandas DataFrame üzerinde indeks tabanlı seçim yapmak için kullanılır. "iloc" kısaltması "integer location"dan gelir ve DataFrame içindeki belirli satır ve sütunlara, konumlarına göre erişim sağlar.

**Kullanım:**
```python
dataframe.iloc[<satır indeksi>, <sütun indeksi>]
```

**Örnekler:**

1. **Tek bir hücre seçimi:**
   ```python
   dataframe.iloc[satır, sütun]
   ```

2. **Satır veya sütun aralığı seçimi:**
   ```python
   dataframe.iloc[başlangıç_satır:bitiş_satır, başlangıç_sütun:bitiş_sütun]
   ```

3. **Belirli satırlar veya sütunlar:**
   ```python
   dataframe.iloc[[satır1, satır2, ...], [sütun1, sütun2, ...]]
   ```

**Notlar:**
- `iloc` kullanımı, indeks tabanlı seçim yapmayı sağlar ve NumPy dizileri gibi indeksleme yapmaya alışkın olanlar için uygun bir seçenektir.
- Bu metot, DataFrame içindeki verilere konumlarına göre erişim sağlamak için kullanılır.

**Örnek:**
```python
import pandas as pd

# Örnek DataFrame oluşturulması
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# İlk satırın ve ikinci sütunun seçimi
print(df.iloc[0, 1])
```