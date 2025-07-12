from main import prepare_errors

def test_prepare_errors():
    errors_list = [
        {
            'file': 'file_1',
            'reason': Exception('exception_1')
        },
        {
            'file': 'file_2',
            'reason': Exception('exception_2')
        },
        {
            'file': 'file_3',
            'reason': Exception('exception_1')
        },
        {
            'file': 'file_4',
            'reason': Exception('exception_1')
        },
    ]

    expected = "В ходе выполнения возникли следующие ошибки:\nexception_1:\n\tfile_1\n\tfile_3\n\tfile_4\nexception_2:\n\tfile_2\n"

    actual = prepare_errors(errors_list)
    if expected != actual:
        print('Незапланированное поведение:\nОжидалось:\n',expected, '\nПолучили:\n', actual, sep='')

test_prepare_errors()
