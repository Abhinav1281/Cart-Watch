import yaml
from checker import check_flipkart, check_amazon
from send_email import send_email
from datetime import date
import os

CHECKERS = {
    "amazon": check_amazon,
    "flipkart": check_flipkart,
    # "myntra": check_myntra,
    # "meesho": check_meesho,
}

def run_checker(config_file="products.yaml",notif_file="notifications.yaml"):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
        
    if os.path.exists(notif_file):
        with open(notif_file, "r") as f:
            notifications = yaml.safe_load(f) or {"notifications": {}}
    else:
        notifications = {"notifications": {}}
        
    today = str(date.today())
    
    for product in config['products']:
        name= product["name"]
        site = product["site"]
        checker = CHECKERS.get(site)
        if not checker:
            print(f"Unsupported site: {site}")
            continue
        product_date = product["listing_date"]
        if product_date > today:
            print(f"Skipping {name}, listing date is in the future: {product_date}")
            continue
        if notifications["notifications"] and name in notifications["notifications"]:
            if notifications["notifications"][name] >= today:
                print(f"Already notified for {name}.")
                continue
        updated = False
        available = checker(product["url"], product["check"], product.get("pincode"))
        if available:
            send_email(
                subject=f"Product {name} Available on {site}",
                body=f"{name} is available: {product['url']}")
            if notifications is None or "notifications" not in notifications or notifications["notifications"] is None:
                notifications = {"notifications": {}}
            notifications["notifications"][name] = today
            updated = True
            if updated:
                print(f"Product available: {name}, email sent.")
            else:
                print(f"Product available: {name}, but email not sent.")
        else:
            print(f"Product not available: {name}")
            
    with open(notif_file, "w") as f:
            yaml.safe_dump(notifications, f, sort_keys=False)