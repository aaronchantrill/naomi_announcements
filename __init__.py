# -*- coding: utf-8 -*-
import os
import re
import shlex
from crontab import CronTab
from datetime import datetime
from naomi import app_utils
from naomi import plugin
from naomi import profile

                        
class AnnouncementPlugin(plugin.NotificationClientPlugin):
    def __init__(self, *args, **kwargs):
        super(AnnouncementPlugin, self).__init__(*args, **kwargs)
        self.update_schedule()

    def update_schedule(self):
        schedule_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "schedule.txt"
        ) 
        self._schedule = []
        # Set last_time to current time so we will start processing events
        # from this point forward
        self.timestamp = datetime.now(tz=app_utils.get_timezone())
        for line in open(schedule_file, 'r'):
            line = line.strip(' \t\n')
            if((len(line) > 0)and(line[0] != '#')):
                # Split the line into cron and text
                crontask = shlex.split(line)
                cron = " ".join(crontask[:-1])
                task = crontask[-1]
                # store these values into a schedule struct
                self._schedule.append({
                    'cron': cron,
                    'task': task
                })
                self._logger.info("added {}: '{}'".format(cron,task))

    def gather(self, last_time):
        tz = app_utils.get_timezone()
        current_time = datetime.now(tz=tz)
        # loop through self._schedule
        for index in range(len(self._schedule)):
            # figure out when the last time the event should have occured is
            event = CronTab(self._schedule[index]['cron'])
            if(event.previous(now=current_time)+(current_time-last_time).total_seconds())>0:
                # The default value for the gather function launches it every 30 seconds,
                # so generally a specific minute should be hit twice. It also may be
                # set to launch less frequently, in which case we want to go ahead and
                # make the announcement the next time it does launch. So we need to know
                # when we last made the announcement so we don't repeat it twice, and
                # also so that we don't skip it if the gather function is not called
                # during the minute it should be.
                self._mic.say(self._schedule[index]['task'])
        return current_time
