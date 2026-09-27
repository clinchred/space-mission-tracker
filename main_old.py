import requests
from datetime import datetime, timedelta


API_URL = "https://ll.thespacedevs.com/2.2.0/launch/upcoming/"


def get_launches():
    """Получает список предстоящих запусков из API."""

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data.get("results", [])

    except requests.RequestException as error:
        print("❌ Ошибка при подключении к API.")
        print(f"Подробности: {error}")
        return []


def parse_launch_date(date_string):
    """Преобразует дату из API в объект datetime."""

    return datetime.fromisoformat(
        date_string.replace("Z", "+00:00")
    )


def show_launch(launch):
    """Выводит информацию о запуске."""

    launch_date = parse_launch_date(launch["net"])

    name = launch["name"]
    status = launch["status"]["name"]
    rocket = launch["rocket"]["configuration"]["full_name"]
    location = launch["pad"]["location"]["name"]

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


def show_upcoming_launches():
    """Показывает пять ближайших запусков."""

    launches = get_launches()

    if not launches:
        return

    print()
    print("=" * 70)
    print("🚀 БЛИЖАЙШИЕ ЗАПУСКИ")
    print("=" * 70)

    for launch in launches[:5]:
        show_launch(launch)


def show_next_launch():
    """Показывает следующий запуск."""

    launches = get_launches()

    if not launches:
        return

    print()
    print("=" * 70)
    print("🚀 СЛЕДУЮЩИЙ ЗАПУСК")
    print("=" * 70)

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
        if search_text in launch["name"].lower()
    ]

    print()

    if not found:
        print("❌ Миссии по вашему запросу не найдены.")
        return

    print("=" * 70)
    print(f"🔎 НАЙДЕНО МИССИЙ: {len(found)}")
    print("=" * 70)

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

    print()
    print("=" * 70)
    print("📊 ФИЛЬТР ПО СТАТУСУ")
    print("=" * 70)

    for number, status in statuses.items():
        print(f"{number}. {status}")

    choice = input("\nВыберите статус: ")

    if choice not in statuses:
        print("❌ Неверный выбор.")
        return

    selected_status = statuses[choice]

    found = [
        launch
        for launch in launches
        if launch["status"]["name"] == selected_status
    ]

    print()

    if not found:
        print(
            f"❌ Запусков со статусом "
            f"'{selected_status}' не найдено."
        )
        return

    print("=" * 70)
    print(f"📊 СТАТУС: {selected_status}")
    print(f"🚀 НАЙДЕНО ЗАПУСКОВ: {len(found)}")
    print("=" * 70)

    for launch in found:
        show_launch(launch)


def filter_by_date():
    """Показывает запуски на ближайшее количество дней."""

    launches = get_launches()

    if not launches:
        return

    try:
        days = int(
            input("\n📅 На сколько дней вперёд искать? ")
        )

        if days <= 0:
            print("❌ Количество дней должно быть больше 0.")
            return

    except ValueError:
        print("❌ Введите целое число.")
        return

    now = datetime.now().astimezone()
    end_date = now + timedelta(days=days)

    found = []

    for launch in launches:
        launch_date = parse_launch_date(launch["net"])

        if now <= launch_date <= end_date:
            found.append(launch)

    print()

    if not found:
        print(
            f"❌ Запусков в ближайшие "
            f"{days} дней не найдено."
        )
        return

    print("=" * 70)
    print(f"📅 ЗАПУСКИ НА БЛИЖАЙШИЕ {days} ДНЕЙ")
    print(f"🚀 НАЙДЕНО: {len(found)}")
    print("=" * 70)

    for launch in found:
        show_launch(launch)


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

        choice = input("Выберите пункт: ")

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
            print("👋 До встречи!")
            break

        else:
            print(
                "❌ Неверный выбор. "
                "Введите число от 1 до 6."
            )


if __name__ == "__main__":
    main()