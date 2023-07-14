import hashlib
import json
import requests

def risk_assessment(request_data, app_secret):

    app_id = request_data['global_params']['app_id']
    scene_group_id = request_data['global_params']['scene_group_id']
    nonce = request_data['global_params']['nonce']
    timestamp = request_data['global_params']['timestamp']
    sign_method = request_data['global_params']['sign_method']
    version = request_data['global_params']['version']


    member_id = request_data['detail_params']['member_id']
    content = request_data['detail_params']['content']


    base_str = f"app_id={app_id}content={json.dumps(content,ensure_ascii=False)}member_id={member_id}nonce={nonce}scene_group_id={scene_group_id}sign_method={sign_method}timestamp={timestamp}version={version}"
    base_str = base_str.upper()
    base_str = app_secret + base_str + app_secret
    print(base_str)

    sign = hashlib.sha256((base_str).encode('utf-8')).hexdigest().upper()
    print(sign)

    request_data['global_params']['sign'] = sign


    response = requests.post("https://antispam.zhihu.com/api/v1/risk", json=request_data)

    return response