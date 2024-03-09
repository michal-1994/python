import feedparser

rss = feedparser.parse("https://waitbutwhy.com/rss")
entry = rss.entries[1]
titles = [feed.title for feed in rss.entries]

for title in titles:
	print(title)
