# Standard Imports
import unittest

# Local Imports
from configerelle.configuration.base import ConfigBase

# External Imports


class BinderTestCase(unittest.TestCase):

    def test_expr(self):
        expression = '{custom::foo::bar}'

        config = ConfigBase()
        config.add_vars_group({
            'foo': {
                'bar': 'hello'
            }
        })

        self.assertEqual('hello', config.expr_of(str, expression))

    def test_full_expr(self):
        expression = 'word {custom::some} with {custom::foo::bar} is {custom::foo::-{custom::baz}-}'

        config = ConfigBase()
        config.add_vars_group({
            'some': 'spoon',
            'foo': {
                'bar': 'fork',
                'all': 'spoon fork'
            },
            'baz': 'all'
        })

        self.assertEqual('word spoon with fork is spoon fork', config.expr_of(str, expression))

