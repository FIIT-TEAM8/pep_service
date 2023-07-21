import pandas as pd
from unidecode import unidecode
import pycountry

def load_data(filename):
    return pd.read_csv(filename)

def transform_names_to_ascii(df, column_name):
    df['{}_ascii'.format(column_name)] = df[column_name].apply(lambda x: unidecode(x).lower())
    return df

def transform_non_alphabetic(df, column_name):
    #filtered_df = df[df[column_name].str.contains('[^a-zA-Z\s]')]
    df[column_name] = df[column_name].str.replace("'", "").str.replace("-", " ").str.replace(",", "")
    return df

def get_country_name_from_code(code):
    try:
        return pycountry.countries.get(alpha_2=code).name
    except AttributeError:
        return "Unknown"

def transform_country_codes_to_names(df, column_name):
    df['countries_full'] = df[column_name].apply(lambda codes: [get_country_name_from_code(code) for code in str(codes).split(';')])
    return df

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)


peps = load_data("data_transformer/data/pep.targets.simple.csv")
sanctions = load_data("data_transformer/data/sanctions.targets.simple.csv")

peps = transform_names_to_ascii(peps, 'name')
sanctions = transform_names_to_ascii(sanctions, 'name')

peps = transform_non_alphabetic(peps, 'name_ascii')
sanctions = transform_non_alphabetic(sanctions, 'name_ascii')

peps = transform_country_codes_to_names(peps, "countries")
sanctions = transform_country_codes_to_names(sanctions, "countries")

save_to_csv(peps, 'data_transformer/data/peps.new.csv')
save_to_csv(sanctions, 'data_transformer/data/sanctions.new.csv')