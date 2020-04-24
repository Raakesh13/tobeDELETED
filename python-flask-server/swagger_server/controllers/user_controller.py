import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_put import UserPut  # noqa: E501
from swagger_server import util


def delete_user(username):  # noqa: E501
    """Delete user

    Delete user # noqa: E501

    :param username: 
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_details(username):  # noqa: E501
    """Get user details

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


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
        body = UserPut.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_post(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
