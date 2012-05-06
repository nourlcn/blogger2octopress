__author__ = 'nourlcn'

class Blogger():
    def __init__(self,blogger_feedparser):
        self.blogger = blogger_feedparser
        self.current = 0
        self.entry_num = -1
        self.post_num = -1
        
    def get_post_num(self):
        if self.entry_num > 0:
            return self.entry_num
        count = 0
        for x in self.blogger.entries:
            count += 1
        self.entry_num = count
        return count
    
    def get_all_entry(self,comment_entry=False):
#        TODO return Comment Eentry
        result =[]
        count = 0
#        print type(self.blogger.entries)
        for x in self.blogger.entries:

            if x['id'].find('post') > 0:
                flag = True
                for link in x['links']:
                    if link['href'].find('showComment') > 0:
                        flag = False
                        break
                if flag:
                    result.append(x)
                    count += 1

        self.post_num = count
        return result

    def get_entry_date(self,entry):
        return entry['updated'][:10]
    def get_entry_time(self,entry):
        return entry['updated'][11:16]

    def get_entry_title(self,entry):
        return entry['title']
    def get_entry_url(self,entry):
        result=""
        for x in entry['links']:
            if x['type'] == u'text/html':
#                result = x['href'].split('/')[-1] # do not use base_url
#                if result[-5:] == '.html':
#                    result = result[:-5]
                result = x['href']
        return result
    def get_entry_tags(self,entry):
        result=[]
        for x in entry['tags']:
            if x['term'].find('google.com') == -1:
                result.append(x['term'])
        return result
    def get_entry_content(self,entry):
        return entry['content'][0]['value']


#        for x in entry:
#            print x,
#
#        print
#
##        print entry['id']
#        print "tags",entry['tags']
#        print "title",entry['title']
#        print "links",entry['links']


#        print entry['published_parsed']
#        print entry['updated_parsed']



