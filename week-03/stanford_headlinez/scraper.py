def print_hedz(url='https://www.stanford.edu/news/'):
    
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)
    
    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)

def extract_headline_text(txt):
    headline = txt.split('<')
    for x in headline:
        if 'href' in x:
            return x.split('>')[1]

def parse_headline_tags(txt):
    
    htmlstrings = []
    lines = txt.splitlines()
    for x in lines:
        if 'h3><a' in x:
            htmlstrings.append(x)
    return htmlstrings

def fetch_html(url):
    
    import requests
    resp = requests.get(url)
    return resp.text

