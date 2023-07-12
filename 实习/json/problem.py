import requests

def api_request(content):
    """
    API请求
    :param messages: 输入消息
    :return: 生成的消息 or None
    """
    if isinstance(content, str):
        # {"role": "user", "content": "请根据提供的材料，提出一个问题，并给出问题的回答。" + content + "样式要求：\n问题：\n回答：\n"}]
        messages = [
            {"role": "user", "content": """1、 请指出下列哪一项货物或物品不适用暂准进出口通关制度（ ）。
A、展览会期间出售的小卖品
B、在展览会中展示或示范用的进口货物、物品
C、承装一般进口货物进境的外国集装箱
D、进行新闻报道使用的设备、仪器
标准答案：a 
A属于一般进口货物的范围。暂准进出境货物的范围要熟悉。

将上述问题转换成如下格式：
问题：
选项：
答案："""}]
    content += """将上述问题转换成如下格式：
问题：
选项：
答案："""
    messages = [
        {
            "role":"user","content":content
        }
    ]
    response, retry_flag = None, True
    retry_times = 10

    while retry_flag:
        try:
            response = requests.post(
                "http://47.254.22.102:8989/chat",
                json={
                    "model": "gpt-3.5-turbo-0301",
                    "messages": messages,
                    "max_tokens": 1024,
                    "presence_penalty": 0,
                    "frequency_penalty": 0
                },
                timeout=300
            )
            status_code = response.status_code
            response = response.json()
            if status_code == 200:
                break
            else:
                retry_times -= 1
                if retry_times <= 0:
                    retry_flag = False
        except Exception as e:
            retry_times -= 1
            if retry_times <= 0:
                retry_flag = False
    try:
        response = response['choices'][0]['message']['content'].strip()
    except:
        response = None
    return response, content

