#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAC4 _ Visualització de dades

@author: carlotafont
"""

'''
    Importation of libraries
'''
import pandas as pd
import numpy as np

'''
    Import data
'''

# Import csv file
df = pd.read_csv('/Users/carlotafont/Documents/UOC/S4 - 2020_09/Visualització de dades/pax_all_agreements_data.csv', ',')
# Check df
print(df.head())


'''
    Clean data
'''

# Substitute all N/A values for empty values
df.fillna('', inplace = True)


'''
    Subset atributes of interest

'''
# Select Country, Region, Length, Number of characters, 
df_sub = df[['Con', 'Reg','Lgt','N_characters','Loc1ISO']]

# Add one column, which stands for 1 agreement
df_sub['NrAg'] = 1
print(df_sub.head())

# Save the file in the directory, which is ready for importation to Tableau
#df_sub.to_excel('/Users/carlotafont/Documents/UOC/S4 - 2020_09/Visualització de dades/data_pac4.xlsx', index=False)

'''
    Sum table to compute average character and page length
'''
# Sum tables per country and region
dfsum_con = pd.pivot_table(df_sub, values=['Lgt','N_characters', 'NrAg'], index=['Con'], aggfunc=sum)
dfsum_reg = pd.pivot_table(df_sub, values=['Lgt', 'N_characters', 'NrAg'], index=['Reg'], aggfunc=np.sum)

# Aggregate average page and character length per agreement and per country and region, as well as average character length per page
dfsum_con['Lgt_Avg'] = dfsum_con['Lgt']/dfsum_con['NrAg']
dfsum_con['NCh_Avg'] = dfsum_con['N_characters']/dfsum_con['NrAg']
dfsum_con['NchLgt_Avg'] = dfsum_con['N_characters']/dfsum_con['Lgt']
dfsum_reg['Lgt_Avg'] = dfsum_reg['Lgt']/dfsum_reg['NrAg']
dfsum_reg['NCh_Avg'] = dfsum_reg['N_characters']/dfsum_reg['NrAg']
dfsum_reg['NchLgt_Avg'] = dfsum_reg['N_characters']/dfsum_reg['Lgt']


# Save them into excel to import to Tableau
dfsum_con.to_excel('/Users/carlotafont/Documents/UOC/S4 - 2020_09/Visualització de dades/sum_con.xlsx', index=True)
dfsum_reg.to_excel('/Users/carlotafont/Documents/UOC/S4 - 2020_09/Visualització de dades/sum_reg.xlsx', index=True)



