[![tests](https://github.com/boutetnico/ansible-role-influxdb/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-influxdb/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.influxdb-blue.svg)](https://galaxy.ansible.com/boutetnico/influxdb)


ansible-role-influxdb
=====================

This role installs and configures [InfluxDB](https://docs.influxdata.com/influxdb/v2.0/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                  | Required | Default                            | Choices   | Comments                     |
|---------------------------|----------|------------------------------------|-----------|------------------------------|
| influxdb_dependencies     | yes      | `[apt-transport-https,curl,gnupg]` | list      |                              |
| influxdb_package_state    | yes      | `present`                          | string    | Use `latest` to upgrade.     |
| influxdb_host             | yes      | `http://localhost:8086`            | string    |                              |
| influxdb_config_path      | yes      | `/etc/influxdb`                    | string    |                              |
| influxdb_bolt_path        | yes      | `/var/lib/influxdb/influxd.bolt`   | string    |                              |
| influxdb_engine_path      | yes      | `/var/lib/influxdb/engine`         | string    |                              |
| influxdb_config           | yes      | `{}`                               | dict      | Main configuration object.   |
| influxdb_primary_org      | yes      | `example-org`                      | string    | Primary organization name.   |
| influxdb_primary_bucket   | yes      | `example-bucket`                   | string    | Primary bucket name.         |
| influxdb_primary_username | yes      | `example-user`                     | string    | Primary username.            |
| influxdb_primary_password | yes      | `ExAmPl3PA55W0rD`                  | string    | Password for primary user.   |
| influxdb_admin_token      | yes      | `EXAMPLE-TOKEN`                    | string    | Token for admin user.        |
| influxdb_orgs             | yes      | `[]`                               | list      | Additional orgs to create.   |
| influxdb_users            | yes      | `[]`                               | list      | Additional users to create.  |
| influxdb_buckets          | yes      | `[]`                               | list      | Additional buckets to create.|
| influxdb_service_enabled  | yes      | `true`                             | bool      | Start InfluxDB at boot.      |
| influxdb_service_state    | yes      | `started`                          | bool      | Use `started` or `stopped`.  |

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

    molecule test --all

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
