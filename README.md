# Slack Status Service

Change your slack status based on your current wifi essid. 

## Install

For easy installation and removal you can use the scripts

```sh
# Install (prompts for root)
./install.sh

# Uninstall (prompts for root)
./uninstall.sh
```

#### Requirements
python3

#### Authentication token

This service require a slack legacy token to work. It can be obtained from:

https://api.slack.com/custom-integrations/legacy-tokens

The install script will also prompt for this.

## Wifi rules

Rules can be edited in the configration file located at `~/.config/slack-status.json`. If you ran `install.sh` this file should be initialized with an empty rule set and a token. 

#### Rule fields

| key             | Usage                                             | Required | Default |
|-----------------|---------------------------------------------------|----------|---------|
| essid_regex     | A regex to match for a wifi essid                 | Yes      |         |
| status_text     | The status text                                   | Yes      |         |
| status_emoji    | The status emoji                                  | No       |         |
| status_duration | How long before the status will expire in seconds | No       | 3600    |

#### Example configuration

```
{
    "token": "xoxp-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "rules": [
        {
            "essid_regex": "MyNetwork",
            "status_text": "Test message",
            "status_emoji": ":tram:",
            "status_duration": 3600
        }
    ]
}
```