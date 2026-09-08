"""Smoke tests guarding against publishing a package that cannot be used at all.

Versions 11.10.0 and 11.10.1 shipped with a broken ``endpoints/_base.py`` that
made every endpoint module fail to import, yet the test suite passed because no
test imported the driver or the generated endpoints. These tests make sure that
every module in the distribution imports, that the drivers expose every
generated endpoint, and that the version string the release bot writes is well
formed.
"""

import importlib
import pkgutil
import re

import pytest

import mattermostautodriver
from mattermostautodriver import AsyncTypedDriver, TypedDriver
from mattermostautodriver import version


def _raise(name):
    raise ImportError(f"Failed to import package {name}")


def _all_module_names():
    # walk_packages silently skips packages that fail to import unless onerror
    # raises, which would hide exactly the kind of breakage tested for here
    return sorted(
        module.name
        for module in pkgutil.walk_packages(mattermostautodriver.__path__, "mattermostautodriver.", onerror=_raise)
    )


def _endpoint_module_names():
    return sorted(
        name.rsplit(".", 1)[1]
        for name in _all_module_names()
        if name.startswith("mattermostautodriver.endpoints.") and not name.rsplit(".", 1)[1].startswith("_")
    )


ALL_MODULES = _all_module_names()
ENDPOINT_MODULES = _endpoint_module_names()

# Offline driver options, the client is created but never connects
DRIVER_OPTIONS = {"url": "localhost", "max_retries": 0}


def test_package_contains_endpoint_modules():
    # Guard the parametrized tests below against silently testing nothing
    assert len(ENDPOINT_MODULES) > 50


@pytest.mark.parametrize("module_name", ALL_MODULES)
def test_module_imports(module_name):
    importlib.import_module(module_name)


@pytest.mark.parametrize("driver_cls", [TypedDriver, AsyncTypedDriver])
def test_driver_can_be_constructed(driver_cls):
    driver = driver_cls(DRIVER_OPTIONS)
    assert driver.client is not None


@pytest.mark.parametrize("driver_cls", [TypedDriver, AsyncTypedDriver])
@pytest.mark.parametrize("module_name", ENDPOINT_MODULES)
def test_driver_exposes_endpoint(driver_cls, module_name):
    module = importlib.import_module(f"mattermostautodriver.endpoints.{module_name}")
    (class_name,) = module.__all__
    endpoint_cls = getattr(module, class_name)

    driver = driver_cls(DRIVER_OPTIONS)
    endpoint = getattr(driver, module_name, None)
    assert isinstance(endpoint, endpoint_cls), f"{driver_cls.__name__}.{module_name} is not a {class_name} instance"
    assert endpoint.client is driver.client


def test_full_version_is_well_formed():
    # Release versions track the Mattermost server version, optionally with a
    # PEP 440 post-release suffix when a package had to be republished
    assert re.fullmatch(r"\d+\.\d+\.\d+(\.post\d+)?", version.full_version), version.full_version


def test_short_version_is_major_minor():
    major, minor, *_ = version.full_version.split(".")
    assert version.short_version == f"{major}.{minor}"
