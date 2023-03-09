# Standard Imports
import unittest

# Local Imports
from tests.configuration.jess import Jess

# External Imports


class SingleTestCase(unittest.TestCase):

    def test_defined_class_value(self):
        jess = Jess(
            items=['keys', 'spoon'],
            quotes=['i brought something with me', 'i brought a spoon']
        )

        self.assertEqual('spoon', jess.items[1])
        self.assertEqual('i brought a spoon', jess.quotes[1])

    def test_expr_value(self):
        jess = Jess(
            items=['keys', 'spoon'],
            quotes=['i brought something with me', 'i brought a {cfg::items::#1}']
        )
        jess.file_path = 'temp/'

        self.assertEqual('i brought a spoon', jess.expr_of(str, jess.quotes[1]))

    def test_expr_pointer_unresolved(self):
        jess = Jess(
            items=['keys', 'spoon'],
            quotes=['i brought something']
        )
        jess.add_vars_group({
            'spoon': ''
        })

        expr = r'\{custom::{cfg::items::#1}\}'
        self.assertEqual('{custom::spoon}', jess.expr_of(str, expr))


