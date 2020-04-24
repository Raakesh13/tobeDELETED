import connexion
import six

from swagger_server.models.meal import Meal  # noqa: E501
from swagger_server import util
import swagger_server.controllers.user_controller as UC
from swagger_server.controllers.util import unique_id, generate_csv


def add_meal(username, body):  # noqa: E501
    """Add meal

     # noqa: E501

    :param username: 
    :type username: str
    :param body: Meal object to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    uid = unique_id()
    UC.user_meal_map[username][1][uid] = body
    print(UC.user_meal_map)
    return uid


def delete_meal(mealId, username):  # noqa: E501
    """Delete meal entry

    This can only be done by the logged in user. # noqa: E501

    :param mealId: The meal that needs to be deleted.
    :type mealId: str
    :param username: 
    :type username: str

    :rtype: None
    """

    del(UC.user_meal_map[username][1][mealId])
    print(UC.user_meal_map)
    return "meal deleted"


def get_mealby_meal_id(mealId, username):  # noqa: E501
    """get meal details

    get meal by mealId # noqa: E501

    :param mealId: 
    :type mealId: str
    :param username: 
    :type username: str

    :rtype: Meal
    """
    if mealId not in UC.user_meal_map[username][1]:
        return "mealId does not exist", 404
    return UC.user_meal_map[username][1][mealId].to_dict()


def update_meal(mealId, username, body):  # noqa: E501
    """Update Meal entry

    This can only be done by the logged in user. # noqa: E501

    :param mealId: meal that needs to be updated
    :type mealId: str
    :param username: 
    :type username: str
    :param body: Updated meal object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501

    del(UC.user_meal_map[username][1][mealId])
    UC.user_meal_map[username][1][mealId] = body
    print(UC.user_meal_map)

    return 'meal updated'
