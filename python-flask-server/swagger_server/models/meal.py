# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Meal(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mealname: str=None, description: str=None, calorie: int=None, _date: str=None, time: str=None, day_limit: bool=None):  # noqa: E501
        """Meal - a model defined in Swagger

        :param mealname: The mealname of this Meal.  # noqa: E501
        :type mealname: str
        :param description: The description of this Meal.  # noqa: E501
        :type description: str
        :param calorie: The calorie of this Meal.  # noqa: E501
        :type calorie: int
        :param _date: The _date of this Meal.  # noqa: E501
        :type _date: str
        :param time: The time of this Meal.  # noqa: E501
        :type time: str
        :param day_limit: The day_limit of this Meal.  # noqa: E501
        :type day_limit: bool
        """
        self.swagger_types = {
            'mealname': str,
            'description': str,
            'calorie': int,
            '_date': str,
            'time': str,
            'day_limit': bool
        }

        self.attribute_map = {
            'mealname': 'mealname',
            'description': 'description',
            'calorie': 'calorie',
            '_date': 'date',
            'time': 'time',
            'day_limit': 'day_limit'
        }

        self._mealname = mealname
        self._description = description
        self._calorie = calorie
        self.__date = _date
        self._time = time
        self._day_limit = day_limit

    @classmethod
    def from_dict(cls, dikt) -> 'Meal':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Meal of this Meal.  # noqa: E501
        :rtype: Meal
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mealname(self) -> str:
        """Gets the mealname of this Meal.


        :return: The mealname of this Meal.
        :rtype: str
        """
        return self._mealname

    @mealname.setter
    def mealname(self, mealname: str):
        """Sets the mealname of this Meal.


        :param mealname: The mealname of this Meal.
        :type mealname: str
        """

        self._mealname = mealname

    @property
    def description(self) -> str:
        """Gets the description of this Meal.


        :return: The description of this Meal.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Meal.


        :param description: The description of this Meal.
        :type description: str
        """

        self._description = description

    @property
    def calorie(self) -> int:
        """Gets the calorie of this Meal.


        :return: The calorie of this Meal.
        :rtype: int
        """
        return self._calorie

    @calorie.setter
    def calorie(self, calorie: int):
        """Sets the calorie of this Meal.


        :param calorie: The calorie of this Meal.
        :type calorie: int
        """

        self._calorie = calorie

    @property
    def _date(self) -> str:
        """Gets the _date of this Meal.


        :return: The _date of this Meal.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date: str):
        """Sets the _date of this Meal.


        :param _date: The _date of this Meal.
        :type _date: str
        """

        self.__date = _date

    @property
    def time(self) -> str:
        """Gets the time of this Meal.


        :return: The time of this Meal.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this Meal.


        :param time: The time of this Meal.
        :type time: str
        """

        self._time = time

    @property
    def day_limit(self) -> bool:
        """Gets the day_limit of this Meal.


        :return: The day_limit of this Meal.
        :rtype: bool
        """
        return self._day_limit

    @day_limit.setter
    def day_limit(self, day_limit: bool):
        """Sets the day_limit of this Meal.


        :param day_limit: The day_limit of this Meal.
        :type day_limit: bool
        """

        self._day_limit = day_limit