# Standard Imports
import unittest
from pathlib import Path

# Local Imports
import tests
from tests.configuration.jess import Jess

# External Imports


data_path = Path(f'{tests.__path__[0]}/_data_/')


class FileTestCase(unittest.TestCase):

    def test_load_file(self):
        jess_data = Jess.from_path(Path(f'{data_path}/single/jess.yml'))

        expected = Jess(
            items=['keys', 'spoon'],
            quotes=['i brought something with me', 'i brought a spoon']
        )

        self.assertEqual(expected, jess_data)
