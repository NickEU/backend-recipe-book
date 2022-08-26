from db_initializer import DbInitializer
from db_context import DbContext


def get_filename_from_arguments():
    return 'hello.db'


def main():
    db_filename = get_filename_from_arguments()
    context = DbContext(db_filename)
    initializer = DbInitializer(context)
    initializer.create_meals()
    initializer.create_measures()
    initializer.create_ingredients()
    initializer.populate_tables()
    context.close()


if __name__ == '__main__':
    main()
