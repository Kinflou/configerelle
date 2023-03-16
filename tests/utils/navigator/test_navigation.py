# Standard Imports
import unittest

# Local Imports

# External Imports
from configerelle.utils.navigator import Navigator


class NavigationTestCase(unittest.TestCase):

    def test_previous_nav(self):
        values = {
            'foo': {
                'bar': {
                    'baz': {}
                }
            }
        }
        navigator = Navigator(values)
        navigator.current_index = 'foo.bar.baz'

        self.assertEqual('foo.bar.baz', navigator.current_index)
        navigator.back()
        self.assertEqual({'baz': {}}, navigator.current_item)

        self.assertEqual('foo.bar', navigator.current_index)
        navigator.back()
        self.assertEqual({'bar': {'baz': {}}}, navigator.current_item)

        self.assertEqual('foo', navigator.current_index)
        navigator.back()
        self.assertEqual({'foo': {'bar': {'baz': {}}}}, navigator.current_item)

        self.assertEqual(None, navigator.current_index)
        navigator.back()
        self.assertEqual({'foo': {'bar': {'baz': {}}}}, navigator.current_item)

    def test_next_nav(self):
        values = {
            'foo': {
                'bar': {}
            }
        }
        navigator = Navigator(values)
        navigator.current_index = 'foo'

        self.assertEqual('foo', navigator.current_index)
        self.assertEqual({'bar': {}}, navigator.current_item)
        self.assertEqual({}, navigator.next('bar'))

        self.assertEqual('foo.bar', navigator.current_index)

        # TODO: Advancing indexes should be done if a value exists or a value is given if not,
        #       fix and re-enable this assertion when implemented
        # with self.assertRaises(KeyError):
        #    navigator.next('baz')
