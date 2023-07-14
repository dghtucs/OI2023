import api
import datetime

now = datetime.datetime.now()
timestamp = int(now.timestamp() * 1000)

app_secret = "XgXIEyrkiXFUhYnURVnLr4C3BxkpXqw9"

request_data = {
  "global_params":{
    "app_id":"icpRW7Xg7lbyEoRjvQGOu2XexH3L050N",
    "nonce":"cb000406-f077-11ed-acc1-8c8590725661",
    "timestamp":timestamp,
    "sign_method":"SHA-256",
    "version":"LLM-V1",
    "scene_group_id":60006
  },
  "detail_params":{
    "member_id":23424523534,
    "content":[
      {"role":"USER","text_id":"12341234","text_desc":"你知道谁xxxx是谁吗?"},
      {"role":"SYSTEM","text_id":"45674567","text_desc":"他是。。。。。，以上仅代表机器的个人观点，请参考。"}
    ]
  }
}

response = api.risk_assessment(request_data, app_secret)
print(response.json())