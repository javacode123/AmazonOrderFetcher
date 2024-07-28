import os


class Constants:
    MAX_TRY_CNT = 5
    MAIN_HOST = "https://www.amazon.com"
    URL_SIGN_IN_REDIRECT = f"{MAIN_HOST}/gp/sign-in.html"
    URL_SIGN_IN = f"{MAIN_HOST}/ap/signin"
    URL_ORDER_HISTORY_LOAD = f"{MAIN_HOST}/gp/css/order-history"
    URL_ORDER_HISTORY = f"{MAIN_HOST}/your-orders/orders"

    # mock browser head
    DEFAULT_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": MAIN_HOST,
        "Referer": URL_SIGN_IN,
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
        "Sec-Ch-Viewport-Width": "1393",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Viewport-Width": "1393",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
    }

    SELECTOR_SIGN_IN = "form[name='signIn']"
    SELECTOR_ORDER_LIST = "div.order-card"
    SELECTOR_ORDER_DETAIL_LINK = "a.yohtmlc-order-details-link"
    SELECTOR_ORDER_DETAIL_INFO = "div#orderDetails"

    SIGN_IN_SUCCESS_WORD = "nav-item-signout"
    HISTORY_FILTER_QUERY_PARAM = "timeFilter"

    ORDER_SAVE_DIR = "storage"

