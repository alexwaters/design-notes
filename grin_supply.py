from tabulate import tabulate

#Grin Issuance Schedule
#Second = 1 | Minute = 60 | Hour = 3,600 | Day = 86,400
#Year = 31,536,000 | Decade = 315,360,000

g_sec = 1
g_min = g_sec * 60
g_hour = g_min * 60
g_day = g_hour * 24
g_year = g_day * 365
g_decade = g_year * 10

starting_year = 2019
decade_years = 10
num_decades = 5

def get_stat(year):
  assert (year >= starting_year)
  delta = (year - starting_year)
  supply = (delta+1)*g_year
  new = g_year
  inflation = new / supply
  return {"Year": year, "Supply": supply, "New Coin": new, 
  "Inflation": '{:.2%}'.format(inflation)}

for d in range(num_decades):
  sy = starting_year + (10 * d)
  years = [get_stat((y + sy)) for y in range(decade_years)]
  print (tabulate(years, headers="keys") + "\n")
