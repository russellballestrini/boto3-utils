def merge_pages(key, pages):
    """Merge boto3 paginated results into single list.
    Args:
        key (str): the key used to gather results from each page.
        pages (list): a list of pages of typically description dictionaries.
    Returns:
        list: a single flat list containing results of all pages.
    """
    return [item for page in pages for item in page[key]]


def make_tag_dict(tag_list):
    """Returns a dictionary of existing tags.
    Args:
        tag_list (list): a list of tag dicts.
    Returns:
        dict: A dictionary where tag names are keys and tag values are values.
    """
    return {i["Key"]: i["Value"] for i in tag_list}


def dict_to_key_value(data, sep='=', pair_sep=', '):
    """turns {'tag1':'value1','tag2':'value2'} into tag1=value1, tag2=value2"""
    return pair_sep.join([sep.join((unicode(key), unicode(value))) for key, value in data.items()])


def key_value_to_dict(key_value_list, sep='=', pair_sep=',' ):
    """
    Accept a key_value_list, like::

      key_value_list = ['a=1,b=2', 'c=3, d=4', 'e=5']

    Return a dict, like::

      {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5'}
    """
    d = {}
    for speclist in key_value_list:
        for spec in speclist.strip().split(','):
            key, value = spec.strip().split('=')
            d[key] = value
    return d


def snake_to_camel_case(name):
    """
    Accept a snake_case string and return a CamelCase string.
    For example::
      >>> snake_to_camel_case('cidr_block')
      'CidrBlock'
    """
    name = name.replace("-", "_")
    return "".join(word.capitalize() for word in name.split("_"))
