class Meal():
    def __init__(self, name=None, servings=None, calories=None, carbs=None, fat=None, protein=None) -> None:
        self.name = name
        self.servings = float(servings)
        self.calories = float(calories)
        self.carbs = float(carbs)
        self.fat = float(fat)
        self.protein = float(protein)


def parse_food_database(path: str):
    import csv
    food_collection = []
    with open(path) as food_db_file:
        reader = csv.DictReader(food_db_file, delimiter=';')
        next(reader)
        for line in reader:
            meal = Meal(
                        line['foodname'],
                        line['servings'],
                        line['calories'],
                        line['carbs'],
                        line['fat'],
                        line['protein']
                        )
            food_collection.append(meal)

    return food_collection

def randomly_select_meals(meal_collection: list):
    import random
    return random.sample(meal_collection, k=3)

def print_meal_report(meal_collection: list):
    header = '{:20}\t{:10}\t{:10}\t{:10}\t{:10}\n'.format('Meal', 'Calories', 'Carbs (g)', 'Protein (g)', 'Fat (g)')
    table = ''
    for meal in meal_collection:
        calories_ps = meal.calories / meal.servings
        carbs_ps = meal.carbs / meal.servings
        protein_ps = meal.protein / meal.servings
        fat_ps = meal.fat / meal.servings

        table += '{:20}\t{:10.2f}\t{:10.2f}\t{:10.2f}\t{:10.2f}\n'.format(meal.name, calories_ps, carbs_ps, protein_ps, fat_ps)

    print(header + table)


if __name__ == '__main__':
    meals = parse_food_database('food_database.csv')
    selected_meals = randomly_select_meals(meals)
    print(len(selected_meals))
    print_meal_report(selected_meals)
