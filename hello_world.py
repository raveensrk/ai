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
    r" _  _ ___ _    _    ___   _ _  ___ ___ _    ___",
    r"| || | __| |  | |  / _ \ | | || _ \| _ \ |  |   \\",
    r"| __ | _|| |__| |_| (_) || \/ /|   /| |/ /| |__| |) |",
    r"|_||_|___|____|____\___/  \/  |_|_\ |___/|____|___/",
]

RAINBOW = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.MAGENTA]


def rainbow_line(text):
    result = ""
    idx = 0
    for ch in text:
        if ch != ' ':
            result += RAINBOW[idx % len(RAINBOW)] + ch
            idx += 1
        else:
            result += ch
    return result + Color.RESET


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
    for art_line in ASCII_ART:
        print(f"  {rainbow_line(art_line)}")

    print()
    print(f"  {rainbow_line('─' * 38)}")

    for i, (col, key, val) in enumerate(info):
        val_color = RAINBOW[i % len(RAINBOW)]
        print(f"  {col}{key:<8}{Color.RESET}: {val_color}{val}{Color.RESET}")

    print()
    print(f"  {color_blocks()}")
    print()


if __name__ == "__main__":
    print_fancy()
