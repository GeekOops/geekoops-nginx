#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_index(host):
	cmd = host.run("curl -v http://127.0.0.1/index.html")
	print(cmd.stdout)
	assert 'HTTP/1.1 200 OK' in cmd.stderr
	assert "Success" in cmd.stdout
	assert "The test page is displayed correctly" in cmd.stdout
