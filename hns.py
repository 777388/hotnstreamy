import certstream
import requests
import urllib3

def check_url_accessibility(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def on_message(message, context):
    domains = message['data']['leaf_cert']['all_domains']
    for domain in domains:
        if "cdn" in domain:
            color = "\033[36m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "api" in domain:
            color = "\033[33m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "dev" in domain:
            color = "\033[35m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "s3" in domain:
            color = "\033[31m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "ftp" in domain:
            color = "\033[32m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "cloud" in domain:
            color = "\033[34m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "archive" in domain:
            color = "\033[37m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "db" in domain:
            color = "\033[90m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "content" in domain:
            color = "\033[94m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "dl" in domain:
            color = "\033[96m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        elif "sql" in domain:
            color = "\033[93m"
            url = f"https://{domain}"
            if check_url_accessibility(url):
                print(f"{color}{url}\033[0m is accessible.")
        else:
            pass
        

certstream.listen_for_events(on_message)
