import pandas as pd
import os
from Scripts.utility import create_time


def clean_production_data():
    # Utility
    file_location = "C:\\Projects\\SeaforthPBI\\DataFiles\\"
    files = os.listdir(file_location)
    file_month, file_year = create_time()
    j = 0

    # Read current file
    columns = ['Provider', 'ProcedureCode', 'Revenue', 'Date', 'Month', 'Year', 'MonthYear', 'FiscalYear',
               'Patient', 'ReferralSource']
    df_clean_data = pd.DataFrame(columns=columns)

    for file in files:
        filename = file_location + file
        df_current_month = pd.read_csv(filename)
        i = 0
        while i <= len(df_current_month) - 1:
            if i == len(df_current_month) - 1:
                break
            else:
                tmp_Provider = df_current_month.iloc[i, 0]
                if len(str(df_current_month.iloc[i, 2]).replace('.0', '')) != 4:
                    tmp_ProcedureCode = str(df_current_month.iloc[i, 2]).replace('.0', '')
                elif str(df_current_month.iloc[i, 2]) == '' or str(df_current_month.iloc[i, 2]) is None:
                    tmp_ProcedureCode = '01234'
                else:
                    tmp_ProcedureCode = '0' + str(df_current_month.iloc[i, 2]).replace('.0', '')
                tmp_Revenue = str(df_current_month.iloc[i, 3])
                tmp_Date = df_current_month.iloc[i, 12]
                tmp_Month = str(df_current_month.iloc[i, 12][0:3])
                if len(str(df_current_month.iloc[i, 12])) == 10:
                    tmp_Year = int(df_current_month.iloc[i, 12][6:10])
                else:
                    tmp_Year = int(df_current_month.iloc[i, 12][7:11])
                tmp_MonthYear = tmp_Month + ' ' + str(tmp_Year)
                if tmp_Year == int(file_year) and tmp_Month in ['Jan', 'Feb', 'Mar', 'Apr', 'May']:
                    tmp_FiscalYear = str(int(file_year) - 1) + '-' + str(file_year)
                elif tmp_Year < int(file_year) and tmp_Month in ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    tmp_FiscalYear = str(int(file_year) - 1) + '-' + file_year
                elif tmp_Year == int(file_year) and tmp_Month in ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    tmp_FiscalYear = str(file_year) + '-' + str(int(file_year) + 1)
                else:
                    tmp_FiscalYear = None
                tmp_Patient = df_current_month.iloc[i, 15]
                if (df_current_month.iloc[i, 16] == 'Dr Wallerstein Connie'
                        or df_current_month.iloc[i, 16] == 'Dr Hamilton, Douglas'
                        or df_current_month.iloc[i, 16] == 'Dr Moraga, Patricia'):
                    tmp_ReferralSource = 'Dr. Hamilton & Dr. Moraga & Dr. Wallerstein'
                elif (df_current_month.iloc[i, 16] == 'Dr Chamlian, Viken'
                      or df_current_month.iloc[i, 16] == 'Dr Alvaro, Caterina'):
                    tmp_ReferralSource = 'Dr. Alvaro & Dr. Chamlian'
                elif (df_current_month.iloc[i, 16] == 'Dr Di Batistta, Luigi'
                      or df_current_month.iloc[i, 16] == 'Dr Rousseau Martin'):
                    tmp_ReferralSource = 'Dr. Di Batistta & Dr. Rousseau'
                elif (df_current_month.iloc[i, 16] == 'Dr Giambattistini, Claudia' or
                      df_current_month.iloc[i, 16] == 'Dr Werbitt Jonathan'):
                    tmp_ReferralSource = 'TGO'
                elif (df_current_month.iloc[i, 16] == 'Dr. Wazirian, Berge' or
                      df_current_month.iloc[i, 16] == 'Dr Mackay, Pierre' or
                      df_current_month.iloc[i, 16] == 'Dr Karazivan, Mona'):
                    tmp_ReferralSource = 'Les Prosthodontistes'
                elif df_current_month.iloc[i, 16] == 'Dr Nguyen, Dac' \
                        or df_current_month.iloc[i, 16] == 'Dr. Martin, Michele':
                    tmp_ReferralSource = 'Dr. Martin & Dr. Nguyen'
                elif df_current_month.iloc[i, 16] == 'Dr. Leontidis, Grace' \
                        or df_current_month.iloc[i, 16] == 'Dr Rougas, Tom':
                    tmp_ReferralSource = 'Dr. Leontidis & Dr. Rougas'
                elif (df_current_month.iloc[i, 16] == 'Dr Stamboulis, Paul'
                      or df_current_month.iloc[i, 16] == 'Dr Roux-Groleau, Marie-France'):
                    tmp_ReferralSource = 'Dr. Roux-Groleau & Dr. Stamboulis'
                elif (df_current_month.iloc[i, 16] == 'Dr Yacovitch, Kathy'
                      or df_current_month.iloc[i, 16] == 'Dr Yacovitch, Terence'):
                    tmp_ReferralSource = 'Dr. Yacovitch (Terence & Kathy)'
                elif df_current_month.iloc[i, 16] == 'Dr Nan Wei-Hung':
                    tmp_ReferralSource = 'Dr. Nan, Wei-Hung'
                elif df_current_month.iloc[i, 16] == 'Dr Nguyen-Khac Christine':
                    tmp_ReferralSource = 'Dr. Nguyen-Khac, Christine'
                elif df_current_month.iloc[i, 16] == 'Dr Retta Ayalnesh':
                    tmp_ReferralSource = 'Dr. Retta, Ayalnesh'
                elif df_current_month.iloc[i, 16] == 'Dr Mui Brennan':
                    tmp_ReferralSource = 'Dr. Mui, Brennan'
                elif df_current_month.iloc[i, 16] == 'Dr Lacoste Paul':
                    tmp_ReferralSource = 'Dr. Lacoste, Paul'
                elif df_current_month.iloc[i, 16] == 'Dr Farina Adriano':
                    tmp_ReferralSource = 'Dr. Farina, Adriano'
                elif df_current_month.iloc[i, 16] == 'Dr Cynthia Simon':
                    tmp_ReferralSource = 'Dr. Cynthia, Simon'
                elif df_current_month.iloc[i, 16] == 'Dr Poulin Mark':
                    tmp_ReferralSource = 'Dr. Poulin, Mark'
                elif df_current_month.iloc[i, 16] == 'Dr Homsi Samer':
                    tmp_ReferralSource = 'Dr. Homsi, Samer'
                elif df_current_month.iloc[i, 16] == 'Dre Hamelin Godin Camille':
                    tmp_ReferralSource = 'Dr. Hamelin Godin, Camille'
                elif df_current_month.iloc[i, 16] == 'Dr Petruccelli Gianni John Antonio':
                    tmp_ReferralSource = 'Dr. Petruccelli Gianni, John Antonio'
                elif df_current_month.iloc[i, 16] == 'Dr Boileau Mantha Elise':
                    tmp_ReferralSource = 'Dr. Boileau Mantha, Elise'
                elif df_current_month.iloc[i, 16] == 'Dr Doucet Sarah':
                    tmp_ReferralSource = 'Dr. Doucet, Sarah'
                elif df_current_month.iloc[i, 16] == 'Dr Bach Normand':
                    tmp_ReferralSource = 'Dr. Bach, Normand'
                elif df_current_month.iloc[i, 16] == 'Dr Kanatselis Spiro':
                    tmp_ReferralSource = 'Dr. Kanatselis, Spiro'
                elif df_current_month.iloc[i, 16] == '' or df_current_month.iloc[i, 16] is None:
                    tmp_ReferralSource = 'INTERNET'
                else:
                    tmp_ReferralSource = str(df_current_month.iloc[i, 16]).replace('Dr ', 'Dr. ').replace('Ã©', 'e') \
                        .replace('Ã´', 'o').replace('Ã§', 'c')

                df_clean_data = df_clean_data.append(dict(Provider=tmp_Provider, ProcedureCode=tmp_ProcedureCode,
                                                          Revenue=tmp_Revenue, Date=tmp_Date, Month=tmp_Month,
                                                          Year=tmp_Year, MonthYear=tmp_MonthYear,
                                                          FiscalYear=tmp_FiscalYear, Patient=tmp_Patient,
                                                          ReferralSource=tmp_ReferralSource), ignore_index=True)

            i += 1

        message1 = f'Successfully inserted {i} from {file}.'
        print(message1)
        j = i + j
    message2 = f'Total lines inserted: {j}.'
    print(message2)

    pbi_file_location = 'C:\\Projects\\SeaforthPBI\\PBIFiles\\'
    df_clean_data.to_excel(pbi_file_location + 'Prod_by_Prov.xlsx', sheet_name='data', index=False)


if __name__ == '__main__':
    clean_production_data()
