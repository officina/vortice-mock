from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from devicesim.views import register, connect, hello, check
from django.urls import resolve, reverse
from os.path import join, dirname
import json
from jsonschema import validate



def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = _load_json_schema(schema_file)
    return validate(data, schema)


def _load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        j = json.loads(schema_file.read())
        return j

# Create your tests here.
class MockTest(TestCase):

    def test_wifi_provisioning(self):

        url = reverse('connect')
        data = '__SL_P_P.A=Officina%20Network&__SL_P_P.C=password&__SL_P_N.L=2'
        response = self.client.post(url, data=data, content_type='application/x-www-form-urlencoded;charset=utf-8')
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")

    def test_verify_provisioning(self):

        url = reverse('check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")

    def test_hello(self):
        url = reverse('hello')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200, "Status code is not 200")
        str = response.content
        assert_valid_schema(json.loads(str), "connect.json")

    def test_provisioning_mqtt(self):
        url = reverse('register')
        data = json.dumps({
            "serial": "1234567890",
            "topic": "test",
            "certificatePem": "test",
            "privateKey": "test"
        })
        response = self.client.post(url, content_type='application/json', data=data )
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")


    def test_provisioning_wifi_second_step(self):
        url = reverse('provisioning_second_step')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")

    def test_verify_provisioning(self):

        url = reverse('verify_provisioning')
        response = self.client.get(url, content_type='application/json', data=[])
        self.assertEqual(response.status_code, 200, "Invalid response, expecting 200")
        self.assertIn(response.content.decode('utf8'), ['0', '1', '2', '3', '4', '5'], "Invalid: expecting response in [0, 1, 2, 3, 4, 5]")


    def test_set_name(self):
        url = reverse('name_set')
        data = '__SL_P_S.B=vorticello'
        response = self.client.post(url, data=data, content_type='application/x-www-form-urlencoded;charset=utf-8')
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")

    def test_get_name(self):
        url = reverse('name_get')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, "Invalid response, expecting 200")
        self.assertIsNotNone(response.content, "Response is empty")