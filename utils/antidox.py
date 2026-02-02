import re

PHONE_REGEX = re.compile(
    r"(\+7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"
)

IP_REGEX = re.compile(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
)

FIO_REGEX = re.compile(
    r"\b[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+( [А-ЯЁ][а-яё]+)?\b"
)

ADDRESS_REGEX = re.compile(
    r"\b(ул\.|улица|проспект|пр-т|дом|д\.)\s?[А-Яа-я0-9\-]+\b"
)


def check_dox(text: str) -> str | None:
    if PHONE_REGEX.search(text):
        return "📞 Номер телефона"

    if IP_REGEX.search(text):
        return "🌐 IP-адрес"

    if FIO_REGEX.search(text):
        return "🧾 ФИО"

    if ADDRESS_REGEX.search(text):
        return "🏠 Адрес"

    return None