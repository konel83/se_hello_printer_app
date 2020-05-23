import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output_1(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Konrad: ", "mgs":"Hello World!"}', rv.data)  # noqa E:501

    def test_msg_with_output_2(self):
        rv = self.app.get('/?output=xml')
        correct_output = ('<greetings>\n\t<name>'
                          + 'Konrad'
                          + '</name>\n\t<msg>'
                          + 'Hello World!'
                          + '</msg>\n</greetings>\n')
        self.assertEqual(correct_output.encode(), rv.data)
