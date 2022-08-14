import pandas as pd


# app created for cristian garzon cristiancamilogarzon@ucundinamarca.edu.co

def frecuency_table():
    df = pd.read_csv('data.csv')

    frecuency_absolute = df['MARCA'].value_counts(ascending=True).values

    marcs = df['MARCA'].value_counts(ascending=True).keys()

    frecuency_absulute_acumulative = frecuency_absolute.cumsum()

    frecuency_relative = frecuency_absolute / len(df)

    frecuency_relative_acumulative = frecuency_absolute.cumsum() / len(df)

    percent = frecuency_relative * 100

    dfexcel = pd.DataFrame({'MARCA': marcs,
                            'FRECUENCIA ABSULUTA': frecuency_absolute,
                            'FRECUANCIA ABSOLUTA ACUMULATIVA': frecuency_absulute_acumulative,
                            'FRECUANCIA RELATIVA': frecuency_relative,
                            'FRECUANCIA RELATIVA ACUMULATIVA': frecuency_relative_acumulative,
                            'PORCENTAJE': percent})
    dfexcel.to_excel("result.xlsx")


if __name__ == '__main__':
    frecuency_table()
