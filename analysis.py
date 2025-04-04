import io
from contextlib import redirect_stdout
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_analysis():
    df_clean = pd.read_csv("cleaned_data.csv")
    if "date" in df_clean.columns:
        df_clean["date"] = pd.to_datetime(df_clean["date"], format="%d/%m/%Y", errors="coerce")  #tarihi g/a/y şeklinde ayarla
    print("Cleaned data loaded:", df_clean.shape[0], "satır")   #temizlenen kaç veri yüklendi
    
    print("=== 1.1 Temel İstatistikler (FORCE_POS_1 & FORCE_POS_2) ===")
    print("FORCE_POS_1 İstatistikleri:")
    print(df_clean["FORCE_POS_1"].describe())  # ortalama std sapma vs. bu değerleri hesapla ve göster
    print("\nFORCE_POS_2 İstatistikleri:")
    print(df_clean["FORCE_POS_2"].describe())
    
    print("\n=== 1.3 NOK Verilerinin Analizi ===")
    nok_df = df_clean[df_clean["result"].str.contains("NOK", na=False)]   #NOK sonuçlarını filtrele
    print(f"NOK veri sayısı: {nok_df.shape[0]}")
    print("NOK tipleri ve sayıları:")
    print(nok_df["result"].value_counts())
    
    nok_pos1 = nok_df[nok_df["result"].str.contains("POS 1", na=False)]
    nok_pos2 = nok_df[nok_df["result"].str.contains("POS 2", na=False)]
    print(f"\nNOK (POS 1) sayısı: {nok_pos1.shape[0]}")
    print(f"NOK (POS 2) sayısı: {nok_pos2.shape[0]}")
    
    print("\n=== 2) Anomali Tespiti (Z-Score) ===")
    mean_pos1 = df_clean["FORCE_POS_1"].mean()
    std_pos1 = df_clean["FORCE_POS_1"].std()
    df_clean.loc[:, "z_score_pos1"] = (df_clean["FORCE_POS_1"] - mean_pos1) / std_pos1
    anomalies_pos1 = df_clean[np.abs(df_clean["z_score_pos1"]) > 3]   #z-skoru 3 ten büyük olanlar anomali kabul et
    print(f"FORCE_POS_1 anomali sayısı (|z|>3): {anomalies_pos1.shape[0]}")
    anomalies_pos1.to_csv("anomalies_pos1.csv", index=False)   #tüm anomalileri kaydet
    nok_anomalies = anomalies_pos1[anomalies_pos1["result"].str.contains("NOK", na=False)]
    print(f"NOK satırları içindeki anomali sayısı: {nok_anomalies.shape[0]}")
    
    print("\n=== 3) Performans Analizi ===")
    df_ok = df_clean[df_clean["result"].str.contains("OK", na=False)]
    mean_pos1_ok = df_ok["FORCE_POS_1"].mean()
    std_pos1_ok  = df_ok["FORCE_POS_1"].std()
    mean_pos2_ok = df_ok["FORCE_POS_2"].mean()
    std_pos2_ok  = df_ok["FORCE_POS_2"].std()
    print(f"OK verilerinde FORCE_POS_1 -> Ortalama: {mean_pos1_ok:.3f}, Sigma: {std_pos1_ok:.3f}")
    print(f"OK verilerinde FORCE_POS_2 -> Ortalama: {mean_pos2_ok:.3f}, Sigma: {std_pos2_ok:.3f}")
    print("\nVerilen örnek ortalamalarla kıyas:")
    print(f"Örnek: FORCE_POS_1: 50,557 kg / Mevcut: {mean_pos1_ok:.3f}")
    print(f"Örnek: FORCE_POS_2: 73,087 kg / Mevcut: {mean_pos2_ok:.3f}")
    LSL_pos1 = 45
    USL_pos1 = 55
    if std_pos1_ok != 0:
        CP_pos1 = (USL_pos1 - LSL_pos1) / (6 * std_pos1_ok)
        print(f"\nFORCE_POS_1 için CP: {CP_pos1:.3f}")
    
    print("\n=== 4) Detaylı Raporlama ===")
    daily_counts = df_clean.groupby(df_clean["date"].dt.date).size()
    print("\nGünlük Üretilen Parça Sayısı:")
    print(daily_counts)
    daily_ok_nok = df_clean.groupby([df_clean["date"].dt.date, "result"]).size().unstack(fill_value=0)
    print("\nGünlük OK/NOK Dağılımı:")
    print(daily_ok_nok)
    nok_records = df_clean[df_clean["result"].str.contains("NOK", na=False)][
        ["date", "time", "code", "FORCE_POS_1", "FORCE_POS_2"]
    ]
    nok_records.to_csv("nok_records.csv", index=False)
    print("\nÖrnek NOK Kayıtları (ilk 10):")
    print(nok_records.head(10))
    
    plt.figure(figsize=(6,4))
    result_counts = df_clean["result"].value_counts()
    result_counts.plot(kind="bar", color=["green", "red", "orange", "blue"])
    plt.title("OK / NOK Dağılımı")
    plt.xlabel("Sonuç Tipi")
    plt.ylabel("Adet")
    plt.show()
    
    print("\n=== Analiz Tamamlandı ===")

if __name__ == "__main__":

    output = io.StringIO()
    with redirect_stdout(output):
        run_analysis()
    analysis_results = output.getvalue()
    with open("analysis_results.txt", "w", encoding="utf-8") as f:
        f.write(analysis_results)
    print(analysis_results)
    print("Analiz sonuçları 'analysis_results.txt' dosyasına kaydedildi.")
