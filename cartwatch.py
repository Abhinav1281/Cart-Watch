from run_check import run_checker
import time
from datetime import datetime

CHECK_INTERVAL_SECONDS = 3600  # 1 hour
def job():
    print("[RUN] Checking products...")
    run_checker("products.yaml", "notifications.yaml")

def start_scheduler():
    print("Product watcher started. Checking every hour. Press Ctrl+C to stop.")

    try:
        while True:
            print(f"[{datetime.now()}] Running product check...")
            run_checker("products.yaml", "notifications.yaml")
            
            print(f"[{datetime.now()}] Sleeping for {CHECK_INTERVAL_SECONDS//60} minutes...")
            time.sleep(CHECK_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\n🛑 Scheduler stopped gracefully.")
                   
if __name__ == "__main__":
    start_scheduler()