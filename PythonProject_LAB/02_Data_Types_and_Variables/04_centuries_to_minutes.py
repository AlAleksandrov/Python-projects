centuries = int(input())

years = 100 * centuries
days = 365.2422 * years
hours = 24 * int(days)
minutes = 60 * hours

print(f"{centuries} centuries = {years} years = {int(days)} days = {hours} hours = {minutes} minutes")
