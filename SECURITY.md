# Security Policy

## Purpose and Responsible Use

BrutePy is a security testing tool designed for **authorized penetration testing and security assessments only**. 

### Legal Notice

- **Only use on systems you own or have explicit written permission to test**
- Unauthorized access to computer systems is illegal in most jurisdictions
- Users are solely responsible for ensuring legal compliance
- The maintainers assume no liability for misuse of this tool

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.1.x   | :white_check_mark: |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting Security Vulnerabilities

We take security vulnerabilities seriously. If you discover a security issue in BrutePy:

### DO:

1. **Email the maintainers directly** (do not create public issues)
2. Provide detailed information about the vulnerability:
   - Description of the issue
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if you have one)
3. Allow reasonable time for a fix before public disclosure
4. Work with us to verify the fix

### DO NOT:

- Create public GitHub issues for security vulnerabilities
- Exploit the vulnerability beyond proof-of-concept
- Share vulnerability details publicly before a fix is available
- Use vulnerabilities for malicious purposes

## Security Best Practices

### For Users

1. **Always use SSL verification** unless absolutely necessary for testing
   - Only use `--ignore-invalid-certificate` when required
   - Understand the security implications

2. **Protect credentials and wordlists**
   - Never commit wordlists with real credentials
   - Store wordlists securely
   - Clear sensitive files after testing

3. **Use rate limiting appropriately**
   - Respect target systems with `--delay` and `--threads` options
   - Monitor for and respect rate limiting responses
   - Avoid overwhelming target systems

4. **Secure output files**
   - Use `--output` option to save results
   - Protect output files with appropriate permissions
   - Securely delete output files when no longer needed

5. **Run in isolated environments**
   - Use dedicated testing VMs or containers
   - Avoid running on production systems
   - Isolate testing networks when possible

### For Developers

1. **Input Validation**
   - All user input must be validated
   - Sanitize URLs and file paths
   - Check parameter ranges

2. **Secure Defaults**
   - SSL verification enabled by default
   - Password redaction in logs
   - Conservative rate limiting defaults

3. **Error Handling**
   - Never expose sensitive data in error messages
   - Redact passwords in all output
   - Handle all exceptions appropriately

4. **Dependencies**
   - Keep dependencies up to date
   - Monitor for security advisories
   - Use only well-maintained libraries

## Security Features

### Current Security Features

- ✅ SSL/TLS certificate validation (enabled by default)
- ✅ Password redaction in console output and logs
- ✅ Input validation for all parameters
- ✅ Rate limiting and respect for HTTP 429 responses
- ✅ Request timeouts to prevent hanging
- ✅ Secure connection handling
- ✅ No credential storage or caching

### Known Limitations

- ⚠️ Passwords appear in process command-line arguments (visible in `ps` output)
  - Mitigation: Avoid using shared systems or untrusted environments
- ⚠️ Wordlist files are read in plain text
  - Mitigation: Protect wordlist files with appropriate filesystem permissions
- ⚠️ Success results may include plain-text passwords in output files
  - Mitigation: Secure and encrypt output files appropriately

## Security Considerations for Target Systems

When testing with BrutePy, be aware that:

1. **Brute force attacks generate significant traffic**
   - May trigger security alerts and IDS/IPS systems
   - Can cause account lockouts
   - May be logged extensively

2. **Detection is expected and intended**
   - This is not a stealth tool
   - Use appropriate test accounts
   - Coordinate with system administrators

3. **Legal and ethical obligations**
   - Obtain proper authorization
   - Document authorization clearly
   - Follow responsible disclosure principles

## Vulnerability Disclosure Timeline

1. **Day 0**: Vulnerability reported to maintainers
2. **Day 1-7**: Maintainers acknowledge and assess
3. **Day 7-30**: Develop and test fix
4. **Day 30-45**: Release patched version
5. **Day 45+**: Public disclosure (coordinated with reporter)

## Security Updates

Security updates will be:
- Released as soon as possible
- Documented in CHANGELOG.md
- Announced in GitHub releases
- Tagged with `security` label

## Contact

For security concerns:
- Email: [Create a private security advisory on GitHub]
- GitHub: https://github.com/wjdavis5/BrutePy/security/advisories/new

## Acknowledgments

We appreciate responsible disclosure and will acknowledge security researchers who:
- Report vulnerabilities responsibly
- Work with us on fixes
- Follow responsible disclosure timelines

Thank you for helping keep BrutePy secure!
