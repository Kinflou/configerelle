# Standard Imports
import unittest

# Local Imports

# External Imports
from configerelle.utils import navigator
from configerelle.utils.navigator import Navigator


class SnowballingNavigatorTestCase(unittest.TestCase):

    def test_add_steps(self):
        values = {}
        nav = Navigator(values)

        nav['foo'] = "world"
        nav['bar'] = {}
        nav['bar.under'] = {}

        self.assertEqual('world', nav['foo'])
        self.assertEqual({'under': {}}, nav['bar'])
        self.assertEqual({}, nav['bar.under'])

        with self.assertRaises(IndexError):
            _ = nav['foo.one']

    def test_fill_steps(self):
        values = {}
        nav = Navigator(values)

        nav['foo.under'] = 'hello'
        nav['foo.others.0'] = 'world'

        self.assertEqual('hello', nav['foo.under'])
        self.assertEqual('world', nav['foo.others.0'])

    def test_keys_reach(self):
        values = {
            'foo': {},
            'bar': [],
            'baz': {
                'under': 'found you',
                'another': []
            },
            'bork': ['ooo']
        }
        nav = Navigator(values)

        self.assertEqual([], navigator.keys_reach_until(nav, ['some']))
        self.assertEqual(['bar'], navigator.keys_reach_until(nav, ['bar']))
        self.assertEqual(['foo'], navigator.keys_reach_until(nav, ['foo', 'place']))
        self.assertEqual(['baz', 'under'], navigator.keys_reach_until(nav, ['baz', 'under']))
        self.assertEqual(['bork', 0], navigator.keys_reach_until(nav, ['bork', 0]))


class ExistentNavigatorDataTestCase(unittest.TestCase):

    def test_access(self):
        values = {
            'foo': {
                'bar': 'some',
                'ber': ['thou', 'test']
            }
        }

        nav = Navigator(values)
        thing = nav['foo']
        thong = nav['foo.bar']

        with self.assertRaises(IndexError):
            thang = nav['foo.bar.baz']

        test = nav['foo.ber.0']

    def test_assignemnt(self):
        values = {
            'foo': {
                'bar': 'some',
                'ber': ['thou', 'test']
            }
        }

        nav = Navigator(values)

        boo = nav['foo.ber.0'] = 'boo'
        nav['foo.ber.1'] = 'does'
        nav['foo.ber'] = None
        nav['foo.dang'] = 'some'
        ...
