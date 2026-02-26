import requests
# templates for requests models at the beginning stages of a payload and header creation

class request_models_template:
    def __init__(self):
        pass

    def payload_format(self, temperature, status, flipState, postStatus):
        return{
            "Temperature": temperature,
            "Status": status,
            "flipState": flipState,
            "POST-Status": postStatus
        }
    
    def headers_format(self):
        return{
            "Content-Type": "application/json",
            "Accept": "application/json",
            # bypassing ngrok splash screen due to free tier use of Ngrok
            "ngrok-skip-browser-warning": "69420"  
        }