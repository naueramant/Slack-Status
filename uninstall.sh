#! /bin/bash

systemctl stop --user slack-status.service slack-status.timer
systemctl disable --user slack-status.service slack-status.timer
sudo rm /usr/local/bin/slack_status_update
sudo rm /etc/systemd/user/slack-status.*