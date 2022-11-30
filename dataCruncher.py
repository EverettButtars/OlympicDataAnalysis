import pandas as pd

df = pd.read_csv ('data/OlympicData.csv')

print("========================")
print("Question 1: Who won the most metals during each of the games? Who is the overall winner?")
print("========================")

s = df['STotal'].max()
print("The country with the most summer game medals: ")
print(df.loc[df['STotal'] == s])
print()

s = df['WTotal'].max()
print("The country with the most winter game medals: ")
print(df.loc[df['WTotal'] == s])
print()

s = df['CTotal'].max()
print("The country with the most game medals: ")
print(df.loc[df['CTotal'] == s])
print()

print("========================")
print("Question 2:Who won the least metals during each of the games? Who is the overall loser?")
print("========================")

s = df['STotal'].min()
print("The country with the least summer game medals: ")
print(df.loc[df['STotal'] == s])
print()

s = df['WTotal'].min()
print("The country with the least winter game medals: ")
print(df.loc[df['WTotal'] == s])
print()

s = df['CTotal'].min()
print("The country with the least game medals: ")
print(df.loc[df['CTotal'] == s])
print()

print("========================")
print("Question 3: What is the average medals won?")
print("========================")

print("Summer games: ")
print(df['STotal'].mean())
print()

print("Winter games: ")
print(df['WTotal'].mean())
print()

print("Both games: ")
print(df['CTotal'].mean())
print()


print("========================")
print("Question 4: What is the total number of medals won?")
print("========================")

print("Summer games: ")
print(df['STotal'].sum())
print()

print("Winter games: ")
print(df['WTotal'].sum())
print()

print("Both games: ")
print(df['CTotal'].sum())
print()









