# import json để đọc file JSON
import json


# hàm load data từ JSON
def load_json_data(filepath):

    # mở file JSON
    with open(filepath, "r", encoding="utf-8") as file:

        # return data dạng Python object
        return json.load(file)