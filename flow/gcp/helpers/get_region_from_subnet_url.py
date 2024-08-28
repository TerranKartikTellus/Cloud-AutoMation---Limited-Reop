from urllib.parse import urlparse

def get_region_from_subnet_url(url:str):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    region = path_parts[-3]
    return region