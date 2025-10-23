# Contributing to BrutePy

Thank you for your interest in contributing to BrutePy! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Remember this tool is for authorized security testing only

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Any error messages** or logs
- **Sanitized examples** (never include real credentials or sensitive data)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Clear description** of the enhancement
- **Use case** explaining why it would be useful
- **Possible implementation** approach (optional)
- **Impact on existing functionality**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/BrutePy.git
cd BrutePy

# Install dependencies
pip install -r requirements.txt

# Run tests
python validate.py
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and modular
- Maximum line length: 100 characters (flexible for readability)

### Comments

- Use comments to explain *why*, not *what*
- Keep comments up-to-date with code changes
- Document complex algorithms or workarounds
- Include security considerations where relevant

### Error Handling

- Handle all expected exceptions explicitly
- Provide clear, actionable error messages
- Clean up resources properly (files, threads, etc.)
- Never expose sensitive information in error messages

### Security Considerations

- **Never commit credentials** or sensitive data
- **Sanitize user input** to prevent injection attacks
- **Redact passwords** in logs and output
- **Validate all input** before use
- **Follow secure defaults** (e.g., SSL verification on)
- **Document security implications** of changes

### Testing

- Run existing validation tests before submitting PR
- Add tests for new features if applicable
- Test edge cases and error conditions
- Verify changes don't break existing functionality

## What to Contribute

### High Priority

- Bug fixes, especially security-related
- Performance improvements
- Documentation improvements
- Test coverage expansion
- Cross-platform compatibility

### Medium Priority

- New authentication method support
- Enhanced reporting features
- User experience improvements
- Code refactoring for maintainability

### Lower Priority

- Minor feature additions
- Style improvements
- Comment additions

## Git Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be 50 characters or less
- Reference issues and pull requests where appropriate
- Provide context in the commit body if needed

Example:
```
Fix connection timeout handling in worker threads

- Workers now drain queue properly on early exit
- Prevents deadlock when connection fails
- Fixes #123
```

## Code Review Process

1. All submissions require review
2. Maintainers will review your code for:
   - Functionality and correctness
   - Code quality and style
   - Security implications
   - Documentation completeness
   - Test coverage
3. Address review feedback promptly
4. Once approved, maintainers will merge your PR

## Release Process

- Version numbers follow [Semantic Versioning](https://semver.org/)
- CHANGELOG.md is updated for each release
- Security fixes may trigger immediate releases
- Features are typically batched in minor releases

## Legal

- By contributing, you agree your code will be licensed under GPL-2.0
- You confirm you have the right to submit the code
- You agree to the project's license terms

## Questions?

Feel free to:
- Open an issue for discussion
- Ask questions in pull requests
- Contact maintainers for guidance

## Recognition

Contributors will be recognized in:
- Git commit history
- GitHub contributors page
- CHANGELOG.md (for significant contributions)

Thank you for helping make BrutePy better!
