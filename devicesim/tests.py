from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from devicesim.views import register, connect, hello, check
from django.urls import resolve
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
        request = HttpRequest()
        data = json.dumps({
          "__SL_P_P.A": "Officina_Network",
          "__SL_P_P.C": "password",
          "__SL_P_N.L": 2
        })
        response = self.client.post('/api/1/wlan/profile_add', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")

    def test_verify_provisioning(self):
        request = HttpRequest()
        response = check(request)

        response = self.client.get('/check')
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")

    def test_hello(self):
        request = HttpRequest()
        response = response = self.client.get('/hello')

        self.assertEqual(response.status_code, 200, "Status code is not 200")
        str = response.content
        assert_valid_schema(json.loads(str), "connect.json")

    def test_provisioning_mqtt(self):
        request = HttpRequest()
        # request.body = "asd"
        data = json.dumps({
            "serial": "1234567890",
            "topic": "test",
            "certificatePem": "test",
            "privateKey": "test"
        })
        response = self.client.post('/register', content_type='application/json', data=data )
        self.assertEqual(response.status_code, 204, "Invalid response, expecting 204")