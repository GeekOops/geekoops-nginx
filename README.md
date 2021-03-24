# geekoops-nginx

Configurable ansible role for setting up a nginx webserver on a Linux server. Works with

- openSUSE Leap 15.2
- Debian Buster

## Role Variables
--------------

You can set the following variables to configure the role. Here listed are the variables and their default settings.

Firewall configuration (disable by default)

	config_firewall: false               # Enable firewall configuration
	firewall_zone: "public"              # Firewall zone to configure
    open_http: true                      # Enable http on the firewall_zone
    open_https: true                     # Enable https on the firewall_zone

Custom `nginx` settings

	nginx_user: "nginx"                  # Default nginx user (for permission ecc.)
	nginx_group: "nginx"                 # Default nginx group (for permission ecc.)


## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: geekoops-nginx, config_firewall: true }

A bit more advanced example for the imaginary `jellyfish` test server

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

## Author Information

phoenix

Have a lot of fun!

# Development

## Add githooks

This repository ships pre-commit git hooks that will check the yaml syntax. To configure them do

    git config --local core.hooksPath .githooks/
