#!/usr/bin/python

import time
import urllib2

print("sent Surprise to GA")
urllib2.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-47009702-1&cid=123&t=event&ec=Consumer%20Mood&ea=Delight&el=Mood%20Per%20Second")
urllib2.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-47009702-1&cid=123&t=event&ec=Total%20Consumer%20Emotion&ea=Total%20Emotion%20Evoked&el=Engagement%20Per%20Second").close
