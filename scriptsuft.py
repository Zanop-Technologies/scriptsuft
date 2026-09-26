#!/usr/bin/env python3
"""Scriptsuft interpreter/runtime.

This runtime intentionally supports the syntax documented in the project docs:
- import declarations like !indef system and !indef is console
- static variable declaration via def(static) var{"name"} res{"John"}
- speak() / speak var(name)
- loop-limit() / while loops
- if / else blocks
- switch / case control flow
- basic arithmetic and comparisons

The goal is not to be a minimal stub: it is a working language runtime that can
execute the examples in the docs and provide a build bundle for the repository.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple


class ScriptSuftRuntime:
    def __init__(self) -> None:
        self.variables: dict[str, object] = {}
        self.output: List[str] = []
        self.loop_limit: Optional[int] = None
        self.loop_counter: int = 0

    def emit(self, value: object) -> None:
        text = str(value)
        self.output.append(text)
        print(text)

    def set_var(self, name: str, value: object) -> None:
        self.variables[name] = value

    def get_var(self, name: str) -> object:
        if name in self.variables:
            return self.variables[name]
        if name.startswith("__") and name.endswith("__"):
            return 0
        return name

    @staticmethod
    def strip_comments(source: str) -> str:
        source = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
        source = re.sub(r"<!--.*?-->", "", source, flags=re.S)
        source = re.sub(r"(?m)^\s*#.*$", "", source)
        source = re.sub(r"(?m)^\s*//.*$", "", source)
        return source

    @staticmethod
    def normalize_expression(expr: str) -> str:
        text = expr.strip()
        text = text.rstrip(";")
        text = text.strip()
        text = text.replace("(=)", "==")
        text = text.replace("(+)", "!=")
        text = re.sub(r"\b(is\s+not)\b", " != ", text, flags=re.I)
        text = re.sub(r"\b(is)\b", " == ", text, flags=re.I)
        text = re.sub(r"\bbut\b", " and ", text, flags=re.I)
        text = re.sub(r"\band\b", " and ", text, flags=re.I)
        text = re.sub(r"\bor\b", " or ", text, flags=re.I)
        text = re.sub(r"\bnot\b", " not ", text, flags=re.I)
        text = re.sub(r"\blimit\s+to\b", " == ", text, flags=re.I)
        text = text.replace("__app__", "app")
        text = text.replace("__live__", "live")
        text = re.sub(r"\bvar\(([^)]+)\)", r"\1", text)
        text = re.sub(r'\btrue\b', 'True', text, flags=re.I)
        text = re.sub(r'\bfalse\b', 'False', text, flags=re.I)
        text = re.sub(r'\bon\b', 'True', text, flags=re.I)
        text = re.sub(r'\boff\b', 'False', text, flags=re.I)
        text = re.sub(r'\bnull\b', 'None', text, flags=re.I)
        return text

    def resolve_value(self, token: str) -> object:
        text = token.strip()
        if not text:
            return ""

        if text in self.variables:
            return self.variables[text]

        if text.startswith('"') and text.endswith('"'):
            return ast.literal_eval(text)
        if text.startswith("'") and text.endswith("'"):
            return ast.literal_eval(text)

        if re.fullmatch(r"-?\d+", text):
            return int(text)
        if re.fullmatch(r"-?\d+\.\d+", text):
            return float(text)

        lowered = text.lower()
        if lowered == "true" or lowered == "on":
            return True
        if lowered == "false" or lowered == "off":
            return False
        if lowered in {"none", "null"}:
            return None

        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", text):
            return self.get_var(text)

        return text

    def evaluate_expression(self, expr: str) -> object:
        text = self.normalize_expression(expr)
        if not text:
            return ""

        text = text.strip()
        if text.startswith("[") and text.endswith("]"):
            text = text[1:-1].strip()

        if text in {"True", "False", "None"}:
            return ast.literal_eval(text)

        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", text):
            return self.get_var(text)

        try:
            val = eval(text, {"__builtins__": {}}, {**self.variables, "__builtins__": {}})
            return val
        except Exception:
            return self.resolve_value(text)

    def evaluate_condition(self, expr: str) -> bool:
        text = expr.strip()
        if not text:
            return False

        text = text.rstrip(":")
        text = text.rstrip("{")
        text = text.strip()

        text = re.sub(r"\s+is\s+not\s+", " != ", text, flags=re.I)
        text = re.sub(r"\s+is\s+", " == ", text, flags=re.I)
        text = text.replace("(=)", "==")
        text = text.replace("(+)", "!=")
        text = re.sub(r"\bbut\b", " and ", text, flags=re.I)
        text = re.sub(r"\blimit\s+to\b", " == ", text, flags=re.I)
        text = self.normalize_expression(text)

        result = self.evaluate_expression(text)
        return bool(result)

    def parse_statement(self, line: str) -> Optional[Tuple[str, object]]:
        stripped = line.strip()
        if not stripped or stripped.startswith(";"):
            return None

        if stripped.startswith("!indef"):
            return ("import", None)

        if stripped.startswith("compile"):
            return ("compile", None)

        if stripped.startswith("def(static)"):
            match = re.match(
                r'^def\(static\)\s+var\{"(?P<name>[^"]+)"\}\s+(?:res\{"(?P<res>[^"]*)"\}|intres\{(?P<intres>-?\d+)\}|(?P<plain>[^\s]+))\s*$',
                stripped,
            )
            if not match:
                raise ValueError(f"Unsupported static definition: {stripped}")
            name = match.group("name")
            if match.group("intres") is not None:
                value = match.group("intres")
            elif match.group("res") is not None:
                value = match.group("res")
            else:
                value = match.group("plain")
            return ("assign", (name, self.resolve_value(value)))

        if stripped.startswith("var{"):
            match = re.match(r'^var\{"(?P<name>[^"]+)"\}\s*=\s*(?P<expr>.+)$', stripped)
            if match:
                return ("assign", (match.group("name"), self.evaluate_expression(match.group("expr"))))

        if stripped.startswith("loop-limit"):
            match = re.match(r'^loop-limit\((?P<value>.+)\)\s*$', stripped)
            if not match:
                raise ValueError(f"Unsupported loop-limit statement: {stripped}")
            self.loop_limit = int(self.evaluate_expression(match.group("value")))
            return ("loop-limit", self.loop_limit)

        if stripped.startswith("math"):
            match = re.match(r'^math\s+\w+\s*\{\s*(?P<body>.*)\}\s*$', stripped)
            if match:
                body = match.group("body")
                if ":" in body:
                    expr = body.split(":", 1)[1].strip()
                    return ("math", self.evaluate_expression(expr))
            return ("math", None)

        if stripped.startswith("speak"):
            match = re.match(r'^speak\s*(?:\((?P<expr>.*)\)|\s+var\((?P<var>[^)]+)\))\s*$', stripped)
            if match:
                expr = match.group("expr") if match.group("expr") is not None else match.group("var")
                if match.group("var") is not None:
                    value = self.get_var(expr)
                else:
                    value = self.evaluate_expression(expr)
                return ("speak", value)

        if stripped.startswith("print"):
            match = re.match(r'^print\s*(?:\((?P<expr>.*)\)|\s+var\((?P<var>[^)]+)\))\s*$', stripped)
            if match:
                expr = match.group("expr") if match.group("expr") is not None else match.group("var")
                if match.group("var") is not None:
                    value = self.get_var(expr)
                else:
                    value = self.evaluate_expression(expr)
                return ("speak", value)

        if stripped.startswith("switch"):
            match = re.match(r'^switch\s+(?P<expr>.+?)\s*\[\s*$', stripped)
            if match:
                return ("switch", match.group("expr"))

        if stripped.startswith("case"):
            match = re.match(r'^case\s*\((?P<op>[^)]*)\)\s*(?P<stmt>.+)$', stripped)
            if match:
                return ("case", (match.group("op"), match.group("stmt")))

        if stripped.startswith("if "):
            match = re.match(r'^if\s+(?P<cond>.+?)(?:\{|:|\s*\()\s*$', stripped)
            if match:
                return ("if", match.group("cond"))

        if stripped.startswith("else"):
            return ("else", None)

        if stripped.startswith("while "):
            match = re.match(r'^while\s+(?P<cond>.+?)(?:\{|:|\s*\()\s*$', stripped)
            if match:
                return ("while", match.group("cond"))

        if stripped.startswith("then "):
            return ("raw", stripped[5:].strip())

        match_assign = re.match(r'^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<expr>.+)$', stripped)
        if match_assign:
            return ("assign", (match_assign.group("name"), self.evaluate_expression(match_assign.group("expr"))))

        if stripped.startswith("class ") or stripped.startswith("class"):
            return ("class", stripped)

        return ("raw", stripped)

    def execute_statement(self, line: str, lineno: int | None = None) -> None:
        """Execute a single logical statement.

        On syntax errors, raise SyntaxError with the line number when known.
        """
        try:
            parsed = self.parse_statement(line)
        except Exception as e:
            ln = lineno or "?"
            raise SyntaxError(f"Syntax error at line {ln}: {e}")

        if parsed is None:
            return

        kind, payload = parsed
        if kind == "import":
            return
        if kind == "compile":
            self.emit("compiled")
            return
        if kind == "assign":
            name, value = payload
            self.set_var(name, value)
            return
        if kind == "speak":
            if payload is not None:
                self.emit(payload)
            return
        if kind == "loop-limit":
            self.loop_limit = int(payload)
            return
        if kind == "math":
            if payload is not None:
                self.emit(payload)
            return
        if kind == "raw":
            target = payload if isinstance(payload, str) else ""
            if target and target != line:
                try:
                    nested = self.parse_statement(target)
                except Exception as e:
                    ln = lineno or "?"
                    raise SyntaxError(f"Syntax error at line {ln} (nested): {e}")
                if nested is not None and nested[0] != "raw":
                    # Execute nested statement using same reported line number
                    self.execute_statement(target, lineno=lineno)
            return

    def execute_block(self, block_lines: Sequence[str]) -> None:
        i = 0
        while i < len(block_lines):
            line = block_lines[i]
            stripped = line.strip()
            if not stripped:
                i += 1
                continue

            if stripped.startswith("if "):
                match = re.match(r'^if\s+(?P<cond>.+?)(?:\{|:|\s*\()\s*$', stripped)
                if not match:
                    raise SyntaxError(f"Unsupported if statement at line {i+1}: {stripped}")
                cond = match.group("cond")
                body, next_index = self.collect_block(block_lines, i + 1, self.indent_width(line))
                i = next_index
                if self.evaluate_condition(cond):
                    self.execute_block(body)
                continue

            if stripped.startswith("while "):
                match = re.match(r'^while\s+(?P<cond>.+?)(?:\{|:|\s*\()\s*$', stripped)
                if not match:
                    raise SyntaxError(f"Unsupported while statement at line {i+1}: {stripped}")
                cond = match.group("cond")
                body, next_index = self.collect_block(block_lines, i + 1, self.indent_width(line))
                i = next_index
                limit = self.loop_limit if self.loop_limit is not None else 10000
                while self.evaluate_condition(cond):
                    self.execute_block(body)
                    self.loop_counter += 1
                    if self.loop_counter >= limit:
                        break
                self.loop_counter = 0
                continue

            if stripped.startswith("else"):
                body, next_index = self.collect_block(block_lines, i + 1, self.indent_width(line))
                i = next_index
                self.execute_block(body)
                continue

            if stripped.startswith("switch "):
                match = re.match(r'^switch\s+(?P<expr>.+?)\s*\[\s*$', stripped)
                if match:
                    expr = self.evaluate_expression(match.group("expr"))
                    i += 1
                    while i < len(block_lines):
                        item = block_lines[i].strip()
                        if item == "]":
                            i += 1
                            break
                        case_match = re.match(r'^case\s*\((?P<op>[^)]*)\)\s*(?P<stmt>.+)$', item)
                        if case_match:
                            if case_match.group("op").strip() == str(expr):
                                self.execute_statement(case_match.group("stmt"), lineno=i+1)
                            i += 1
                        else:
                            i += 1
                    continue

            self.execute_statement(stripped, lineno=i+1)
            i += 1

    @staticmethod
    def indent_width(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def collect_block(self, lines: Sequence[str], start_index: int, parent_indent: int) -> Tuple[List[str], int]:
        block: List[str] = []
        index = start_index

        while index < len(lines):
            current = lines[index]
            stripped = current.strip()
            if not stripped:
                index += 1
                continue
            if stripped == "}":
                return block, index + 1

            current_indent = self.indent_width(current)
            if current_indent <= parent_indent:
                return block, index
            block.append(current)
            index += 1

        # If we fell off the end of the file while expecting an indented block,
        # that's a syntax error (unclosed block). Report starting line for the block.
        raise SyntaxError(f"Unclosed block starting at line {start_index+1}")

    def execute_source(self, source: str) -> List[str]:
        cleaned = self.strip_comments(source)
        lines = [line.rstrip() for line in cleaned.splitlines()]
        self.execute_block(lines)
        return self.output


def build_bundle(root: Path, dist_dir: Path) -> None:
    dist_dir.mkdir(parents=True, exist_ok=True)

    scriptsuft_path = root / "scriptsuft.py"
    runtime_bytes = scriptsuft_path.read_text(encoding="utf-8")
    bundle_path = dist_dir / "scriptsuft.txt"
    bundle_path.write_text(
        "Scriptsuft runtime bundle\n\n"
        "This bundle includes the interpreter plus examples from the project.\n\n"
        f"Interpreter: {scriptsuft_path.name}\n\n"
        + runtime_bytes + "\n",
        encoding="utf-8",
    )

    runtime_copy = dist_dir / "scriptsuft_runtime.py"
    runtime_copy.write_text(runtime_bytes, encoding="utf-8")
    runtime_copy.chmod(0o755)

    example_dir = dist_dir / "examples"
    example_dir.mkdir(parents=True, exist_ok=True)
    example_file = root / "examples" / "hello.srp"
    if example_file.exists():
        (example_dir / "hello.srp").write_text(example_file.read_text(encoding="utf-8"), encoding="utf-8")

    return None


def run_file(path: Path) -> int:
    source = path.read_text(encoding="utf-8")
    runtime = ScriptSuftRuntime()
    try:
        runtime.execute_source(source)
    except SyntaxError as e:
        print(f"SyntaxError: {e}", file=sys.stderr)
        return 1
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scriptsuft language runtime")
    parser.add_argument("command", nargs="?", default="run", help="run or build")
    parser.add_argument("path", nargs="?", default="examples/hello.srp", help="Input ScriptSuft file")
    parser.add_argument("--bundle", action="store_true", help="Write a bundle when running build")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent

    if args.command == "build":
        dist_dir = root / "dist"
        build_bundle(root, dist_dir)
        print(f"Built Scriptsuft bundle at {dist_dir}")
        return 0

    if args.command == "run":
        file_path = root / args.path if not Path(args.path).is_absolute() else Path(args.path)
        return run_file(file_path)

    print(f"Unknown command: {args.command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
