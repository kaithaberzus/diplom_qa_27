import requests
import data
import configuration
def get_new_order_track():
    response=requests.post(configuration.main_link+configuration.create_order, 
                         json=data.order_structure)
    return response.json()['track']
track=get_new_order_track()
#print(track)
def get_new_order_by_track(track):
    response_1= requests.get(configuration.main_link+configuration.get_order_by_track, params={"t":track})
    return response_1
#order_response=get_new_order_by_track(track)
#print(order_response.status_code)