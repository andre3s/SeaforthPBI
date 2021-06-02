import pandas as pd
import os
from Scripts.utility import create_time
from colorama import Fore


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
                elif (int(file_year) - tmp_Year) == 1 and tmp_Month in ['Jan', 'Feb', 'Mar', 'Apr', 'May']:
                    tmp_FiscalYear = str(tmp_Year - 1) + '-' + str(tmp_Year)
                elif (int(file_year) - tmp_Year) == 1 \
                        and tmp_Month in ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    tmp_FiscalYear = str(tmp_Year) + '-' + str(file_year)
                elif (int(file_year) - tmp_Year) == 2 \
                        and tmp_Month in ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    tmp_FiscalYear = str(int(file_year) - 2) + '-' + str(int(file_year) - 1)
                elif tmp_Year == int(file_year) and tmp_Month in ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    tmp_FiscalYear = str(int(file_year)) + '-' + str(int(file_year) + 1)
                else:
                    tmp_FiscalYear = None

                tmp_Patient = df_current_month.iloc[i, 15]

                tmp_ReferralName = str(df_current_month.iloc[i, 16]).replace('Dr ', 'Dr. ')\
                    .replace('Ã©', 'e').replace('Ã´', 'o').replace('Ã§', 'c')

                if (tmp_ReferralName == 'Dr Wallerstein Connie'
                        or tmp_ReferralName == 'Dr. Wallerstein Connie'
                        or tmp_ReferralName == 'Dr Hamilton, Douglas'
                        or tmp_ReferralName == 'Dr. Douglas Hamilton'
                        or tmp_ReferralName == 'Dr. Hamilton, Douglas'
                        or tmp_ReferralName == 'Dr. Moraga, Patricia'
                        or tmp_ReferralName == 'Dr Moraga, Patricia'):
                    tmp_ReferralSource = 'Dr. Hamilton & Dr. Moraga & Dr. Wallerstein'
                elif (tmp_ReferralName == 'Dr Chamlian, Viken'
                      or tmp_ReferralName == 'Dr Alvaro, Caterina'
                      or tmp_ReferralName == 'Dr. Chamlian, Viken'
                      or tmp_ReferralName == 'Dr. Alvaro, Caterina'):
                    tmp_ReferralSource = 'Dr. Alvaro & Dr. Chamlian'
                elif (tmp_ReferralName == 'Dr Di Battista, Luigi'
                      or tmp_ReferralName == 'Dr. Di Battista, Luigi' or tmp_ReferralName == 'Dr. Rousseau Martin'
                      or tmp_ReferralName == 'Dr Rousseau Martin'):
                    tmp_ReferralSource = 'Dr. Di Battista & Dr. Rousseau'
                elif (tmp_ReferralName == 'Dr Giambattistini, Claudia'
                      or tmp_ReferralName == 'Dr. Giambattistini, Claudia'
                      or tmp_ReferralName == 'Dr. Werbitt Jonathan'
                      or tmp_ReferralName == 'Dr Werbitt Jonathan'):
                    tmp_ReferralSource = 'TGO'
                elif (tmp_ReferralName == 'Dr. Wazirian, Berge' or
                      tmp_ReferralName == 'Dr Mackay, Pierre'
                      or tmp_ReferralName == 'Dr. Mackay, Pierre'
                      or tmp_ReferralName == 'Dr. Karazivan, Mona'
                      or tmp_ReferralName == 'Dr Karazivan, Mona'):
                    tmp_ReferralSource = 'Les Prosthodontistes'
                elif (tmp_ReferralName == 'Dr Nguyen, Dac'
                      or tmp_ReferralName == 'Dr. Nguyen, Dac'
                      or tmp_ReferralName == 'Dr. Martin, Michele'):
                    tmp_ReferralSource = 'Dr. Martin & Dr. Nguyen'
                elif (tmp_ReferralName == 'Dr. Leontidis, Grace'
                      or tmp_ReferralName == 'Dr. Rougas, Tom'
                      or tmp_ReferralName == 'Dr. Leontidis, Grace'
                      or tmp_ReferralName == 'Dr Rougas, Tom'):
                    tmp_ReferralSource = 'Dr. Leontidis & Dr. Rougas'
                elif (tmp_ReferralName == 'Dr Stamboulis, Paul'
                      or tmp_ReferralName == 'Dr. Roux-Groleau, Marie-France'
                      or tmp_ReferralName == 'Dr. Stamboulis Paul'
                      or tmp_ReferralName == 'Dr. Stamboulis, Paul'
                      or tmp_ReferralName == 'Dr Roux-Groleau, Marie-France'):
                    tmp_ReferralSource = 'Dr. Roux-Groleau & Dr. Stamboulis'
                elif (tmp_ReferralName == 'Dr Yacovitch, Kathy'
                      or tmp_ReferralName == 'Dr. Yacovitch, Kathy'
                      or tmp_ReferralName == 'Dr. Yacovitch, Terence'
                      or tmp_ReferralName == 'Dr Yacovitch, Terence'):
                    tmp_ReferralSource = 'Dr. Yacovitch (Terence & Kathy)'
                elif tmp_ReferralName == 'Dr Nan Wei-Hung' or tmp_ReferralName == 'Dr. Nan Wei-Hung':
                    tmp_ReferralSource = 'Dr. Nan, Wei-Hung'
                elif (tmp_ReferralName == 'Dr Nguyen-Khac Christine'
                      or tmp_ReferralName == 'Dr. Nguyen-Khac Christine'):
                    tmp_ReferralSource = 'Dr. Nguyen-Khac, Christine'
                elif tmp_ReferralName == 'Dr Retta Ayalnesh' or tmp_ReferralName == 'Dr. Retta Ayalnesh':
                    tmp_ReferralSource = 'Dr. Retta, Ayalnesh'
                elif tmp_ReferralName == 'Dr Mui Brennan' or tmp_ReferralName == 'Dr. Mui Brennan':
                    tmp_ReferralSource = 'Dr. Mui, Brennan'
                elif tmp_ReferralName == 'Dr Lacoste Paul' or tmp_ReferralName == 'Dr. Lacoste Paul':
                    tmp_ReferralSource = 'Dr. Lacoste, Paul'
                elif tmp_ReferralName == 'Dr Farina Adriano' or tmp_ReferralName == 'Dr. Farina Adriano':
                    tmp_ReferralSource = 'Dr. Farina, Adriano'
                elif tmp_ReferralName == 'Dr Cynthia Simon' or tmp_ReferralName == 'Dr. Cynthia Simon':
                    tmp_ReferralSource = 'Dr. Cynthia, Simon'
                elif tmp_ReferralName == 'Dr Poulin Mark' or tmp_ReferralName == 'Dr. Poulin Mark':
                    tmp_ReferralSource = 'Dr. Poulin, Mark'
                elif tmp_ReferralName == 'Dr Homsi Samer' or tmp_ReferralName == 'Dr. Homsi Samer':
                    tmp_ReferralSource = 'Dr. Homsi, Samer'
                elif tmp_ReferralName == 'Dre Hamelin Godin Camille':
                    tmp_ReferralSource = 'Dr. Hamelin Godin, Camille'
                elif (tmp_ReferralName == 'Dr Petruccelli Gianni John Antonio'
                      or tmp_ReferralName == 'Dr. Petruccelli Gianni John Antonio'):
                    tmp_ReferralSource = 'Dr. Petruccelli Gianni, John Antonio'
                elif tmp_ReferralName == 'Dr Boileau Mantha Elise' or tmp_ReferralName == 'Dr. Boileau Mantha Elise':
                    tmp_ReferralSource = 'Dr. Boileau Mantha, Elise'
                elif tmp_ReferralName == 'Dr Doucet Sarah' or tmp_ReferralName == 'Dr. Doucet Sarah':
                    tmp_ReferralSource = 'Dr. Doucet, Sarah'
                elif tmp_ReferralName == 'Dr Bach Normand' or tmp_ReferralName == 'Dr. Bach Normand':
                    tmp_ReferralSource = 'Dr. Bach, Normand'
                elif tmp_ReferralName == 'Dr Kanatselis Spiro' or tmp_ReferralName == 'Dr. Kanatselis Spiro':
                    tmp_ReferralSource = 'Dr. Kanatselis, Spiro'
                elif tmp_ReferralName == '' or tmp_ReferralName is None:
                    tmp_ReferralSource = 'INTERNET'
                elif tmp_ReferralName == 'Dr. Puchinger Brenda':
                    tmp_ReferralSource = 'Dr. Puchinger, Brenda'
                elif tmp_ReferralName == 'Dr. Charbonneau Claudine':
                    tmp_ReferralSource = 'Dr. Charbonneau, Claudine'
                elif tmp_ReferralName == 'DR Phan Victor':
                    tmp_ReferralSource = 'Dr. Phan, Victor'
                elif tmp_ReferralName == 'Dr. Elbaz Valerie':
                    tmp_ReferralSource = 'Dr. Elbaz, Valerie'
                elif tmp_ReferralName == 'Dr. Lavoie Martin':
                    tmp_ReferralSource = 'Dr. Lavoie, Martin'
                elif tmp_ReferralName == 'Dr. Luong Viviane':
                    tmp_ReferralSource = 'Dr. Luong, Viviane'
                elif tmp_ReferralName == 'Dr. Fried Irwin':
                    tmp_ReferralSource = 'Dr. Fried, Irwin'
                elif tmp_ReferralName == 'Dr. Baker Morty':
                    tmp_ReferralSource = 'Dr. Baker, Morty'
                elif tmp_ReferralName == 'Dr. Indig Jeffrey':
                    tmp_ReferralSource = 'Dr. Indig, Jeffrey'
                elif tmp_ReferralName == 'Dr. Dutil Martin':
                    tmp_ReferralSource = 'Dr. Dutil, Martin'
                elif tmp_ReferralName == 'Dr. Issa Rita':
                    tmp_ReferralSource = 'Dr. Issa, Rita'
                elif tmp_ReferralName == 'Dr. Rein Jeffrey':
                    tmp_ReferralSource = 'Dr. Rein, Jeffrey'
                elif tmp_ReferralName == 'Dr. Assef Gilbert':
                    tmp_ReferralSource = 'Dr. Assef, Gilbert'
                elif tmp_ReferralName == 'Dr. Azar Alain':
                    tmp_ReferralSource = 'Dr. Azar, Alain'
                elif tmp_ReferralName == 'Dr. Laprise-Demers Josee':
                    tmp_ReferralSource = 'Dr. Laprise-Demers, Josee'
                elif tmp_ReferralName == 'Dr. Tucci James':
                    tmp_ReferralSource = 'Dr. Tucci, James'
                elif tmp_ReferralName == 'Dr. Papageorgakopoulos Stamatia':
                    tmp_ReferralSource = 'Dr. Papageorgakopoulos, Stamatia'
                elif tmp_ReferralName == 'Dr. Cristiano Vincenzo':
                    tmp_ReferralSource = 'Dr. Vincenzo, Cristiano'
                elif tmp_ReferralName == 'Dr. Hanna Alkass Faraj':
                    tmp_ReferralSource = 'Dr. Hanna Alkass, Faraj'
                elif tmp_ReferralName == 'Dr. Mayantz Bernard':
                    tmp_ReferralSource = 'Dr. Mayantz, Bernard'
                elif tmp_ReferralName == 'Dr. Lindsey Jakubovic':
                    tmp_ReferralSource = 'Dr. Lindsey, Jakubovic'
                elif tmp_ReferralName == 'Dr. Harasymowycz George':
                    tmp_ReferralSource = 'Dr. Harasymowycz, George'
                elif tmp_ReferralName == 'Dr. Bonin Genevieve':
                    tmp_ReferralSource = 'Dr. Genevieve, Bonin '
                elif tmp_ReferralName == 'Dr. Manuel Bautista':
                    tmp_ReferralSource = 'Dr. Bautista, Manuel '
                elif tmp_ReferralName == 'Dr. Alanjian Hagop':
                    tmp_ReferralSource = 'Dr. Hagop, Alanjian'
                elif tmp_ReferralName == 'Dr. Beaulieu Bertrand':
                    tmp_ReferralSource = 'Dr. Beaulieu, Bertrand'
                elif tmp_ReferralName == 'Dr. Denis Forget':
                    tmp_ReferralSource = 'Dr. Forget, Denis'
                elif tmp_ReferralName == 'Dr. Bensaada Nadia':
                    tmp_ReferralSource = 'Dr. Bensaada, Nadia'
                elif tmp_ReferralName == 'Dr. Haswani Lina':
                    tmp_ReferralSource = 'Dr. Haswani, Lina'
                elif tmp_ReferralName == 'Dr. Mechanic Elliot':
                    tmp_ReferralSource = 'Dr. Mechanic, Elliot'
                elif tmp_ReferralName == 'Dr. Enache Lucien':
                    tmp_ReferralSource = 'Dr. Enache, Lucien'
                elif tmp_ReferralName == 'Dr. Baker David':
                    tmp_ReferralSource = 'Dr. Baker, David'
                elif tmp_ReferralName == 'Dr. Tran Bao-Nhu':
                    tmp_ReferralSource = 'Dr. Tran, Bao-Nhu'
                elif tmp_ReferralName == 'Dr. Bercovici Marcelo':
                    tmp_ReferralSource = 'Dr. Bercovici, Marcelo'
                elif tmp_ReferralName == 'Dr. Gamry Rim':
                    tmp_ReferralSource = 'Dr. Gamry, Rim'
                elif tmp_ReferralName == 'Dr. Turcotte Antony':
                    tmp_ReferralSource = 'Dr. Turcotte, Antony'
                elif tmp_ReferralName == 'Dr. Dac Nguyen':
                    tmp_ReferralSource = 'Dr. Nguyen, Dac '
                elif tmp_ReferralName == 'Dr. Wang Jue':
                    tmp_ReferralSource = 'Dr. Wang, Jue'
                elif tmp_ReferralName == 'Dr. Slepchik Lenny':
                    tmp_ReferralSource = 'Dr. Slepchik, Lenny'
                elif tmp_ReferralName == 'Dr. Harton Huguette':
                    tmp_ReferralSource = 'Dr. Harton, Huguette'
                elif tmp_ReferralName == 'Dr. Namjoonik Shiva':
                    tmp_ReferralSource = 'Dr. Namjoonik, Shiva'
                elif tmp_ReferralName == 'Dr. Nourmoussavi Anita':
                    tmp_ReferralSource = 'Dr. Nourmoussavi, Anita'
                elif tmp_ReferralName == 'Dr. Shamim Nazila':
                    tmp_ReferralSource = 'Dr. Shamim, Nazila'
                elif tmp_ReferralName == 'Dr. Leontidis Grace':
                    tmp_ReferralSource = 'Dr. Leontidis, Grace'
                elif tmp_ReferralName == 'Dr. Galvis Mauricio':
                    tmp_ReferralSource = 'Dr. Galvis, Mauricio'
                elif tmp_ReferralName == 'Dr. Faraj Hanna':
                    tmp_ReferralSource = 'Dr. Hanna Alkass, Faraj'
                elif tmp_ReferralName == 'Dr. Schwarz Karl':
                    tmp_ReferralSource = 'Dr. Schwarz, Karl'
                elif tmp_ReferralName == 'Dr. Ho Tam André':
                    tmp_ReferralSource = 'Dr. Ho Tam, André'
                elif tmp_ReferralName == 'Dr. Courtel Domitille':
                    tmp_ReferralSource = 'Dr. Courtel, Domitille'
                elif tmp_ReferralName == 'Dr. Pham Johanna':
                    tmp_ReferralSource = 'Dr. Pham, Johanna'
                elif tmp_ReferralName == 'Dr. Jecki Myriam':
                    tmp_ReferralSource = 'Dr. Jecki, Myriam'
                elif tmp_ReferralName == 'Dr. Shizgal Morty':
                    tmp_ReferralSource = 'Dr. Shizgal, Morty'
                elif tmp_ReferralName == 'Dr. Douglas Hamilton':
                    tmp_ReferralSource = 'Dr. Hamilton, Douglas'
                elif tmp_ReferralName == 'Dr. Racy Ly':
                    tmp_ReferralSource = 'Dr. Racy, Ly'
                elif tmp_ReferralName == 'Dr. El-Ansari Ahlam':
                    tmp_ReferralSource = 'Dr. El-Ansari, Ahlam'
                elif tmp_ReferralName == 'Dr. El Ansari, Ahlam':
                    tmp_ReferralSource = 'Dr. El-Ansari, Ahlam'
                elif tmp_ReferralName == 'Dr. Levesque Martin':
                    tmp_ReferralSource = 'Dr. Levesque, Martin'
                elif tmp_ReferralName == 'Dr. Vassiliadis Anthony':
                    tmp_ReferralSource = 'Dr. Vassiliadis, Anthony'
                elif tmp_ReferralName == 'Dr. Donald Collins':
                    tmp_ReferralSource = 'Dr. Collins, Donald'
                elif tmp_ReferralName == 'Dr. Nguyen Dam':
                    tmp_ReferralSource = 'Dr. Nguyen, Dam'
                elif tmp_ReferralName == 'Dr. Kuzina Victoria':
                    tmp_ReferralSource = 'Dr. Kuzina, Victoria'
                elif tmp_ReferralName == 'Dr. Muradali Sheri' or tmp_ReferralName == 'Dr. Muradali. Sheri':
                    tmp_ReferralSource = 'Dr. Muradali. Sheri'
                elif tmp_ReferralName == 'Dr. Lemieux Dominique':
                    tmp_ReferralSource = 'Dr. Lemieux, Dominique'
                elif tmp_ReferralName == 'Dr. Dolman Robert':
                    tmp_ReferralSource = 'Dr. Dolman, Robert'
                elif tmp_ReferralName == 'Dr. Sohmer Gerald':
                    tmp_ReferralSource = 'Dr. Sohmer, Gerald'
                elif tmp_ReferralName == 'Dr. George Hwang':
                    tmp_ReferralSource = 'Dr. Hwang, George'
                elif tmp_ReferralName == 'Dr. Rosario Ambayec':
                    tmp_ReferralSource = 'Dr. Rosario, Ambayec'
                elif tmp_ReferralName == 'Dr. Masri. Maher':
                    tmp_ReferralSource = 'Dr. Masri, Maher'
                elif tmp_ReferralName == 'Dr. Lacroix Vincent':
                    tmp_ReferralSource = 'Dr. Lacroix, Vincent'
                elif tmp_ReferralName == 'Dr. Bousquet Isabelle':
                    tmp_ReferralSource = 'Dr. Bousquet, Isabelle'
                elif tmp_ReferralName == 'Dr. Ubha Reena':
                    tmp_ReferralSource = 'Dr. Ubha, Reena'
                elif tmp_ReferralName == 'Dr. Basma Dabbagh':
                    tmp_ReferralSource = 'Dr. Basma, Dabbagh'
                elif tmp_ReferralName == 'Dr. Chiasson Geneviève':
                    tmp_ReferralSource = 'Dr. Chiasson, Geneviève'
                elif tmp_ReferralName == 'Dr. Obarian Tamara':
                    tmp_ReferralSource = 'Dr. Obarian, Tamara'
                elif tmp_ReferralName == 'Dr. Baghdassarian Rosemary':
                    tmp_ReferralSource = 'Dr. Baghdassarian, Rosemary'
                elif tmp_ReferralName == 'Dr. Dumoulin Jean Marc':
                    tmp_ReferralSource = 'Dr. Dumoulin, Jean Marc'
                elif tmp_ReferralName == 'Dr. Kandalett Tarek':
                    tmp_ReferralSource = 'Dr. Kandalett, Tarek'
                elif tmp_ReferralName == 'Dr. Ghanem Rana':
                    tmp_ReferralSource = 'Dr. Ghanem, Rana'
                elif tmp_ReferralName == 'Dr. Turkewicz Jack':
                    tmp_ReferralSource = 'Dr. Turkewicz, Jack'
                elif tmp_ReferralName == 'Dr. Ghatas Karim':
                    tmp_ReferralSource = 'Dr. Ghatas, Karim'
                elif tmp_ReferralName == 'Dr. Drummond John':
                    tmp_ReferralSource = 'Dr. Drummond, John'
                elif tmp_ReferralName == 'Dr. DSouza Marina':
                    tmp_ReferralSource = 'Dr. DSouza, Marina'
                elif tmp_ReferralName == 'Dr. Martin Michelle':
                    tmp_ReferralSource = 'Dr. Martin, Michelle'
                elif tmp_ReferralName == 'Dr. Criton Muller Nathalie':
                    tmp_ReferralSource = 'Dr. Criton Muller, Nathalie'
                elif tmp_ReferralName == 'Dr. Hilal Sirban':
                    tmp_ReferralSource = 'Dr. Hilal, Sirban'
                elif tmp_ReferralName == 'Dr. Laflamme Sara':
                    tmp_ReferralSource = 'Dr. Laflamme, Sara'
                elif tmp_ReferralName == 'Dr. Lavoie Frederic':
                    tmp_ReferralSource = 'Dr. Lavoie, Frederic'
                elif tmp_ReferralName == 'Dr. Benarroch Michael':
                    tmp_ReferralSource = 'Dr. Benarroch, Michael'
                elif tmp_ReferralName == 'Dr. Louis-René Charette':
                    tmp_ReferralSource = 'Dr. Charette, Louis-René'
                elif tmp_ReferralName == 'Dr. Omid Kiarash':
                    tmp_ReferralSource = 'Dr. Kiarash, Omid'
                elif tmp_ReferralName == 'Dr. Pierre Mackay':
                    tmp_ReferralSource = 'Dr. Mackay, Pierre '
                elif tmp_ReferralName == 'Dr. Mhanna Souzie':
                    tmp_ReferralSource = 'Dr. Mhanna, Souzie'
                elif tmp_ReferralName == 'Dre. Zina El-Guizawi':
                    tmp_ReferralSource = 'Dre. Zina, El-Guizawi'
                elif tmp_ReferralName == 'Dr. Vaillancourt Julie':
                    tmp_ReferralSource = 'Dr. Vaillancourt, Julie'
                elif tmp_ReferralName == 'Dr. Stephanisson Robert John':
                    tmp_ReferralSource = 'Dr. Stephanisson, Robert John'
                elif tmp_ReferralName == 'Dre Cristina Ionescu':
                    tmp_ReferralSource = 'Dre Cristina, Ionescu'
                elif tmp_ReferralName == 'Dr. Abou Khalil Zeina':
                    tmp_ReferralSource = 'Dr. Abou Khalil, Zeina'
                elif tmp_ReferralName == 'Dr. Tran Stefanny':
                    tmp_ReferralSource = 'Dr. Tran, Stefanny'
                elif tmp_ReferralName == 'Dr. Kordlouie Chahin':
                    tmp_ReferralSource = 'Dr. Kordlouie, Chahin'
                elif tmp_ReferralName == 'Dr. Darich La':
                    tmp_ReferralSource = 'Dr. Darich, La'
                elif tmp_ReferralName == 'Dr. Mcmullan John Francis':
                    tmp_ReferralSource = 'Dr. Mcmullan, John Francis'
                elif tmp_ReferralName == 'Dr. Nguyen Le Tuyen Jean':
                    tmp_ReferralSource = 'Dr. Nguyen, Le Tuyen Jean'
                elif tmp_ReferralName == 'Dr. Carere James':
                    tmp_ReferralSource = 'Dr. Carere, James'
                elif tmp_ReferralName == 'Dr. Tshy Aaron':
                    tmp_ReferralSource = 'Dr. Tshy, Aaron'
                elif tmp_ReferralName == 'Dr. Lussier Joanne':
                    tmp_ReferralSource = 'Dr. Lussier, Joanne'
                elif tmp_ReferralName == 'Dr. Doan, Duy Chinh':
                    tmp_ReferralSource = 'Dr.  Doan, Duy-Chinh'
                elif tmp_ReferralName == '' or tmp_ReferralName is None or tmp_ReferralName == 'nan':
                    tmp_ReferralSource = 'INTERNET'
                else:
                    tmp_ReferralSource = tmp_ReferralName

                if tmp_ReferralSource == '' or tmp_ReferralSource is None or tmp_ReferralSource == 'nan':
                    message_error_referral = f'Problem with Referral Name. File {file}, line {i+1}'
                    print(Fore.RED, message_error_referral)
                else:
                    pass

                df_clean_data = df_clean_data.append(dict(Provider=tmp_Provider, ProcedureCode=tmp_ProcedureCode,
                                                          Revenue=tmp_Revenue, Date=tmp_Date, Month=tmp_Month,
                                                          Year=tmp_Year, MonthYear=tmp_MonthYear,
                                                          FiscalYear=tmp_FiscalYear, Patient=tmp_Patient,
                                                          ReferralSource=tmp_ReferralSource), ignore_index=True)

            i += 1

        message1 = f'Successfully extracted {i} procedures from {file}.'
        print(Fore.GREEN, message1)
        j = i + j

    message2 = f'Total procedures extracted: {j}.'
    print(Fore.GREEN, message2)

    pbi_file_location = 'C:\\Projects\\SeaforthPBI\\PBIFiles\\'
    df_clean_data.to_excel(pbi_file_location + 'Prod_by_Prov.xlsx', sheet_name='data', index=False)


if __name__ == '__main__':
    clean_production_data()
