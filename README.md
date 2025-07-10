# BrutePy
Python HTTP Basic Authentication Brute Force Tool

BrutePy is a modern, feature-rich tool for performing HTTP Basic Authentication brute force attacks for penetration testing and security assessment purposes.

## Features

- **Python 3 Compatible**: Fully updated for Python 3.x
- **Multi-threaded**: Support for concurrent requests to speed up brute force attacks
- **Modern HTTP Library**: Uses the `requests` library for better reliability and features
- **SSL/TLS Support**: Proper SSL certificate validation with option to ignore self-signed certificates
- **Progress Reporting**: Real-time progress updates and statistics
- **Output Logging**: Save results to file for documentation
- **Robust Error Handling**: Comprehensive error handling for network issues, timeouts, and invalid inputs
- **Security Enhancements**: Password redaction in logs and secure defaults
- **Input Validation**: Validates URLs, file existence, and parameter ranges
- **Flexible Configuration**: Multiple command-line options for customization

## Requirements

- Python 3.6+
- `requests` library (usually pre-installed)

## Installation

```bash
git clone https://github.com/wjdavis5/BrutePy.git
cd BrutePy
```

## Usage

### Basic Usage
```bash
python Brute.py https://target.com/admin wordlist.txt admin
```

### Advanced Usage
```bash
python Brute.py https://target.com/admin wordlist.txt admin \
    --delay 1000 \
    --threads 5 \
    --verbose \
    --output results.txt \
    --ignore-invalid-certificate
```

### Command Line Options

```
usage: Brute.py [-h] [--delay DELAY] [--startat STARTAT] 
                [--ignore-consecutive-empty IGNORE_CONSECUTIVE_EMPTY]
                [--threads THREADS] [--verbose] [--output OUTPUT] 
                [--ignore-invalid-certificate]
                target words user

HTTP Auth Brute Force Tool

positional arguments:
  target                The target URI. ex http://192.168.1.1
  words                 The wordlist to choose passwords from
  user                  The username to use

optional arguments:
  -h, --help            show this help message and exit
  --delay DELAY         Time in milliseconds between each request (default: 5)
  --startat STARTAT     Start at this line in the wordlist file (default: 0)
  --ignore-consecutive-empty IGNORE_CONSECUTIVE_EMPTY
                        Ignore this many consecutive empty lines before exiting (default: 4)
  --threads THREADS     Number of concurrent threads (default: 1, max: 50)
  --verbose, -v         Enable verbose output showing each attempt
  --output OUTPUT, -o OUTPUT
                        Output results to file
  --ignore-invalid-certificate
                        Ignore untrusted SSL certificates
```

## Examples

### Single-threaded scan with 2-second delay
```bash
python Brute.py https://example.com/admin rockyou.txt admin --delay 2000
```

### Multi-threaded scan for faster results
```bash
python Brute.py https://example.com/admin rockyou.txt admin --threads 10 --delay 100
```

### Resume scan from specific line
```bash
python Brute.py https://example.com/admin rockyou.txt admin --startat 1000
```

### Scan with self-signed certificate and verbose output
```bash
python Brute.py https://192.168.1.1:8443/admin wordlist.txt admin \
    --ignore-invalid-certificate \
    --verbose \
    --output scan_results.txt
```

## Security Considerations

- **Responsible Use**: Only use this tool against systems you own or have explicit permission to test
- **Rate Limiting**: Use appropriate delays to avoid overwhelming target servers
- **SSL Verification**: SSL certificate validation is enabled by default for security
- **Password Logging**: Passwords are redacted in console output to prevent accidental exposure

## Changes from Original

### Version 2.0 Improvements:
- **Python 3 Compatibility**: Fixed all Python 2 syntax issues
- **Modern Libraries**: Migrated from `httplib2` to `requests`
- **Multi-threading**: Added concurrent request support for better performance
- **Enhanced Security**: SSL verification enabled by default, password redaction
- **Better Error Handling**: Comprehensive exception handling and input validation
- **Progress Reporting**: Real-time status updates and completion statistics
- **Output Options**: Save results to file with `--output` flag
- **Verbose Mode**: Detailed logging with `--verbose` flag
- **Input Validation**: Validates URLs, files, and parameter ranges
- **Graceful Interruption**: Proper handling of Ctrl+C and cleanup

## Wordlists

Common wordlists for brute force attacks:
- [SecLists](https://github.com/danielmiessler/SecLists)
- [RockYou](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)
- [FuzzDB](https://github.com/fuzzdb-project/fuzzdb)

## Legal Disclaimer

This tool is intended for authorized security testing and educational purposes only. Users are responsible for ensuring they have proper authorization before testing any systems. Unauthorized access to computer systems is illegal and may result in criminal charges.

## License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Version History

- **v2.0**: Complete modernization with Python 3, threading, enhanced security
- **v1.0**: Original Python 2 implementation