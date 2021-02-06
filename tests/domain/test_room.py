import uuid
from rentomatic.domain.room import Room

def test_room_model_init():
    code = uuid.uuid4()
    room = Room(
        code,
        size = 200,
        price = 10,
        longitude = -9.23,
        latitude = 1.230,
    )

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -9.23
    assert room.latitude == 1.230

def test_room_model_from_dict():
    code = uuid.uuid4()
    dictionary = {
        "code": code,
        "size": 199,
        "price": 15,
        "longitude": 1.23,
        "latitude": 12.33,
    }

    new_room = Room.from_dict(dictionary)
    assert new_room.code == code
    assert new_room.size == 199
    assert new_room.price == 15
    assert new_room.longitude == 1.23
    assert new_room.latitude == 12.33

def test_room_model_to_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "size": 199,
        "price": 15,
        "longitude": 1.23,
        "latitude": 12.33,
    }

    new_room = Room.from_dict(init_dict)
    assert init_dict == new_room.to_dict()

def test_model_room_comparison():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "size": 199,
        "price": 15,
        "longitude": 1.23,
        "latitude": 12.33,
    }

    room1 = Room.from_dict(init_dict)
    room2 = Room.from_dict(init_dict)
    assert room1 == room2