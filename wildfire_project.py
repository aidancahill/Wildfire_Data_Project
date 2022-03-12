from ast import match_case
from unicodedata import name
import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

#This line reads the data into a a pandas dataframe#
df = pd.read_csv('California_Fire_Perimeters_(all).csv')

#fills any empty cause rows with 14 the unidentified ignition source#
df['CAUSE'].fillna(14, inplace = True)
#fill any empty gis acre rows with 0#
df['GIS_ACRES'].fillna(0, inplace = True)

#change the gis acre feature from string variables to float#
df['GIS_ACRES'] = df['GIS_ACRES'].astype(str).astype(float)
#change the cause from float to int type#
df['CAUSE'] = df['CAUSE'].astype(float).astype(int)
#change the alarm date column to a date time variable with yyyy/mm/dd format#
df['ALARM_DATE'] = pd.to_datetime(df['ALARM_DATE'], errors='coerce')

#create seperate dataframes based on the ignition source and create there respictive names#
Lightning = df.loc[df.CAUSE == 1, :]
Lightning.name = 'Lightning'
Equipment_Use = df.loc[df.CAUSE == 2, :]
Equipment_Use.name = 'Equiment Use'
Smoking = df.loc[df.CAUSE == 3, :]
Smoking.name = 'Smoking'
Campfire = df.loc[df.CAUSE == 4, :]
Campfire.name = 'Campfire'
Debris = df.loc[df.CAUSE == 5, :]
Debris.name = 'Debris'
Railroad = df.loc[df.CAUSE == 6, :]
Railroad.name = 'Railroad'
Arson = df.loc[df.CAUSE == 7, :]
Arson.name = 'Arson'
Playing_with_Fire = df.loc[df.CAUSE == 8, :]
Playing_with_Fire.name = 'Playing With Fire'
Miscellaneous = df.loc[df.CAUSE == 9, :]
Miscellaneous.name = 'Miscellaneous'
Vehicle = df.loc[df.CAUSE == 10, :]
Vehicle.name = 'Vehicle'
Power_Line = df.loc[df.CAUSE == 11, :]
Power_Line.name = 'Power Line'
Firefighter_Training = df.loc[df.CAUSE == 12, :]
Firefighter_Training.name = 'Firefighter Training'
Non_Firefighter_Training = df.loc[df.CAUSE == 13, :]
Non_Firefighter_Training.name = 'Non Firefighter Training'
Unidentified = df.loc[df.CAUSE == 14, :]
Unidentified.name =  'Unidentified'
Structure = df.loc[df.CAUSE == 15, :]
Structure.name = 'Structure'
Aircraft = df.loc[df.CAUSE == 16, :]
Aircraft.name = 'Aircraft'
Volcanic = df.loc[df.CAUSE == 17, :]
Volcanic.name = 'Volcanic'
Escaped_Prescribed_Burn = df.loc[df.CAUSE == 18, :]
Escaped_Prescribed_Burn.name = 'Escaped Prescribed Burn'
Illegal_Alien_Campfire = df.loc[df.CAUSE == 19, :]
Illegal_Alien_Campfire.name = 'Illegal Alien Campfire'

#create a list of the ignition types based on there name and the order in which they occur#
#1 corresponding with lightning and 19 with illegal alien campfire#
caused_by = ['Lightning','Equipment Use','Smoking','Campfire','Debris','Railroad','Arson','Playing with Fire','Miscellaneous','Vehicle','Power Line','Firefighter Training','Non-Firefighter Training','Unidentified','Structure','Aircraft','Volcanic','Escaped Prescribed Burn','Illegal Alien Campfire']
#create a list with the months of the year#
months_of_the_year = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


#a function that creates a list of the total acres burned by ignition source#
#the total acres burned by that ignition source is adding all the rows of the GIS ACRES#
#column and creating a list of the toal acres burned by ignition source#
#then plots this using matplotlib#
def total_acres_burned() :
    tab_Light = Lightning.loc[ : , 'GIS_ACRES'].sum()
    tab_Equip = Equipment_Use.loc[ : , 'GIS_ACRES'].sum() 
    tab_Smoking = Smoking.loc[ : , 'GIS_ACRES'].sum()
    tab_Campfire = Campfire.loc[ : , 'GIS_ACRES'].sum()
    tab_Debris = Debris.loc[ : , 'GIS_ACRES'].sum()
    tab_Railroad = Railroad.loc[ : , 'GIS_ACRES'].sum()
    tab_Arson = Arson.loc[ : , 'GIS_ACRES'].sum()
    tab_Playing_with_Fire = Playing_with_Fire.loc[ : , 'GIS_ACRES'].sum()
    tab_Miscellaneous = Miscellaneous.loc[ : , 'GIS_ACRES'].sum()
    tab_Vehicle = Vehicle.loc[ : , 'GIS_ACRES'].sum()
    tab_PowerLine = Power_Line.loc[ : , 'GIS_ACRES'].sum()
    tab_Firefighter_Training = Firefighter_Training.loc[ : , 'GIS_ACRES'].sum()
    tab_Non_Firefighter_Training = Non_Firefighter_Training.loc[ : , 'GIS_ACRES'].sum()
    tab_Unidentified = Unidentified.loc[ : , 'GIS_ACRES'].sum()
    tab_Structure = Structure.loc[ : , 'GIS_ACRES'].sum()
    tab_Aircraft = Aircraft.loc[ : , 'GIS_ACRES'].sum()
    tab_Volcanic = Volcanic.loc[ : , 'GIS_ACRES'].sum()
    tab_Escaped_Prescribed_Burn = Escaped_Prescribed_Burn.loc[ : , 'GIS_ACRES'].sum()
    tab_Illegal_Alien_Campfire = Illegal_Alien_Campfire.loc[ : , 'GIS_ACRES'].sum()

    
    total_acres_burned = [tab_Light,tab_Equip,tab_Smoking,tab_Campfire,tab_Debris,tab_Railroad,tab_Arson,tab_Playing_with_Fire,tab_Miscellaneous,tab_Vehicle,tab_PowerLine,tab_Firefighter_Training,tab_Non_Firefighter_Training,tab_Unidentified,tab_Structure,tab_Aircraft,tab_Volcanic,tab_Escaped_Prescribed_Burn,tab_Illegal_Alien_Campfire]

    mpl.bar(caused_by,total_acres_burned)
    mpl.title('Total Acres Burned by Category')
    mpl.xlabel('Fires Ignited By', fontsize=14)
    mpl.ylabel('Total Acres Burned', fontsize=14)
    mpl.xticks(rotation = 90)
    mpl.grid(True)
    mpl.show()

#a function that creates seperate datframes based on the total counts of fires regardless#
#of ignition type but just counts the number fires during a respective month#
#stores the fire count per month from 1950-2021 in a list then plots this using matplotlib#
def number_of_fires():
    fire_count_Jan = df.loc[(df.ALARM_DATE.dt.month == 1), :]
    fire_count_Feb = df.loc[(df.ALARM_DATE.dt.month == 2), :]
    fire_count_Mar = df.loc[(df.ALARM_DATE.dt.month == 3), :]
    fire_count_Apr = df.loc[(df.ALARM_DATE.dt.month == 4), :]
    fire_count_May = df.loc[(df.ALARM_DATE.dt.month == 5), :]
    fire_count_Jun = df.loc[(df.ALARM_DATE.dt.month == 6), :]
    fire_count_Jul = df.loc[(df.ALARM_DATE.dt.month == 7), :]
    fire_count_Aug = df.loc[(df.ALARM_DATE.dt.month == 8), :]
    fire_count_Sep = df.loc[(df.ALARM_DATE.dt.month == 9), :]
    fire_count_Oct = df.loc[(df.ALARM_DATE.dt.month == 10), :]
    fire_count_Nov = df.loc[(df.ALARM_DATE.dt.month == 11), :]
    fire_count_Dec = df.loc[(df.ALARM_DATE.dt.month == 12), :]

    fire_count_per_month = [fire_count_Jan.shape[0], fire_count_Feb.shape[0], fire_count_Mar.shape[0], fire_count_Apr.shape[0], fire_count_May.shape[0], fire_count_Jun.shape[0], fire_count_Jul.shape[0], fire_count_Aug.shape[0], fire_count_Sep.shape[0], fire_count_Oct.shape[0], fire_count_Nov.shape[0], fire_count_Dec.shape[0]]

    mpl.bar(months_of_the_year,fire_count_per_month)
    mpl.title('Count of Fires Per Month From 1950 - 2021')
    mpl.xlabel('Months of the Year', fontsize=14)
    mpl.ylabel('# of Fires', fontsize=14)
    mpl.xticks(rotation = 90)
    mpl.grid(True)
    mpl.show()

#a function that creates a list of the average acres burned by ignition source#
#then plots these on a bar chart and returns a list of the average acres burned list#
#by ignition type#
def average_acres_burned():
    aab_Light = Lightning.loc[ : , 'GIS_ACRES'].mean()
    aab_Equip = Equipment_Use.loc[ : , 'GIS_ACRES'].mean() 
    aab_Smoking = Smoking.loc[ : , 'GIS_ACRES'].mean()
    aab_Campfire = Campfire.loc[ : , 'GIS_ACRES'].mean()
    aab_Debris = Debris.loc[ : , 'GIS_ACRES'].mean()
    aab_Railroad = Railroad.loc[ : , 'GIS_ACRES'].mean()
    aab_Arson = Arson.loc[ : , 'GIS_ACRES'].mean()
    aab_Playing_with_Fire = Playing_with_Fire.loc[ : , 'GIS_ACRES'].mean()
    aab_Miscellaneous = Miscellaneous.loc[ : , 'GIS_ACRES'].mean()
    aab_Vehicle = Vehicle.loc[ : , 'GIS_ACRES'].mean()
    aab_PowerLine = Power_Line.loc[ : , 'GIS_ACRES'].mean()
    aab_Firefighter_Training = Firefighter_Training.loc[ : , 'GIS_ACRES'].mean()
    aab_Non_Firefighter_Training = Non_Firefighter_Training.loc[ : , 'GIS_ACRES'].mean()
    aab_Unidentified = Unidentified.loc[ : , 'GIS_ACRES'].mean()
    aab_Structure = Structure.loc[ : , 'GIS_ACRES'].mean()
    aab_Aircraft = Aircraft.loc[ : , 'GIS_ACRES'].mean()
    aab_Volcanic = Volcanic.loc[ : , 'GIS_ACRES'].mean()
    aab_Escaped_Prescribed_Burn = Escaped_Prescribed_Burn.loc[ : , 'GIS_ACRES'].mean()
    aab_Illegal_Alien_Campfire = Illegal_Alien_Campfire.loc[ : , 'GIS_ACRES'].mean()
    
    average_acres_burned = [aab_Light,aab_Equip,aab_Smoking,aab_Campfire,aab_Debris,aab_Railroad,aab_Arson,aab_Playing_with_Fire,aab_Miscellaneous,aab_Vehicle,aab_PowerLine,aab_Firefighter_Training,aab_Non_Firefighter_Training,aab_Unidentified,aab_Structure,aab_Aircraft,aab_Volcanic,aab_Escaped_Prescribed_Burn,aab_Illegal_Alien_Campfire]

    mpl.bar(caused_by,average_acres_burned)
    mpl.title('Average Acres Burned by Causation')
    mpl.xlabel('Fires Ignited By', fontsize=14)
    mpl.ylabel('Average Fire Size', fontsize=14)
    mpl.xticks(rotation = 90)
    mpl.grid(True)
    mpl.show()
    return average_acres_burned

#a function that seperates the main dataframe into smaller dataframes that#
#are designated by its ignition type and every month in the year the ignition source#
#is present so everytime from 1950-2021 a lightning fire happened in the month of january#
#there is a respective datframe for it, for every ignition source and every month#
#then storing the count of the number of rows or occurences into a list, so the count#
#of lightning fires during january is first and so on until december#
def correlation_between_cause_month():
    Lightning_Jan = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 1), :]
    Lightning_Feb = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 2), :]
    Lightning_Mar = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 3), :]
    Lightning_Apr = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 4), :]
    Lightning_May = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 5), :]
    Lightning_Jun = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 6), :]
    Lightning_Jul = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 7), :]
    Lightning_Aug = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 8), :]
    Lightning_Sep = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 9), :]
    Lightning_Oct = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 10), :]
    Lightning_Nov = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 11), :]
    Lightning_Dec = df.loc[(df.CAUSE == 1) & (df.ALARM_DATE.dt.month == 12), :]


    Lightning_fires_per_month = [Lightning_Jan.shape[0], Lightning_Feb.shape[0], Lightning_Mar.shape[0], Lightning_Apr.shape[0], Lightning_May.shape[0], Lightning_Jun.shape[0], Lightning_Jul.shape[0], Lightning_Aug.shape[0], Lightning_Sep.shape[0], Lightning_Oct.shape[0], Lightning_Nov.shape[0], Lightning_Dec.shape[0]]

    Equipment_Jan = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 1), :]
    Equipment_Feb = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 2), :]
    Equipment_Mar = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 3), :]
    Equipment_Apr = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 4), :]
    Equipment_May = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 5), :]
    Equipment_Jun = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 6), :]
    Equipment_Jul = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 7), :]
    Equipment_Aug = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 8), :]
    Equipment_Sep = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 9), :]
    Equipment_Oct = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 10), :]
    Equipment_Nov = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 11), :]
    Equipment_Dec = df.loc[(df.CAUSE == 2) & (df.ALARM_DATE.dt.month == 12), :]

    Equipment_fires_per_month = [Equipment_Jan.shape[0], Equipment_Feb.shape[0], Equipment_Mar.shape[0], Equipment_Apr.shape[0], Equipment_May.shape[0], Equipment_Jun.shape[0], Equipment_Jul.shape[0], Equipment_Aug.shape[0], Equipment_Sep.shape[0], Equipment_Oct.shape[0], Equipment_Nov.shape[0], Equipment_Dec.shape[0]]

    Smoking_Jan = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 1), :]
    Smoking_Feb = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 2), :]
    Smoking_Mar = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 3), :]
    Smoking_Apr = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 4), :]
    Smoking_May = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 5), :]
    Smoking_Jun = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 6), :]
    Smoking_Jul = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 7), :]
    Smoking_Aug = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 8), :]
    Smoking_Sep = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 9), :]
    Smoking_Oct = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 10), :]
    Smoking_Nov = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 11), :]
    Smoking_Dec = df.loc[(df.CAUSE == 3) & (df.ALARM_DATE.dt.month == 12), :]

    Smoking_fires_per_month = [Smoking_Jan.shape[0], Smoking_Feb.shape[0], Smoking_Mar.shape[0], Smoking_Apr.shape[0], Smoking_May.shape[0], Smoking_Jun.shape[0], Smoking_Jul.shape[0], Smoking_Aug.shape[0], Smoking_Sep.shape[0], Smoking_Oct.shape[0], Smoking_Nov.shape[0], Smoking_Dec.shape[0]]

    Campfire_Jan = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 1), :]
    Campfire_Feb = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 2), :]
    Campfire_Mar = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 3), :]
    Campfire_Apr = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 4), :]
    Campfire_May = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 5), :]
    Campfire_Jun = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 6), :]
    Campfire_Jul = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 7), :]
    Campfire_Aug = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 8), :]
    Campfire_Sep = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 9), :]
    Campfire_Oct = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 10), :]
    Campfire_Nov = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 11), :]
    Campfire_Dec = df.loc[(df.CAUSE == 4) & (df.ALARM_DATE.dt.month == 12), :]

    Campfire_fires_per_month = [Campfire_Jan.shape[0], Campfire_Feb.shape[0], Campfire_Mar.shape[0], Campfire_Apr.shape[0], Campfire_May.shape[0], Campfire_Jun.shape[0], Campfire_Jul.shape[0], Campfire_Aug.shape[0], Campfire_Sep.shape[0], Campfire_Oct.shape[0], Campfire_Nov.shape[0], Campfire_Dec.shape[0]]

    Debris_Jan = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 1), :]
    Debris_Feb = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 2), :]
    Debris_Mar = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 3), :]
    Debris_Apr = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 4), :]
    Debris_May = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 5), :]
    Debris_Jun = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 6), :]
    Debris_Jul = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 7), :]
    Debris_Aug = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 8), :]
    Debris_Sep = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 9), :]
    Debris_Oct = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 10), :]
    Debris_Nov = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 11), :]
    Debris_Dec = df.loc[(df.CAUSE == 5) & (df.ALARM_DATE.dt.month == 12), :]

    Debris_fires_per_month = [Debris_Jan.shape[0], Debris_Feb.shape[0], Debris_Mar.shape[0], Debris_Apr.shape[0], Debris_May.shape[0], Debris_Jun.shape[0], Debris_Jul.shape[0], Debris_Aug.shape[0], Debris_Sep.shape[0], Debris_Oct.shape[0], Debris_Nov.shape[0], Debris_Dec.shape[0]]

    Railroad_Jan = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 1), :]
    Railroad_Feb = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 2), :]
    Railroad_Mar = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 3), :]
    Railroad_Apr = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 4), :]
    Railroad_May = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 5), :]
    Railroad_Jun = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 6), :]
    Railroad_Jul = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 7), :]
    Railroad_Aug = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 8), :]
    Railroad_Sep = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 9), :]
    Railroad_Oct = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 10), :]
    Railroad_Nov = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 11), :]
    Railroad_Dec = df.loc[(df.CAUSE == 6) & (df.ALARM_DATE.dt.month == 12), :]

    Railroad_fires_per_month = [Railroad_Jan.shape[0],Railroad_Feb.shape[0],Railroad_Mar.shape[0],Railroad_Apr.shape[0],Railroad_May.shape[0],Railroad_Jun.shape[0],Railroad_Jul.shape[0],Railroad_Aug.shape[0],Railroad_Sep.shape[0],Railroad_Oct.shape[0],Railroad_Nov.shape[0],Railroad_Dec.shape[0]]

    Arson_Jan = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 1), :]
    Arson_Feb = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 2), :]
    Arson_Mar = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 3), :]
    Arson_Apr = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 4), :]
    Arson_May = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 5), :]
    Arson_Jun = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 6), :]
    Arson_Jul = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 7), :]
    Arson_Aug = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 8), :]
    Arson_Sep = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 9), :]
    Arson_Oct = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 10), :]
    Arson_Nov = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 11), :]
    Arson_Dec = df.loc[(df.CAUSE == 7) & (df.ALARM_DATE.dt.month == 12), :]

    Arson_fires_per_month = [Arson_Jan.shape[0], Arson_Feb.shape[0], Arson_Mar.shape[0], Arson_Apr.shape[0], Arson_May.shape[0], Arson_Jun.shape[0], Arson_Jul.shape[0], Arson_Aug.shape[0], Arson_Sep.shape[0], Arson_Oct.shape[0], Arson_Nov.shape[0], Arson_Dec.shape[0]]

    Playing_Jan = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 1), :]
    Playing_Feb = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 2), :]
    Playing_Mar = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 3), :]
    Playing_Apr = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 4), :]
    Playing_May = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 5), :]
    Playing_Jun = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 6), :]
    Playing_Jul = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 7), :]
    Playing_Aug = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 8), :]
    Playing_Sep = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 9), :]
    Playing_Oct = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 10), :]
    Playing_Nov = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 11), :]
    Playing_Dec = df.loc[(df.CAUSE == 8) & (df.ALARM_DATE.dt.month == 12), :]

    Playing_fires_per_month = [Playing_Jan.shape[0], Playing_Feb.shape[0], Playing_Mar.shape[0], Playing_Apr.shape[0], Playing_May.shape[0], Playing_Jun.shape[0], Playing_Jul.shape[0], Playing_Aug.shape[0], Playing_Sep.shape[0], Playing_Oct.shape[0], Playing_Nov.shape[0], Playing_Dec.shape[0]]

    Miscellaneous_Jan = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 1), :]
    Miscellaneous_Feb = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 2), :]
    Miscellaneous_Mar = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 3), :]
    Miscellaneous_Apr = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 4), :]
    Miscellaneous_May = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 5), :]
    Miscellaneous_Jun = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 6), :]
    Miscellaneous_Jul = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 7), :]
    Miscellaneous_Aug = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 8), :]
    Miscellaneous_Sep = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 9), :]
    Miscellaneous_Oct = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 10), :]
    Miscellaneous_Nov = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 11), :]
    Miscellaneous_Dec = df.loc[(df.CAUSE == 9) & (df.ALARM_DATE.dt.month == 12), :]

    Miscellaneous_fires_per_month = [Miscellaneous_Jan.shape[0], Miscellaneous_Feb.shape[0], Miscellaneous_Mar.shape[0], Miscellaneous_Apr.shape[0], Miscellaneous_May.shape[0], Miscellaneous_Jun.shape[0], Miscellaneous_Jul.shape[0], Miscellaneous_Aug.shape[0], Miscellaneous_Sep.shape[0], Miscellaneous_Oct.shape[0], Miscellaneous_Nov.shape[0], Miscellaneous_Dec.shape[0]]

    Vehicle_Jan = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 1), :]
    Vehicle_Feb = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 2), :]
    Vehicle_Mar = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 3), :]
    Vehicle_Apr = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 4), :]
    Vehicle_May = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 5), :]
    Vehicle_Jun = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 6), :]
    Vehicle_Jul = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 7), :]
    Vehicle_Aug = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 8), :]
    Vehicle_Sep = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 9), :]
    Vehicle_Oct = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 10), :]
    Vehicle_Nov = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 11), :]
    Vehicle_Dec = df.loc[(df.CAUSE == 10) & (df.ALARM_DATE.dt.month == 12), :]

    Vehicle_fires_per_month = [Vehicle_Jan.shape[0], Vehicle_Feb.shape[0], Vehicle_Mar.shape[0], Vehicle_Apr.shape[0], Vehicle_May.shape[0], Vehicle_Jun.shape[0], Vehicle_Jul.shape[0], Vehicle_Aug.shape[0], Vehicle_Sep.shape[0], Vehicle_Oct.shape[0], Vehicle_Nov.shape[0], Vehicle_Dec.shape[0]]

    Powerline_Jan = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 1), :]
    Powerline_Feb = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 2), :]
    Powerline_Mar = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 3), :]
    Powerline_Apr = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 4), :]
    Powerline_May = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 5), :]
    Powerline_Jun = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 6), :]
    Powerline_Jul = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 7), :]
    Powerline_Aug = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 8), :]
    Powerline_Sep = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 9), :]
    Powerline_Oct = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 10), :]
    Powerline_Nov = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 11), :]
    Powerline_Dec = df.loc[(df.CAUSE == 11) & (df.ALARM_DATE.dt.month == 12), :]

    Powerline_fires_per_month = [Powerline_Jan.shape[0], Powerline_Feb.shape[0], Powerline_Mar.shape[0], Powerline_Apr.shape[0], Powerline_May.shape[0], Powerline_Jun.shape[0], Powerline_Jul.shape[0], Powerline_Aug.shape[0], Powerline_Sep.shape[0], Powerline_Oct.shape[0], Powerline_Nov.shape[0], Powerline_Dec.shape[0]]

    Firefighter_training_Jan = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 1), :]
    Firefighter_training_Feb = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 2), :]
    Firefighter_training_Mar = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 3), :]
    Firefighter_training_Apr = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 4), :]
    Firefighter_training_May = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 5), :]
    Firefighter_training_Jun = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 6), :]
    Firefighter_training_Jul = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 7), :]
    Firefighter_training_Aug = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 8), :]
    Firefighter_training_Sep = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 9), :]
    Firefighter_training_Oct = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 10), :]
    Firefighter_training_Nov = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 11), :]
    Firefighter_training_Dec = df.loc[(df.CAUSE == 12) & (df.ALARM_DATE.dt.month == 12), :]

    Firefighter_training_fires_per_month = [Firefighter_training_Jan.shape[0], Firefighter_training_Feb.shape[0], Firefighter_training_Mar.shape[0], Firefighter_training_Apr.shape[0], Firefighter_training_May.shape[0], Firefighter_training_Jun.shape[0], Firefighter_training_Jul.shape[0], Firefighter_training_Aug.shape[0], Firefighter_training_Sep.shape[0], Firefighter_training_Oct.shape[0], Firefighter_training_Nov.shape[0], Firefighter_training_Dec.shape[0]]

    Non_firefighter_training_Jan = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 1), :]
    Non_firefighter_training_Feb = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 2), :]
    Non_firefighter_training_Mar = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 3), :]
    Non_firefighter_training_Apr = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 4), :]
    Non_firefighter_training_May = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 5), :]
    Non_firefighter_training_Jun = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 6), :]
    Non_firefighter_training_Jul = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 7), :]
    Non_firefighter_training_Aug = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 8), :]
    Non_firefighter_training_Sep = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 9), :]
    Non_firefighter_training_Oct = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 10), :]
    Non_firefighter_training_Nov = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 11), :]
    Non_firefighter_training_Dec = df.loc[(df.CAUSE == 13) & (df.ALARM_DATE.dt.month == 12), :]

    Non_firefighter_training_fires_per_month = [Non_firefighter_training_Jan.shape[0], Non_firefighter_training_Feb.shape[0], Non_firefighter_training_Mar.shape[0], Non_firefighter_training_Apr.shape[0], Non_firefighter_training_May.shape[0], Non_firefighter_training_Jun.shape[0], Non_firefighter_training_Jul.shape[0], Non_firefighter_training_Aug.shape[0], Non_firefighter_training_Sep.shape[0], Non_firefighter_training_Oct.shape[0], Non_firefighter_training_Nov.shape[0], Non_firefighter_training_Dec.shape[0]]

    Unidentified_Jan = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 1), :]
    Unidentified_Feb = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 2), :]
    Unidentified_Mar = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 3), :]
    Unidentified_Apr = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 4), :]
    Unidentified_May = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 5), :]
    Unidentified_Jun = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 6), :]
    Unidentified_Jul = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 7), :]
    Unidentified_Aug = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 8), :]
    Unidentified_Sep = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 9), :]
    Unidentified_Oct = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 10), :]
    Unidentified_Nov = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 11), :]
    Unidentified_Dec = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 12), :]

    Unidentified_fires_per_month = [Unidentified_Jan.shape[0],Unidentified_Feb.shape[0],Unidentified_Mar.shape[0],Unidentified_Apr.shape[0],Unidentified_May.shape[0],Unidentified_Jun.shape[0],Unidentified_Jul.shape[0],Unidentified_Aug.shape[0],Unidentified_Sep.shape[0],Unidentified_Oct.shape[0],Unidentified_Nov.shape[0],Unidentified_Dec.shape[0]]

    Structure_Jan = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 1), :]
    Structure_Feb = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 2), :]
    Structure_Mar = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 3), :]
    Structure_Apr = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 4), :]
    Structure_May = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 5), :]
    Structure_Jun = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 6), :]
    Structure_Jul = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 7), :]
    Structure_Aug = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 8), :]
    Structure_Sep = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 9), :]
    Structure_Oct = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 10), :]
    Structure_Nov = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 11), :]
    Structure_Dec = df.loc[(df.CAUSE == 15) & (df.ALARM_DATE.dt.month == 12), :]

    Structure_fires_per_month = [Structure_Jan.shape[0], Structure_Feb.shape[0], Structure_Mar.shape[0], Structure_Apr.shape[0], Structure_May.shape[0], Structure_Jun.shape[0], Structure_Jul.shape[0], Structure_Aug.shape[0], Structure_Sep.shape[0], Structure_Oct.shape[0], Structure_Nov.shape[0], Structure_Dec.shape[0]]

    Aircraft_Jan = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 1), :]
    Aircraft_Feb = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 2), :]
    Aircraft_Mar = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 3), :]
    Aircraft_Apr = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 4), :]
    Aircraft_May = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 5), :]
    Aircraft_Jun = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 6), :]
    Aircraft_Jul = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 7), :]
    Aircraft_Aug = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 8), :]
    Aircraft_Sep = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 9), :]
    Aircraft_Oct = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 10), :]
    Aircraft_Nov = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 11), :]
    Aircraft_Dec = df.loc[(df.CAUSE == 16) & (df.ALARM_DATE.dt.month == 12), :]

    Aircraft_fires_per_month = [Aircraft_Jan.shape[0], Aircraft_Feb.shape[0], Aircraft_Mar.shape[0], Aircraft_Apr.shape[0], Aircraft_May.shape[0], Aircraft_Jun.shape[0], Aircraft_Jul.shape[0], Aircraft_Aug.shape[0], Aircraft_Sep.shape[0], Aircraft_Oct.shape[0], Aircraft_Nov.shape[0], Aircraft_Dec.shape[0]]

    Volcanic_Jan = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 1), :]
    Volcanic_Feb = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 2), :]
    Volcanic_Mar = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 3), :]
    Volcanic_Apr = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 4), :]
    Volcanic_May = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 5), :]
    Volcanic_Jun = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 6), :]
    Volcanic_Jul = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 7), :]
    Volcanic_Aug = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 8), :]
    Volcanic_Sep = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 9), :]
    Volcanic_Oct = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 10), :]
    Volcanic_Nov = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 11), :]
    Volcanic_Dec = df.loc[(df.CAUSE == 17) & (df.ALARM_DATE.dt.month == 12), :]

    Volcanic_fires_per_month = [Volcanic_Jan.shape[0], Volcanic_Feb.shape[0], Volcanic_Mar.shape[0], Volcanic_Apr.shape[0], Volcanic_May.shape[0], Volcanic_Jun.shape[0], Volcanic_Jul.shape[0], Volcanic_Aug.shape[0], Volcanic_Sep.shape[0], Volcanic_Oct.shape[0], Volcanic_Nov.shape[0], Volcanic_Dec.shape[0]]

    Escaped_prescribed_Jan = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 1), :]
    Escaped_prescribed_Feb = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 2), :]
    Escaped_prescribed_Mar = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 3), :]
    Escaped_prescribed_Apr = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 4), :]
    Escaped_prescribed_May = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 5), :]
    Escaped_prescribed_Jun = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 6), :]
    Escaped_prescribed_Jul = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 7), :]
    Escaped_prescribed_Aug = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 8), :]
    Escaped_prescribed_Sep = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 9), :]
    Escaped_prescribed_Oct = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 10), :]
    Escaped_prescribed_Nov = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 11), :]
    Escaped_prescribed_Dec = df.loc[(df.CAUSE == 18) & (df.ALARM_DATE.dt.month == 12), :]

    Escaped_prescribed_fires_per_month = [Escaped_prescribed_Jan.shape[0], Escaped_prescribed_Feb.shape[0], Escaped_prescribed_Mar.shape[0], Escaped_prescribed_Apr.shape[0], Escaped_prescribed_May.shape[0], Escaped_prescribed_Jun.shape[0], Escaped_prescribed_Jul.shape[0], Escaped_prescribed_Aug.shape[0], Escaped_prescribed_Sep.shape[0], Escaped_prescribed_Oct.shape[0], Escaped_prescribed_Nov.shape[0], Escaped_prescribed_Dec.shape[0]]

    Illegal_alien_Jan = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 1), :]
    Illegal_alien_Feb = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 2), :]
    Illegal_alien_Mar = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 3), :]
    Illegal_alien_Apr = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 4), :]
    Illegal_alien_May = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 5), :]
    Illegal_alien_Jun = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 6), :]
    Illegal_alien_Jul = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 7), :]
    Illegal_alien_Aug = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 8), :]
    Illegal_alien_Sep = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 9), :]
    Illegal_alien_Oct = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 10), :]
    Illegal_alien_Nov = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 11), :]
    Illegal_alien_Dec = df.loc[(df.CAUSE == 19) & (df.ALARM_DATE.dt.month == 12), :]

    Illegal_alien_fires_per_month = [Illegal_alien_Jan.shape[0], Illegal_alien_Feb.shape[0], Illegal_alien_Mar.shape[0], Illegal_alien_Apr.shape[0], Illegal_alien_May.shape[0], Illegal_alien_Jun.shape[0], Illegal_alien_Jul.shape[0], Illegal_alien_Aug.shape[0], Illegal_alien_Sep.shape[0], Illegal_alien_Oct.shape[0], Illegal_alien_Nov.shape[0], Illegal_alien_Dec.shape[0]]

    #these next functions then find the respective greatest number of fire ignition source for#
    #every month from january until december, the problem that was ran into was that these#
    #functions were all returning unidentified ignition source as the greatest fire count for#
    #each month so then copying the geatest cause list then setting the unidentified source count#
    #to zero then find the second greatest cause output the corresponding month and the#
    #the most amount of fire ignition sources during that month#
    def greatest_cause_jan():

        cause_in_Jan = [Lightning_Jan.shape[0], Equipment_Jan.shape[0], Smoking_Jan.shape[0], Campfire_Jan.shape[0], Debris_Jan.shape[0], Railroad_Jan.shape[0], Arson_Jan.shape[0], Playing_Jan.shape[0], Miscellaneous_Jan.shape[0], Vehicle_Jan.shape[0], Powerline_Jan.shape[0], Firefighter_training_Jan.shape[0], Non_firefighter_training_Jan.shape[0], Unidentified_Jan.shape[0], Structure_Jan.shape[0], Aircraft_Jan.shape[0], Volcanic_Jan.shape[0], Escaped_prescribed_Jan.shape[0], Illegal_alien_Jan.shape[0]]
        
        greatest_cause = max(cause_in_Jan)

        cause = cause_in_Jan.index(greatest_cause)

        sec_greatest_cause_in_Jan = cause_in_Jan

        sec_greatest_cause_in_Jan[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Jan)

        sec_cause = sec_greatest_cause_in_Jan.index(sec_greatest_cause)

        print("January had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_jan()

    def greatest_cause_feb():

        cause_in_Feb = [Lightning_Feb.shape[0], Equipment_Feb.shape[0], Smoking_Feb.shape[0], Campfire_Feb.shape[0], Debris_Feb.shape[0], Railroad_Feb.shape[0], Arson_Feb.shape[0], Playing_Feb.shape[0], Miscellaneous_Feb.shape[0], Vehicle_Feb.shape[0], Powerline_Feb.shape[0], Firefighter_training_Feb.shape[0], Non_firefighter_training_Feb.shape[0], Unidentified_Feb.shape[0], Structure_Feb.shape[0], Aircraft_Feb.shape[0], Volcanic_Feb.shape[0], Escaped_prescribed_Feb.shape[0], Illegal_alien_Feb.shape[0]]
        
        greatest_cause = max(cause_in_Feb)

        cause = cause_in_Feb.index(greatest_cause)

        sec_greatest_cause_in_Feb = cause_in_Feb

        sec_greatest_cause_in_Feb[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Feb)

        sec_cause = sec_greatest_cause_in_Feb.index(sec_greatest_cause)


        print("Febuary had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_feb()

    def greatest_cause_mar():

        cause_in_Mar = [Lightning_Mar.shape[0], Equipment_Mar.shape[0], Smoking_Mar.shape[0], Campfire_Mar.shape[0], Debris_Mar.shape[0], Railroad_Mar.shape[0], Arson_Mar.shape[0], Playing_Mar.shape[0], Miscellaneous_Mar.shape[0], Vehicle_Mar.shape[0], Powerline_Mar.shape[0], Firefighter_training_Mar.shape[0], Non_firefighter_training_Mar.shape[0], Unidentified_Mar.shape[0], Structure_Mar.shape[0], Aircraft_Mar.shape[0], Volcanic_Mar.shape[0], Escaped_prescribed_Mar.shape[0], Illegal_alien_Mar.shape[0]]
        
        greatest_cause = max(cause_in_Mar)

        cause = cause_in_Mar.index(greatest_cause)

        sec_greatest_cause_in_Mar = cause_in_Mar

        sec_greatest_cause_in_Mar[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Mar)

        sec_cause = sec_greatest_cause_in_Mar.index(sec_greatest_cause)


        print("March had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_mar()

    def greatest_cause_apr():

        cause_in_Apr = [Lightning_Apr.shape[0], Equipment_Apr.shape[0], Smoking_Apr.shape[0], Campfire_Apr.shape[0], Debris_Apr.shape[0], Railroad_Apr.shape[0], Arson_Apr.shape[0], Playing_Apr.shape[0], Miscellaneous_Apr.shape[0], Vehicle_Apr.shape[0], Powerline_Apr.shape[0], Firefighter_training_Apr.shape[0], Non_firefighter_training_Apr.shape[0], Unidentified_Apr.shape[0], Structure_Apr.shape[0], Aircraft_Apr.shape[0], Volcanic_Apr.shape[0], Escaped_prescribed_Apr.shape[0], Illegal_alien_Apr.shape[0]]
        
        greatest_cause = max(cause_in_Apr)

        cause = cause_in_Apr.index(greatest_cause)

        sec_greatest_cause_in_Apr = cause_in_Apr

        sec_greatest_cause_in_Apr[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Apr)

        sec_cause = sec_greatest_cause_in_Apr.index(sec_greatest_cause)


        print("April had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_apr()

    def greatest_cause_may():

        cause_in_May = [Lightning_May.shape[0], Equipment_May.shape[0], Smoking_May.shape[0], Campfire_May.shape[0], Debris_May.shape[0], Railroad_May.shape[0], Arson_May.shape[0], Playing_May.shape[0], Miscellaneous_May.shape[0], Vehicle_May.shape[0], Powerline_May.shape[0], Firefighter_training_May.shape[0], Non_firefighter_training_May.shape[0], Unidentified_May.shape[0], Structure_May.shape[0], Aircraft_May.shape[0], Volcanic_May.shape[0], Escaped_prescribed_May.shape[0], Illegal_alien_May.shape[0]]
        
        greatest_cause = max(cause_in_May)

        cause = cause_in_May.index(greatest_cause)

        sec_greatest_cause_in_May = cause_in_May

        sec_greatest_cause_in_May[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_May)

        sec_cause = sec_greatest_cause_in_May.index(sec_greatest_cause)


        print("May had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_may()

    def greatest_cause_jun():

        cause_in_Jun = [Lightning_Jun.shape[0], Equipment_Jun.shape[0], Smoking_Jun.shape[0], Campfire_Jun.shape[0], Debris_Jun.shape[0], Railroad_Jun.shape[0], Arson_Jun.shape[0], Playing_Jun.shape[0], Miscellaneous_Jun.shape[0], Vehicle_Jun.shape[0], Powerline_Jun.shape[0], Firefighter_training_Jun.shape[0], Non_firefighter_training_Jun.shape[0], Unidentified_Jun.shape[0], Structure_Jun.shape[0], Aircraft_Jun.shape[0], Volcanic_Jun.shape[0], Escaped_prescribed_Jun.shape[0], Illegal_alien_Jun.shape[0]]
        
        greatest_cause = max(cause_in_Jun)

        cause = cause_in_Jun.index(greatest_cause)

        sec_greatest_cause_in_Jun = cause_in_Jun

        sec_greatest_cause_in_Jun[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Jun)

        sec_cause = sec_greatest_cause_in_Jun.index(sec_greatest_cause)


        print("June had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_jun()

    def greatest_cause_jul():

        cause_in_Jul = [Lightning_Jul.shape[0], Equipment_Jul.shape[0], Smoking_Jul.shape[0], Campfire_Jul.shape[0], Debris_Jul.shape[0], Railroad_Jul.shape[0], Arson_Jul.shape[0], Playing_Jul.shape[0], Miscellaneous_Jul.shape[0], Vehicle_Jul.shape[0], Powerline_Jul.shape[0], Firefighter_training_Jul.shape[0], Non_firefighter_training_Jul.shape[0], Unidentified_Jul.shape[0], Structure_Jul.shape[0], Aircraft_Jul.shape[0], Volcanic_Jul.shape[0], Escaped_prescribed_Jul.shape[0], Illegal_alien_Jul.shape[0]]
        
        greatest_cause = max(cause_in_Jul)

        cause = cause_in_Jul.index(greatest_cause)

        sec_greatest_cause_in_Jul = cause_in_Jul

        sec_greatest_cause_in_Jul[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Jul)

        sec_cause = sec_greatest_cause_in_Jul.index(sec_greatest_cause)


        print("July had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_jul()

    def greatest_cause_aug():

        cause_in_Aug = [Lightning_Aug.shape[0], Equipment_Aug.shape[0], Smoking_Aug.shape[0], Campfire_Aug.shape[0], Debris_Aug.shape[0], Railroad_Aug.shape[0], Arson_Aug.shape[0], Playing_Aug.shape[0], Miscellaneous_Aug.shape[0], Vehicle_Aug.shape[0], Powerline_Aug.shape[0], Firefighter_training_Aug.shape[0], Non_firefighter_training_Aug.shape[0], Unidentified_Aug.shape[0], Structure_Aug.shape[0], Aircraft_Aug.shape[0], Volcanic_Aug.shape[0], Escaped_prescribed_Aug.shape[0], Illegal_alien_Aug.shape[0]]
        
        greatest_cause = max(cause_in_Aug)

        cause = cause_in_Aug.index(greatest_cause)

        sec_greatest_cause_in_Aug = cause_in_Aug

        sec_greatest_cause_in_Aug[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Aug)

        sec_cause = sec_greatest_cause_in_Aug.index(sec_greatest_cause)


        print("August had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_aug()

    def greatest_cause_sep():

        cause_in_Sep = [Lightning_Sep.shape[0], Equipment_Sep.shape[0], Smoking_Sep.shape[0], Campfire_Sep.shape[0], Debris_Sep.shape[0], Railroad_Sep.shape[0], Arson_Sep.shape[0], Playing_Sep.shape[0], Miscellaneous_Sep.shape[0], Vehicle_Sep.shape[0], Powerline_Sep.shape[0], Firefighter_training_Sep.shape[0], Non_firefighter_training_Sep.shape[0], Unidentified_Sep.shape[0], Structure_Sep.shape[0], Aircraft_Sep.shape[0], Volcanic_Sep.shape[0], Escaped_prescribed_Sep.shape[0], Illegal_alien_Sep.shape[0]]
        
        greatest_cause = max(cause_in_Sep)

        cause = cause_in_Sep.index(greatest_cause)

        sec_greatest_cause_in_Sep = cause_in_Sep

        sec_greatest_cause_in_Sep[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Sep)

        sec_cause = sec_greatest_cause_in_Sep.index(sec_greatest_cause)


        print("September had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")


    greatest_cause_sep()

    def greatest_cause_oct():

        cause_in_Oct = [Lightning_Oct.shape[0], Equipment_Oct.shape[0], Smoking_Oct.shape[0], Campfire_Oct.shape[0], Debris_Oct.shape[0], Railroad_Oct.shape[0], Arson_Oct.shape[0], Playing_Oct.shape[0], Miscellaneous_Oct.shape[0], Vehicle_Oct.shape[0], Powerline_Oct.shape[0], Firefighter_training_Oct.shape[0], Non_firefighter_training_Oct.shape[0], Unidentified_Oct.shape[0], Structure_Oct.shape[0], Aircraft_Oct.shape[0], Volcanic_Oct.shape[0], Escaped_prescribed_Oct.shape[0], Illegal_alien_Oct.shape[0]]
        
        greatest_cause = max(cause_in_Oct)

        cause = cause_in_Oct.index(greatest_cause)

        sec_greatest_cause_in_Oct = cause_in_Oct

        sec_greatest_cause_in_Oct[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Oct)

        sec_cause = sec_greatest_cause_in_Oct.index(sec_greatest_cause)


        print("October had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")

    greatest_cause_oct()

    def greatest_cause_nov():

        cause_in_Nov = [Lightning_Nov.shape[0], Equipment_Nov.shape[0], Smoking_Nov.shape[0], Campfire_Nov.shape[0], Debris_Nov.shape[0], Railroad_Nov.shape[0], Arson_Nov.shape[0], Playing_Nov.shape[0], Miscellaneous_Nov.shape[0], Vehicle_Nov.shape[0], Powerline_Nov.shape[0], Firefighter_training_Nov.shape[0], Non_firefighter_training_Nov.shape[0], Unidentified_Nov.shape[0], Structure_Nov.shape[0], Aircraft_Nov.shape[0], Volcanic_Nov.shape[0], Escaped_prescribed_Nov.shape[0], Illegal_alien_Nov.shape[0]]
        
        greatest_cause = max(cause_in_Nov)

        cause = cause_in_Nov.index(greatest_cause)

        sec_greatest_cause_in_Nov = cause_in_Nov

        sec_greatest_cause_in_Nov[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Nov)

        sec_cause = sec_greatest_cause_in_Nov.index(sec_greatest_cause)


        print("November had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")
        print("-------------------------------------------------------------------------------------")

    greatest_cause_nov()

    def greatest_cause_dec():

        cause_in_Dec = [Lightning_Dec.shape[0], Equipment_Dec.shape[0], Smoking_Dec.shape[0], Campfire_Dec.shape[0], Debris_Dec.shape[0], Railroad_Dec.shape[0], Arson_Dec.shape[0], Playing_Dec.shape[0], Miscellaneous_Dec.shape[0], Vehicle_Dec.shape[0], Powerline_Dec.shape[0], Firefighter_training_Dec.shape[0], Non_firefighter_training_Dec.shape[0], Unidentified_Dec.shape[0], Structure_Dec.shape[0], Aircraft_Dec.shape[0], Volcanic_Dec.shape[0], Escaped_prescribed_Dec.shape[0], Illegal_alien_Dec.shape[0]]
        
        greatest_cause = max(cause_in_Dec)

        cause = cause_in_Dec.index(greatest_cause)

        sec_greatest_cause_in_Dec = cause_in_Dec

        sec_greatest_cause_in_Dec[cause] = 0

        sec_greatest_cause = max(sec_greatest_cause_in_Dec)

        sec_cause = sec_greatest_cause_in_Dec.index(sec_greatest_cause)


        print("December had", greatest_cause, caused_by[cause], "fires,", "the second largest ingition source was", caused_by[sec_cause], "with", sec_greatest_cause, "fires.")

    greatest_cause_dec()

#this function is the the embodying function that calculates risk based on a risk matrix#
#the risk calculator takes a pandas dataframe as on argument, to calculate the overall#
#risk it divides the number of fire ignition types by the overall number of fires#
def risk_calculator(this):
    
    def overall_risk(this):
        return this.shape[0] / df.shape[0]
    
    #this risk calculator calculates it based on the numbers fires without#
    #counting the unidentified fires because if they are unidentified then#
    #calculating the risk that is associated with it does not have substance#
    def with_out_unidentified_risk(this):
        return this.shape[0] / (df.shape[0] - Unidentified.shape[0])

    #these next functions calculate the risk that is associated with the specific#
    #dataframe fire ignition source during the corresponding month. it does this by#
    #taking the overall fire count for that month and subtracts the unidentified#
    #fire count from it then is the denominator and the fire ignition source count#
    #for the specific month is the numerator#
    def risk_jan(this):

        fire_count_jan = df.loc[(df.ALARM_DATE.dt.month == 1), :]
        Unidentified_Jan = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 1), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 1)]

        return ignition_count.shape[0] / (fire_count_jan.shape[0] - Unidentified_Jan.shape[0])

    def risk_feb(this):

        fire_count_feb = df.loc[(df.ALARM_DATE.dt.month == 2), :]
        Unidentified_Feb = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 2), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 2)]

        return ignition_count.shape[0] / (fire_count_feb.shape[0] - Unidentified_Feb.shape[0])

    def risk_mar(this):

        fire_count_mar = df.loc[(df.ALARM_DATE.dt.month == 3), :]
        Unidentified_Mar = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 3), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 3)]

        return ignition_count.shape[0] / (fire_count_mar.shape[0] - Unidentified_Mar.shape[0])

    def risk_apr(this):

        fire_count_apr = df.loc[(df.ALARM_DATE.dt.month == 4), :]
        Unidentified_Apr = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 4), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 4)]

        return ignition_count.shape[0] / (fire_count_apr.shape[0] - Unidentified_Apr.shape[0])

    def risk_may(this):

        fire_count_may = df.loc[(df.ALARM_DATE.dt.month == 5), :]
        Unidentified_May = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 5), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 5)]

        return ignition_count.shape[0] / (fire_count_may.shape[0] - Unidentified_May.shape[0])

    def risk_jun(this):

        fire_count_jun = df.loc[(df.ALARM_DATE.dt.month == 6), :]
        Unidentified_Jun = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 6), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 6)]

        return ignition_count.shape[0] / (fire_count_jun.shape[0] - Unidentified_Jun.shape[0])

    def risk_jul(this):

        fire_count_jul = df.loc[(df.ALARM_DATE.dt.month == 7), :]
        Unidentified_Jul = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 7), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 7)]

        return ignition_count.shape[0] / (fire_count_jul.shape[0] - Unidentified_Jul.shape[0])

    def risk_aug(this):

        fire_count_aug = df.loc[(df.ALARM_DATE.dt.month == 8), :]
        Unidentified_Aug = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 8), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 8)]

        return ignition_count.shape[0] / (fire_count_aug.shape[0] - Unidentified_Aug.shape[0])

    def risk_sep(this):

        fire_count_sep = df.loc[(df.ALARM_DATE.dt.month == 9), :]
        Unidentified_Sep = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 9), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 9)]

        return ignition_count.shape[0] / (fire_count_sep.shape[0] - Unidentified_Sep.shape[0])
    
    def risk_oct(this):

        fire_count_oct = df.loc[(df.ALARM_DATE.dt.month == 10), :]
        Unidentified_Oct = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 10), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 10)]

        return ignition_count.shape[0] / (fire_count_oct.shape[0] - Unidentified_Oct.shape[0])

    def risk_nov(this):

        fire_count_nov = df.loc[(df.ALARM_DATE.dt.month == 11), :]
        Unidentified_Nov = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 11), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 11)]

        return ignition_count.shape[0] / (fire_count_nov.shape[0] - Unidentified_Nov.shape[0])

    def risk_dec(this):

        fire_count_dec = df.loc[(df.ALARM_DATE.dt.month == 1), :]
        Unidentified_Dec = df.loc[(df.CAUSE == 14) & (df.ALARM_DATE.dt.month == 1), :]
        ignition_count = this.loc[(df.ALARM_DATE.dt.month == 1)]

        return ignition_count.shape[0] / (fire_count_dec.shape[0] - Unidentified_Dec.shape[0])
    
    #the risk matrix is 5 x 5 matrix with the left most column the risk percentage#
    #and the top row the average fire size in acres, traversing the matrix gives#
    #you the risk number (1-3 low risk), (4-6 moderate risk), (8-10 high risk)#
    #(12-16 extreme risk)
    risk_matrix = [["0", "0 - 999", "1000 - 1999", "2000 - 2999", "3000 - 3999"],
                    ["0 - 0.0199%", 1, 2, 3, 4],
                    [".02 - 0.0499%", 2, 4, 6, 8],
                    [".05 - 00.1499%", 3, 6, 9, 12],
                    ["0.1500% <=", 4, 8, 12, 16]]
    
    #accepts input from the user to decide what month to analyze a#
    #fire ignition source's risk based on the month chosen#
    print ("Enter the month number to find out how Risky a", this.name, "fire will be  during that month")
    print("Enter 0 to find out the overall risk of", this.name, "fires")

    for (i, item) in enumerate(months_of_the_year, start=1):
        print(i, item)

    month = int(input(""))
    
    risk_by_ignition = 0
    ignition_and_month = 0

#this conditional then runs the risk calculator based on the month chosen#
#by the user#
    if month == 0:
        risk_by_ignition = overall_risk(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 1]
    elif month == 1:
        risk_by_ignition = risk_jan(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 1]
    elif month == 2:
        risk_by_ignition = risk_feb(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 2]
    elif month == 3:
        risk_by_ignition = risk_mar(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 3]
    elif month == 4:
        risk_by_ignition = risk_apr(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 4]
    elif month == 5:
        risk_by_ignition = risk_may(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 5]
    elif month == 6:
        risk_by_ignition = risk_jun(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 6]
    elif month == 7:
        risk_by_ignition = risk_jul(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 7]
    elif month == 8:
        risk_by_ignition = risk_aug(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 8]
    elif month == 9:
        risk_by_ignition = risk_sep(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 9]
    elif month == 10:
        risk_by_ignition = risk_oct(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 10]
    elif month == 11:
        risk_by_ignition = risk_nov(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 11]
    elif month == 12:
        risk_by_ignition = risk_dec(this)
        ignition_and_month = this.loc[this.ALARM_DATE.dt.month == 12]

    #the below statement takes the average fire size by ignition source chosen#
    #but it calculates the average fire size for that ignition source based on the#
    #month that was chosen and not on the avaerage fire size based on ignition#
    #for all months#
    ignition_and_average_acres_burned = ignition_and_month.loc[ : , 'GIS_ACRES'].mean()
    risk = 0

    #this conditional statement traverses the matrix based on the calulated risk#
    #percentage for that month and the average fire size based on month and ignition type#
    if (risk_by_ignition <= .0199) & (ignition_and_average_acres_burned <= 999):
        risk = risk_matrix[1][1]
    elif (risk_by_ignition <= .0199) & (ignition_and_average_acres_burned <= 1999):
        risk = risk_matrix[1][2]
    elif (risk_by_ignition <= .0199) & (ignition_and_average_acres_burned <= 2999):
        risk = risk_matrix[1][3]
    elif (risk_by_ignition <= .0199) & (ignition_and_average_acres_burned <= 3999):
        risk = risk_matrix[1][4]
    elif (risk_by_ignition <= .0499) & (ignition_and_average_acres_burned <= 999):
        risk = risk_matrix[2][1]
    elif (risk_by_ignition <= .0499) & (ignition_and_average_acres_burned <= 1999):
        risk = risk_matrix[2][2]
    elif (risk_by_ignition <= .0499) & (ignition_and_average_acres_burned <= 2999):
        risk = risk_matrix[2][3]
    elif (risk_by_ignition <= .0499) & (ignition_and_average_acres_burned <= 3999):
        risk = risk_matrix[2][4]
    elif (risk_by_ignition <= .1499) & (ignition_and_average_acres_burned <= 999):
        risk = risk_matrix[3][1]
    elif (risk_by_ignition <= .1499) & (ignition_and_average_acres_burned <= 1999):
        risk = risk_matrix[3][2]
    elif (risk_by_ignition <= .1499) & (ignition_and_average_acres_burned <= 2999):
        risk = risk_matrix[3][3]
    elif (risk_by_ignition <= .1499) & (ignition_and_average_acres_burned <= 3999):
        risk = risk_matrix[3][4]
    elif (risk_by_ignition >= .1599) & (ignition_and_average_acres_burned <= 999):
        risk = risk_matrix[4][1]
    elif (risk_by_ignition >= .1599) & (ignition_and_average_acres_burned <= 1999):
        risk = risk_matrix[4][2]
    elif (risk_by_ignition >= .1599) & (ignition_and_average_acres_burned <= 2999):
        risk = risk_matrix[4][3]
    elif (risk_by_ignition >= .1599) & ((ignition_and_average_acres_burned <= 3999) | (ignition_and_average_acres_burned > 3999)):
        risk = risk_matrix[4][4]

    risk_level = ""

    #this conditional checks what the value that the risk was assigned to#
    #based on that value the the risk level (1-3 low risk), (4-6 moderate risk), (8-10 high risk)#
    #(12-16 extreme risk)#
    if risk <= 3:
        risk_level = "Low Risk"
    elif (risk > 3) & (risk <= 6):
        risk_level = "Moderate Risk"
    elif (risk > 6) & (risk <= 10):
        risk_level = "High Risk"
    elif (risk > 10) & (risk <= 16):
        risk_level = "Extreme Risk"

    #the overall risk is printed for a certain ignition source if the month is set to 0#
    #if the month is greater than 0 the risk level is printed to the console and#
    #how that risk level is associated to the month and ignition source#
    if month == 0:
        print("The overall risk associated with a fire started by a", this.name, "is", risk_level)
    elif month > 0:
        print ("There is a", risk_level, "associated with a fire that is started by", this.name, "during", months_of_the_year[month - 1])

#within the main program the user is asked to input a number that is associated to an#
#ignition source (1-Lightning,...,19-Illegal Alien Campfire)#
#once the month is inputed by the user the specfic ignition source is#
#used as an argument for the risk calculator function call#
#the overall risk can be assesed based on all months or#
#the risk of a specific month can be assesed as well#
print("Enter the number of the Fire Ignition Source to find its  risk")

for (i, item) in enumerate(caused_by, start=1):
    print(i, item)

ignition_type = int(input(""))

if (ignition_type - 1) == (caused_by.index('Lightning')):
    risk_calculator(Lightning)
elif (ignition_type - 1) == (caused_by.index('Equipment Use')):
    risk_calculator(Equipment_Use)
elif (ignition_type - 1) == (caused_by.index('Smoking')):
    risk_calculator(Smoking)
elif (ignition_type - 1) == (caused_by.index('Campfire')):
    risk_calculator(Campfire)
elif (ignition_type - 1) == (caused_by.index('Debris')):
    risk_calculator(Debris)
elif (ignition_type - 1) == (caused_by.index('Railroad')):
    risk_calculator(Railroad)
elif (ignition_type - 1) == (caused_by.index('Arson')):
    risk_calculator(Arson)
elif (ignition_type - 1) == (caused_by.index('Playing with Fire')):
    risk_calculator(Playing_with_Fire)
elif (ignition_type - 1) == (caused_by.index('Miscellaneous')):
    risk_calculator(Miscellaneous)
elif (ignition_type - 1) == (caused_by.index('Vehicle')):
    risk_calculator(Vehicle)
elif (ignition_type - 1) == (caused_by.index('Power Line')):
    risk_calculator(Power_Line)
elif (ignition_type - 1) == (caused_by.index('Firefighter Training')):
    risk_calculator(Firefighter_Training)
elif (ignition_type - 1) == (caused_by.index('Non-Firefighter Training')):
    risk_calculator(Non_Firefighter_Training)
elif (ignition_type - 1) == (caused_by.index('Unidentified')):
    risk_calculator(Unidentified)
elif (ignition_type - 1) == (caused_by.index('Structure')):
    risk_calculator(Structure)
elif (ignition_type - 1) == (caused_by.index('Aircraft')):
    risk_calculator(Aircraft)
elif (ignition_type - 1) == (caused_by.index('Volcanic')):
    risk_calculator(Volcanic)
elif (ignition_type - 1) == (caused_by.index('Escaped Prescribed Burn')):
    risk_calculator(Escaped_Prescribed_Burn)
elif (ignition_type - 1) == (caused_by.index('Illegal Alien Campfire')):
    risk_calculator(Illegal_Alien_Campfire)

