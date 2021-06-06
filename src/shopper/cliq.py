import time

import requests
from bs4 import BeautifulSoup

from .sms import CONTACTS, send_message


def back_in_stock(button):
    sold_out = "sold out"
    return button.text.lower() != sold_out


def main():
    DESIRED = "2-4 Chair Bag"
    still_out_of_stock = True

    URL = "https://www.cliqproducts.com/pages/bags"

    while still_out_of_stock:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        products = soup.find_all(class_="custom-product-details")
        bag = [p for p in products if p.find("h2").text == DESIRED][0]

        buttons = bag.select("button")

        if len(buttons) == 1:
            button = buttons[0]
            if back_in_stock(button):
                send_message(
                    "Cliq Chair Bag back in stock!", recipient=CONTACTS["andy"]
                )
                still_out_of_stock = False
            else:
                pass
        else:
            send_message("Cliq website changed!", recipient=CONTACTS["michelle"])

        time.sleep(3600)


if __name__ == "__main__":
    main()
