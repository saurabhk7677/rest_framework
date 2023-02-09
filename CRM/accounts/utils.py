

def ok_response(data : dict, message : str="ok", status_code: int=200):

    response = {
        "data": data,
        "status": "success",
        "message": message,
        "error": {},
    }

    return response

def error_response(status_code : int, message : str, error_details : dict):
    data = None

    response = {
        "data": data,
        "status": "failure",
        "error": {
            "message": message,
            "detail": error_details,
            "code": status_code,
        }
    }

    return response