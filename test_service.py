# -*- coding: utf-8 -*-

# run with:
# python -m unittest discover
# or use
# nosetests
# For junit with nosetests use:
# nosetests --with-xunit

import service
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class TestServer(unittest.TestCase):

    def setUp(self):
        service.app.debug = True
        self.app = service.app.test_client()

    def test_index(self):
        resp = self.app.get('/')
        self.assertTrue ('Hello World Docker Application' in resp.data)
        self.assertEquals(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
