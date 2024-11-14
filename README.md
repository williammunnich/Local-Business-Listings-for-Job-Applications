# JSON to Excel Contact Extractor

This project reads JSON data containing contact information, extracts relevant details, and exports them into a structured Excel file. The extracted data includes name, office type, address, phone number, email, and website, if available. This output file provides an organized, accessible overview of contact details.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Getting Data from Overpass Turbo](#getting-data-from-overpass-turbo)
6. [Usage](#usage)
7. [Data Structure](#data-structure)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview
This project takes data from JSON files (such as those generated from OpenStreetMap using Overpass Turbo) and converts it to an Excel file, focusing on entries with a phone, email, or website. This is ideal for managing contact information for local businesses or amenities.

### Key Highlights
- Parses contact information from JSON.
- Filters entries that include `phone`, `email`, or `website` details.
- Compiles entries into a formatted Excel file for easy use.
- Formats address components, including house number, street, city, state, and postal code.

## Features
- **Selective Filtering**: Only includes contacts with phone, email, or website information.
- **Address Formatting**: Concatenates and formats address components into a single string.
- **Data Export**: Outputs contact data to an Excel file (`compiled_data.xlsx`).
- **Extensibility**: Easily adapt the script to extract additional fields if required.

## Requirements
- Python 3.x
- pandas
- openpyxl (for Excel export support in pandas)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/json-to-excel-contact-extractor.git
   cd json-to-excel-contact-extractor
   ```

2. **Install Dependencies**
   ```bash
   pip install pandas openpyxl
   ```

3. **Prepare Data**
   Prepare the JSON data as described in [Getting Data from Overpass Turbo](#getting-data-from-overpass-turbo) or ensure you have an existing `data.json` file in the project directory.

## Getting Data from Overpass Turbo

To gather relevant data, you can use [Overpass Turbo](https://overpass-turbo.eu/), an interface for querying data from OpenStreetMap. Follow these steps to retrieve local business data:

1. **Go to Overpass Turbo**
   Open [Overpass Turbo](https://overpass-turbo.eu/).

2. **Enter Query Script**
   Copy and paste the following script into the Overpass Turbo query editor:

   ```overpass
   /*
   This query retrieves businesses within a specific radius of defined coordinates.
   In this case, the coordinates are 44.975659, -93.270559.
   Replace "radius" with your desired radius in meters (e.g., 500 for 500 meters).
   */

   [out:json][timeout:25];
   node
     ["shop"](around:500, 44.975659, -93.270559);
   node
     ["amenity"](around:500, 44.975659, -93.270559);
   node
     ["office"](around:500, 44.975659, -93.270559);
   out body;
   >;
   out skel qt;
   ```

   - Adjust the `radius` and `coordinates` as needed to cover the area of interest.

3. **Run the Query and Export JSON**
   Click **Run** to execute the query. When the results appear, click **Export** and select **Download as GeoJSON**. Save the file as `data.json` in your project directory.

## Usage

1. **Run the Script**
   Execute the following command in your terminal:
   ```bash
   python contact_extractor.py
   ```

2. **Output**
   The output Excel file, `compiled_data.xlsx`, will contain the extracted and formatted contact information.

## Data Structure
The JSON file (`data.json`) should include contact information in a nested structure, with each entry stored in a list under an `"elements"` key, with various fields (such as `phone`, `email`, and address components) in a `"tags"` object.

### Sample Structure
```json
{
    "elements": [
        {
            "tags": {
                "name": "Contact Name",
                "office": "Office Type",
                "phone": "123-456-7890",
                "email": "contact@example.com",
                "website": "https://example.com",
                "addr:housenumber": "123",
                "addr:street": "Main St",
                "addr:city": "Anytown",
                "addr:state": "CA",
                "addr:postcode": "12345"
            }
        },
        ...
    ]
}
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes you’d like to make.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Open a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).