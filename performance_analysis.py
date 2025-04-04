def performance_analysis(df):

    if "result" in df.columns:
        df_ok = df[df["result"].str.contains("OK")] #OK sonuçlarını filtrele
    else:
        df_ok = df
    
    mean_pos1 = df_ok["FORCE_POS_1"].mean()
    std_pos1 = df_ok["FORCE_POS_1"].std()
    mean_pos2 = df_ok["FORCE_POS_2"].mean()
    std_pos2 = df_ok["FORCE_POS_2"].std()
    
    print("OK kayıtları için:")
    print("FORCE_POS_1 - Ortalama: {:.3f}, Sigma: {:.3f}".format(mean_pos1, std_pos1))
    print("FORCE_POS_2 - Ortalama: {:.3f}, Sigma: {:.3f}".format(mean_pos2, std_pos2))
    
    LSL = 45
    USL = 55
    if std_pos1 != 0:
        CP = (USL - LSL) / (6 * std_pos1)
        print("FORCE_POS_1 için CP: {:.3f}".format(CP))
    
    return df_ok

if __name__ == "__main__":
    from data_cleaning import clean_data
    from csv_extraction import extract_data
    df_raw = extract_data("data.csv")
    df_clean = clean_data(df_raw)
    performance_analysis(df_clean)
