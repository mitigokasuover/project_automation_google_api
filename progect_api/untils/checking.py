from requests import Response
import json

"""method to chack output requests"""

class Checking():

    """method to chack status code"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code # 1 = waiting: 2 = accept
        if response.status_code == status_code:
            print("Correct, ststus code = " +  str(response.status_code))
        else:
            print("Wrong, ststus code = " +  str(response.status_code))


    """Method to checking the presence of the required fields """
    
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields [Are present]")


    """Method checking the values of the required fields """
    
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " correct!!!")

    """Method checking the values of the required fields for one word"""
    
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + " is present!!!")
        else:
            print("Word " + search_word + " isn't present!!!")