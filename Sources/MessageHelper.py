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

    def ding_message(self, text):
        timestamp, sign = self.get_timestamp_and_sign()

        # headers = {'Content-Type': 'application/json;charset=utf-8'}
        proxies = {
            'http': 'http://127.0.0.1:8000',
            'https': 'http://127.0.0.1:8000'
        }
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s" % (self.access_token, timestamp, sign)

        json_text = \
        {
            "msgtype": "text",
            "at": { "isAtAll": False },
            "text": { "content": text }
        }

        try:
            r = requests.post(api_url, json=json_text, proxies=proxies)
        except Exception as e:
            print(e)

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
    # "https://oapi.dingtalk.com/robot/send?access_token=39112f6272375d567dae642307290013685802daeb5df56d7fca2a0ecb4ee07f"
    # "SECf7a986ec8da03314c7f2e272cb7142b17dce8c9972ab3fb7fe13029f935e76f0"
