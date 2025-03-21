import sender_stand_requests
def test_get_order_code_200(order_track):
    order_track = sender_stand_requests.get_new_order_track().json()['track']
    response_get = sender_stand_requests.get_new_order_by_track(order_track)  
    assert response_get.status_code == 200
