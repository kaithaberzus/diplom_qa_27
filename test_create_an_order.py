import sender_stand_requests
def test_get_new_user_token_by_track():
    order_response=sender_stand_requests.get_new_order_by_track(track=sender_stand_requests.track)
    assert order_response.status_code==200
