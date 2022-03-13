# 钉钉警报机器人
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import json

class DingDingMessageHelper :
    def __init__(self, token, secret):
        self.access_token = token
        self.secret = secret
        self.proxy = \
        {
            'http': 'http://127.0.0.1:8000',
            'https': 'http://127.0.0.1:8000'
        }
        self.url = "https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s"


    def ding_message(self, text):
        json_text = \
        {
            "msgtype": "text",
            "at": { "isAtAll": False },
            "text": { "content": text }
        }
        try:
            timestamp, sign = self.get_timestamp_and_sign()
            api_url = self.url % (self.access_token, timestamp, sign)
            r = requests.post(api_url, json=json_text, proxies=self.proxy)
            return
        except Exception as e:
            pass

        try:
            timestamp, sign = self.get_timestamp_and_sign()
            api_url = self.url % (self.access_token, timestamp, sign)
            r = requests.post(api_url, json=json_text)
            return
        except Exception as e:
            pass

    def get_timestamp_and_sign(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign

def get_dingding_msg_helper(token, secret):
    msgHelper =  DingDingMessageHelper(token, secret)
    return msgHelper

if __name__ == "__main__":
    pass
    # ding = get_dingding_msg_helper('39112f6272375d567dae642307290013685802daeb5df56d7fca2a0ecb4ee07f',
    #                         'xxx')
    # ding.ding_message("Test Class for Test")