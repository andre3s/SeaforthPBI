from Scripts.prod_provider import clean_production_data
from colorama import Fore


def main():
    print(Fore.GREEN, 'Hi, I will start to clean your data files. Please wait.')
    clean_production_data()


if __name__ == '__main__':
    main()
