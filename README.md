[![Test deployment](https://github.com/GeekOops/geekoops-nginx/actions/workflows/CI.yml/badge.svg)](https://github.com/GeekOops/geekoops-nginx/actions/workflows/CI.yml)

# geekoops-nginx

Configurable ansible role for setting up a nginx webserver on a Linux server. Works with

- openSUSE Leap 15.5
- openSUSE Leap 15.6
- Debian Bookworm (11)

## Role Variables
--------------

You can set the following variables to configure the role. Here listed are the variables and their default settings.

Firewall configuration (disable by default)


| Value | Description | Default |
|-------|-------------|---------|
|`config_firewall` | Enable firewall configuration | false |
|`firewall_zone` | Firewall zone to configure | "public" |
|`open_http` | Open http port | true |
|`open_https` | Open https port | true |
|`setup_default_page` | Setup a default page | false |
|`default_page_hostname`| Hostname for the default page | "localhost" |


## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: jellyfish
      roles:
         - { role: geekoops-nginx, config_firewall: true }

An advanced example for the imaginary `jellyfish` test server

    - hosts: jellyfish
      roles:
         - role: geekoops-nginx
           vars:
             setup_default_page: true
             default_page_hostname: "{{ansible_host}}"
             config_firewall: true
             firewall_zone: "public"

## License

MIT

# Development

## Add githooks

This repository ships pre-commit git hooks that will check the yaml syntax. To configure them do

    git config --local core.hooksPath .githooks/
