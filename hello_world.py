#!/usr/bin/env python3
"""
Fancy Hello World - neofetch style
"""

import platform
import os
import sys
import datetime


# ANSI color codes
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"


ASCII_ART = [
    "  _   _      _ _        ",
    " | | | | ___| | | ___  ",
    " | |_| |/ _ \\ | |/ _ \\ ",
    " |  _  |  __/ | | (_) |",
    " |_| |_|\\___|_|_|\\___/ ",
    "                        ",
    "  __        __         _     _  _ ",
    " \\ \\      / /__  _ __| | __| || |",
    "  \\ \\ /\\ / / _ \\| '__| |/ _` || |",
    "   \\ V  V / (_) | |  | | (_| ||_|",
    "    \\_/\\_/ \\___/|_|  |_|\\__,_|(_)",
]

ART_COLORS = [
    Color.CYAN,
    Color.CYAN,
    Color.BLUE,
    Color.BLUE,
    Color.MAGENTA,
    Color.RESET,
    Color.YELLOW,
    Color.YELLOW,
    Color.GREEN,
    Color.GREEN,
    Color.RED,
]


def get_info():
    now = datetime.datetime.now()
    uname = platform.uname()
    python_ver = sys.version.split()[0]

    uptime = ""
    try:
        with open("/proc/uptime") as f:
            seconds = float(f.read().split()[0])
        h, rem = divmod(int(seconds), 3600)
        m, s   = divmod(rem, 60)
        uptime = f"{h}h {m}m {s}s"
    except Exception:
        uptime = "N/A"

    shell = os.environ.get("SHELL", "unknown").split("/")[-1]
    term  = os.environ.get("TERM", os.environ.get("TERM_PROGRAM", "unknown"))
    user  = os.environ.get("USER", os.environ.get("USERNAME", "unknown"))
    host  = platform.node()

    return [
        (Color.CYAN   + Color.BOLD, "OS",     f"{uname.system} {uname.release}"),
        (Color.GREEN  + Color.BOLD, "Host",   host),
        (Color.YELLOW + Color.BOLD, "User",   user),
        (Color.MAGENTA+ Color.BOLD, "Python", python_ver),
        (Color.BLUE   + Color.BOLD, "Shell",  shell),
        (Color.RED    + Color.BOLD, "Term",   term),
        (Color.CYAN   + Color.BOLD, "Arch",   uname.machine),
        (Color.GREEN  + Color.BOLD, "Uptime", uptime),
        (Color.YELLOW + Color.BOLD, "Date",   now.strftime("%Y-%m-%d %H:%M:%S")),
        (Color.MAGENTA+ Color.BOLD, "Msg",    "Hello, World!"),
    ]


def color_blocks():
    blocks = ""
    colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN,
              Color.BLUE, Color.MAGENTA, Color.WHITE, Color.RESET]
    for c in colors:
        blocks += f"{c}███"
    return blocks + Color.RESET


def print_fancy():
    info = get_info()
    separator = Color.BOLD + Color.WHITE + "─" * 38 + Color.RESET

    print()
    for i, art_line in enumerate(ASCII_ART):
        color = ART_COLORS[i] if i < len(ART_COLORS) else Color.RESET
        print(f"  {color}{art_line}{Color.RESET}")

    print()
    print(f"  {separator}")

    for col, key, val in info:
        print(f"  {col}{key:<8}{Color.RESET}: {Color.WHITE}{val}{Color.RESET}")

    print()
    print(f"  {color_blocks()}")
    print()


if __name__ == "__main__":
    print_fancy()
