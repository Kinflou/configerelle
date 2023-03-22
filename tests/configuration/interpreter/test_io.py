# Standard Imports
import unittest

# Local Imports

# External Imports
from configerelle.configuration.logic import INTERPRETER
from configerelle.utils.navigator import Navigator
from configerelle.configuration.base import ConfigBase
from configerelle.configuration.interpretation.binder import Binder


class InputOutputTestCase(unittest.TestCase):

    def test_input(self):
        expr = "word {custom::come} with {custom::foo::bar} is {custom::foo::-{custom::baz}-}"
        s = INTERPRETER().sections_from_expr(expr)

        sections = {
            'ExpressionsContext': [
                {'texts': ['word ']},
                {
                    'NamespaceContext': {
                        'SegmentsContext': [
                            {
                                'texts': ['custom', 'some'],
                                'Literal_namespaceContext': []
                            }
                        ]
                    }
                },
                {'texts': [' with ']},
                {
                    'NamespaceContext': {
                        'SegmentsContext': [
                        {
                            'texts': ['custom', 'foo', 'bar'],
                            'Literal_namespaceContext': []}
                        ]
                    }
                },
                {'texts': [' is ']},
                {
                    'NamespaceContext': {
                        'SegmentsContext': [
                            {
                                'texts': ['custom', 'foo'],
                                'Literal_namespaceContext': [
                                    {
                                        'SegmentsContext': [
                                            {
                                                'texts': ['custom', 'baz'],
                                                'Literal_namespaceContext': []
                                            }
                                        ]
                                    }
                                ],
                                'positions': [2]
                            }
                        ]
                    }
                }
            ]
        }

        navigator = Navigator(sections)

        config = ConfigBase()
        config.add_vars_group({
            'some': 'spoon',
            'foo': {
                'bar': 'fork',
                'all': 'spoon fork'
            },
            'baz': 'all'
        })

        binder = Binder(INTERPRETER, config)
        solved = binder.from_expr_of(str, navigator.inner)

        self.assertEqual('word spoon with fork is spoon fork', solved)

