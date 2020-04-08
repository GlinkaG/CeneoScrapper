#import bibliotek
import os
import pandas as pd

#wyswietlanie zawartosci
print(os.listdir("./opinions"))

#
product_id = input("Podaj kod produktu: ")


opinions = pd.read_json("opinions/"+product_id+".json")
opinions = opinions.set_index("opinion_id")



print(opinions)