# Standard Imports
import unittest

# Local Imports

# External Imports
from configerelle.configuration.logic import INTERPRETER
from configerelle.expr.generated.exprParser import exprParser
from configerelle.utils.navigator import Navigator
from configerelle.configuration.base import ConfigBase
from configerelle.configuration.interpretation.binder import Binder


class InputOutputTestCase(unittest.TestCase):

    def test_input(self):
        sections = {
            exprParser.ExpressionsContext.__name__: [
                {'texts': ['word ']},
                {
                    exprParser.NamespaceContext.__name__: {
                        exprParser.SegmentsContext.__name__: [
                            {
                                'texts': ['custom', 'some'],
                                exprParser.Literal_namespaceContext.__name__: []
                            }
                        ]
                    }
                },
                {'texts': [' with ']},
                {
                    exprParser.NamespaceContext.__name__: {
                        exprParser.SegmentsContext.__name__: [
                            {
                                'texts': ['custom', 'foo', 'bar'],
                                exprParser.Literal_namespaceContext.__name__: []}]}
                },
                {'texts': [' is ']},
                {
                    exprParser.NamespaceContext.__name__: {
                        exprParser.SegmentsContext.__name__: [
                            {
                                'texts': ['custom', 'foo'],
                                exprParser.Literal_namespaceContext.__name__: {
                                    exprParser.SegmentsContext.__name__: [
                                        {
                                            'texts': ['custom', 'baz'],
                                            exprParser.Literal_namespaceContext.__name__: []
                                        }
                                    ]
                                }
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

