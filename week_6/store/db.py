import json

# json.dump Takes a string(formatted like javascript) outputs json notation
# json.dumps will take the entire json and convert it
# json.load Takes json and formats it back to python
# json.loads streams it and converts it

def create_database(dst_file='my_file.json'):
    data = [
        {
            'name': 'iphone 9',
            'price': 799,
            'instock': True
        },

        {
            'name': 'Macbook Pro',
            'price': 4799,
            'instock': False
        },

        {
            'name': 'Apple Watch',
            'price': 10799,
            'instock': True
        },

        {
            'name': 'Apple stand pro',
            'price': 99999,
            'instock': True
        },
    ]
    with open(dst_file, 'w') as file_obj:
        json.dump(data, file_obj)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(src_file)
    return data