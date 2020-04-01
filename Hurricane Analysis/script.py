# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael'];

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October'];

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018];

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160];

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']];

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B'];

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74];

# write your update damages function here:
def returnFloats(list_input):
  updated_list = [];
  for element in list_input:
    if ("M" in element):
      element_num = element.replace("M", "");
      updated_list.append(float(element_num)*1000000);
    elif ("B" in element):
      element_num = element.replace("B", "");
      updated_list.append(float(element_num)*1000000000);
    else:
      updated_list.append(element);
  
  return updated_list;

damages_fixed = returnFloats(damages);
# write your construct hurricane dictionary function here:
def hurricane_dict_by_name(name, month, year, max_sustained_wind, areas_affected, damage, death):
  values = [];
  for i in range(len(names)):
    values.append({"Name": names[i],
                 "Month": months[i],
                 "Year": years[i],
                 "Max Sustained Wind": max_sustained_winds[i],
                 "Areas Affected": areas_affected[i],
                 "Damage": damages_fixed[i],
                 "Deaths": deaths[i]});
  
  hurricanes = dict(zip(names, values));
  return hurricanes;

# Using above function to create "hurricanes" value:
hurricanes = hurricane_dict_by_name(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# write your construct hurricane by year dictionary function here:
def hurricane_dict_by_year(name, month, year, max_sustained_wind, areas_affected, damage, death):
  values = [];
  for i in range(len(names)):
    values.append({"Name": names[i],
                 "Month": months[i],
                 "Year": years[i],
                 "Max Sustained Wind": max_sustained_winds[i],
                 "Areas Affected": areas_affected[i],
                 "Damage": damages_fixed[i],
                 "Deaths": deaths[i]});
  
  hurricanes = dict(zip(years, values));
  return hurricanes;

# write your count affected areas function here:
def count_areas(hurricanes):
  count_dict = dict();
  for area in hurricanes:
    for area2 in hurricanes[area]["Areas Affected"]:
      if (area2 not in count_dict):
        count_dict[area2] = 1;
      else:
        count_dict[area2] += 1;
        
  return count_dict;

# Using above function to create "area_count" value:
area_count = count_areas(hurricanes);

# write your find most affected area function here:
def most_affected_area(area_count):
  most_affected = "";
  most_affected_count = 0;
  for area in area_count:
    if(area_count[area] > most_affected_count):
      most_affected = area;
      most_affected_count = area_count[area];
  
  return most_affected, most_affected_count;

# Using function to create "most_affected, most_affected_count" values:
most_affected, most_affected_count = most_affected_area(area_count);

# write your greatest number of deaths function here:
def greatest_deaths(hurricanes):
  max_deaths = "";
  max_deaths_count = 0;
  for area in hurricanes:
    if hurricanes[area]["Deaths"] > max_deaths_count:
      max_deaths = area;
      max_deaths_count = hurricanes[area]["Deaths"];
  return max_deaths, max_deaths_count;

# Using function to create "greatest_deaths, greatest_deaths_count" values:
greatest_deaths, greatest_deaths_count = greatest_deaths(hurricanes);
  
# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricanes):
  mortality_scale = {0: 0,
                 1: 100,
                 2: 500,
                 3: 1000,
                 4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    num_deaths = hurricanes[cane]['Deaths'];
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[cane]);
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[cane]);
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[cane]);
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[cane]);
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[cane]);
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricanes[cane]);
  return hurricanes_by_mortality;

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = categorize_by_mortality(hurricanes);

def highest_damage(hurricanes):

  max_damage_cane = 'Cuba I';
  max_damage = 0;
  for cane in hurricanes:
    if hurricanes[cane]['Damage'] == "Damages not recorded":
      pass
    elif hurricanes[cane]['Damage'] > max_damage:
      max_damage_cane = cane;
      max_damage = hurricanes[cane]['Damage'];
  return max_damage_cane, max_damage;

# find highest damage inducing hurricane and its total cost
max_damage_cane, max_damage = highest_damage(hurricanes);

def categorize_by_damage(hurricanes):

  damage_scale = {0: 0,
                 1: 100000000,
                 2: 1000000000,
                 3: 10000000000,
                 4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    total_damage = hurricanes[cane]['Damage'];
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[cane]);
    elif total_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[cane]);
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[cane]);
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[cane]);
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[cane]);
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[cane]);
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[cane]);
  return hurricanes_by_damage;

# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage = categorize_by_damage(hurricanes);
