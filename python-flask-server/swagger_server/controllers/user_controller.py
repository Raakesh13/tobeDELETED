import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_put import UserPut  # noqa: E501
from swagger_server import util

user_meal_map = {}


def delete_user(username):  # noqa: E501
    """Delete user

    Delete user # noqa: E501

    :param username: 
    :type username: str

    :rtype: None
    """
    if username in user_meal_map:
        del(user_meal_map[username])
        print(user_meal_map)
        return "user deleted"
    return "no user with {} username".format(username)


def get_user_details(username):  # noqa: E501
    """Get user details

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: User
    """
    if username in user_meal_map:
        print(user_meal_map)
        return user_meal_map[username][0]
    return "no user with {} username".format(username)


def update_user(username, body):  # noqa: E501
    """Update user details

     # noqa: E501

    :param username: 
    :type username: str
    :param body: Updated user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    if username in user_meal_map:
        meal = user_meal_map[username].pop(0)
        print(type(meal.to_dict()))
        print(meal)
        print(type(body))
        print(body)
        meal.to_dict().update(
            body.to_dict())

        return meal
    return "no user with {} username".format(username)


def user_post(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    if body.username in user_meal_map:
        return "username already exist... Try another user name"

    user_meal_map[body.username] = [
        body, {}]
    print(user_meal_map)
    return user_meal_map


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
