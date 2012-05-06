#!encoding: utf-8
__author__ = 'nourlcn'

import feedparser
from Blogger import Blogger
from OctopressPost import OctopressPost
#target_url = "http://feeds.feedburner.com/nourlcn?redirect=false&amp;start-index=1&amp;max-results=500"

def convert(url, target):
    blogger = Blogger(feedparser.parse(url))
#    print blogger.get_post_num()
    count = 0 #for debug
    for x in blogger.get_all_entry(comment_entry=False):
        try:
            date = blogger.get_entry_date(x)
            time = blogger.get_entry_time(x)
            title = blogger.get_entry_title(x)
            url = blogger.get_entry_url(x)
            content = blogger.get_entry_content(x)
            tags = blogger.get_entry_tags(x)
        except Exception:
            print "Generate Post Error"
        else:
            post = OctopressPost()
            post.static_info(title,url,date,time,content,categories=tags)
#            post.write_new_md_file(target)
            list = post.get_posts_list()
            print list
            pass
#        print content
        count += 1
#        if count == 2:
#            break

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print "Usage: Python b2o.py blogger.xml dest_folder"
        sys.exit()

    target_url='/home/nourl/Dropbox/backup/blogger_content/blog-05-02-2012.xml'
    target_folder='/home/nourl/octopress_post'
    import os
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)

    convert(target_url,target_folder)
