import pytest

import os

import json


@pytest.mark.parametrize(
    "name",
    [
        ("influxdb2"),
        ("influxdb2-cli"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("influxdb", "influxdb", "/etc/influxdb/config.yml"),
        ("root", "root", "/etc/default/influxdb2"),
    ],
)
def test_influxdb_config_file(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/lib/systemd/system/influxdb.service"),
    ],
)
def test_systemd_config_file_exists(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize(
    "name",
    [
        ("influxdb"),
    ],
)
def test_influxdb_service_is_running_and_enabled(host, name):
    service = host.service(name)
    assert service.is_enabled
    assert service.is_running


def test_influxdb_replies_to_ping(host):
    command = "influx ping"
    ping = host.check_output(command)
    assert ping == "OK"


@pytest.mark.parametrize(
    "url,token,org,active,path",
    [
        (
            os.environ.get("INFLUX_HOST"),
            "EXAMPLE-TOKEN",
            "example-org",
            "true",
            "/root/.influxdbv2/configs",
        ),
    ],
)
def test_influxdb_auth_file(host, url, token, org, active, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.contains(f'url = "{url}"')
    assert config.contains(f'token = "{token}"')
    assert config.contains(f'org = "{org}"')
    assert config.contains(f"active = {active}")


@pytest.mark.parametrize(
    "name,description",
    [
        ("example-org", ""),
        ("main-org", "Main organization"),
        ("guest-org", ""),
    ],
)
def test_influxdb_organizations_exist(host, name, description):
    command = "influx org ls --json"
    json_data = host.check_output(command)
    items_list = json.loads(json_data)
    for item in items_list:
        if item["name"] == name and item["description"] == description:
            assert True
            break
    else:
        assert False


@pytest.mark.parametrize(
    "name",
    [
        ("example-user"),
        ("admin01"),
        ("guest01"),
    ],
)
def test_influxdb_users_exist(host, name):
    command = "influx user ls --json"
    json_data = host.check_output(command)
    items_list = json.loads(json_data)
    for item in items_list:
        if item["name"] == name:
            assert True
            break
    else:
        assert False


@pytest.mark.parametrize(
    "name,description,org",
    [
        ("example-bucket", "", "example-org"),
        ("bucket01", "First bucket", "main-org"),
        ("bucket02", "", "main-org"),
    ],
)
def test_influxdb_buckets_exist(host, name, description, org):
    command = f"influx bucket ls --json --org {org}"
    json_data = host.check_output(command)
    items_list = json.loads(json_data)
    for item in items_list:
        if item["name"] == name:
            if "description" in item:
                assert item["description"] == description
                break
            assert True
            break
    else:
        assert False
