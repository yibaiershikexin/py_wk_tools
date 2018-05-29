import json
from pprint import pprint

json_file = open('../datas/data.json', 'r')


def test_base():
    reader = json_file.read()
    datas = json.loads(reader)
    pprint(datas)





test_base()
