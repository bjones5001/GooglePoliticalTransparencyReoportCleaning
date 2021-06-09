#!/usr/bin/env python

#load pandas
import pandas as pd

#use pandas to load our csv
df = pd.read_csv("/home/usr/Downloads/google-political-ads-transparency-bundle/google-political-ads-creative-stats.csv")

#set the key value to advertiser id
df.set_index("Advertiser_ID", inplace=True)
df1 = df.loc[['AR105500339708362752',
              'AR38159238236733440',
              'AR462410610177474560',
              'AR427507713065353216',
              'AR470412855804428288',
              'AR92331695100919808',
              'AR285644324803182592',
              'AR121262938404159488',
              'AR128797891589308416',
              'AR568018702025359360',
              'AR110003939335733248',
              'AR427517952267386880'
              ]]

df2 = df1.drop(['Spend_Range_Min_EUR',
                'Spend_Range_Max_EUR',
                'Spend_Range_Min_INR',
                'Spend_Range_Max_INR',
                'Spend_Range_Min_BGN',
                'Spend_Range_Max_BGN',
                'Spend_Range_Min_HRK',
                'Spend_Range_Max_HRK',
                'Spend_Range_Min_CZK',
                'Spend_Range_Max_CZK',
                'Spend_Range_Min_DKK',
                'Spend_Range_Max_DKK',
                'Spend_Range_Min_HUF',
                'Spend_Range_Max_HUF',
                'Spend_Range_Min_PLN',
                'Spend_Range_Max_PLN',
                'Spend_Range_Min_RON',
                'Spend_Range_Max_RON',
                'Spend_Range_Min_SEK',
                'Spend_Range_Max_SEK',
                'Spend_Range_Min_GBP',
                'Spend_Range_Max_GBP',
                'Spend_Range_Min_ILS',
                'Spend_Range_Max_ILS',
                'Spend_Range_Min_NZD',
                'Spend_Range_Max_NZD',
                'Spend_Range_Min_TWD',
                'Spend_Range_Max_TWD',
                'Spend_Range_Min_AUD',
                'Spend_Range_Max_AUD'], axis=1)

print(df2)

df2.to_csv("/home/usr/Documents/Projects/gopdata.csv")
