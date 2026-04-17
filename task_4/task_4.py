import datetime
import os

class CustomException(Exception):
    def __init__(self, msg: str):
        # Викликаємо конструктор класу Exception, щоб зберегти текст помилки
        super().__init__(msg)
        self.msg = msg

        self.log_to_file()

    def log_to_file(self):
        """Записує повідомлення про помилку у файл logs.txt """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Шлях до файлу в тій же директорії, де лежить скрипт
        file_path = os.path.join(os.path.dirname(__file__), "logs.txt")

        # Відкриваємо файл у режимі 'a'=додавання, щоб не затирати старі записи
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] CUSTOM_ERROR: {self.msg}\n")

if __name__ == "__main__":

    error_messages = [
        "Користувач ввів від'ємне число для віку.",
        "Спроба доступу до бази даних без пароля.",
        "Файл конфігурації пошкоджений або відсутній."
    ]

    print("Генерація помилок та запис у logs.txt...")

    for message in error_messages:
        try:
            raise CustomException(message)
        except CustomException as e:
            print(f"Оброблено: {e}")

    print("\nПеревір файл в якому зберігаються помилки task_4/logs.txt")