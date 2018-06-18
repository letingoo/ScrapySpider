from scrapy import cmdline


name = 'tikubaba'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())