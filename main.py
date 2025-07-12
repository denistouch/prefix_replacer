import os
import argparse


def is_file_and_starts_with(filename: str, folder_path: str, prefix: str) -> bool:
    path = os.path.join(folder_path, filename)

    return os.path.isfile(path) and filename.startswith(prefix)


def combine_errors(errors: list) -> dict:
    errors_hash = {}
    for error in errors:
        file = error['file']
        reason = str(error['reason'])
        if reason not in errors_hash:
            errors_hash[reason] = []
        errors_hash[reason].append(file)

    return errors_hash


def prepare_errors(errors: list) -> str:
    errors_hash = combine_errors(errors)
    error_report = ''
    for reason, files in errors_hash.items():
        files_list = '\n\t'.join(files)
        error_report += f"{reason}:\n\t{files_list}\n"

    if error_report == '':
        return ''

    return 'В ходе выполнения возникли следующие ошибки:\n' + error_report


def prepare_report(raw_report: dict) -> str:
    if raw_report['total'] == 0:
        return 'В папке не найдены файлы'

    if raw_report['found'] == 0:
        return f'В папке отсутствуют файлы с префиксом {raw_report["prefix"]}'

    changed = f'В папке {raw_report["folder_path"]} найдено {raw_report["found"]} файлов с префиксом "{raw_report["prefix"]}", успешно переименовано {raw_report["renamed"]}.'

    if len(raw_report['errors']) != 0:
        changed = f'{changed}\n' + prepare_errors(raw_report['errors'])

    return changed


def rename_in_folder(folder_path: str, prefix: str, replacement: str) -> str:
    # prefix = r'IMG_'
    # extension = '.jpg'
    # replacement = ''
    total, found, renamed, errors = 0, 0, 0, []

    for filename in os.listdir(folder_path):
        total += 1
        path = os.path.join(folder_path, filename)

        if not os.path.isfile(path) or not filename.startswith(prefix):
            continue

        found += 1
        new_filename = filename.replace(prefix, replacement)
        new_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(path, new_path)
            renamed += 1
        except Exception as e:
            errors.append({
                'file': filename,
                'reason': e
            })

    return prepare_report({
        'folder_path': folder_path,
        'prefix': prefix,
        'total': total,
        'found': found,
        'renamed': renamed,
        'errors': errors
    })


def another():
    pass
# if os.path.isfile(os.path.join(folder_path, filename)) and filename.endswith(extension):
#     date_string = get_exif_date(os.path.join(folder_path, filename))
#     if date_string is None:
#         continue
#
#     created_at = strptime(date_string, '%Y:%m:%d %H:%M:%S')
#     new_name = f'{strftime('%Y%m%d_%H%M%S', created_at)}{extension}'
#
#     if new_name == filename:
#         continue
#
#     found += 1
#     old_path = os.path.join(folder_path, filename)
#     new_path = os.path.join(folder_path, new_name)
#
#     try:
#         os.rename(old_path, new_path)
#         renamed += 1
#     except Exception as e:
#         errors.append({
#             'file': filename,
#             'reason': e
#         })

#     if os.path.isfile(os.path.join(folder_path, filename)) and filename.startswith(prefix):
#         found += 1
#
#         new_name = filename.replace(prefix, replacement)
#         old_path = os.path.join(folder_path, filename)
#         new_path = os.path.join(folder_path, new_name)
#
#         try:
#             os.rename(old_path, new_path)
#             renamed += 1
#         except Exception as e:
#             errors.append({
#                 'file': filename,
#                 'reason': e
#             })
#

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Программа по массовому отрезанию префикса от файлов в каталоге')

    parser.add_argument("--folder", type=str, help='Каталог в котором будет происходить переименование', required=True)
    parser.add_argument("--prefix", type=str, help='Префикс, который по которому будут отбираться файлы для переименования', required=True)
    parser.add_argument("--replacement", type=str, help='Строка на которую будет заменён префикс, в переименовываемом файле', default='')

    args = parser.parse_args()

    print(rename_in_folder(args.folder, args.prefix, args.replacement))
