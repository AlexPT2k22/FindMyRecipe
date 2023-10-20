import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("api_id") #Get your credentials in Edamam.com
api_key = os.getenv("api_key") #Get your credentials in Edamam.com
url = os.getenv("url") #https://api.edamam.com/search

user_ingredients = input("Enter the ingredients you have: ")
print("\n-------------------------------")

query = {'q': user_ingredients, 'app_id': api_id, 'app_key': api_key}

response = requests.get(url, params=query)

if response.status_code == 200:
    data = response.json()
    if "hits" in data:
        recipes = data["hits"]
        if recipes:
            print("\nMatching recipes:")
            for i, recipe in enumerate(recipes, 1):
                recipe_info = recipe["recipe"]
                print(f"{i}. {recipe_info['label']}")
            user_choice = int(input("\nEnter the number of the recipe you want to see (e.g., 1, 2, etc.): "))
            print("\n-------------------------------")
            if 1 <= user_choice <= len(recipes):
                chosen_recipe = recipes[user_choice - 1]["recipe"]
                calories = chosen_recipe["calories"]
                f_calories = f"{calories:.2f}"
                print("\nChosen Recipe:", chosen_recipe["label"])
                print("\nIngredients:\n")
                for ingredient in chosen_recipe["ingredients"]:
                    print(f"- {ingredient['text']}")
                print("\nInformation:\n")
                print(f"- Servings: {chosen_recipe['yield']}")
                print(f"- Total Calories: {f_calories} kcal")
                print(f"- Diet Labels: {', '.join(chosen_recipe['dietLabels'])}")
                print("\nFull recipe:", chosen_recipe["url"])
            else:
                print("Invalid choice. Please select a valid recipe number.")
        else:
            print("No matching recipes found.")
    else:
        print("No recipes found in the response.")
else:
    print("Failed to fetch data from the API.")
