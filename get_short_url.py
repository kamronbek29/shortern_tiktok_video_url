import requests

BASE_URL = 'https://api16-normal-c-alisg.tiktokv.com/shorten/'
PARAMS = {'target': 'https://m.tiktok.com/{}.html', 'share_item_id': '', 'belong': 'musical_ly'}


def get_shorter_url(video_id):
    PARAMS['share_item_id'] = str(video_id)
    PARAMS['target'].format(str(video_id))

    response = requests.get(BASE_URL, params=PARAMS)
    response_json = response.json()
    print(response_json)


if __name__ == '__main__':
    # Sample video id: 6896522967551986946
    get_shorter_url('VIDEO ID')


