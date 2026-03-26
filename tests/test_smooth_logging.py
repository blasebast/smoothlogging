"""Tests for SmoothLogging module."""

import glob
import logging
import re
import tempfile
import unittest
from pathlib import Path

from smoothlogging import SmoothLogging, get_logger


class TestSmoothLogging(unittest.TestCase):
    """Test suite for SmoothLogging class."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.logger_name = "testlog"

    def tearDown(self):
        """Clean up after tests."""
        # Remove all log files
        for log_file in glob.glob(f"{self.temp_dir}/testlog_*.log"):
            Path(log_file).unlink()

    def test_logger_creation(self):
        """Test that logger is created successfully."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)
        self.assertIsNotNone(logger)
        self.assertIsInstance(logger, logging.Logger)

    def test_logger_info(self):
        """Test logging info level."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)
        result = logger.info("log info message")
        self.assertIsNone(result)

    def test_logger_warning(self):
        """Test logging warning level."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)
        result = logger.warning("log warning message")
        self.assertIsNone(result)

    def test_logger_error(self):
        """Test logging error level."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)
        result = logger.error("log error message")
        self.assertIsNone(result)

    def test_debug_level(self):
        """Test logging debug level."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)
        result = logger.debug("log debug message")
        self.assertIsNone(result)

    def test_log_file_created(self):
        """Test that log file is created with correct name format."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)
        logger.info("test message")

        # Check log files exist
        log_files = glob.glob(f"{self.temp_dir}/{self.logger_name}_*.log")
        self.assertGreaterEqual(len(log_files), 1, "No log file created")

        # Verify filename format
        pattern = re.compile(rf"{self.logger_name}_\d{{14}}\.log")
        for log_file in log_files:
            filename = Path(log_file).name
            self.assertIsNotNone(
                pattern.match(filename),
                f"Log filename {filename} doesn't match expected pattern",
            )

    def test_log_file_content(self):
        """Test that messages are written to log file."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)

        test_message = "test log message content"
        logger.info(test_message)

        # Find log file
        log_files = glob.glob(f"{self.temp_dir}/{self.logger_name}_*.log")
        self.assertEqual(len(log_files), 1)

        # Verify content
        with open(log_files[0], 'r') as f:
            content = f.read()
            self.assertIn(test_message, content)
            self.assertIn("INFO", content)

    def test_multiple_log_levels_in_file(self):
        """Test that multiple log levels are written to file."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name)

        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")

        log_files = glob.glob(f"{self.temp_dir}/{self.logger_name}_*.log")
        with open(log_files[0], 'r') as f:
            content = f.read()
            self.assertIn("INFO", content)
            self.assertIn("WARNING", content)
            self.assertIn("ERROR", content)

    def test_get_existing_logger(self):
        """Test retrieving a previously created logger."""
        smooth = SmoothLogging()
        logger1 = smooth.get_logger(self.temp_dir, "logger1")
        logger2 = smooth.get_existing_logger("logger1")

        self.assertIsNotNone(logger2)
        self.assertEqual(logger1.name, logger2.name)

    def test_get_nonexistent_logger(self):
        """Test that getting non-existent logger returns None."""
        smooth = SmoothLogging()
        logger = smooth.get_existing_logger("nonexistent")
        self.assertIsNone(logger)

    def test_console_output_disabled(self):
        """Test creating logger without console output."""
        smooth = SmoothLogging()
        logger = smooth.get_logger(self.temp_dir, self.logger_name, console=False)

        # Should have only file handler
        handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
        self.assertEqual(len(handlers), 1)

        # StreamHandler that is not a FileHandler
        console_handlers = [
            h for h in logger.handlers
            if isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
        ]
        self.assertEqual(len(console_handlers), 0)

    def test_invalid_log_directory(self):
        """Test that invalid log directory raises ValueError."""
        smooth = SmoothLogging()
        with self.assertRaises(ValueError):
            # Try to create logger with a path we don't have permissions for
            smooth.get_logger("/root/nonexistent/deeply/nested/path", self.logger_name)

    def test_convenience_function(self):
        """Test the convenience get_logger function."""
        logger = get_logger(self.temp_dir, self.logger_name)
        self.assertIsNotNone(logger)
        self.assertIsInstance(logger, logging.Logger)

        logger.info("test message")
        log_files = glob.glob(f"{self.temp_dir}/{self.logger_name}_*.log")
        self.assertGreaterEqual(len(log_files), 1)


if __name__ == '__main__':
    unittest.main()
