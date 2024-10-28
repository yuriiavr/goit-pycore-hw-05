import sys
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    if len(parts) == 4:
        date, time, level, message = parts
        return {"date": date, "time": time, "level": level, "message": message.strip()}
    else:
        return {}

def load_logs(file_path: str) -> List[dict]:

    logs = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                log = parse_log_line(line)
                if log: 
                    logs.append(log)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:

    return [log for log in logs if log["level"] == level.upper()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:

    levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
    counts = {level: 0 for level in levels}
    for log in logs:
        if log["level"] in counts:
            counts[log["level"]] += 1
    return counts

def display_log_counts(counts: Dict[str, int]):

    print("\nСтатистика за рівнями логування:")
    print(f"{'Рівень':<10} | {'Кількість':<10}")
    print("-" * 22)
    for level, count in counts.items():
        print(f"{level:<10} | {count:<10}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python task3.py <шлях_до_файлу_логу> [рівень_логування]")
        return

    file_path = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f"\nЛоги для рівня {log_level}:")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
        else:
            print(f"Немає записів для рівня {log_level}.")
    else:
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)

if __name__ == "__main__":
    main()
