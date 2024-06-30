import glob
import pandas as pd
import xml.etree.ElementTree as ET

log_file = "log_file.txt"
target_file = "transformed_data.csv"


def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = float(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        dataframe = pd.concat([dataframe, pd.DataFrame(
            [{"car_model": car_model, "year_of_manufacture": year_of_manufacture, "price": price, "fuel": fuel}])],
                              ignore_index=True)
    return dataframe


def extract():
    extracted_data = pd.DataFrame(
        columns=['car_model', 'year_of_manufacture', 'price',
                 'fuel'])  # create an empty data frame to hold extracted data

    # process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

        # process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

        # process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)

    return extracted_data


def transform(data):
    """Convert inches to meters and round off to two decimals
    1 inch is 0.0254 meters """
    data['price'] = round(data.price * 0.0254, 2)

    return data


def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)
