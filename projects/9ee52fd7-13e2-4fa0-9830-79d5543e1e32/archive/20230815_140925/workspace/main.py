from functions import get_menu, upsert_menu

def main():
    store_id = 'test'
    menu = get_menu(store_id)
    response = upsert_menu(store_id, menu)
    print(response)

if __name__ == '__main__':
    main()
