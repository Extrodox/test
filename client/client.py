import requests
import fire


def main(url='http://localhost:4000', data='pig',):
    data = {'string': data}
    res = requests.post(url, json=data)
    assert res.status_code == 200

    print('[INFO]', 'input', '->', 'output')
    print(data['string'], '->', res.json())


if __name__ == '__main__':
    fire.Fire(main)
