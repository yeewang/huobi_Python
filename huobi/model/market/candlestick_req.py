from huobi.constant import *


class CandlestickReq:
    """
    The candlestick/kline data received by subscription of candlestick/kline.

    :member
        rep: the Channel or topic you subscribed.
        id: the UNIX formatted timestamp generated by server in UTC.
        data: the data of candlestick/kline.

    """

    def __init__(self):
        self.rep = ""
        self.id = 0
        self.data = list()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.rep, format_data + "Channel")
        PrintBasic.print_basic(self.id, format_data + "Unix Time")
        print()
        if len(self.data):
            for row in self.data:
                row.print_object()
                print()