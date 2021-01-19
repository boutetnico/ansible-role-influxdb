[![tests](https://github.com/boutetnico/ansible-role-influxdb/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-influxdb/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.influxdb-blue.svg)](https://galaxy.ansible.com/boutetnico/influxdb)


ansible-role-influxdb
=====================

This role installs and configures [InfluxDB](https://docs.influxdata.com/influxdb/v2.0/).

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                  | Required | Default                          | Choices   | Comments                     |
|---------------------------|----------|----------------------------------|-----------|------------------------------|
| influxdb_dependencies     | yes      | `[gnupg]`                        | list      |                              |
| influxdb_version          | yes      | `2.0.3`                          | string    |                              |
| influxdb_config_path      | yes      | `/etc/influxdb/config.yml`       | string    |                              |
| influxdb_bolt_path        | yes      | `/var/lib/influxdb/influxd.bolt` | string    |                              |
| influxdb_engine_path      | yes      | `/var/lib/influxdb/engine`       | string    |                              |
| influxdb_config           | yes      | `{}`                             | dict      |                              |
| influxdb_default_org      | yes      | `example-org`                    | string    |                              |
| influxdb_default_bucket   | yes      | `example-bucket`                 | string    |                              |
| influxdb_default_username | yes      | `example-user`                   | string    |                              |
| influxdb_default_password | yes      | `ExAmPl3PA55W0rD`                | string    |                              |
| influxdb_orgs             | yes      | `[]`                             | list      |                              |
| influxdb_users            | yes      | `[]`                             | list      |                              |
| influxdb_buckets          | yes      | `[]`                             | list      |                              |
| influxdb_service_enabled  | yes      | `true`                           | bool      | Start InfluxDB at boot.      |
| influxdb_service_state    | yes      | `started`                        | bool      | Use `started` or `stopped`.  |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-influxdb

          influxdb_orgs:
            - name: main-org
              description: Main organization
            - name: guest-org

          influxdb_users:
            - name: admin01
              org: main-org
              password: secretPassword
            - name: guest01
              org: guest-org
              password: secretPassword

          influxdb_buckets:
            - name: bucket01
              description: First bucket
              org: main-org
              retention: 1d
            - name: bucket02
              org: main-org

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
