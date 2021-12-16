import pandas as pd
import csv 

df = pd.read_csv(r'C:\Users\C274839\Desktop\FDA.csv')
print("File read!!")
#print (df["Name of Person"])
# new data frame with split value columns 
name = df["Name of Person"].str.split(",", n=1, expand=True)
df["first_name"] = name[0]
df["last_name"] = name[1]
df.drop(columns = ["Name of Person"], inplace = True)
eff_date = df["Effective Date"]
df["effective_date"] = eff_date
df.drop(columns = ["Effective Date"], inplace = True)
end_term = df["End/Term of Debarment"]
df["term_of_debarment"] = end_term
df.drop(columns = ["End/Term of Debarment"], inplace = True)
date_txt = df["FR Date.txt (MM/DD/YY)"]
df["fr_date_txt"] = date_txt
df.drop(columns = ["FR Date.txt (MM/DD/YY)"], inplace = True)
vol_page = df["Volume Page.pdf"]
df["volume_page"] = vol_page
df.drop(columns = ["Volume Page.pdf"], inplace = True)
print(df)

df.to_csv(r'C:\Users\C274839\Desktop\FDA1.csv', encoding='utf-8', index = False)