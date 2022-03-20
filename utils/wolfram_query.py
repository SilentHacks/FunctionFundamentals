from wolframalpha import Client
from dotenv import load_dotenv


load_dotenv()
client = Client.from_env()


def is_function(func: str, func_property: str) -> bool:
    res = client.query(f'is f(x)={func} {func_property}')
    if not res['@success']:
        raise ValueError('Invalid equation')

    if 'not' in next(res.results).text:
        return False

    return True
