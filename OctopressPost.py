#!encoding: utf-8
__author__ = 'nourlcn'

class OctopressPost():
    def __init__(self):
        self.valid_post = False

    def static_info(self,title,url,date,time,content,categories=None,comment=None):
        self.title = title
        self.url = url
        self.date = date
        self.comment = True
        try:
            self.categories = ['ImportFromBlogger'] + [str(x) for x in categories]
        except :
            self.categories = ['ImportFromBlogger']
        self.basic_info = """---
layout: post
title: "%s"
date: %s
comments: true
categories: %s
---""" % (self.title, self.date + ' ' + time , self.categories)
        self.content = "\n\n\n" + content
        
    def write_new_md_file(self,target):
        """
        Format: <li><span>01 May 2012</span> &raquo; <a href="http://nourlcn.ownlinux.net">My Google Blogger</a></li>
        """
        file_name = self.date + '-' + self.url + '.markdown'

        print """<li><span>%s</span> &raquo; <a href="%s">%s</a></li>""" % (self.date, self.url, self.title)
#        md_file = file(target + '/' + file_name,'w')
#        md_file.write(self.basic_info)
#        md_file.write(self.content.encode('utf-8'))
#        md_file.close()
#        print "Done"

    def get_posts_list(self):
        """
        Format: <li><span>01 May 2012</span> &raquo; <a href="http://nourlcn.ownlinux.net">My Google Blogger</a></li>
        """
        return """<li><span>%s</span> &raquo; <a href="%s">%s</a></li>""" % (self.date, self.url, self.title)

