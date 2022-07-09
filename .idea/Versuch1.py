import pandas as pd
import numpy as np

df_with_duplicates = pd.read_excel("/Users/justus/Desktop/Studium/Systemmodellierung/ZugeschnitteneDaten1.xlsx")

df_without_duplicates = df_with_duplicates.drop_duplicates(subset=['Status description','Status date/time'])

#df_without_duplicates.to_excel("Ergebnis_Datenaufbereitung1.xlsx")

id_list = np.unique(df_without_duplicates["Shipment no."])

df_only_shipmentcreation = df_without_duplicates

for id in id_list:
    id_df = df_without_duplicates[df_without_duplicates["Shipment no."] == id]

    if 'Shipment created' in id_df["Status description"].tolist():
        continue

    else:
        #print(False, id)
        df_only_shipmentcreation.drop(df_only_shipmentcreation[df_only_shipmentcreation['Shipment no.'] == id].index, inplace=True)

id_list2 = np.unique(df_only_shipmentcreation["Shipment no."])

for id in id_list2:
    id_df2 = df_without_duplicates[df_without_duplicates["Shipment no."] == id]

    if 'Delivered - clean POD' in id_df2["Status description"].tolist():
        continue

    else:
        #print(False, id)
        df_only_shipmentcreation.drop(df_only_shipmentcreation[df_only_shipmentcreation['Shipment no.'] == id].index, inplace=True)

df_only_shipmentcreation = df_only_shipmentcreation.reset_index()

for idx in range(len(df_only_shipmentcreation["Status description"])):
    #print(idx)
    if "Not out for delivery yet" in df_only_shipmentcreation["Status description"][idx]:
        #print(idx, df_only_shipmentcreation["Status description"][idx])
        df_only_shipmentcreation["Status description"][idx] = "Not out for delivery yet"

    else:
        #print(False)
        continue

#print(df_only_shipmentcreation["Status description"].value_counts())

df_only_shipmentcreation.to_excel("Humbug.xlsx")

print("Länge df_only_shipmentcreation:", len(df_only_shipmentcreation),",", "Länge df_without_duplicates:", len(df_without_duplicates))

