# Changelog

All notable changes to BrutePy will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-10-23

### Added
- Python package management with `setup.py`, `requirements.txt`, and `pyproject.toml`
- Example wordlist for quick testing (`example_wordlist.txt`)
- CHANGELOG.md for tracking version history
- Improved package installation support

### Fixed
- Connection failure handling now exits immediately instead of hanging
- Queue draining logic prevents deadlocks on early exit
- Worker threads properly handle found_password flag

### Improved
- More responsive exit on connection failures
- Better thread synchronization and cleanup

## [2.0.0] - 2024

### Added
- Python 3 compatibility (migrated from Python 2)
- Multi-threading support (1-50 concurrent threads)
- Modern `requests` library (replaced deprecated `httplib2`)
- SSL/TLS certificate validation (enabled by default)
- Verbose output mode (`--verbose` flag)
- Output logging to file (`--output` flag)
- Progress reporting (every 10 attempts in normal mode)
- Input validation for URLs, files, and parameters
- Graceful interruption handling (Ctrl+C)
- HTTP 429 rate limit handling with exponential backoff
- Retry-After header support for rate limiting
- Configurable retry attempts for rate limits
- Password redaction in logs for security
- Comprehensive error handling for network issues
- Resume capability from specific line in wordlist
- SSL certificate validation toggle for self-signed certificates
- Request timeout protection (10 seconds)
- User-agent header in requests

### Changed
- SSL verification is now enabled by default (was disabled)
- Minimum thread count is 1, maximum is 50
- Default delay reduced from unspecified to 5ms
- Better error messages and user feedback
- Improved code organization and modularity

### Fixed
- All Python 2 to Python 3 migration issues
- Hanging on connection failures
- Race conditions in multi-threaded execution
- Missing error handling for various failure modes

### Security
- SSL certificate validation enabled by default
- Password redaction in console output
- Secure defaults for all options
- Input validation to prevent injection attacks

## [1.0.0] - Original Release

### Initial Features
- Basic HTTP Basic Authentication brute force
- Python 2 implementation
- Single-threaded operation
- httplib2 library for HTTP requests
- Basic command-line interface

