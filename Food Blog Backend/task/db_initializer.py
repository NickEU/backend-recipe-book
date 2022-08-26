from db_context import DbContext
from util import wrap_with_braces
from constants import MEALS, MEASURES, INGREDIENTS


class DbInitializer:
    def __init__(self, context: DbContext):
        self.context = context

    def create_meals(self):
        sql_query: str = """CREATE TABLE IF NOT EXISTS meals (
        meal_id INTEGER PRIMARY KEY,
        meal_name TEXT UNIQUE NOT NULL);"""
        self.context.execute_query(sql_query)

    def create_ingredients(self):
        sql_query: str = """CREATE TABLE IF NOT EXISTS ingredients (
        ingredient_id INTEGER PRIMARY KEY,
        ingredient_name TEXT UNIQUE NOT NULL);"""
        self.context.execute_query(sql_query)

    def create_measures(self):
        sql_query: str = """CREATE TABLE IF NOT EXISTS measures (
        measure_id INTEGER PRIMARY KEY,
        measure_name TEXT UNIQUE);"""
        self.context.execute_query(sql_query)

    def populate_tables(self):
        data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
                "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
                "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

        self.__sql_insert_query(MEALS, 'meal_name', wrap_with_braces(data[MEALS]))
        self.__sql_insert_query(INGREDIENTS, 'ingredient_name', wrap_with_braces(data[INGREDIENTS]))
        self.__sql_insert_query(MEASURES, 'measure_name', wrap_with_braces(data[MEASURES]))

    def __sql_insert_query(self, table_name: str, column: str, values: str):
        sql_query = f"INSERT INTO {table_name} ({column}) values {values};"
        self.context.execute_query(sql_query)

