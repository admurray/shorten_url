import shortuuid


def get_short_url_id():
    short_url_mapping = shortuuid.uuid()
    return f'{short_url_mapping}'


def get_short_url(short_url_id):
    return f"/s/{short_url_id}"
