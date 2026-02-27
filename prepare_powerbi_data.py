import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv('matches.csv')

# 1. Clean Goals
def extract_goals(result, home_team):
    try:
        score_part = str(result).split('AET')[0].split('on pens')[0].strip()
        home_goals, away_goals = map(int, score_part.split(':'))
        
        fcb_goals = home_goals if 'Barcelona' in str(home_team) else away_goals
        rma_goals = away_goals if 'Barcelona' in str(home_team) else home_goals
        
        return pd.Series([fcb_goals, rma_goals])
    except:
        return pd.Series([0, 0])

df[['FCB_Goals', 'RMA_Goals']] = df.apply(
    lambda row: extract_goals(row['Result'], row['Home Team']), 
    axis=1
)

# calculate total goals
df['Total_Goals'] = df['FCB_Goals'] + df['RMA_Goals']

# clean Attendance
def clean_attendance(att):
    if pd.isna(att):
        return 0.0
    return float(str(att).replace('.', ''))

df['Attendance_Clean'] = df['Attendance'].apply(clean_attendance)

# clean Dates
df['Formatted_Date'] = pd.to_datetime(df['Date'].str.split(', ').str[-1], format="%d/%m/%Y", errors='coerce')
df['Year'] = df['Formatted_Date'].dt.year

df.to_csv('powerbi_matches.csv', index=False)
print("Successfully generated 'powerbi_matches.csv' for Power BI visualization!")
