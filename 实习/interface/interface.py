import hashlib
import json
import time
import requests

def risk_assessment(params):

    
    base_params = params.copy()
    base_params.pop("sign", None)
    base = "".join(["{}={}".format(k,v) for k,v in sorted(base_params.items())])
    base = base.upper()
    sign = hashlib.sha256((app_secret + base + app_secret).encode('utf-8')).hexdigest().upper()

    params["sign"] = sign
    
    
    url = "https://antispam.zhihu.com/api/v1/risk" 
    headers = {
        "Ip": params["ip"],
        "Port": params["port"],
        "User-Agent": params["user_agent"], 
        "Referer": params["referer"]
    }
    resp = requests.post(url, json=params, headers=headers)

    return resp.json()


if __name__ == "__main__":

    app_secret = "XgXIEynkiXfuhYnURVnLr4c3BxkpXqw9"
    app_id = "icpRW7Xg7lbyEoRjvQ60u2XexH3Lo50N" 

    params = {
        "ip": "1.1.1.1",
        "port": '80',
        "user_agent": "Mozilla/5.0",
        "referer": "https://www.example.com",

        "global_params": {
            "app_id":"icpRW7Xg7lbyEoRjvQ60u2XexH3Lo50N",
            "scene_group_id": 60006,
            "nonce": "cb000406-f077-11ed-acc1-8c8590725661",
            "timestamp": int(time.time()*1000),
            "sign_method": "SHA-256",
            "version": "LLM-V1"
        },

        "detail_params": {
            "member_id": 23424523534,
            "content": [
                {
                    "role": "USER",
                    "text_id": "12341234",
                    "text_desc": "你知道谁xxxx是谁吗?"
                },
                {
                    "role": "SYSTEM",
                    "text_id": "45674567",
                    "text_desc": "他是。。。。。,以上仅代表机器的个人观点,请参考。"
                }
            ]
        }
    }

    result = risk_assessment(params)
    print(result)