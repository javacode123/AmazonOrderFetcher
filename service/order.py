import datetime

from service.client import Client
from service.constants import Constants
from model.order import OrderModel
from util.util import extract_order_id


class Order:
    """
    Order Class used to get order list.
    """

    def __init__(self, client: Client) -> None:
        self.client: Client = client

    def save_orders(self, year: int = datetime.date.today().year):
        self.client.get(Constants.URL_ORDER_HISTORY_LOAD)
        next_page = "{url}?{query_param}=year-{year}".format(url=Constants.URL_ORDER_HISTORY,
                                                             query_param=Constants.HISTORY_FILTER_QUERY_PARAM,
                                                             year=year)
        while next_page:
            self.client.get(next_page)
            for order_tag in self.client.last_response_parsed.select(Constants.SELECTOR_ORDER_LIST):
                detail_link = order_tag.select_one(Constants.SELECTOR_ORDER_DETAIL_LINK)
                full_detail_link = Constants.MAIN_HOST + detail_link.get("href")
                print("get order detail link:", full_detail_link)
                order_id = extract_order_id(full_detail_link)
                self.client.get(full_detail_link)
                od = self.client.last_response_parsed.select_one(Constants.SELECTOR_ORDER_DETAIL_INFO)
                if od is not None:
                    om = OrderModel(od, order_id)
                    om.save()
                    # TODO parse and save
            # TODO should load all pages orders
            next_page = ""
