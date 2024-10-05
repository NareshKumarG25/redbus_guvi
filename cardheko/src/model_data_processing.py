import pandas as pd
from  common_functions import convert_currency_to_number,convert_km_to_number,convert_register_year_string_to_number

import re

def data_processing(file):
    print("Processing data for model training from structured data....")
    df= pd.read_excel(file)

    new_data=[]
    column =['city', 'manufacturer', 'model', 'variant_type', 'fuel_type', 'model_year', 'number_of_owners', 'km_driven', 'year_of_registration','price']

    for rows in range(len(df)):
        new_data.append([df['city'][rows],
                        df['oem'][rows],
                        df['model'][rows],
                        df['variantName'][rows],
                        df['Fuel Type'][rows],
                        int(df['modelYear'][rows]),
                        int(df['ownerNo'][rows]),
                        convert_km_to_number(df['km'][rows]),
                        convert_register_year_string_to_number(df['Registration Year'][rows]),
                        convert_currency_to_number(df['price'][rows])
                        ])

    new_df=pd.DataFrame(new_data,columns=column)
    return new_df