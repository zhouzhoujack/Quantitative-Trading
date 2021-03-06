import ccxt
import time
import sys
import logging
from .MessageHelper import *

def set_logging_helper():
    logger = logging.getLogger()
    # setting for log.txt
    log_file_name = "{}_log.txt".format(time.strftime('%Y_%m_%d %H_%M', time.localtime()))
    logging.basicConfig(filename=log_file_name,
                        format='[%(asctime)s](%(levelname)s) %(message)s',
                        level=logging.INFO)

    # setting for console
    # format = logging.Formatter('[%(asctime)s](%(levelname)s) %(message)s')
    # hander = logging.StreamHandler(sys.stderr)
    # hander.setLevel(logging.INFO)
    # hander.setFormatter(format)
    # logger.addHandler(hander)

    return logger

logger = set_logging_helper()       # 记录日志信息

def get_exchange(apikey, secret):
    exchange = ccxt.binance(
        {
            'proxies': {
            'http': 'http://127.0.0.1:8000',
            'https': 'http://127.0.0.1:8000'
        },
        'options': {'adjustForTimeDifference': True},
        'apiKey': apikey,
        'secret': secret,
    })
    return exchange

class mid_class():
    def __init__(self, robot, this_exchange):
        '''
        初始化数据填充交易所的信息，首次获取价格，首次获取account信息
        设定好密钥……
        Args:
            this_exchange: FMZ的交易所结构
        '''
        self.init_timestamp = time.time()
        self.exchange = this_exchange
        self.symbol = 'ETH/USDT'
        self.robot = robot

    def get_account(self):
        '''
        获取账户的USDT余额和ETH余额
        '''
        try:
            self.account = self.exchange.fetch_balance()
            self.USDT_balance = self.account['USDT']['free']
            self.ETH_balance = self.account['ETH']['free']
        except Exception as e:
            msg = "get_account() have a error : {}".format(e)
            logger.error(msg)
            print("[{}] {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))
            self.robot.ding_message(msg)
            return False
        return True

    def get_ticker(self):
        '''
        获取市价信息
        '''
        try:
            self.ticker = self.exchange.fetch_ticker(self.symbol)
            self.high = self.ticker['high']
            self.low = self.ticker['low']
            self.last = self.ticker['last']
        except Exception as e:
            msg = "get_ticker() have a error : {}".format(e)
            logger.error(msg)
            print("[{}] {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))
            self.robot.ding_message(msg)
            return False
        return True

    def create_order(self, order_type , order_side, price, amount):
        '''
        post一个挂单信息,
        order_type: market 为市价交易, limit 为限价交易
        order_side: buy 或者 sell
        '''
        if order_type == "market":
            order_id = self.exchange.create_order(self.symbol, 'market', order_side, amount)
        elif order_type == 'limit':
            if order_side == 'buy':
                order_id = self.exchange.create_limit_buy_order(self.symbol, amount, price)
            else:
                order_id = self.exchange.create_limit_sell_order(self.symbol, amount, price)

        return order_id

    def cancel_order(self, order_id):
        '''
        取消一个挂单信息
        '''
        return self.exchange.cancel_order(order_id, self.symbol)

    def refreash_data(self):
        '''
        刷新信息
        Returns:
            刷新信息成功返回， 否则返回相应刷新失败的信息提示
        '''
        if(not self.get_account()):
            return False
        if(not self.get_ticker()):
            return False
        return True

class avg_position_class():
    def __init__(self, robot, mid_class, min_bs_amount, min_trade_quantity):
        self.jys = mid_class
        self.last_time = time.time()
        self.Buy_count = 0
        self.Sell_count = 0
        self.Min_Buy_Sell_Amount = min_bs_amount
        self.Min_Trade_Quantity = min_trade_quantity
        self.strategy_status_info = {}
        self.last_trade_price = self.correct_last_trade_price()
        self.robot = robot

    def correct_last_trade_price(self):
        # 有时断点重启，需要自动更新到上次的均仓价格
        try:
            if(self.jys.USDT_balance != 0):
                return self.jys.USDT_balance / self.jys.ETH_balance
        except:
            pass

    def make_need_account_info(self):
        self.strategy_status_info = {}

        if(not self.jys.refreash_data()):
            return False, self.strategy_status_info

        self.B = self.jys.ETH_balance
        self.money = self.jys.USDT_balance
        now_price = self.jys.last

        self.total_money = self.B * now_price + self.money
        self.half_money = self.total_money / 2
        self.need_buy = (self.half_money - self.B * now_price) / now_price
        self.need_sell = (self.half_money - self.money) / now_price

        self.strategy_status_info['eth'] = self.B
        self.strategy_status_info['usdt'] = self.money
        self.strategy_status_info['last'] = self.jys.last
        self.strategy_status_info['need_buy'] = self.need_buy
        self.strategy_status_info['need_sell'] = self.need_sell
        self.strategy_status_info['last_trade_price'] = self.last_trade_price

        return True, self.strategy_status_info

    def do_juncang(self):
        # 需要确保最小交易额大于10usdt，不然会报错
        if self.need_buy > self.Min_Buy_Sell_Amount and self.need_buy*self.jys.last > self.Min_Trade_Quantity:
            self.jys.create_order('market', 'buy', self.jys.low, self.need_buy)
            msg = "Buy: {}  price: {}".format(self.need_buy, self.jys.last)
            logging.critical(msg)
            print("[{}] {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))
            self.robot.ding_message(msg)
            return True

        elif self.need_sell > self.Min_Buy_Sell_Amount and self.need_sell*self.jys.last > self.Min_Trade_Quantity:
            self.jys.create_order('market', 'sell', self.jys.high, self.need_sell)
            msg = "Sell: {}  price: {}".format(self.need_sell, self.jys.last)
            logging.critical(msg)
            print("[{}] {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))
            self.robot.ding_message(msg)
            return True

        return False

    def if_need_trade(self, condition, prama):
        if condition == 'price':
            vol = abs((self.jys.last - self.last_trade_price) / self.last_trade_price)*100
            if vol >= prama and self.do_juncang():
                self.last_trade_price = self.jys.last

def test_connect_exchange(apiKey, secret, ding_token, ding_secret):
    # 测试所提供的Api key和secret是否能连接上交易所
    # 同时测试钉钉机器人是否连接
    # 若可以，则返回账户余额信息
    # 若无法连接，则返回连接失败，并返回错误的账户信息
    exchange = get_exchange(apiKey, secret)
    dingding_msg_robot = get_dingding_msg_helper(ding_token, ding_secret)
    test_mid = mid_class(dingding_msg_robot, exchange)
    if(test_mid.refreash_data()):
        return True, test_mid.USDT_balance, test_mid.ETH_balance
    else:
        return False, "can not connect exchange", "can not connect exchange"

def init_setting_of_strategy(params):
    # 利用页面的参数初始化策略
    exchange = get_exchange(params['key'], params['secret'])
    dingding_msg_robot = get_dingding_msg_helper(params['ding_access_token'], params['ding_secret'])
    test_mid = mid_class(dingding_msg_robot, exchange)
    test_mid.refreash_data()
    strategy = avg_position_class(dingding_msg_robot, test_mid, params['min_amount'], params['min_trading_limit'])
    strategy.make_need_account_info()
    return strategy

if __name__ == '__main__':
    pass