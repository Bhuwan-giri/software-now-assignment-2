# save_files.py - Module for saving analysis results to text files

def save_averages(seasonal_averages):
    """Save seasonal average temperatures to a text file."""
    with open("average_temp.txt", "w") as file:
        for season, avg_temp in seasonal_averages.items():
            file.write(f"{season}: {avg_temp:.1f}°C\n")  # Formatting for one decimal place
    print("Saved: average_temp.txt")

def save_ranges(temperature_ranges):
    """Save the largest temperature ranges for each station to a text file."""
    with open("largest_temp_range_station.txt", "w") as file:
        if temperature_ranges:
            for station, info in temperature_ranges:
                file.write(f"Station {station}: Range {info['range']:.1f}°C ")
                file.write(f"(Max: {info['max']:.1f}°C, Min: {info['min']:.1f}°C)\n")
        else:
            file.write("No data available\n")
    print("Saved: largest_temp_range_station.txt")

def save_stability(stable_stations, variable_stations):
    """Save stability results of temperature stations to a text file."""
    with open("temperature_stability_stations.txt", "w") as file:
        file.write("Most Stable Stations:\n")
        
        if stable_stations:
            for station, stddev in stable_stations:
                file.write(f"  Station {station}: StdDev {stddev:.2f}°C\n")
        else:
            file.write("  No stable stations data available\n")
        
        file.write("\nMost Variable Stations:\n")
        
        if variable_stations:
            for station, stddev in variable_stations:
                file.write(f"  Station {station}: StdDev {stddev:.2f}°C\n")
        else:
            file.write("  No variable stations data available\n")
    
    print("Saved: temperature_stability_stations.txt")