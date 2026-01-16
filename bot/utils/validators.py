from collections import Counter


def validate_input(text: str, min_len: int = 10, max_len: int = 4000) -> tuple[bool, str]:
    if not text or not text.strip():
        return False, '📝 Опишите тему чуть подробнее.'

    if len(text) < min_len:
        return False, f'📝 Пожалуйста, опишите тему подробнее (минимум {min_len} символов).'
    if len(text) > max_len:
        return False, f'📝 Запрос слишком длинный. Попробуйте сократить до {max_len} символов.'

    cleaned = ''.join(ch for ch in text if not ch.isspace())
    if len(cleaned) >= 20:
        counts = Counter(cleaned)
        most_common = counts.most_common(1)[0][1]
        if most_common / len(cleaned) > 0.6:
            return False, '📝 Похоже, в запросе много повторяющихся символов. Попробуйте переформулировать.'

    return True, ''
