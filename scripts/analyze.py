
import json
from collections import Counter
from pathlib import Path

log_files = sorted(
    p for p in Path("evidence/full-logs").glob("cowrie.json*")
    if not p.name.endswith("2026-10-27")
)

events = Counter()
ips = Counter()
usernames = Counter()
passwords = Counter()
commands = Counter()
days = Counter()
timestamps = []

for log_file in log_files:
    with log_file.open(encoding="utf-8") as f:
        for line in f:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            event_type = event.get("eventid", "")
            events[event_type] += 1

            if event.get("timestamp"):
                timestamp = event["timestamp"]
                timestamps.append(timestamp)
                days[timestamp[:10]] += 1

            if event_type == "cowrie.session.connect":
                if event.get("src_ip"):
                    ips[event["src_ip"]] += 1

            elif event_type in (
                "cowrie.login.failed",
                "cowrie.login.success",
            ):
                usernames[event.get("username", "unknown")] += 1
                passwords[event.get("password", "unknown")] += 1

            elif event_type == "cowrie.command.input":
                commands[event.get("input", "")] += 1


def show_top(title, counter, n=10):
    print(f"\n=== {title} ===")
    for value, count in counter.most_common(n):
        print(f"{count:>6}  {value}")


print("=== COWRIE ATTACK SUMMARY ===")
print("Files analyzed:", len(log_files))
print("Total events:", sum(events.values()))
print("SSH connections:", events["cowrie.session.connect"])
print("Unique source IPs:", len(ips))
print("Failed logins:", events["cowrie.login.failed"])
print("Successful honeypot logins:", events["cowrie.login.success"])
print("Commands executed:", events["cowrie.command.input"])

if timestamps:
    print("First event:", min(timestamps))
    print("Last event:", max(timestamps))

show_top("Top 10 Source IPs", ips)
show_top("Top 10 Usernames", usernames)
show_top("Top 10 Passwords", passwords)
show_top("Top 10 Commands", commands)
show_top("Event Types", events, 20)

print("\n=== EVENTS BY DATE (UTC) ===")
for day, count in sorted(days.items()):
    print(f"{day}: {count:,} events")
