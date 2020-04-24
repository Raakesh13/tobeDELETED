# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_put import UserPut  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            '/v1/user/{username}'.format(username='username_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_details(self):
        """Test case for get_user_details

        Get user details
        """
        response = self.client.open(
            '/v1/user/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Update user details
        """
        body = UserPut()
        response = self.client.open(
            '/v1/user/{username}'.format(username='username_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_post(self):
        """Test case for user_post

        Create user
        """
        body = User()
        response = self.client.open(
            '/v1/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()