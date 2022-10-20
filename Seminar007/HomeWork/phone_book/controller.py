import model
import view


def check_choice(choice):
    check_choice(model.print_phonebook()) if choice == '0-1' else \
    check_choice(view.edit_menu()) if choice == '0-2' else \
    check_choice(model.add_record()) if choice == '2-1' else \
    check_choice(model.del_record(view.find_menu(choice))) if choice == '2-2' else \
    check_choice(view.find_menu(choice)) if choice in ('0-3', '2-2') else \
    check_choice(view.export_menu()) if choice == '0-4' else \
    check_choice(view.import_menu()) if choice == '0-5' else \
    check_choice(model.find_records(choice)[0]) if choice in ('3-1', '3-2') else \
    check_choice(model.export_phonebook(choice)) if choice in ('4-2', '4-1') else \
    check_choice(model.import_phonebook(choice)) if choice in ('5-2', '5-1') else \
    check_choice(view.main_menu()) if choice in ('2-0', '3-0', '4-0', '5-0', '0') else \
    quit("\033[32mСпасибо, что воспользовались нашим справочником. Ждём Вас снова.\033[0m") if choice == '0-0' else \
    print('Error')


check_choice(view.main_menu())
