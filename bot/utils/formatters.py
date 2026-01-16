from typing import Iterable, List


def split_text(text: str, max_len: int) -> List[str]:
    if max_len <= 0:
        return [text]

    chunks: List[str] = []
    start = 0
    length = len(text)

    while start < length:
        end = min(start + max_len, length)
        if end < length:
            newline = text.rfind('
', start, end)
            if newline != -1 and newline > start:
                end = newline
        chunks.append(text[start:end].rstrip())
        start = end
        if start < length and text[start] == '
':
            start += 1

    return chunks


def format_for_telegram(text: str, max_len: int) -> Iterable[str]:
    for chunk in split_text(text, max_len):
        yield chunk
