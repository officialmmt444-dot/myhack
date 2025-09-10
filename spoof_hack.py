#!/usr/bin/env python3
"""
spoof_hack.py
A harmless, local visual "spoof" that shows your name and animated random code.
For education/entertainment only. Does NOT access networks or other devices.
"""
import sys
import time
import random
import argparse
import shutil
from datetime import datetime

TERMINAL_WIDTH = shutil.get_terminal_size((80, 20)).columns

def center(text):
    return text.center(TERMINAL_WIDTH)

def slow_print(line, delay=0.01):
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def banner(name):
    lines = [
        "=" * min(TERMINAL_WIDTH, 80),
        "",
        center(f"*** {name} — SESSION LAUNCH **"),
        center(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')} (UTC)"),
        "",
        "=" * min(TERMINAL_WIDTH, 80),
    ]
    print("\n".join(lines))

def random_hex(n):
    return ''.join(random.choice("0123456789abcdef") for _ in range(n))

def animated_code_run(duration=6, speed=0.002):
    start = time.time()
    while time.time() - start < duration:
        line = "0x" + random_hex(32) + "  " + random.choice(["OK","ERR","WARN","SYNC","AUTH"])
        # randomly inject some ascii "commands"
        if random.random() < 0.08:
            line = random.choice(["[SCAN]","[BRUTE]","[INJECT]","[PROBE]"]) + " " + line
        sys.stdout.write(line + "\r")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

def progress_bar(total_steps=30, label="Processing"):
    for i in range(total_steps + 1):
        pct = int((i / total_steps) * 100)
        filled = int((TERMINAL_WIDTH-30) * (i/total_steps))
        bar = "[" + "#" * filled + "-" * max(0,(TERMINAL_WIDTH-30)-filled) + "]"
        sys.stdout.write(f"\r{label.ljust(12)} {bar} {pct}%")
        sys.stdout.flush()
        time.sleep(0.08 + random.random()*0.05)
    sys.stdout.write("\n")

def faux_report():
    items = [
        ("Open ports", random.randint(1, 27)),
        ("Credentials found", random.randint(0, 5)),
        ("Exploit modules", random.randint(0, 12)),
        ("Sessions created", random.randint(0, 3)),
        ("Data exfiltrate (MB)", random.uniform(0, 12.34)),
    ]
    print("\n" + center("=== SESSION SUMMARY ==="))
    for k,v in items:
        if isinstance(v, float):
            print(center(f"{k}: {v:.2f} MB"))
        else:
            print(center(f"{k}: {v}"))
    print(center("*** End of demo (no real actions performed) ***"))
    print()

def main():
    parser = argparse.ArgumentParser(description="Harmless spoof hack visualizer (educational).")
    parser.add_argument("--name", "-n", default="Your Name", help="Name to show in banner")
    parser.add_argument("--fast", "-f", action="store_true", help="Faster animation")
    parser.add_argument("--duration", "-d", type=float, default=6.0, help="Duration of animated code phase (seconds)")
    args = parser.parse_args()

    if args.fast:
        speed = 0.001
    else:
        speed = 0.003

    banner(args.name)
    slow_print(center("Initializing virtual console..."), delay=0.003)
    time.sleep(0.5)
    animated_code_run(duration=args.duration, speed=speed)
    progress_bar(total_steps=40, label="Analyzing")
    animated_code_run(duration=max(3, args.duration/2), speed=speed/2)
    progress_bar(total_steps=25, label="Finalizing")
    faux_report()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[Interrupted] Exiting safely.")
