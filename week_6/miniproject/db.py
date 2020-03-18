import json

def create_database(dst_file='my_file.json'):
    data = { 'products' :[
        {
            'id': 0,
            'name': 'Innisfree: Best Seller Discovery Set',
            'price': 40,
            "stock": 50,
            'image': 'all-in-one1.png',
            'category': 'allinone',
            'what is it': "What is it: An essential set of Innisfree's bestselling pore clearing clay mask, hydrating serum, and firming cream\n\n",
            'skin type': 'Skin Type: Normal, Dry, Combination, and Oily',
            'concerns': 'Concerns: Dryness, Pores, Dullness, Uneven Texture, and Loss of Firmness',
            'core ingredients': 'This set contains: Miracle Seed Essence, Alpine Berry Water Cream, Mild Facial Peeling Gel, Clean Berry Lip Mask, Miracle Seed Cotton sheets'
        },
        {
            'id': 1,
            'name': 'Primera: Glow Is All You Seed Intro Kit',
            'price': 40,
            "stock": 50,
            'image': 'all-in-one2.png',
            'category': 'all-in-one',
            'what is it': "What is it: A glow-boosting skin sampler featuring four of Primera’s bestselling heroes, all TSA-approved and designed to deliver nonstop radiance and moisture",
            'skin Type': "Skin Type: Normal, Dry, Combination, and Oily",
            'concerns': "Concerns: Dryness, Dullness, and Uneven Texture",
            'core ingredients': 'This set contains: (Super Volcanic Clusters) Pore Clearing Clay Mask, (Green Tea Seed) Intensive Hydrating Serum, (Orchid) Youth-Enriched Cream'
        },

        {
            'id': 2,
            'name': 'Saturday Skin: Wide Awake Brightening Eye Cream',
            'price': 46,
            "stock": 50,
            'image': 'eyecare1.png',
            'category': 'eye care',
            'what is it': "What is it: A hydrating eye cream with date seed extract that illuminates and refreshes the eye area.",
            'skin type': 'Skin Type: Normal, Dry, Combination, and Oily',
            'concerns': 'Concerns: Dryness, Dark Circles, and Puffiness',
            'core ingredients': 'Core Ingredients: Cha-7 es Complex, Date Seed Extract, Avocado Protein Extract'
    },
        {
            'id': 2,
            'name': 'Belif: Moisturizing Eye Bomb',
            'price': 48,
            "stock": 50,
            'image': 'eyecare2.png',
            'category': 'eye care',
            'what is it': 'What is it: A lightweight, refreshing eye cream that smooths fine lines with a 26-hour burst of moisture, boosts elasticity, and increases the resilience of the skin for flawless makeup application.',
            'skin type': 'Skin Type: Normal, Dry, Combination, Sensitive, and Oily',
            'concerns': 'Concerns: Dryness, loss of firmness and elasticity, fine lines and wrinkles',
            'core ingredients': 'Core Ingredients: Tiger Grass (Pennywort), Comfrey Leaf'
    },
        {
            'id': 3,
            'name': 'Inissfree: Orchid Youth-Enriched Gel Cream',
            'price': 29,
            "stock": 50,
            'image': 'moisturizer1.png',
            'category': 'moisturizer',
            'what is it': 'What is it: A daily gel-cream that offers lightweight hydration, and targets early signs of aging with Jeju orchid, naturally-derived hyaluronic acid, and beta glucan.',
            'skin type': 'Skin Type: Combination and Oily',
            'concerns': 'Concerns: Loss of Firmness and Elasticity, Fine Lines and Wrinkles, and Oiliness',
            'core ingredients': 'Core Ingredients: Orchid Elixir, Hyaluronic Acid, Peptides'
    },
        {
            'id': 4,
            'name': 'Belif: The True Cream Aqua Bomb',
            'price': 38,
            "stock": 50,
            'image': 'moisturizer2.png',
            'category': 'moisturizer',
            'what is it': 'What is it: An ultra-lightweight, oil-free gel cream that instantly cools and refreshes skin while providing intensive hydration',
            'skin type': 'Normal, Oily, Combination',
            'concerns': 'Concerns: Dryness and Pores',
            'core ingredients': 'Core Ingredients: Lady\'s Mantle, Malachite, Plantin, Oat Husk'
    },
        {
            'id': 5,
            'name': 'Primera: Alpine Berry Water Cream',
            'price': 40,
            "stock": 50,
            'image': 'moisturizer3.png',
            'category': 'moisturizer',
            'what is it': 'What is it: A dewy cream that sinks in instantly while providing lasting hydration and nourishment',
            'skin type': 'Skin Type: Dry',
            'concerns': 'Dryness, Dullness, and Uneven Texture',
            'core ingredients': 'Core Ingredients: Water-Stay Technology, Coconut-derived Oil, Artemisia Extract'
    },
        {
            'id': 6,
            'name': 'Innisfree: Super Volcanic Clusters Pore Clearing Clay Mask',
            'price': 15,
            "stock": 50,
            'image': 'mask1.png',
            'category': 'masks',
            'what is it': 'What is it: A deep-cleansing creamy clay mask—formulated with absorbent Jeju Super Volcanic Clusters™ and AHA—that helps clear pores while it exfoliates.',
            'skin type': 'Skin Type: Normal, Combination, and Oily',
            'concerns': 'Concerns: Pores, Oiliness, Dullness, and uneven texture',
            'core ingredients': 'Core Ingredients: Jeju Volcanic Clusters and Lactic Acid'
    },
        {
            'id': 7,
            'name': 'Innisfree: Super Volcanic Clusters Pore Clearing Clay Mousse Mask',
            'price': 21,
            "stock": 50,
            'image': 'mask2.png',
            'category': 'masks',
            'what is it': 'What is it: A clay mask in a light-as-air mousse that helps clear pores with Jeju Super Volcanic Clusters™ while AHA and BHA dually exfoliate skin.',
            'skin type': 'Skin Type: Normal, Combination, and Oily',
            'concerns': 'Concerns: Pores, Dullness and Uneven Texture, and Oiliness',
            'core ingredients': 'Core Ingredients: Jeju Volcanic Clusters and Salicylic Acid'
        }

        ]
    }

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


