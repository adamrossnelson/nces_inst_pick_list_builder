import pandas as pd
import requests
import zipfile
import os

# Use this code to download the latest higher edcuationdirectory information 
# from the National Center for Education Statistics (NCES).

# Jul/2017  Adam Ross Nelson - Initial build.
# Aug/2019  Adam Ross Nelson - GitHub rebuild.

print('''/*#############################################################################
      Maintained/more information at:
      https://github.com/adamrossnelson/nces_inst_pick_list_builder
##############################################################################*''')

# Set parameters
currentdir = os.getcwd()
year = '2017'
nceszipfile = r'HD{}_Data_Stata.zip'.format(year)
ncescsvfile = r'HD{}_Data_Stata.csv'.format(year)

print('Downloading NCES {} institutional directory information.'.format(year))
url = 'https://nces.ed.gov/ipeds/datacenter/data/{}'.format(nceszipfile)
r = requests.get(url)

print('Writing {}{}'.format(currentdir, nceszipfile))
with open(nceszipfile, 'wb') as f:
    f.write(r.content)

print('Extracting {}{}'.format(currentdir, nceszipfile))
with zipfile.ZipFile(nceszipfile, 'r') as zip_ref:
    zip_ref.extractall('.')

print('Reading {}{}'.format(currentdir, ncescsvfile))
df = pd.read_csv(ncescsvfile, encoding='ISO-8859-1')

df['NAME'] = df['INSTNM'] + ', ' + df['UNITID'].astype(str)
df = df[['STABBR','NAME','SECTOR']]
df = df.sort_values(by=['STABBR','NAME']).reset_index(drop=True)


df[df['SECTOR'] == 1].to_csv('1_nces_inst_pick_listPub_4-yr.csv', 
                             index=False,
                             header=False)

df[df['SECTOR'] == 2].to_csv('2_nces_inst_pick_listPri_not-for-profit_4-yr.csv', 
                             index=False,
                             header=False)

df[df['SECTOR'] == 3].to_csv('3_nces_inst_pick_listPri_for-profit_4-yr.csv', 
                             index=False,
                             header=False)

df[df['SECTOR'] == 4].to_csv('4_nces_inst_pick_listPub_2-yr.csv', 
                             index=False,
                             header=False)

df[df['SECTOR'] == 5].to_csv('5_nces_inst_pick_listPri_not-for-profit_2-yr.csv', 
                             index=False,
                             header=False)

df[df['SECTOR'] == 6].to_csv('6_nces_inst_pick_listPri_for-profit_2-yr.csv', 
                             index=False,
                             header=False)

df[df['SECTOR'] == 7].to_csv('7_nces_inst_pick_listPub_less-than_2-yr.csv', 
                             index=False,
                             header=False)

df[(df['SECTOR'] > 7) & \
   (df['SECTOR'] < 99)].to_csv('8_nces_inst_pick_listOth_Private_less_than_2-years.csv', 
                                                index=False,
                                                header=False)

print('''/*#############################################################################
      Saved pick list files in the current working directory:
##############################################################################*/''')
