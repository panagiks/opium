=====
opium
=====


.. image:: https://img.shields.io/pypi/v/opium.svg
        :target: https://pypi.python.org/pypi/opium

.. image:: https://img.shields.io/travis/panagiks/opium.svg
        :target: https://travis-ci.com/panagiks/opium

.. image:: https://readthedocs.org/projects/opium/badge/?version=latest
        :target: https://opium.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




OpenShift Pod Independent Usage Metrics (OPIUM) pulling & aggregating metrics from multiple pods made easy!


* Free software: MIT license
* Documentation: https://opium.readthedocs.io.


Aggregating metrics from pods through OKD's router can be a challenge. OPIUM offers the next best thing.
While it doesn't (yet) aggregate the varius metrics it gathers the metrics from the defined Deployment Configs
on a specific OKD project and serves them to a single /metrics endpoint. This way it allows for easier gathering
of per-pod metrics.

Configuration
-------------

OPIUM is configured through environment variables and specifically the following:

* OPIUM_OKD_URL => The url of the OKD instance's master, including the scheme and without a trailing `/`
* OPIUM_OKD_TOKEN => An access token for a service account with `view` and `edit` permissions on the desired project
* OPIUM_PROJECT => Project to be exported
* OPIUM_DEPLOYMENT_CONFIGS => Comma separated (no spaces) list of Deployment Configs to export

OKD Preparation
---------------

In your OKD admin CLI you will need to run the following

.. code-block:: bash

    # create a service account
    oc create serviceaccount <account>
    # Retrieve the service account's access token (set this to OPIUM_OKD_TOKEN)
    oc serviceaccounts get-token <account>
    # Give the service account the required permissions to the desired project
    oc policy add-role-to-user view system:serviceaccount:<project>:<account>
    oc policy add-role-to-user edit system:serviceaccount:<project>:<account>


Execution
---------

To start OPIUM (after you've set the configuration environment variables appropriately) simly run:

.. code-block:: bash

    opium

This will spawn an HTTP server listening on your system's public interface and on port 8080.

Configuration for the listening interface, as well as a containerized version of OPIUM will follow in later versions.

Features
--------

* Gather the response of `/metrics` from all the pods of the specified `deployment_config`
* Serve them as one response

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
