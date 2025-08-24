import csv

def save_to_csv(data, filename):
    if not data:
        print("[WARN] No data to save.")
        return

    # Use the keys of the first dict as fieldnames
    fieldnames = ["title", "year", "rating"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"[INFO] Data saved to {filename}")
