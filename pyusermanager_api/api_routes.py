from sanic import Sanic


from . import api_permissions
from . import api_sessions
from . import api_misc
from . import api_register
from . import api_user

def RegisterRoutes(route_prefix = "/", app = None):
    
    app.add_route(api_user.get_info_for_header, f"{route_prefix}header", methods=["GET"], name="userapi.header")

    # login/logout/register routes
    app.add_route(api_sessions.login_user, f"{route_prefix}login", methods=["POST"], name="userapi.login")
    app.add_route(api_sessions.logout_user, f"{route_prefix}logout", methods=["GET"], name="userapi.logout")
    app.add_route(api_register.register_user, f"{route_prefix}register", methods=["POST"], name="userapi.register")

    # to get versions of stuff
    app.add_route(api_misc.version, f"/version/userapi", methods=["GET"], name="userapi.version")


    # Route to get useravatar
    app.add_route(api_misc.get_avatar, f"{route_prefix}avatar/<avatarname>", methods=["GET"], name="userapi.avatar")

    # Methods Regarding Users
    app.add_route(api_user.create_by_admin, f"{route_prefix}admin/create", methods=["POST"], name="userapi.admin_create")
    app.add_route(api_user.get_users, f"{route_prefix}users", methods=["GET"], name="userapi.users")
    
    @app.route(f"{route_prefix}perms", methods=["GET", "POST", "DELETE"], name="userapi.permissions")
    async def handle_rest_perm(request):

        if request.method == "GET":
            return await api_permissions.get_perms(request)
        elif request.method == "POST":
            return await api_permissions.change_perm(request, True)
        elif request.method == "DELETE":
            return await api_permissions.change_perm(request, False)
        else:
            pass

    @app.route(f"{route_prefix}user/<username>", methods=["GET", "PUT", "DELETE"], name="userapi.user")
    async def handle_rest_user(request, username):

        if request.method == "GET":
            return await api_user.get_user_info(request, username)
        elif request.method == "PUT":
            return await api_user.update_user_info(request, username)
        elif request.method == "DELETE":
            return await api_user.delete_user(request, username)
        else:
            pass