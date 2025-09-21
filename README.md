# Cart-Watch
CartWatch is a lightweight Python app that tracks product availability on Amazon, Flipkart, Myntra, and Meesho. Configure URLs and check types, in YAML, and receive email alerts when items are in stock. Efficient, configurable, and prevents duplicate notifications.


## YAML Configuration Formats

CartWatch uses YAML files to specify which products to monitor and how to check their availability. It also uses YAML files to configure email notifications. Below are example formats for the configuration files:

### Example: `products.yaml`

```yaml
products:
    - name: "Product A"
      url: "https://www.flipkart.com/example-product-a"
      site: "flipkart"
      check: "button"
      pincode: "452103"
      listing_date: "2024-07-15"

    - name: "Product B"
      url: "https://www.flipkart.com/example-product-b"
      site: "flipkart"
      check: "button"
      pincode: "761204"
      listing_date: "2024-11-03"
```

- `name`: Human-readable name for the product.
- `url`: Product page URL.
- `site`: Marketplace to monitor (e.g., flipkart, amazon).
- `check`: Method to verify availability (e.g., button, stock).
- `pincode`: Delivery area code for availability checks.
- `listing_date`: Date when monitoring should start (YYYY-MM-DD).

### Example: `email_config.yaml`

```yaml
email:
  - user_email: "your_email@email.com"
    password : "YOUR_PASSWORD"
    smtp_server: "YOUR SMTP PORT"
    smtp_port: "YOUR PORT"
```

- `email.user_email`: Email address used to send alerts.
- `email.password`: Password or app-specific password for the sender.
- `email.smtp_server`: SMTP server address.
- `email.smtp_port`: SMTP server port.