# Standard Imports
import os
import unittest

# Local Imports
from configerelle.configuration.base import ConfigBase

# External Imports


class BaseTestCase(unittest.TestCase):

    def test_namespace_resolution(self):
        result = ConfigBase.namespace_of('test::foo')
        expected = ['test', 'foo']

        self.assertEqual(expected, result)

    def test_namespace_group_var(self):
        raw_dict = {
            'test': {
                'foo': 'Foo'
            }
        }

        config = ConfigBase()
        config.file_path = 'temp'
        config.add_vars_group(raw_dict)

        val: str = config.var_of(str, 'custom::test::foo')
        expected: str = "Foo"

        self.assertEqual(expected, val)

    def test_std_namespace_resolve(self):
        config = ConfigBase()
        config.file_path = 'temp/'
        config.add_vars_group({
            'working_dir': os.getcwd()
        })
        val: str = config.expr_of(str, '{custom::working_dir}/test/')

        expected: str = f"{os.getcwd()}/test/"

        self.assertEqual(expected, val)

    def test_std_namespace_resolve_missing(self):
        config = ConfigBase()
        config.file_path = 'temp/'
        config.add_vars_group({
            'working_dir': os.getcwd()
        })

        val: str = config.expr('{custom::working_dir}/test/{std::doesnt_exist}')

        expected: str = f"{os.getcwd()}/test/"

        self.assertEqual(expected, val)

    def test_std_namespace_resolve_missing_raises(self):
        config = ConfigBase()
        config.file_path = 'temp/'
        config.add_vars_group({
            'working_dir': os.getcwd()
        })

        with self.assertRaises(ValueError):
            config.expr('{custom::working_dir}/test/{std::doesnt_exist}', True)


if __name__ == '__main__':
    unittest.main()

