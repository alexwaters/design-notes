from tabulate import tabulate

#Grin Issuance and Inflation Schedule

#Free Code available at: #https://github.com/alexwaters/sandbox/blob/master/grin_supply.py

g_sec = 1             #Amount of grin per second/hour/day/year
g_min = g_sec * 60    #60
g_hour = g_min * 60   #3,600
g_day = g_hour * 24   #86,400
g_year = g_day * 365  #31,536,000

decade = 10           #years in a decade

starting_year = 2019  #genesis block year
decades = 7           #number of decades to display

#Get the stats for a single year
def get_stat(year):
  assert (year >= starting_year)
  delta = (year - starting_year)
  supply = (delta+1)*g_year
  new = g_year
  inflation = new / supply
  return {"Year": year, "Total Supply": supply, "New $GRIN": new, 
  "Inflation": '{:.2%}'.format(inflation)}

#Get the stats for the specified number of decades
for d in range(decades):
  sy = starting_year + (10 * d)
  years = [get_stat((y + sy)) for y in range(decade)]
  print (tabulate(years, headers="keys") + "\n")
