from pjson import pseudo_dumps

from collections import OrderedDict

test_data_1 = {
    "name": "Jim",
    "surname": "Wick",
    "children": [
        {
            "name": "Leo",
            "surname": "Wick",
            "marks": [
                5,
                4,
                3,
                2,
                5
            ]
        },
        {
            "name": "Jim",
            "surname": "Wick",
            "marks": "No marks"
        }
    ],
    "Job": {
        "company": "NoCompany",
        "position": "Developer"
    }
}

test_data_2 = ['1', '2', '4', 7, 3.43, {'key': 'value', 'k2': [1, 2, 3], 'k3': (1, 3)}]

test_data_3 = OrderedDict({'k': 'v'})


if __name__ == "__main__":
    print(pseudo_dumps(test_data_1))
    print('-' * 20)
    print(pseudo_dumps(test_data_2))
    print('-' * 20)
    print(pseudo_dumps(test_data_3))

