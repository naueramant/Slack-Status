#! /bin/bash

function install {
    sudo cp slack_status.py /usr/local/bin/slack_status_update
    sudo chmod 755 /usr/local/bin/slack_status_update
    sudo cp -p systemd/* /etc/systemd/user
    systemctl enable --user slack-status.service
    systemctl start --user slack-status.service
}

function gen_config {
    echo ""
    echo "Generate an authentication token here:"
    echo "https://api.slack.com/custom-integrations/legacy-tokens"
    echo "and insert it below."
    echo ""

    read -p "Token: " TOKEN

    echo ""
    
    cat > ~/.config/slack-status.json << EOL
{
    "token": "$TOKEN",
    "rules": []
}
EOL
}

install
gen_config

echo "Now add some rules to ~/.config/slack-status.json"
echo "See the readme for more information"