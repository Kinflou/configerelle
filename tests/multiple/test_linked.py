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

        cass = Cass(
            items=[],
            quotes=[],
            dreams=[]
        )
        cass.link_config('jess', jess)

        self.assertEqual(jess, cass.expr_of(Jess, '{linked::jess}'))

        # TODO: Possibly unnecessary access test case, think about it
        # self.assertEqual(jess.items[0], cass.expr_of(dict, '{linked::jess}')['items'][0])

    def test_link_other_self_cfg(self):
        jess = Jess(
            items=['spoon'],
            missing=['fork'],
            quotes=['I only have a {cfg::items::#0}, do you have a {cfg::missing::#0}']
        )

        cass = Cass(
            items=['fork'],
            quotes=['Yes i have a {cfg::items::#0}'],
        )
        jess.link_config('cass', cass)

        self.assertEqual('Yes i have a fork', jess.expr_of(str, '{linked::cass::quotes::#0}'))

    def test_link_other_self_cfg_two_deep_linked(self):
        jess = Jess(
            items=['spoon'],
            quotes=['{cfg::items::#0}']
        )

        cass = Cass(
            items=['{linked::jess::items::#0}'],
            quotes=['{cfg::items::#0}'],
        )
        cass.link_config('jess', jess)

        self.assertEqual('spoon', cass.expr_of(str, '{cfg::quotes::#0}'))

    def test_link_other_two_deep(self):
        jess = Jess(
            items=['spoon'],
            quotes=[]
        )

        cass = Cass(
            items=[],
            quotes=['i like Jess, they have a {linked::jess::items::#0}'],
            dreams=[]
        )
        cass.link_config('jess', jess)

        ali = Ali(
            friends=['{linked::cass}', '{linked::jess}']
        )
        ali.link_config('jess', jess)
        ali.link_config('cass', cass)

        self.assertEqual('i like Jess, they have a spoon', ali.expr_of(str, '{linked::cass::quotes::#0}'))

    def test_link_other_with_literal(self):
        jess = Jess(
            items=['#1', 'spoon'],
            quotes=[]
        )

        cass = Cass(
            items=['{linked::jess::items::-{linked::jess::items::#0}-'],
            quotes=[],
            dreams=[]
        )
        cass.link_config('jess', jess)
        jess.link_config('cass', cass)

        self.assertEqual('spoon', jess.expr_of(str, '{linked::cass::items::#0}'))

    def test_link_other_with_literal_extra_segment(self):
        jess = Jess(
            items=[],
            quotes=[],
            dreams={
                'current': 'night',
                'day': {
                    'early': 'I want a dog',
                    'late': 'I want a donkey'
                 },
                'night': {
                    'early': 'I want a cat',
                    'late': 'I want a hampter'
                }
            }
        )

        cass = Cass(
            items=[],
            quotes=[],
            dreams=[
                '{linked::jess::dreams::-{linked::jess::dreams::current}-::early}',
                '{linked::jess::dreams::-{linked::jess::dreams::current}-::late}'
            ]
        )
        cass.link_config('jess', jess)
        jess.link_config('cass', cass)

        self.assertEqual('I want a cat', cass.expr_of(str, '{cfg::dreams::#0}'))
        self.assertEqual('I want a hampter', cass.expr_of(str, '{cfg::dreams::#1}'))

    def test_link_other_with_literal_extra_segment_link_other(self):
        jess = Jess(
            items=[],
            quotes=['I want a hampter'],
            dreams={
                'current': 'night',
                'day': {
                    'early': 'I want a dog',
                    'late': 'I want a donkey'
                 },
                'night': {
                    'early': 'I want a cat',
                    'late': '{cfg::quotes::#0}, sorry i mean hamster'
                }
            }
        )

        cass = Cass(
            items=[],
            quotes=[],
            dreams=[
                '{linked::jess::dreams::-{linked::jess::dreams::current}-::early}',
                '{linked::jess::dreams::-{linked::jess::dreams::current}-::late}'
            ]
        )
        cass.link_config('jess', jess)
        jess.link_config('cass', cass)

        self.assertEqual('I want a cat', cass.expr_of(str, '{cfg::dreams::#0}'))
        self.assertEqual('I want a hampter, sorry i mean hamster', cass.expr_of(str, '{cfg::dreams::#1}'))

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
            'pocket': []
        })
        cass.link_config('jess', jess)

        ali = Ali(
            friends=['{linked::cass}', '{linked::jess}']
        )
        ali.link_config('jess', jess)
        ali.link_config('cass', cass)

        with self.assertRaises(IndexError):
            self.assertEqual(
                'i like Jess, they have a spoon',
                ali.expr_of(str, '{linked::cass::custom::pocket::#0}')
            )

