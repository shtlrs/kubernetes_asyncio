# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.29.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.authentication_v1beta1_api import AuthenticationV1beta1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestAuthenticationV1beta1Api(unittest.TestCase):
    """AuthenticationV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.authentication_v1beta1_api.AuthenticationV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_self_subject_review(self):
        """Test case for create_self_subject_review

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass


if __name__ == '__main__':
    unittest.main()
