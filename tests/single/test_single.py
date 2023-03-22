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

        self.assertEqual('i brought a spoon', jess.expr_of(str, jess.quotes[1]))

    @unittest.skip(reason='Possibly unnecessary feature')
    def test_expr_pointer_unresolved(self):
        jess = Jess(
            items=['keys', 'spoon'],
            quotes=['i brought something']
        )
        jess.add_vars_group({
            'spoon': 'bark'
        })

        # TODO: Unresolved means that literal expressions (the ones inside '-{..}-') are resolved
        #       and have a value while the expressions (the ones in just '{...}') are not.
        #       This might not be necessary or tricky to do, decide if this functionality necessary
        # expr = r'{custom::-{cfg::items::#1}-}'
        # self.assertEqual('bark', jess.from_expr_of(str, expr))


