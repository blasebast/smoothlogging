===============================
SmoothLogging
===============================

.. image:: https://img.shields.io/pypi/v/smoothlogging.svg
        :target: https://pypi.python.org/pypi/smoothlogging

Effortless logging to both file and console with automatic timestamped filenames.

Features
--------

* Simple API for configurable logging to file and console
* Automatic timestamped log files (``myapp_20240326143022.log``)
* Consistent log formatting across your application
* Full Python 3.7+ support
* Type hints for better IDE support
* Proper error handling and validation

Installation
------------

.. code-block:: bash

    pip install smoothlogging

Quick Start
-----------

**Using the convenience function:**

.. code-block:: python

    from smoothlogging import get_logger

    logger = get_logger("/var/log/myapp", "myapp")
    logger.info("Application started")
    logger.warning("Something unexpected happened")
    logger.error("An error occurred")

**Using the SmoothLogging class:**

.. code-block:: python

    from smoothlogging import SmoothLogging
    import logging

    smooth = SmoothLogging()
    logger = smooth.get_logger("/var/log/myapp", "myapp", level=logging.DEBUG)

    # Log to file and console (default)
    logger.info("Message with file and console output")

    # Create another logger without console output
    file_only = smooth.get_logger("/var/log/myapp", "file-only", console=False)

API Reference
-------------

**get_logger(log_dir, name, level=logging.DEBUG, console=True)**

    Convenience function to create and configure a logger.

    - ``log_dir``: Directory for log files (created if doesn't exist)
    - ``name``: Logger and log file prefix name
    - ``level``: Logging level (default: DEBUG)
    - ``console``: Enable console output (default: True)
    - Returns: Configured logger instance

**SmoothLogging.get_logger(...)**

    Class method with same parameters as convenience function.

**SmoothLogging.get_existing_logger(name)**

    Retrieve a previously created logger by name.
    - Returns: Logger instance or None if not found

