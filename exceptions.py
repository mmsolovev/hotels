from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserIsNotExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class UserIncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token has expired"


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is absent"


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class UserIsNotExistsException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "401 Not Found"

class RoomCannotBeBookedException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No free room available"
