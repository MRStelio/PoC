import os
import re
import datetime


def _get_log_filename():
    """Получить имя лог файла. Проставляются порядковые номера логов и дата тест рана.
    Так как не было никаких условий для логов (в т.ч. условий их хранения / удаления), а в тестовом задании речь идёт
    про один лог, функция рассчитана только для 10 лог файлов.
    """

    log_id = None
    current_path = os.getcwd()
    for files in os.walk(current_path.replace('Framework', 'logs')):
        files_list = list(files[2])
        if not files_list:
            log_id = 1
        else:
            files_list.sort()
            last_log_id = re.match(r'\d+', files_list[-1])
            log_id = int(last_log_id[0]) + 1

    test_run_time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    filename = f'{log_id}. Testrun: {test_run_time}'
    return filename


def _get_log_path():
    """Получение пути хранения логов."""

    current_path = os.getcwd()
    logs_path = f"{current_path}/logs"
    return logs_path


def _create_log_file():
    """Создание файла логов."""

    log_path = _get_log_path()
    os.chdir(log_path)
    filename = _get_log_filename()
    log_file = open(filename, 'w')
    return log_file


def write_logs(logs):
    """Запись логов в файл."""

    file = _create_log_file()
    file.write(logs)
