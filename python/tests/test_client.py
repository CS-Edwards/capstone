import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add parent directory to Python path
from client import create_client


class TestWeaviateClient(unittest.TestCase):
    def test_client_connection(self):

        #Test client.py created client
        client = create_client()
        self.assertIsNotNone(client)

        #Test client ready
        self.assertTrue(client.is_ready())


if __name__=='__main__':
    unittest.main()