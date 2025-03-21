import requests
import data
import configuration
def get_new_order_track():
    return requests.post(configuration.MAIN_LINK+configuration.CREATE_ORDER, 
                         json=data.order_structure)
response=get_new_order_track()
print(response.json()["track"])
def get_new_order_by_track(order_track):
    return requests.get(configuration.MAIN_LINK+configuration.GET_ORDER_BY_TRACK, params={"t":order_track})
