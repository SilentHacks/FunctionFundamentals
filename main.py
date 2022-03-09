from wolframalpha import Client
from dotenv import load_dotenv


load_dotenv()
client = Client.from_env()


def main():
    res = client.query('is f(x)=x^2 surjective')
    if res['@success']:
        print(next(res.results).text)
    else:
        print(res)


if __name__ == '__main__':
    main()
