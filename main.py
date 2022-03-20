from wolframalpha import Client
from dotenv import load_dotenv


load_dotenv()
client = Client.from_env()


def main():
    res = client.query('is f(x)=((2x+5)^3)/41 injective')
    if res['@success']:
        print(next(res.results).text)
    else:
        print(res)


if __name__ == '__main__':
    main()
