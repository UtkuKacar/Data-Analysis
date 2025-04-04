import matplotlib.pyplot as plt

def eda_summary(df):
    #Özet bilgileri hesapla ve göster adet,std sapma...
    if "FORCE_POS_1" in df.columns:
        print("FORCE_POS_1 İstatistikleri:")
        print(df["FORCE_POS_1"].describe())
    if "FORCE_POS_2" in df.columns:
        print("\nFORCE_POS_2 İstatistikleri:")
        print(df["FORCE_POS_2"].describe())
    
    plt.figure(figsize=(12, 5))
    
    if "FORCE_POS_1" in df.columns:
        plt.subplot(1, 2, 1)
        plt.hist(df["FORCE_POS_1"].dropna(), bins=30, edgecolor="k")
        plt.title("FORCE_POS_1 Dağılımı")
        plt.xlabel("Kuvvet (kg)")
        plt.ylabel("Frekans")
    
    if "FORCE_POS_2" in df.columns:
        plt.subplot(1, 2, 2)
        plt.hist(df["FORCE_POS_2"].dropna(), bins=30, edgecolor="k")
        plt.title("FORCE_POS_2 Dağılımı")
        plt.xlabel("Kuvvet (kg)")
    
    plt.tight_layout()
    plt.savefig("eda_summary.jpg", format="jpg", dpi=300)
    plt.show()

if __name__ == "__main__":
    from data_cleaning import clean_data
    from csv_extraction import extract_data
    df_raw = extract_data("data.csv")
    df_clean = clean_data(df_raw)
    eda_summary(df_clean)
