import json
import os
from typing import Optional
from bs4 import Tag
from service.constants import Constants


class OrderModel:
    def __init__(self, info: Optional[Tag], order_id: str):
        self.info = info
        self.order_id = order_id
        self.ordered: str = self._ordered()
        self.address: dict = self._parse_addr()

    def _ordered(self) -> str:
        order_date_span = self.info.find('span', class_='order-date-invoice-item')
        order_date = order_date_span.get_text(strip=True).replace("Ordered on ", "")
        return order_date

    def _parse_addr(self) -> dict:
        address = {"full_name": self.info.find('li', class_='displayAddressFullName').text,
                   "address_line1": self.info.find('li', class_='displayAddressAddressLine1').text,
                   "city_state_postal": self.info.find('li', class_='displayAddressCityStateOrRegionPostalCode').text,
                   "country": self.info.find('li', class_='displayAddressCountryName').text}
        return address

    def save(self):
        """Dump the instance attributes to a JSON file."""
        storage_dir = Constants.ORDER_SAVE_DIR
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        filename = os.path.join(storage_dir, f"{self.order_id}.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_serializable_dict(), f, ensure_ascii=False, indent=4)

    def to_serializable_dict(self):
        """Convert the instance to a serializable dictionary."""
        return {
            'order_id': self.order_id,
            'ordered': self.ordered,
            'address': self.address
        }
