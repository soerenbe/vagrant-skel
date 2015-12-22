#!/bin/bash
#
# Make sure that apt is up-to-date
#
test -e /var/cache/apt-updated || apt-get update
test -e /var/cache/apt-updated && echo 'Skipping apt-get update. /var/cache/apt-updated exists' || /bin/true
touch /var/cache/apt-updated
