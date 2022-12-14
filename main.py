import pandas as pd
from rumus import Fuzzy as fz

dataset = 'data/world_population.csv'

rd = pd.read_csv(dataset)

# TAHUN
rd_2022 = rd['2022 Population']
rd_2020 = rd['2020 Population']
rd_2015 = rd['2015 Population']
rd_2010 = rd['2010 Population']
rd_2000 = rd['2000 Population']
rd_1990 = rd['1990 Population']
rd_1980 = rd['1980 Population']
rd_1970 = rd['1970 Population']
rd_area = rd['Area (km²)']
rd_density = rd['Density (per km²)']
rd_growth = rd['Growth Rate']
rd_percentage = rd['World Population Percentage']


populasi_2022 = []
for i in rd_2022:
    country = rd['Country'][rd['2022 Population']==i]
    Low = fz.linearturun(10000000,250000000,i)
    Intermediate = fz.Segitiga(10000000,34000000,1400000000,i)
    High = fz.linearnaik(750000000,1400000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_2022.append(dict)

populasi_2020 = []
for i in rd_2020:
    country = rd['Country'][rd['2020 Population']==i]
    Low = fz.linearturun(12000000,33000000,i)
    Intermediate = fz.Segitiga(12000000,33000000,1400000000,i)
    High = fz.linearnaik(33000000,1400000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_2020.append(dict)

populasi_2015 = []
for i in rd_2015:
    country = rd['Country'][rd['2015 Population']==i]
    Low = fz.linearturun(15000000,31000000,i)
    Intermediate = fz.Segitiga(15000000,31000000,1300000000,i)
    High = fz.linearnaik(31000000,1300000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_2015.append(dict)

populasi_2010 = []
for i in rd_2010:
    country = rd['Country'][rd['2010 Population']==i]
    Low = fz.linearturun(16000000,29000000,i)
    Intermediate = fz.Segitiga(16000000,29000000,1300000000,i)
    High = fz.linearnaik(29000000,1300000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_2010.append(dict)

populasi_2000 = []
for i in rd_2000:
    country = rd['Country'][rd['2000 Population']==i]
    Low = fz.linearturun(18000000,26000000,i)
    Intermediate = fz.Segitiga(18000000,26000000,1200000000,i)
    High = fz.linearnaik(26000000,1200000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_2000.append(dict)

populasi_1990 = []
for i in rd_1990:
    country = rd['Country'][rd['1990 Population']==i]
    Low = fz.linearturun(18500000,22000000,i)
    Intermediate = fz.Segitiga(18500000,22000000,1100000000,i)
    High = fz.linearnaik(22000000,1100000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_1990.append(dict)

populasi_1980 = []
for i in rd_1980:
    country = rd['Country'][rd['1980 Population']==i]
    Low = fz.linearturun(1800000,21000000,i)
    Intermediate = fz.Segitiga(18800000,21000000,982000000,i)
    High = fz.linearnaik(21000000,982000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_1980.append(dict)

populasi_1970 = []
for i in rd_1970:
    country = rd['Country'][rd['1970 Population']==i]
    Low = fz.linearturun(19000000,20000000,i)
    Intermediate = fz.Segitiga(19000000,20000000,822000000,i)
    High = fz.linearnaik(20000000,822000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    populasi_1970.append(dict)

percentage = []
for i in rd_percentage:
    country = rd['Country'][rd['World Population Percentage']==i]
    Low = fz.linearturun(0.1,6,i)
    Intermediate = fz.Segitiga(0.1,6,17,i)
    High = fz.linearnaik(0.1,6.17,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    percentage.append(dict)

growth = []
for i in rd_growth:
    country = rd['Country'][rd['Growth Rate']==i]
    Low = fz.linearturun(0.01,1.008,i)
    Intermediate = fz.Segitiga(0.01,1.008,1.8,i)
    High = fz.linearnaik(1.008,1.8,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    growth.append(dict)

density = []
for i in rd_density:
    country = rd['Country'][rd['Density (per km²)']==i]
    Low = fz.linearturun(0.2,452,i)
    Intermediate = fz.Segitiga(0.2,452,23.000,i)
    High = fz.linearnaik(452,23000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    density.append(dict)

area = []
for i in rd_area:
    country = rd['Country'][rd['Area (km²)']==i]
    Low = fz.linearturun(50,581000,i)
    Intermediate = fz.Segitiga(50,581000,17000000,i)
    High = fz.linearnaik(581000,17000000,i)

    dict = {
        'Negara': f'{country}',
        'M [Low]': f'{Low}',
        'M [Intermediate]': f'{Intermediate}',
        'M [High]': f'{High}',
    }
    area.append(dict)



df1 = pd.DataFrame(populasi_2022)
df2 = pd.DataFrame(populasi_2020)
df3 = pd.DataFrame(populasi_2015)
df4 = pd.DataFrame(populasi_2010)
df5 = pd.DataFrame(populasi_2000)
df6 = pd.DataFrame(populasi_1990)
df7 = pd.DataFrame(populasi_1980)
df8 = pd.DataFrame(populasi_1970)
df9 = pd.DataFrame(area)
df10 = pd.DataFrame(density)
df11 = pd.DataFrame(growth)
df12 = pd.DataFrame(percentage)



with pd.ExcelWriter('output/Populasi.xlsx') as writer:
    df1.to_excel(writer, sheet_name='2022')
    df2.to_excel(writer, sheet_name='2020')
    df3.to_excel(writer, sheet_name='2015')
    df4.to_excel(writer, sheet_name='2010')
    df5.to_excel(writer, sheet_name='2000')
    df6.to_excel(writer, sheet_name='1990')
    df7.to_excel(writer, sheet_name='1980')
    df8.to_excel(writer, sheet_name='1970')
    df9.to_excel(writer, sheet_name='Area')
    df10.to_excel(writer, sheet_name='Density')
    df11.to_excel(writer, sheet_name='Growth')
    df12.to_excel(writer, sheet_name='Percentage')

