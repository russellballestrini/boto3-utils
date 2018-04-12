
from unittest import TestCase

from . import (
  dict_to_key_value,
  key_value_to_dict,
  snake_to_camel_case,
  make_tag_dict,
)


class TestSnakeToCamelCase(TestCase):
    """Test Suite for snake_to_camel_case function."""
    def setUp(self):
        self.answers = {'http_response':'HTTPResponse'}

    def test_name_cidr_block(self):
        self.assertEqual(
          snake_to_camel_case('cidr_block'),
          'CidrBlock'
        )

    def test_name_http_response(self):
        # this tests short circut of answers.
        self.assertEqual(
          snake_to_camel_case('http_response', answers=self.answers),
          'HTTPResponse'
        )

    def test_name_vpc_id(self):
        self.assertEqual(
          snake_to_camel_case('vpc_id'),
          'VpcId'
        )


class TestMakeTagDict(TestCase):

    def setUp(self):
        class TestSubject(object):
            tags = [
              {'Key':'Name', 'Value':'myapp01-web01'},
              {'Key':'role', 'Value':'web'},
            ]
    self.test_obj = TestSubject

    def test_make_tag_dict(self):            
        tags = make_tag_dict(test_obj.tags)
        self.assertIn('Name', tags)
        self.assertIn('role', tags)
        self.assertEqual(tags['Name'], 'myapp01-web01')
        self.assertEqual(tags['role'], 'web')
    
    
class TestDictToKeyValue(TestCase):

    def test_dict_to_key_value(self):
        data = {'key1':'value1','key2':'value2'}
        pretty_str = dict_to_key_value(data)
        self.assertIn('key1=value1', pretty_str)
        self.assertIn('key2=value2', pretty_str)
        self.assertEqual(pretty_str.count(','), 1)
        not_as_pretty = dict_to_key_value(data,'x','x')
        self.assertEqual(not_as_pretty.count('x'), 3)

    def test_key_value_to_dict():
        key_value_list = ['a=1,b=2', 'c=3, d=4', 'e=5']
        desired_result = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5'}
        self.assertEqual(key_value_to_dict(key_value_list), desired_result)
