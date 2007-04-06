"""MoinMoin wiki integration."""

from exceptions import ImportError

from paste.httpexceptions import HTTPException
from sqlalchemy import create_session

from zookeepr.lib.base import *
from zookeepr.lib.BeautifulSoup import BeautifulSoup
from zookeepr.model import Person

try:
    from MoinMoin.server.wsgi import moinmoinApp
    from MoinMoin.request import RequestWSGI
    import cgi

    class RequestZookeepr(RequestWSGI):
        def __init__(self, request):
            self.requestZookeepr = request
            RequestWSGI.__init__(self, request.environ)
            
        def setup_args(self, form=None):
            formvars = self.requestZookeepr.POST
            getvars = self.requestZookeepr.GET
            vars = [formvars, getvars]
            args = {}

            for var in vars:
                for key in var:
                    values = var.getall(key)
                    fixedResult = []
                    for item in values:
                       if isinstance(item, cgi.FieldStorage) and item.filename:
                           args[key + '__filename__'] = item.filename
                           fixedResult.append(item.value)
                       else:
                           fixedResult.append(item)
                    args[key] = fixedResult

            return self.decodeArgs(args)
    
    has_moin = True
except ImportError:
    has_moin = False

import re

cleaner_regexp = re.compile(r'<body.*?>(.*?)</body>', re.S)

def get_wiki_response(request, start_response):
    from zookeepr.lib.base import abort
    if not has_moin:
        abort(404)
        return

    dbsession = create_session()

    if 'signed_in_person_id' in session:
        people = dbsession.query(Person).select_by(id=session['signed_in_person_id'])
        if len(people) > 0:
            request.environ['AUTH_TYPE'] = 'Basic'
            request.environ['REMOTE_USER'] = people[0].handle
        
    moinReq = RequestZookeepr(request)
    moinReq.run()
    start_response(moinReq.status, moinReq.headers)
    dbsession.close()
    res = ''.join(moinReq.output())
    if type(res)==str:
      res = res.decode('utf8', 'replace')
    return res

def wiki_here():
    from zookeepr.lib.base import request
    def start_response(status, headers, exc_info=None):
        pass

    try:
        wiki_content = get_wiki_response(request, start_response)
        match = cleaner_regexp.search(wiki_content)
        if match:
            return match.groups()[0]
    except HTTPException:
        return ''

def wiki_fragment(page_name='Home'):
    """Use a Moin page as content as a fragment."""
    from zookeepr.lib.base import request
    def start_response(status, headers, exc_info=None):
        pass

    request.environ['PATH_INFO'] = '/' + page_name
    soup = BeautifulSoup(get_wiki_response(request, start_response))
    try:
        content = soup.findAll('div', id='content')
	if len(content)==0:
	  content = '(no content)'
	else:
	  content = content[0]
        return '<div class="wiki">\n%s\n</div>' % (content,)
    except IndexError:
        print "soup is: %r" % (soup.prettify(),)
        # If it's a boring old security issue, then don't show anything,
        # because we're a fragment!
        if "You are not allowed to access this!" in soup.prettify():
            return ''
        else:
            # Raise an error so we can print it out when this happens during
            # a test and see what MoinMoin is complaining about
            raise
        return 'BONE'

def wiki_html_fragment(page_name='Home'):
    """Use a Moin page as a raw HTML fragment."""
    # TODO jaq to refactor this as johnf doesn't know what he's doing :)
    from zookeepr.lib.base import request
    def start_response(status, headers, exc_info=None):
        pass

    from MoinMoin.request import RequestCLI
    from MoinMoin.Page import Page
    from MoinMoin.PageEditor import PageEditor

    request = RequestCLI('localhost/mywiki', page_name)
    editor = PageEditor(request, page_name)
    text = editor.get_raw_body()

    # Remove ACLs TODO - use a better regex
    regex = re.compile( '(^|\n) *#[^\n]*' )
    text = regex.sub('\n', text)

    return text
