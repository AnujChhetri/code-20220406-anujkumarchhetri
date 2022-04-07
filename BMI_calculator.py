import json
import sys
from os import path

BMI = {
    "<18.4": ("Underweight", "Malnutrition risk"),
    "18.5-24.9": ("Normal Weight", "Low risk"),
    "25-29.9": ("Overweight", "Enhanced risk"),
    "30-34.9": ("Moderately obese", "Medium risk"),
    "35-39.9": ("Severely obese", "High risk"),
    ">40": ("Very severely obese", "Very high risk")
}


def get_range(bmi: float or int) -> str or bool:
    if not isinstance(bmi, (float, int)):
        return False

    if bmi <= 18.4:
        range = "<18.4"
    elif  bmi >= 18.5 and bmi <=29.9:
        range = "18.5-24.9"
    elif bmi >= 25 and bmi  <= 29.9:
        range = "25-29.9"
    elif bmi >= 30 and bmi <= 34.9:
        range = "30-34.9"
    elif bmi >= 35 and bmi <= 39.9:
        range = "35-39.9"
    else:
        range = ">40"

    return range


def calculate_bmi(height: float, weight: float) -> float or str:
    try:
        bmi = weight / (height/100)**2
    except TypeError:
        bmi = ""

    return bmi


def get_health_risk(bmi_range: str) -> tuple or str:
    if not isinstance(bmi_range, str):
        return ""
    return BMI.get(bmi_range) and BMI[bmi_range][1] or ""


def get_bmi_category(bmi_range: str) -> tuple or str:
    if not isinstance(bmi_range, str):
        return ""
    return BMI.get(bmi_range) and BMI[bmi_range][0] or ""


def process_data(data: list({})) -> list({}):
    if not isinstance(data,  list):
        raise ValueError(f"Wrong data provided, refer to the following error message:\n"\
                         f" {str(type(data))} is provided where as 'list' is required")

    for i, person_data in enumerate(data):
        if not isinstance(person_data, dict):
            # Pop and skip if the provided person data is not dictionary to avoid further crashes
            data.pop(i)
            continue

        bmi = calculate_bmi(person_data.get("HeightCm"), person_data.get("WeightKg"))
        _range = get_range(bmi)
        risk = get_health_risk(_range)
        category = get_bmi_category(_range)
        person_data["BMICategory"] = category
        person_data["HealthRisk"] = risk
        person_data["BMI"] = bmi

    return data


def get_overweight(data):
    overweight = filter(lambda x: x.get("BMICategory", "") == "Overweight", data)
    return len(list(overweight))


if __name__ == "__main__":

    args = sys.argv

    if len(args) > 1:
        f_path = args[1]
        is_file = path.isfile(f_path)
        if not is_file:
            print("Invalid path provided. Please provide correct path.")
        else:
            try:
                with open(f_path, 'r') as json_file:
                    data = json.load(json_file)
                    print(process_data(data))
                    print(get_overweight(data))
            except json.decoder.JSONDecodeError as jde:
                print("Following error occurred while decoding the json data:\n", str(jde))
            except ValueError as ve:
                print(str(ve))
    else:
        print("Please provide the file path")
