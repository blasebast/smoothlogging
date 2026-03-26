"""SmoothLogging - Easy and consistent logging with file and console output."""

import logging
import os
import time
from pathlib import Path
from typing import Optional


LOG_FORMAT = '%(asctime)-16s %(levelname)-8s %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class SmoothLogging:
    """
    Configurable logging to both file and console output.

    Example usage:
        from smoothlogging import SmoothLogging

        logger = SmoothLogging().get_logger("/path/to/logs", "myapp")
        logger.info('Application started')
        logger.warning('Something unexpected happened')
        logger.error('An error occurred')

    Log files are created with timestamp: myapp_20240326143022.log
    """

    def __init__(self):
        """Initialize SmoothLogging."""
        self._loggers = {}

    def get_logger(
        self,
        log_dir: str,
        name: str,
        level: int = logging.DEBUG,
        console: bool = True,
    ) -> logging.Logger:
        """
        Create and configure a logger with file and optional console output.

        Args:
            log_dir: Directory to store log files
            name: Name for the logger and log file prefix
            level: Logging level (default: DEBUG)
            console: Whether to also log to console (default: True)

        Returns:
            Configured logger instance

        Raises:
            ValueError: If log_dir is invalid or cannot be created
            OSError: If log file cannot be created
        """
        # Validate and create log directory
        try:
            log_path = Path(log_dir)
            log_path.mkdir(parents=True, exist_ok=True)
        except (OSError, PermissionError) as e:
            raise ValueError(f"Cannot create log directory '{log_dir}': {e}") from e

        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Remove existing handlers to avoid duplicates
        for handler in logger.handlers:
            handler.close()
            logger.removeHandler(handler)

        # Create formatter
        formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

        # Add file handler
        timestamp = time.strftime('%Y%m%d%H%M%S')
        log_file = log_path / f'{name}_{timestamp}.log'

        try:
            file_handler = logging.FileHandler(log_file, mode='w')
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (OSError, PermissionError) as e:
            raise OSError(f"Cannot create log file '{log_file}': {e}") from e

        # Add console handler if requested
        if console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        # Store reference to logger
        self._loggers[name] = logger

        return logger

    def get_existing_logger(self, name: str) -> Optional[logging.Logger]:
        """
        Get a previously created logger by name.

        Args:
            name: Logger name

        Returns:
            Logger instance if exists, None otherwise
        """
        return self._loggers.get(name)


# Convenience function for simple usage
def get_logger(
    log_dir: str,
    name: str,
    level: int = logging.DEBUG,
    console: bool = True,
) -> logging.Logger:
    """
    Create a logger with one function call.

    Args:
        log_dir: Directory to store log files
        name: Name for the logger and log file prefix
        level: Logging level (default: DEBUG)
        console: Whether to also log to console (default: True)

    Returns:
        Configured logger instance
    """
    smooth = SmoothLogging()
    return smooth.get_logger(log_dir, name, level, console)


__all__ = ['SmoothLogging', 'get_logger']
