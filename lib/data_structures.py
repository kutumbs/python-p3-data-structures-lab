spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    answer = [food["name"] for food in spicy_foods]
    return answer

def get_spiciest_foods(spicy_foods):
    level = [food
             for food in spicy_foods if food.get("heat_level", 0) > 5]
    return level


def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emojis}")

     return emojis



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    result = [food for food in spicy_foods if food.get('cuisine') == cuisine]
    if result:
        return result[0]
    else:
        return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            emojis = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emojis}")

def get_average_heat_level(spicy_foods):
        result = [food["heat_level"] for food in spicy_foods]
        return sum(result)/len(result)

def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods
