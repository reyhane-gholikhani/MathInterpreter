"""تبدیل خطاهای خام ANTLR به پیام‌های فارسی و آموزشی."""
import re

TOKENS = {
    "FLOAT": "عدد اعشاری",
    "INT": "عدد صحیح",
    "ID": "نام متغیر",
    "EOF": "پایان برنامه",
    "'<EOF>'": "پایان برنامه",
    "'('": "پرانتز باز '('",
    "')'": "پرانتز بسته ')'",
    "'+'": "علامت جمع '+'",
    "'-'": "علامت منفی '-'",
    "'*'": "علامت ضرب '*'",
    "'/'": "علامت تقسیم '/'",
    "'%'": "عملگر باقیمانده '%'",
    "'^'": "عملگر توان '^'",
    "'='": "علامت انتساب '='",
    "';'": "نقطه‌ویرگول ';'",
    "','": "ویرگول ','",
    "'<'": "عملگر کوچک‌تر '<'",
    "'>'": "عملگر بزرگ‌تر '>'",
    "'=='": "عملگر برابری '=='",
    "'!='": "عملگر نابرابری '!='",
    "'print'": "دستور چاپ 'print'",
}


def token_label(value):
    value = value.strip()
    if value in TOKENS:
        return TOKENS[value]
    # نمایش توکن‌های ناشناخته بدون قالب‌بندی فنی ANTLR
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return f"نماد '{value[1:-1]}'"
    return f"«{value}»"


def expected_label(value):
    value = value.strip()
    if value.startswith("{") and value.endswith("}"):
        choices = [token_label(item) for item in value[1:-1].split(",") if item.strip()]
        if len(choices) == 1:
            return choices[0]
        if len(choices) == 2:
            return f"{choices[0]} یا {choices[1]}"
        if choices:
            return "، ".join(choices[:-1]) + " یا " + choices[-1]
    return token_label(value)


def translate_lexer_error(msg):
    match = re.search(r"token recognition error at: (.+)$", msg)
    if match:
        bad = match.group(1).strip()
        return (
            f"کاراکتر «{bad}» در زبان MathScript تعریف نشده است. "
            "آن را حذف کنید یا با یک نماد معتبر جایگزین کنید."
        )
    return "یک کاراکتر نامعتبر در کد پیدا شد. نمادهای استفاده‌شده را بررسی کنید."


def translate_parser_error(msg):
    match = re.match(r"extraneous input (.+?) expecting (.+)$", msg)
    if match:
        found = token_label(match.group(1))
        expected = expected_label(match.group(2))
        return (
            f"{found} در این نقطه از عبارت اضافی است. "
            f"در اینجا باید {expected} نوشته شود؛ ترتیب عملگرها و مقادیر را بررسی کنید."
        )

    match = re.match(r"mismatched input (.+?) expecting (.+)$", msg)
    if match:
        found = token_label(match.group(1))
        expected = expected_label(match.group(2))
        return (
            f"{found} در این جایگاه معتبر نیست. "
            f"به‌جای آن باید {expected} قرار بگیرد."
        )

    match = re.match(r"missing (.+?) at (.+)$", msg)
    if match:
        missing = token_label(match.group(1))
        location = token_label(match.group(2))
        return (
            f"{missing} جا افتاده است. "
            f"پیش از {location} باید {missing} را وارد کنید."
        )

    match = re.match(r"no viable alternative at input (.+)$", msg)
    if match:
        fragment = match.group(1)
        return (
            f"بخش «{fragment}» با هیچ‌یک از ساختارهای معتبر زبان مطابقت ندارد. "
            "ترتیب عملگرها، اعداد و پرانتزها را بررسی کنید."
        )

    return (
        "ساختار این دستور با قواعد زبان MathScript سازگار نیست. "
        "نحوه نوشتن عبارت و جایگاه عملگرها و پرانتزها را بررسی کنید."
    )


def format_error(kind, line, column, detail):
    return f"خطای {kind} در خط {line}، ستون {column + 1}: {detail}"
