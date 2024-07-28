import unittest
from urllib.parse import urlparse, parse_qs


def extract_order_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    order_id = query_params.get('orderID', [None])[0]
    return order_id


class TestExtractOrderId(unittest.TestCase):
    def test_valid_url(self):
        url = "https://www.amazon.com/gp/your-account/order-details/ref=ppx_yo_dt_b_order_details_o00?ie=UTF8&orderID=111-3411981-3280229"
        expected_order_id = "111-3411981-3280229"
        self.assertEqual(extract_order_id(url), expected_order_id)

    def test_url_without_order_id(self):
        url = "https://www.amazon.com/gp/your-account/order-details/ref=ppx_yo_dt_b_order_details_o00?ie=UTF8"
        expected_order_id = None
        self.assertEqual(extract_order_id(url), expected_order_id)

    def test_url_with_multiple_query_params(self):
        url = "https://www.amazon.com/gp/your-account/order-details/ref=ppx_yo_dt_b_order_details_o00?ie=UTF8&orderID=111-3411981-3280229&anotherParam=value"
        expected_order_id = "111-3411981-3280229"
        self.assertEqual(extract_order_id(url), expected_order_id)

    def test_invalid_url(self):
        url = "this_is_not_a_valid_url"
        expected_order_id = None
        self.assertEqual(extract_order_id(url), expected_order_id)
