# clean_data.py - Clean temperature values

def clean_temp(value):
    # Handle empty or missing values
    if not value or value.strip() == '':
        return None
    
    # Check for NaN strings (case insensitive)
    if value.upper() == 'NAN':
        return None
    
    # Try to convert to float, return None if it fails
    try:
        temp = float(value)
        return temp
    except:
        # Couldn't convert to number
        return None

def get_month_temp(row, month):
    # Just a helper function to get and clean temp in one go
    temp_value = row.get(month, '')
    return clean_temp(temp_value)