from fastapi import FastAPI


import requests, json

from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/")

async def root():

    return {"message": "Hello World"}

@app.get("/{user_input}")
async def read_user_input(user_input: str):
    headers = {
        'Host': 'www.y2mate.com',
        'Connection': 'keep-alive',
        # 'Content-Length': '84',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.y2mate.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.y2mate.com/en401/convert-youtube',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,en-GB;q=0.9,en-US;q=0.8',
    }

    data = {
        'k_query': 'https://youtu.be/'+user_input,
        'k_page': 'Youtube Converter',
        'hl': 'en',
        'q_auto': '0',
    }

    response = requests.post('https://www.y2mate.com/mates/analyzeV2/ajax', headers=headers, data=data)
    data = json.loads(response.content)
    k_values = {}
    for resolution, info in data["links"]["mp4"].items():
        k_values[resolution] = info["k"]
    html_string = ""
    for resolution, k in k_values.items():
        headers = {
            'Host': 'www.y2mate.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '84',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.y2mate.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.y2mate.com/convert-youtube/'+user_input,
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en,en-GB;q=0.9,en-US;q=0.8',
        }

        data = {
            'vid': user_input,
            'k': k,
        }

        response = requests.post('https://www.y2mate.com/mates/convertV2/index', headers=headers, data=data)
        data = json.loads(response.content)
        html_string +=f"Quality: {data['fquality']} <br> Download link: {data['dlink']} <br> <br>"

    return HTMLResponse(content=html_string, status_code=200)

@app.get("/youtube/{user_input}")
async def read_user_input(user_input: str):
    headers = {
        'Host': 'www.y2mate.com',
        'Connection': 'keep-alive',
        # 'Content-Length': '84',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.y2mate.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.y2mate.com/en401/convert-youtube',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,en-GB;q=0.9,en-US;q=0.8',
    }

    data = {
        'k_query': 'https://youtu.be/'+user_input,
        'k_page': 'Youtube Converter',
        'hl': 'en',
        'q_auto': '0',
    }

    response = requests.post('https://www.y2mate.com/mates/analyzeV2/ajax', headers=headers, data=data)
    data = json.loads(response.content)
    k_values = {}
    for resolution, info in data["links"]["mp4"].items():
        k_values[resolution] = info["k"]
    html_string = ""
    for resolution, k in k_values.items():
        headers = {
            'Host': 'www.y2mate.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '84',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.y2mate.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.y2mate.com/convert-youtube/'+user_input,
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en,en-GB;q=0.9,en-US;q=0.8',
        }

        data = {
            'vid': user_input,
            'k': k,
        }

        response = requests.post('https://www.y2mate.com/mates/convertV2/index', headers=headers, data=data)
        data = json.loads(response.content)
        html_string +=f"Download link: <a href={data['dlink']}>Quality: {data['fquality']}</a>  <br> <br>"
    return HTMLResponse(content=html_string, status_code=200)
