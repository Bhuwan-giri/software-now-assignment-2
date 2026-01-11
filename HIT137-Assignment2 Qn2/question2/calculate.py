# calculate.py - Do all calculations
import math

# Seasons dictionary - southern hemisphere I think?
seasons = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

# All the months in order
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

def get_season_averages(data):
    # Initialize empty lists for each season
    season_temps = {'Summer': [], 'Autumn': [], 'Winter': [], 'Spring': []}
    
    # Go through all the data rows
    for row in data:
        for season, month_list in seasons.items():
            for month in month_list:
                temp = clean_temp(row.get(month, ''))
                if temp is not None:
                    season_temps[season].append(temp)
    
    # Now calculate averages for each season
    averages = {}
    for season in season_temps:
        temps = season_temps[season]
        if len(temps) > 0:
            avg = sum(temps) / len(temps)
            averages[season] = round(avg, 1)
        else:
            averages[season] = 0.0  # default to zero if no data
    
    return averages

def get_station_ranges(data):
    # Store info about each station
    station_info = {}
    
    # First pass - collect all temps and find min/max
    for row in data:
        station = row.get('STATION_NAME', 'Unknown')
        
        # Create new entry if we haven't seen this station before
        if station not in station_info:
            station_info[station] = {
                'max': -100,  # start with really low value
                'min': 100,   # start with really high value
                'temps': []
            }
        
        # Check each month
        for month in months:
            temp = clean_temp(row.get(month, ''))
            if temp is not None:
                station_info[station]['temps'].append(temp)
                
                # Update max
                if temp > station_info[station]['max']:
                    station_info[station]['max'] = temp
                
                # Update min
                if temp < station_info[station]['min']:
                    station_info[station]['min'] = temp
    
    # Calculate ranges and find the largest one
    largest_range = 0
    largest_stations = []
    
    for station in station_info:
        info = station_info[station]
        if len(info['temps']) > 0:
            temp_range = info['max'] - info['min']
            info['range'] = temp_range
            
            # Check if this is the largest range we've seen
            if temp_range > largest_range:
                largest_range = temp_range
                largest_stations = [(station, info)]  # start new list
            elif temp_range == largest_range:
                # There might be multiple stations with same range
                largest_stations.append((station, info))
    
    return largest_stations, largest_range

def get_station_stability(data):
    station_temps = {}
    
    # Collect all temperatures for each station
    for row in data:
        station = row.get('STATION_NAME', 'Unknown')
        if station not in station_temps:
            station_temps[station] = []
        
        # Get temps from all months
        for month in months:
            temp = clean_temp(row.get(month, ''))
            if temp != None:
                station_temps[station].append(temp)
    
    # Calculate standard deviation for each station
    # Note: Using population std dev here, not sample
    station_std = {}
    for station, temps in station_temps.items():
        if len(temps) > 1:  # need at least 2 values
            # Calculate mean first
            mean = sum(temps) / len(temps)
            
            # Then variance
            variance = sum((t - mean) ** 2 for t in temps) / len(temps)
            
            # Finally std dev
            stddev = math.sqrt(variance)
            station_std[station] = round(stddev, 1)
    
    # Handle edge case where no stations have enough data
    if not station_std:
        return [], [], 0, 0
    
    # Find min and max std deviations
    min_std = min(station_std.values())
    max_std = max(station_std.values())
    
    # Get all stations with min std (most stable)
    stable = [(s, d) for s, d in station_std.items() if d == min_std]
    
    # Get all stations with max std (most variable)
    variable = [(s, d) for s, d in station_std.items() if d == max_std]
    
    return stable, variable, min_std, max_std

# Import the cleaning function from the other file
from clean_data import clean_temp