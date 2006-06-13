import md5

from zookeepr.tests.model import *

class TestCFP(ModelTest):
    model = 'CFP'

    samples = [dict(handle='testguy',
                    email_address='testguy@example.org',
                    password='passw04d',
                    firstname='Firstname',
                    lastname='Lastname',
                    title="title yo",
                    abstract="abstract yo",
                    experience="some",
                    url="url"),
               ]
    
