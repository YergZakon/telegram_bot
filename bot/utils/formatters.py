import html
from typing import Iterable, List


def escape_html(text: str) -> str:
    return html.escape(text, quote=False)


def split_text(text: str, max_len: int) -> List[str]:
    if max_len <= 0:
        return [text]

    chunks: List[str] = []
    start = 0
    length = len(text)

    while start < length:
        end = min(start + max_len, length)
        chunks.append(text[start:end])
        start = end

    return chunks


def format_for_telegram(text: str, max_len: int) -> Iterable[str]:
    escaped = escape_html(text)
    reserved = len('<pre></pre>')
    chunk_size = max(1, max_len - reserved)

    for chunk in split_text(escaped, chunk_size):
        yield f'<pre>{chunk}</pre>'
