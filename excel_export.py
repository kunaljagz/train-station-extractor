import pandas as pd

class ExcelExport:
    def __init__(self, data):
        self.data = data

    def to_excel(self, file_name):
        # Define columns
        columns = ['Station Name', 'Platform Numbers', 'Track Information', 'Facilities',
                   'Connections', 'Dimensions', 'Special Features', 'Confidence Score']

        # Create a DataFrame
        df = pd.DataFrame(self.data)

        # Ensure DataFrame has the right columns
        df = df.reindex(columns=columns)

        # Save to Excel
        df.to_excel(file_name, index=False)

# Usage:
# data = [
#     {'Station Name': 'Station A', 'Platform Numbers': '1, 2', 'Track Information': 'Track 1',
#      'Facilities': 'Restroom, Parking', 'Connections': 'Bus, Subway', 'Dimensions': '50m x 20m',
#      'Special Features': 'Wi-Fi', 'Confidence Score': 0.95},
#     # Add more stations as needed
# ]
# exporter = ExcelExport(data)
# exporter.to_excel('stations.xlsx')
