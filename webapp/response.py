def ok(ret=None):
    if ret is None:
        return {
            "code": 200,
            "msg": "OK"
        }

    else:
        return {
            "code": 200,
            "msg": "OK",
            "result": ret
        }


def not_found():
    return {
        "code": 404,
        "msg": "Not Found"
    }


def bad_request(info=""):
    return {
        "code": 400,
        "msg": "Bad Request",
        "info": info
    }
