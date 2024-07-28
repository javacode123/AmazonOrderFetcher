from typing import Any, Optional
from requests import Response, Session
from bs4 import BeautifulSoup, Tag
from service.constants import Constants


class Client:
    """
    Simulate browser operations, mainly designed to simulate user login and send requests
    """

    def __init__(self, email: str, password: str):
        self.email: str = email
        self.password: str = password
        self.session: Session = Session()
        self.last_response: Optional[Response] = None
        self.last_response_parsed: Optional[Tag] = None

    def sign_in(self) -> None:
        """
        Login Amazon Web Service with provided username and password. Just login whit singn-in page. Current not support
        login with 2FA authentication.
        """
        self.get(Constants.URL_SIGN_IN_REDIRECT)
        attempts = 0
        while attempts < Constants.MAX_TRY_CNT:
            # TODO we can abstract a form class
            form = self.last_response_parsed.select_one(Constants.SELECTOR_SIGN_IN)
            if form is not None:
                submit_data = {}
                for field in form.select("input"):
                    try:
                        submit_data[field["name"]] = field["value"]
                    except Exception:
                        pass
                submit_data.update({
                    'email': self.email,
                    'password': self.password,
                    'rememberMe': 'true',
                })
                method = form.get("method", "GET").upper()
                url = form.get("action")
                request_data = {"params" if method == "GET" else "data": submit_data}
                self.request(method, url, **request_data)
                if Constants.SIGN_IN_SUCCESS_WORD in self.last_response.text:
                    # TODO using log sdk
                    print("Login successful")
                    break
                elif "cvf-widget-form-captcha" in self.last_response.text:
                    print("TODO current not support captcha")
                else:
                    print("login failed with status code: ", self.last_response.status_code, " message: ", self.last_response.text)
            attempts += 1

        if attempts == Constants.MAX_TRY_CNT:
            raise Exception("login failed, please contact the developer")

    def logout(self) -> None:
        raise Exception("Not implemented")

    def request(self, method: str, url: str, **kwargs: Any) -> Response:
        # Build Request header and storage response
        if "headers" not in kwargs:
            kwargs["headers"] = {}
        kwargs["headers"].update(Constants.DEFAULT_HEADERS)
        self.last_response = self.session.request(method, url, **kwargs)
        self.last_response_parsed = BeautifulSoup(self.last_response.text, "html.parser")
        # TODO use logging
        print("do request with url = ", url, " and response status code = ", self.last_response.status_code)
        return self.last_response

    def get(self,
            url: str,
            **kwargs: Any):
        """
        HTTP GET request
        """
        return self.request("GET", url, **kwargs)

    def post(self,
             url,
             **kwargs: Any) -> Response:
        raise Exception("Not implemented")
