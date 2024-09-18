import pandas

jerosalem_shelters = pandas.read_csv("EN_Shelters.csv", encoding="ISO-8859-1")
jerosalem_shelters = jerosalem_shelters.dropna()
print(jerosalem_shelters)














# # jerosalem_shelters = jerosalem_shelters.drop("מספר מקלט", axis= 1)
# print(f"Found {len(jerosalem_shelters)} tables")
# print(jerosalem_shelters)
# print(jerosalem_shelters.head(8))
# # count = 1
# # for shelters in jerosalem_shelters:
# #     print(f"Area {count}")
# #     print(shelters)
# #     count += 1
