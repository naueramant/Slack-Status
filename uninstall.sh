#! /bin/bash

systemctl stop --user slack-status.service
systemctl disable --user slack-status.service
sudo rm /usr/local/bin/slack_status_update
sudo rm /etc/systemd/user/slack-status.service