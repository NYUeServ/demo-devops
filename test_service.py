# -*- coding: utf-8 -*-

# run with:
# python -m unittest discover
# or use
# nosetests
# For junit with nosetests use:
# nosetests test_service.py --with-xunit

import service
import unittest

class TestServer(unittest.TestCase):

    def setUp(self):
        service.app.debug = True
        self.app = service.app.test_client()

    def test_index(self):
        resp = self.app.get('/')
        self.assertTrue ('Hello World Docker Application' in resp.data)
        self.assertEquals(resp.status_code, 200)

    def test_math1(self):
    	self.assertTrue(3+4 == 6)


if __name__ == '__main__':
    unittest.main()
