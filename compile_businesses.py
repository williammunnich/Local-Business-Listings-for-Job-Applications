import json
import pandas as pd

# Load the JSON data from a file
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

elements = data.get('elements', [])

# List to hold the compiled data
compiled_data = []

for element in elements:
    tags = element.get('tags', {})
    # Check if 'phone', 'email', or 'website' exists in 'tags'
    if 'phone' in tags or 'email' in tags or 'website' in tags:
        name = tags.get('name', '')
        office_type = tags.get('office', '')
        # Build address
        addr_housenumber = tags.get('addr:housenumber', '')
        addr_street = tags.get('addr:street', '')
        addr_unit = tags.get('addr:unit', '')
        addr_city = tags.get('addr:city', '')
        addr_state = tags.get('addr:state', '')
        addr_postcode = tags.get('addr:postcode', '')
        address_parts = [addr_housenumber, addr_street]
        if addr_unit:
            address_parts.append(addr_unit)
        address = ', '.join(filter(None, address_parts))
        city_state_zip = ', '.join(filter(None, [addr_city, addr_state, addr_postcode]))
        full_address = ', '.join(filter(None, [address, city_state_zip]))
        phone = tags.get('phone', '')
        email = tags.get('email', '')
        website = tags.get('website', '')
        
        compiled_data.append({
            'Name': name,
            'Office Type': office_type,
            'Address': full_address,
            'Phone': phone,
            'Email': email,
            'Website': website,
            'Notes': ''
        })

# Create a DataFrame from the compiled data
df = pd.DataFrame(compiled_data)

# Write the DataFrame to an Excel file
df.to_excel('compiled_data.xlsx', index=False)

print('Data has been compiled into compiled_data.xlsx')