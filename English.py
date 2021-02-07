import requests
from bs4 import BeautifulSoup

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'input token here'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {
        'message': f'今日のNHK英語\n\n {notification_message}','stickerPackageId': 2,
        'stickerId': 516,
        }
    requests.post(line_notify_api, headers = headers, data = data)


def main():

    # Webページを取得して解析する
    load_url = "https://gogakuru.com/english/phrase/genre/index.html"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    body =""
    i=0

    # classで検索、日本語はjp、 
    topic = soup.find(class_="list_wrapper")
    for element in topic.find_all("dd"):
        if i%4==0 :
            body += element.text + "\n"
        if i%4==1:
            body += element.text + "\n\n"        
        i+=1 

    send_line_notify(body)

if __name__ == "__main__":
    main()
