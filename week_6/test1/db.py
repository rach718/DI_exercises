import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'name': 'The Goddess Velvet Pillow',
            'price': 250,
            'instock': True
        },

        {
            'name': 'The Dashing Mocha Pillow',
            'price': 200,
            'instock': True
        },

        {
            'name': 'The Metallic Fury Pillow',
            'price': 150,
            'instock': True
        },

    ]

    with open(dst_file, 'w') as f:
        json.dump(data, f, indent=4)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data


