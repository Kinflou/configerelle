# Standard Imports
import unittest

# Local Imports
from tests.configuration.cass import Cass
from tests.configuration.jess import Jess
from tests.configuration.ali import Ali

# External Imports


class LinkedTestCase(unittest.TestCase):

    def test_link_other(self):
        jess = Jess(
            items=['spoon'],
            quotes=[]
        )
        jess.file_path = 'test/'

        cass = Cass(
            items=[],
            quotes=[],
            dreams=[]
        )
        cass.file_path = 'test/'
        cass.link_config('jess', jess)

        self.assertEqual(jess.__dict__, cass.from_expr_of(dict, '{linked::jess}'))
        self.assertEqual(jess.items[0], cass.from_expr_of(dict, '{linked::jess}')['items'][0])

    def test_link_other_two_deep(self):
        jess = Jess(
            items=['spoon'],
            quotes=[]
        )
        jess.file_path = 'test/'

        cass = Cass(
            items=[],
            quotes=['i like Jess, they have a {linked::jess::items::#0}'],
            dreams=[]
        )
        cass.file_path = 'test/'
        cass.link_config('jess', jess)

        ali = Ali(
            friends=['{linked::cass}', '{linked::jess}']
        )
        ali.link_config('jess', jess)
        ali.link_config('cass', cass)

        self.assertEqual('i like Jess, they have a spoon', ali.from_expr_of(str, '{linked::cass::quotes::#0}'))

    def test_link_other_two_deep_missing(self):
        jess = Jess(
            items=['spoon'],
            quotes=[]
        )

        cass = Cass(
            items=[],
            quotes=['i like Jess, they have a {linked::jess::items::#0}'],
            dreams=[]
        )
        cass.add_vars_group({
            'pocket': {}
        })
        cass.link_config('jess', jess)

        ali = Ali(
            friends=['{linked::cass}', '{linked::jess}']
        )
        ali.link_config('jess', jess)
        ali.link_config('cass', cass)

        with self.assertRaises(AttributeError):
            self.assertEqual(
                'i like Jess, they have a spoon',
                ali.from_expr_of(str, '{linked::cass::custom::pocket::#0}')
            )

