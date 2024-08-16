import xml.etree.ElementTree as ET
import csv

def convert_xml_to_csv(xml_file, csv_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write the header
        csvwriter.writerow(['Test Case', 'Result', 'Time'])

        # Iterate through the test cases
        for testcase in root.findall('.//testcase'):
            name = testcase.get('name')
            time = testcase.get('time')
            
            # Determine the result
            if testcase.find('failure') is not None:
                result = 'Fail'
            elif testcase.find('error') is not None:
                result = 'Error'
            else:
                result = 'Pass'

            # Write the row
            csvwriter.writerow([name, result, time])

if __name__ == "__main__":
    convert_xml_to_csv('results.xml', 'results.csv')
    print("Conversion complete. Results saved to results.csv")
