import getpass
from lxml import html
from bs4 import BeautifulSoup
from requests import Session
import urllib.request
import urllib3

# disable unsafe message
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# TODO: implement username and password feeding to this
USERNAME = input()
PASSWORD = getpass.getpass()

# this code snippet suppresses any SSL_ERROR
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

# get ics, raises an Exception when invalid credentials
with Session() as s:
    site = s.get('https://wasm.usyd.edu.au/login.cgi?apprealm=usyd&appID=tt-studentweb&destURL=https%3A//www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/view/', verify=False)
    bs_content = BeautifulSoup(site.content, "html.parser")
    login_data = {"credential_0":USERNAME, "credential_1":PASSWORD}
    s.post('https://wasm.usyd.edu.au/login.cgi?apprealm=usyd&appID=tt-studentweb&destURL=https%3A//www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/view/', login_data, verify=False)
    try:
        ics_page = s.get('https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/view/')
    except:
        raise(Exception)
    ics_page = s.get('https://www.timetable.usyd.edu.au/personaltimetable/timetable/calendar/view/')
    get_ics = html.fromstring(ics_page.content)
    href = get_ics.xpath('//a/@href')
    ics_url = href[4]
    urllib.request.urlretrieve(ics_url, "receiveTimetable.ics")