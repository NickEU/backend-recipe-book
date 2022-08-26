from db_context import DbContext


class DbInitializer:
    def __init__(self, context: DbContext):
        self.context = context

    def create_meals(self):
        sql_query: str = 'select * from meals'
        self.context.cursor_name.execute(sql_query)
        pass

    def create_ingredients(self):
        pass

    def create_measures(self):
        pass

    def populate_tables(self):
        pass

