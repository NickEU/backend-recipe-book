from db_initializer import DbInitializer
from db_context import DbContext
import sys


def get_filename_from_arguments():
    if len(sys.argv) != 2:
        return None
    return sys.argv[1]


def main():
    db_filename = get_filename_from_arguments()
    if db_filename is None:
        print('Please pass the DB filename as a parameter when launching the script. Halting!')
        return

    context = DbContext(db_filename)
    initializer = DbInitializer(context)
    initializer.create_meals()
    initializer.create_measures()
    initializer.create_ingredients()
    initializer.populate_tables()
    context.close()


if __name__ == '__main__':
    main()
