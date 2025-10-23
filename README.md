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

### Method 1: Direct Use (Recommended)
```bash
git clone https://github.com/wjdavis5/BrutePy.git
cd BrutePy
pip install -r requirements.txt
```

### Method 2: Package Installation
```bash
git clone https://github.com/wjdavis5/BrutePy.git
cd BrutePy
pip install -e .
```

### Quick Start
After installation, try the example wordlist:
```bash
python Brute.py http://httpbin.org/basic-auth/user/pass example_wordlist.txt user --verbose
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
                [--ignore-invalid-certificate] [--max-retries MAX_RETRIES]
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
  --max-retries MAX_RETRIES
                        Maximum retries for 429 rate limit responses (default: 3)
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

### Scan with custom rate limit retry settings
```bash
python Brute.py https://example.com/admin rockyou.txt admin \
    --threads 5 \
    --max-retries 5 \
    --delay 500 \
    --verbose
```

## Rate Limiting and 429 Response Handling

BrutePy now includes intelligent handling of HTTP 429 (Too Many Requests) responses:

### Automatic Retry Logic
- **Exponential Backoff**: If no `Retry-After` header is present, uses 1s, 2s, 4s, 8s delays
- **Retry-After Header**: Respects server-specified retry delays when provided
- **Configurable Retries**: Use `--max-retries` to set retry limit (0-10, default: 3)
- **Thread-Safe**: Each thread handles its own retries without blocking others

### Example Rate Limit Handling
```
Trying: admin:[REDACTED] (line 150) -> 429
Rate limited (429). Server requests waiting 5.0s (Retry-After header)
Retrying in 5.0 seconds... (attempt 1/3)
Trying: admin:[REDACTED] (line 150) (attempt 2/4) -> 200
[SUCCESS] Authentication successful!
```

### Best Practices for Rate-Limited Targets
```bash
# Conservative approach for heavily rate-limited targets
python Brute.py https://example.com/admin wordlist.txt admin \
    --threads 1 \
    --delay 2000 \
    --max-retries 5 \
    --verbose

# Balanced approach for moderate rate limiting
python Brute.py https://example.com/admin wordlist.txt admin \
    --threads 3 \
    --delay 1000 \
    --max-retries 3
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
- **Rate Limit Handling**: Intelligent 429 response handling with exponential backoff and Retry-After header support

## Wordlists

Common wordlists for brute force attacks:
- [SecLists](https://github.com/danielmiessler/SecLists)
- [RockYou](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt)
- [FuzzDB](https://github.com/fuzzdb-project/fuzzdb)

Example usage with included wordlist:
```bash
python Brute.py https://target.com/admin example_wordlist.txt admin --verbose
```

## Troubleshooting

### Connection Issues

**Problem**: `Connection failed` error immediately after starting
```
Error: Connection failed - [Errno 111] Connection refused
```
**Solutions**:
- Verify the target URL is correct and accessible
- Check if the target server is running
- Ensure you have network connectivity to the target
- Try testing with `curl` or a browser first

**Problem**: Connection timeout
```
Error: Request timed out
```
**Solutions**:
- Increase connection timeout (currently hardcoded to 10 seconds)
- Check for network latency issues
- Verify the target isn't blocking your IP
- Consider using `--delay` to slow down requests

### SSL/TLS Issues

**Problem**: SSL certificate verification fails
```
Error: SSL/TLS error - certificate verify failed
```
**Solutions**:
- Use `--ignore-invalid-certificate` flag for self-signed certificates
- Update your system's CA certificates
- Only bypass SSL verification for testing environments you control

### Rate Limiting

**Problem**: Getting 429 responses
```
Rate limited (429). Using exponential backoff
```
**Solutions**:
- Increase `--delay` value (e.g., `--delay 2000` for 2 seconds)
- Reduce `--threads` count (e.g., `--threads 1`)
- Increase `--max-retries` value (e.g., `--max-retries 5`)
- The tool automatically handles 429 with exponential backoff

### Performance Issues

**Problem**: Scan is too slow
**Solutions**:
- Increase thread count: `--threads 10`
- Decrease delay: `--delay 10`
- Use a smaller, targeted wordlist
- Ensure good network connectivity

**Problem**: Scan is too fast / getting blocked
**Solutions**:
- Decrease thread count: `--threads 1`
- Increase delay: `--delay 1000`
- Use `--max-retries` to handle rate limiting better

### Wordlist Issues

**Problem**: `Wordlist file not found`
**Solutions**:
- Check file path is correct
- Use absolute path instead of relative
- Verify file permissions are readable
- Check for typos in filename

**Problem**: Scan ends too quickly with empty wordlist
**Solutions**:
- Verify wordlist file has content
- Check for encoding issues (should be UTF-8)
- Ensure wordlist has one password per line
- Try the included `example_wordlist.txt`

### Authentication Issues

**Problem**: No success but credentials are correct
**Solutions**:
- Verify the authentication type is Basic Auth
- Check if the endpoint requires different credentials format
- Test credentials manually with browser or curl
- Verify URL points to correct authentication endpoint

**Problem**: Success but shows wrong credentials
**Solutions**:
- This shouldn't happen - please file a bug report
- Verify with manual test using the credentials shown
- Check output file with `--output` for details

### Python/Dependency Issues

**Problem**: `ModuleNotFoundError: No module named 'requests'`
**Solutions**:
```bash
pip install -r requirements.txt
# or
pip install requests>=2.31.0
```

**Problem**: Python 2 syntax errors
**Solutions**:
- Use Python 3.6 or later
- Check Python version: `python --version`
- Use `python3` explicitly if needed

### General Tips

- **Start with verbose mode** (`--verbose`) to see what's happening
- **Test with small wordlists first** to verify everything works
- **Use the example wordlist** to confirm setup is correct
- **Check logs** with `--output` flag to review all attempts
- **Monitor target system** logs to understand response patterns
- **Respect rate limits** to avoid being blocked or causing issues
- **Use appropriate delays** based on target system capacity

### Getting Help

If you encounter issues not covered here:
1. Check existing [GitHub Issues](https://github.com/wjdavis5/BrutePy/issues)
2. Review the [SECURITY.md](SECURITY.md) for security-related questions
3. Read [CONTRIBUTING.md](CONTRIBUTING.md) for development help
4. Create a new issue with:
   - Python version (`python --version`)
   - Operating system
   - Command used (redact sensitive info)
   - Error message (full output)
   - Expected vs actual behavior

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