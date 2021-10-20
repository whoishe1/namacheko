from dotenv import dotenv_values
from email_me import Email
from scrape import namacheko
import time

config = dotenv_values(".env")
url = "https://shop.namacheko.com/aw21/"
to_emails = ", ".join(["jkoapp9112@gmail.com"])


def main():
    try:
        print("""Scraping Namacheko Website""")
        namacheko(url)
        time.sleep(1)
        print("Scraped website")

        print("""Sending email""")
        n_email = Email(
            sender_email="jkoapp9112@gmail.com",
            receiver_email=to_emails,
            password=config["PASSWORD"],
        )

        n_email.set_body_file()
        n_email.connect()
        time.sleep(1)
        print("""Sent email""")

    except Exception as e:
        print(f"""Error due to {e}""")


if __name__ == "__main__":
    main()
