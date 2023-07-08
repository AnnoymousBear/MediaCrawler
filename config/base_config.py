PLATFORM = "xhs"
KEYWORDS = "松鼠"
LOGIN_TYPE = "cookies"  # qrcode or phone or cookies
# If it's on the Xiaohongshu platform, only the web_session cookie will be kept.
# xhs cookie format -> web_session=040069b2acxxxxxxxxxxxxxxxxxxxx;
COOKIES = "web_session=0400698e8ef20d56096f5d50ad364ba1553316;"

# redis config
REDIS_DB_HOST = "redis://127.0.0.1"  # your redis host
REDIS_DB_PWD = "123456"  # your redis password

# enable ip proxy
ENABLE_IP_PROXY = False

# retry_interval
RETRY_INTERVAL = 60 * 30  # 30 minutes

# playwright headless
HEADLESS = True

max_note_len=200
output_path = 'output/output.json'
