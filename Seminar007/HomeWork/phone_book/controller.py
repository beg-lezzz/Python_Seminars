import model
import view


def check_choice(choice):
    check_choice(model.print_phonebook()) if choice == '0-1' else \
    check_choice(view.edit_menu()) if choice == '0-2' else \
    check_choice(model.add_record()) if choice == '2-1' else \
    check_choice(view.find_menu()) if choice == '0-3' else \
    check_choice(view.import_menu()) if choice == '0-4' else \
    check_choice(model.find_fio()) if choice == '3-1' else \
    check_choice(model.import_phonebook(choice)) if choice in ('4-2', '4-1') else \
    check_choice(view.main_menu()) if choice in ('2-0', '3-0', '4-0', '0') else \
    quit("\033[32mСпасибо, что воспользовались нашим справочником. Ждём Вас снова.\033[0m") if choice == '0-0' else \
    print('Error')


check_choice(view.main_menu())