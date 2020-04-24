import uuid


def unique_id():
    _uid = str(uuid.uuid4())
    _uid = _uid.upper()
    _uid = _uid.replace("-", "")
    return _uid[0:13]


print(unique_id())
