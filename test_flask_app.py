import unittest
from test_base import TestFlaskBase

class TestWeb(TestFlaskBase):
    def test_server_is_on(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_rounte_index_is_hola_mundo(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hola Mundo' )

        

if __name__ == '__main__':
    unittest.main()