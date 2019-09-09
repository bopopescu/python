class AuctionException(Exception):
    pass


class AuctionTest:
    def __init__(self, init_prica):
        self.init_price = init_prica

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            # 此处知识简单地打印异常信息
            print('转换出异常：', e)
            # 再次引发自定义异常
            # raise AuctionException('竞拍价必须是数值，不能包含其他字符！')
            # 再次引发当前激活的异常
            raise
        if self.init_price > d:
            raise AuctionException('竞拍价比起拍价低，不允许竞拍！')
        initPrice = d


def main():
    at = AuctionTest(20.4)
    try:
        at.bid('df')
    except AuctionException as ae:
        print('main函数捕获的异常：', ae)


main()
