import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import os


class Email:
    """Send Email
    Attributes:
        sender_email: sender smail
        receiver_email: receipient email(s)
        self.password: sender password
    """

    def __init__(self, sender_email, receiver_email, password):
        """Initialize Email"""
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.password = password

    def check_df(self):
        """Checks for any differences on pieces posted on namacheko website"""
        files = os.listdir("./xlsx")
        most_rec = files[-1]
        second_most_rec = files[-2]

        first_df = pd.read_csv(f"./xlsx/{most_rec}")
        second_df = pd.read_csv(f"./xlsx/{second_most_rec}")

        change = pd.merge(first_df, second_df, how="outer", on=["Item", "Price"], indicator=True)

        diff = change[change["_merge"] != "both"][["Item", "Price"]]
        diff_dict = diff.to_dict("records")

        if len(diff_dict) == 0:
            val = "There has been no new Namacheko pieces added."
        else:
            val = diff_dict

        return val

    def set_body_file(self):
        """Set email, body, attachments, etc"""
        msg = MIMEMultipart()

        msg["Subject"] = "Namacheko AW21 Update"

        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email

        df = self.check_df()

        if isinstance(df, list):
            html = f"""
            <html>
                <head>
                <body>
                <p>Hi,</p>
                <p style = 'width: 650px; word-wrap: break-word;'>There are new Namacheko items, {df}.</p>
                </body>
                </head>
            </html>
            """
            body = MIMEText(html, "html")
            msg.attach(body)

        elif isinstance(df, str):
            html = f"""
            <html>
                <head>
                <body>
                <p>Hi,</p>
                <p style = 'width: 650px; word-wrap: break-word;'>{df}</p>
                </body>
                </head>
            </html>
            """

            body = MIMEText(html, "html")
            msg.attach(body)

        return msg

    def connect(self):
        """Connect to gmail account and send email"""
        port = 465
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email,
                self.receiver_email.split(","),
                self.set_body_file().as_string(),
            )

    def __repr__(self):
        return f"receiver email:{self.receiver_email}, sender email:{self.sender_email}"
