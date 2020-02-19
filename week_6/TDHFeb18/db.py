import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'id': 0,
            'name': 'The Aqua Envy Pillow',
            'price': 250.00,
            'stock': 5,
            'image': 'aquaenvy.JPG'
        },

        {
            'id': 1,
            'name': 'Winter Frost Sochi Pillow',
            'price': 200,
            'stock': 5,
            'image': '0.JPG'
        },

        {
            'id': 2,
            'name': 'Velvet Goes Wordly Pillow',
            'price': 250,
            'stock': 5,
            'image': 'velvetgoeswordly.png'
        },
        {
            'id': 3,
            'name': 'Reptillian Gold Pillow',
            'price': 250,
            'stock': 3,
            'image': '14site.JPG'
        },
    ]

    with open(dst_file, 'w') as f:
        json.dump(data, f, indent=4)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data

def update_database(products, src_file='my_file.json'):
    with open(src_file, 'w') as f:
        json.dump(products, f, indent=4)
        print("database updated...")



