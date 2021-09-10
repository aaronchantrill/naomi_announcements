---
id: announcements
label: Announcements
title: Announcements - NotificationClient
type: speechhandlers
description: "Have Naomi make announcements on a pre-configured schedule"
source: https://github.com/aaronchantrill/naomi_announcements/blob/master/readme.md
meta:
  - property: og:title
    content: "Announcements - NotificationClient"
  - property: og:description
    content: "Have Naomi make announcements on a pre-configured schedule"
---

# Announcements - NotificationClient

This plugin allows [Naomi](https://projectnaomi.com) to make announcements on a pre-determined schedule.

To create an announcement, edit the schedule.txt file in this directory.

The schedule.txt file uses a crontab format. It uses the [CronTab](https://pypi.org/project/crontab/)
module to interpret the time information.

The text to be read should be quoted so it is not split into words.

A typical announcement would be structured like:
`0  12  *   *   1-5 "It's lunchtime!"`
This will cause Naomi to announce "It's lunchtime!" Monday through Friday at Noon.

Installation:
`$ Naomi --install Announcements`

<EditPageLink/>
