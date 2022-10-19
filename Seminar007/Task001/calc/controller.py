import model
import view
import logger


def button_click():
    nums_type = view.get_type()
    value_a = view.get_value(nums_type)
    value_b = view.get_value(nums_type)
    operation = view.get_operation()
    result = model.sum_num(value_a, value_b) if operation == '+' else \
        model.sub_num(value_a, value_b) if operation == '-' else \
            model.mult_num(value_a, value_b) if operation == '*' else \
                model.div_num(value_a, value_b) if operation == '/' else \
                    print('Некорректный ввод. Введите одну из операций => "+, -, *, /"')
    math_expression = f'{value_a} {operation} {value_b}'
    view.view_data(math_expression, result)
    logger.calc_logger(math_expression, result)
