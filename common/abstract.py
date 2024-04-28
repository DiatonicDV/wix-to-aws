class Response:
    """ HTTP Response class which is used to collect the result of a function call. """

    default_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true"
    }

    def __init__(self, status_code=200, body="Success", headers=default_headers):
        self.status_code = status_code
        self.body = body
        self.headers = headers

    def add_header(self, header):
        self.headers.update(header)

    def set_status_code(self, status_code):
        self.status_code = status_code

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

    def result(self):
        return {
            "statusCode": self.status_code,
            "headers": self.headers,
            "body": self.body
        }