# main.py - Main program for temperature data analysis

from read_data import get_all_data
from calculate import (
    get_season_averages,
    get_station_ranges,
    get_station_stability,
)
from save_files import save_averages, save_ranges, save_stability

def main():
    """Main function for performing temperature analysis."""

    print("=" * 50)
    print("       TEMPERATURE ANALYSIS")
    print("=" * 50)

    # Step 1: Load temperature data
    print("\n1. Loading temperature data...")
    temperature_data = get_all_data()

    if not temperature_data:
        print("No data found. Exiting the program.")
        return

    # Step 2: Calculate seasonal average temperatures
    print("\n2. Calculating seasonal averages...")
    seasonal_averages = get_season_averages(temperature_data)
    print("Seasonal Averages:")
    for season, average_temp in seasonal_averages.items():
        print(f"  {season}: {average_temp:.1f}°C")

    # Step 3: Identify the largest temperature range
    print("\n3. Finding the largest temperature range across stations...")
    range_info, largest_range = get_station_ranges(temperature_data)
    print(f"Largest Temperature Range: {largest_range:.1f}°C")
    for station, info in range_info:
        print(f"  Station {station}: Range = {info['range']:.1f}°C")

    # Step 4: Determine stable and variable temperature stations
    print("\n4. Analyzing station stability...")
    stable_stations, variable_stations, min_std, max_std = get_station_stability(temperature_data)

    print(f"Most Stable Stations (StdDev {min_std:.2f}°C):")
    for station, stddev in stable_stations:
        print(f"  {station}: StdDev = {stddev:.2f}°C")

    print(f"\nMost Variable Stations (StdDev {max_std:.2f}°C):")
    for station, stddev in variable_stations:
        print(f"  {station}: StdDev = {stddev:.2f}°C")

    # Step 5: Save results to files
    print("\n5. Saving results to files...")
    save_averages(seasonal_averages)
    save_ranges(range_info)
    save_stability(stable_stations, variable_stations)

    print("\n" + "=" * 50)
    print("DONE! Results have been saved. Check the following files:")
    print("  average_temp.txt")
    print("  largest_temp_range_station.txt")
    print("  temperature_stability_stations.txt")
    print("=" * 50)

if __name__ == "__main__":
    main()