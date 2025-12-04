from __future__ import annotations

from pathlib import Path
import re

from rich.console import Console


console = Console(highlight=False)


# HTML -> Rich-markup regexes
_BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
_CODE_RE = re.compile(r"<code>(.*?)</code>", re.IGNORECASE | re.DOTALL)
_PRE_RE = re.compile(r"<pre>(.*?)</pre>", re.IGNORECASE | re.DOTALL)
_SPAN_COLOR_RE = re.compile(
    r"<span\s+style=\"[^\">]*color:([^\";]+)[^\"]*\">(.*?)</span>",
    re.IGNORECASE | re.DOTALL,
)
_SPAN_BOLD_RE = re.compile(
    r"<span\s+style=\"[^\">]*font-weight\s*:\s*bold[^\">]*\">(.*?)</span>",
    re.IGNORECASE | re.DOTALL,
)
_SPAN_RE = re.compile(r"</?span[^>]*>", re.IGNORECASE)

# Map some HTML color names to Rich-friendly colors
_COLOR_MAP: dict[str, str] = {
    "gold": "#ffd700",  # Rich supports hex colors
}


def _format_inline_code(content: str) -> str:
    """Format inline code as cyan, but not bold.

    If you want bold code, wrap it in **...**, e.g. **`123`**.
    """

    return f"[cyan]{content}[/]"


def _html_to_rich(text: str) -> str:
    """Convert a tiny subset of HTML to Rich markup.

    Supported conversions:
    - <br> / <br /> -> newline
    - <code>inline</code> -> cyan inline code (preserving inner Rich markup)
    - <pre>block</pre> -> dim code-style block
    - <span style=\"color:...\">text</span> -> [color]text[/]
    - <span style=\"font-weight:bold\">text</span> -> [bold]text[/]
    Other <span> tags are stripped, but their contents are kept.
    """

    # Line breaks: real single newlines
    text = _BR_RE.sub("\n", text)

    # First handle span-based styling so it can live *inside* code elements.
    # Colored spans -> Rich color markup
    def _span_color_repl(match: re.Match[str]) -> str:
        color = match.group(1).strip().lower()
        content = match.group(2)
        color = _COLOR_MAP.get(color, color)
        return f"[{color}]{content}[/]"

    text = _SPAN_COLOR_RE.sub(_span_color_repl, text)

    # Bold-only spans -> Rich bold markup
    def _span_bold_repl(match: re.Match[str]) -> str:
        content = match.group(1)
        return f"[bold]{content}[/]"

    text = _SPAN_BOLD_RE.sub(_span_bold_repl, text)

    # Any remaining span tags are removed (keep content)
    text = _SPAN_RE.sub("", text)

    # Inline code from HTML -> cyan (after spans so nested styling is preserved)
    text = _CODE_RE.sub(lambda m: _format_inline_code(m.group(1)), text)

    # Preformatted blocks -> dim block (we will also box fenced code below)
    def _pre_repl(match: re.Match[str]) -> str:
        inner = match.group(1).strip("\n")
        return f"\n[dim]{inner}[/dim]\n"

    text = _PRE_RE.sub(_pre_repl, text)

    return text


# Markdown-ish -> Rich markup
_HEADING_RE = re.compile(r"^(#{1,6})\s*(.+)$", re.MULTILINE)
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
_FENCE_RE = re.compile(r"```[ \t]*[^\n`]*\n(.*?)```", re.DOTALL)  # ```lang?\n...```
_LIST_RE = re.compile(r"^([*-])\s+", re.MULTILINE)
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _box_block(text: str) -> str:
    """Wrap a multiline string in a simple box using box-drawing chars."""

    lines = text.splitlines() or [""]
    width = max(len(line) for line in lines)
    top = "┌" + "─" * (width + 2) + "┐"
    bottom = "└" + "─" * (width + 2) + "┘"
    body = "\n".join("│ " + line.ljust(width) + " │" for line in lines)
    return f"[dim]{top}\n{body}\n{bottom}[/dim]"


def _markdown_to_rich(text: str) -> str:
    """Very small Markdown → Rich converter, tuned for AoC-style text.

    Handles:
    - # / ## / ... headings -> bold / bold+underline
    - **bold** -> [bold]bold[/]
    - `code` -> cyan inline code
    - ``` code fences ``` -> boxed block
    - lists starting with - or * -> bullets
    - [text](url) links -> just `text` (no color)
    """

    # Code fences (``` ... ```)
    def _fence_repl(match: re.Match[str]) -> str:
        inner = match.group(1).rstrip("\n")
        boxed = _box_block(inner)
        return "\n" + boxed + "\n"

    text = _FENCE_RE.sub(_fence_repl, text)

    # Links: keep just the link text, drop URL to avoid odd coloring
    text = _LINK_RE.sub(lambda m: m.group(1), text)

    # Headings
    def _heading_repl(match: re.Match[str]) -> str:
        level = len(match.group(1))
        content = match.group(2).strip()
        style = "bold underline" if level <= 2 else "bold"
        return f"[{style}]{content}[/]"

    text = _HEADING_RE.sub(_heading_repl, text)

    # Bold
    text = _BOLD_RE.sub(lambda m: f"[bold]{m.group(1)}[/]", text)

    # Inline code (after bold so we don't nest badly)
    text = _INLINE_CODE_RE.sub(lambda m: _format_inline_code(m.group(1)), text)

    # Simple lists
    text = _LIST_RE.sub("• ", text)

    return text


def _to_rich_markup(text: str) -> str:
    """Full pipeline: HTML + Markdown → Rich markup string."""

    text = _html_to_rich(text)
    text = _markdown_to_rich(text)
    return text


def print_markdown(path: str | Path) -> None:
    """Pretty-print a Markdown file to the terminal using Rich **with colors**.

    This is not a full Markdown renderer, but supports:
    - Headings with #, ##, ...
    - **bold**, `inline code` (cyan)
    - simple bullet lists (- or *)
    - [text](url) links (text only)
    - HTML <br>, <code>, <pre>, and <span style=\"color:…\">
    - ``` fenced code blocks ``` displayed inside a Unicode box
    """

    file_path = Path(path)
    raw = file_path.read_text(encoding="utf-8")
    markup = _to_rich_markup(raw)
    console.print(markup, markup=True)

def print_solution(solution: str) -> None:
    solution = f"\nYour puzzle answer was [bold cyan]{solution}[/]."
    console.print(solution, markup=True)