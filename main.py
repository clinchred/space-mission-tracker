import requests
from datetime import datetime, timedelta


# ============================================================
# НАСТРОЙКИ
# ============================================================

API_URL = "https://ll.thespacedevs.com/2.2.0/launch/upcoming/"
REQUEST_TIMEOUT = 10
LAUNCHES_TO_SHOW = 5


# ============================================================
# РАБОТА С API
# ============================================================

def get_launches():
    """Получает список предстоящих запусков из API."""

    try:
        response = requests.get(
            API_URL,
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

        data = response.json()

        return data.get("results", [])

    except requests.RequestException as error:
        print("\n❌ Не удалось получить данные от API.")
        print(f"Подробности: {error}")
        return []

    except ValueError:
        print("\n❌ API вернул некорректные данные.")
        return []


# ============================================================
# РАБОТА С ДАТАМИ
# ============================================================

def parse_launch_date(date_string):
    """Преобразует дату из API в datetime."""

    return datetime.fromisoformat(
        date_string.replace("Z", "+00:00")
    )


# ============================================================
# ОТОБРАЖЕНИЕ ИНФОРМАЦИИ
# ============================================================

def show_launch(launch):
    """Выводит подробную информацию о запуске."""

    launch_date = parse_launch_date(launch["net"])

    name = launch.get("name", "Неизвестно")

    status = launch.get(
        "status", {}
    ).get(
        "name",
        "Неизвестно"
    )

    rocket = launch.get(
        "rocket", {}
    ).get(
        "configuration", {}
    ).get(
        "full_name",
        "Неизвестно"
    )

    location = launch.get(
        "pad", {}
    ).get(
        "location", {}
    ).get(
        "name",
        "Неизвестно"
    )

    formatted_date = launch_date.strftime("%d.%m.%Y")
    formatted_time = launch_date.strftime("%H:%M")

    print()
    print(f"🚀 Миссия: {name}")
    print(f"📅 Дата запуска: {formatted_date}")
    print(f"🕐 Время запуска: {formatted_time} UTC")
    print(f"📊 Статус: {status}")
    print(f"🚀 Ракета: {rocket}")
    print(f"🌍 Космодром: {location}")

    if launch.get("webcast_live"):
        print("📺 Трансляция: доступна")
    else:
        print("📺 Трансляция: нет информации")

    if launch.get("image"):
        print(f"🖼 Изображение: {launch['image']}")

    print("-" * 70)


def show_title(title):
    """Выводит заголовок раздела."""

    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


# ============================================================
# ОСНОВНЫЕ ФУНКЦИИ
# ============================================================

def show_upcoming_launches():
    """Показывает ближайшие запуски."""

    launches = get_launches()

    if not launches:
        return

    show_title("🚀 БЛИЖАЙШИЕ ЗАПУСКИ")

    for launch in launches[:LAUNCHES_TO_SHOW]:
        show_launch(launch)


def show_next_launch():
    """Показывает следующий запуск."""

    launches = get_launches()

    if not launches:
        return

    show_title("🚀 СЛЕДУЮЩИЙ ЗАПУСК")

    show_launch(launches[0])


def search_mission():
    """Ищет миссии по названию."""

    launches = get_launches()

    if not launches:
        return

    search_text = input(
        "\n🔎 Введите название миссии: "
    ).strip().lower()

    if not search_text:
        print("❌ Поисковый запрос не может быть пустым.")
        return

    found = [
        launch
        for launch in launches
        if search_text in launch.get(
            "name", ""
        ).lower()
    ]

    if not found:
        print("\n❌ Миссии по вашему запросу не найдены.")
        return

    show_title(
        f"🔎 НАЙДЕНО МИССИЙ: {len(found)}"
    )

    for launch in found:
        show_launch(launch)


def filter_by_status():
    """Фильтрует запуски по статусу."""

    launches = get_launches()

    if not launches:
        return

    statuses = {
        "1": "Go for Launch",
        "2": "To Be Determined",
        "3": "Launch Successful",
        "4": "Launch Failure",
        "5": "Отмена"
    }

    show_title("📊 ФИЛЬТР ПО СТАТУСУ")

    for number, status in statuses.items():
        print(f"{number}. {status}")

    choice = input("\nВыберите статус: ").strip()

    if choice not in statuses:
        print("❌ Неверный выбор.")
        return

    selected_status = statuses[choice]

    found = [
        launch
        for launch in launches
        if launch.get(
            "status", {}
        ).get(
            "name"
        ) == selected_status
    ]

    if not found:
        print(
            f"\n❌ Запусков со статусом "
            f"'{selected_status}' не найдено."
        )
        return

    show_title(
        f"📊 СТАТУС: {selected_status}\n"
        f"🚀 НАЙДЕНО ЗАПУСКОВ: {len(found)}"
    )

    for launch in found:
        show_launch(launch)


def filter_by_date():
    """Показывает запуски на ближайшее количество дней."""

    launches = get_launches()

    if not launches:
        return

    try:
        days = int(
            input(
                "\n📅 На сколько дней вперёд искать? "
            )
        )

        if days <= 0:
            print(
                "❌ Количество дней должно быть "
                "больше 0."
            )
            return

    except ValueError:
        print("❌ Введите целое число.")
        return

    now = datetime.now().astimezone()
    end_date = now + timedelta(days=days)

    found = []

    for launch in launches:
        launch_date = parse_launch_date(
            launch["net"]
        )

        if now <= launch_date <= end_date:
            found.append(launch)

    if not found:
        print(
            f"\n❌ Запусков в ближайшие "
            f"{days} дней не найдено."
        )
        return

    show_title(
        f"📅 ЗАПУСКИ НА БЛИЖАЙШИЕ {days} ДНЕЙ\n"
        f"🚀 НАЙДЕНО: {len(found)}"
    )

    for launch in found:
        show_launch(launch)


# ============================================================
# МЕНЮ
# ============================================================

def show_menu():
    """Показывает главное меню."""

    print()
    print("=" * 70)
    print("🚀 SPACE MISSION TRACKER")
    print("=" * 70)
    print("1. Ближайшие запуски")
    print("2. Следующий запуск")
    print("3. Поиск миссии")
    print("4. Фильтр по статусу")
    print("5. Фильтр по дате")
    print("6. Выход")
    print("=" * 70)


def main():
    """Запускает основное меню программы."""

    while True:
        show_menu()

        choice = input(
            "Выберите пункт: "
        ).strip()

        if choice == "1":
            show_upcoming_launches()

        elif choice == "2":
            show_next_launch()

        elif choice == "3":
            search_mission()

        elif choice == "4":
            filter_by_status()

        elif choice == "5":
            filter_by_date()

        elif choice == "6":
            print("\n👋 До встречи!")
            break

        else:
            print(
                "\n❌ Неверный выбор. "
                "Введите число от 1 до 6."
            )


# ============================================================
# ЗАПУСК ПРОГРАММЫ
# ============================================================

if __name__ == "__main__":
    main()