'''
Configures login

login<string user, string pass>: accepts a user and password
'''

def login(url, u, p):
    page = requests.get(url)
    if (page.status_code == 200):
        #tree = html.fromstring(page.content)
        #input_text = tree.xpath('//input/text()')
        #for item in input_text:
        #    print(item)
        decoded = page.content.decode('UTF-8')
        post_url = re.search("<form[^>]*method=('|\")post('|\")[^>]*(\/)?>", decoded)
        if post_url != None:
            post_url = re.split("action=('|\")", post_url.group(0))
            for item in post_url:
                if item.startswith('http'):
                    post_url = re.split("\" ", item)
                    post_url = post_url[0]
                    break
            #print(post_url[0])
        else:
            return None
        user = re.search("<input[^>]*type=('|\")(text|email)('|\")[^>]*(\/)?>", decoded)
        password = re.search("<input[^>]*type=('|\")password('|\")[^>]*(\/)?>", decoded)
        if user != None and password != None:
            # print(user.group(0))
            # print(password.group(0))
            # print(post_url)
            user = user.group(0)
            password = password.group(0)
            payload = {'email': u, 'pass': p}
            r = requests.post(post_url, data=payload)
            print(r.text)
        else:
            return None

login("http://www.facebook.com", "username", "password")
