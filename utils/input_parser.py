import re

from lib.func_parser import FuncParser


parser = FuncParser()
valid_input = re.compile(r'(?:[0-9-+*/^()x]|abs|e\^x|ln|log(?:sin|cos|tan)h?)+')


def input_legal(input_str: str) -> bool:
    """Returns True if the input_str is a valid input, False otherwise"""
    return valid_input.search(string=input_str) is not None


def can_parse(input_str: str) -> bool:
    """
    Returns True if the input_str is grammatically correct
    and can be parsed as a valid mathematical function
    """

    # res = parser.eval(num_string=input_str)
    # print(res)

    return parser.is_valid(input_str=input_str)
