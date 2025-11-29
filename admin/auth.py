from fastapi.params import Depends
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from exceptions import UserIncorrectEmailOrPasswordException
from users.auth import user_auth, create_access_token
from users.dependencies import get_current_user, get_token


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["email"], form["password"]

        user = await user_auth(email, password)
        if user:
            access_token = create_access_token({'sub': str(user.id)})
            request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if token:
            user = await get_current_user(token)

        if not token:
            return False

        # Check the token in depth
        return True

authentication_backend = AdminAuth(secret_key="...")
