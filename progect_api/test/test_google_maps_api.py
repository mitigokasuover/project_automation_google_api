from requests import Response
from untils.checking import Checking 
from untils.api import Google_maps_api
from untils.logger import Logger
import json
"""Create update and delete location"""

class Test_create_place():

    def test_create_new_place(self):

        print("Method - POST: ")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200) # correct
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')
        # token = json.loads(result_post.text)
        # print(list(token))

        print("Method - GET = > POST:")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200) # correct
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        # "address": "29, side layout, cohen 09",
        # token = json.loads(result_get.text)
        # print(list(token))

        print("Method - PUT:")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200) # correct
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Method - GET = > PUT:") # see result for put method{ change adress}
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200) # correct
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')
        # token = json.loads(result_get.text)
        # print(list(token))


        print("Method - DELETE:") # delete place_id
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200) # correct
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')
        # token = json.loads(result_delete.text)
        # print(list(token))


        print("Method - GET = > DELETE:") # chack delete status place_id
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404) # correct {Non}
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')
        # token = json.loads(result_get.text)
        # print(list(token))

        print("**![Test to create update and delete location - ended]!**")