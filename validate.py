#!/usr/bin/env python3
"""
Simple validation tests for BrutePy
Tests basic functionality without requiring a live HTTP server
"""

import subprocess
import sys
import os
import tempfile

def run_command(cmd, expected_exit_code=0):
    """Run a command and check exit code"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f"Command: {cmd}")
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"Stdout: {result.stdout.strip()}")
    if result.stderr:
        print(f"Stderr: {result.stderr.strip()}")
    
    if result.returncode != expected_exit_code:
        print(f"❌ Expected exit code {expected_exit_code}, got {result.returncode}")
        return False
    else:
        print("✅ Command executed as expected")
    print("-" * 50)
    return True

def main():
    print("BrutePy Validation Tests")
    print("=" * 50)
    
    # Test 1: Help message
    print("Test 1: Help message")
    if not run_command("python Brute.py -h"):
        return False
    
    # Test 2: Invalid URL validation
    print("Test 2: Invalid URL validation")  
    if not run_command("python Brute.py invalid-url wordlist.txt user", expected_exit_code=1):
        return False
    
    # Test 3: Missing file validation
    print("Test 3: Missing file validation")
    if not run_command("python Brute.py http://example.com /nonexistent/file.txt user", expected_exit_code=1):
        return False
    
    # Test 4: Invalid thread count
    print("Test 4: Invalid thread count validation")
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("test\npassword\nadmin\n")
        wordlist = f.name
    
    try:
        if not run_command(f"python Brute.py http://example.com {wordlist} user --threads 100", expected_exit_code=1):
            return False
        
        # Test 5: Connection refused (expected behavior)
        print("Test 5: Connection refused handling")
        # This should fail with connection error but exit code 1 (not crash)
        cmd = f"python Brute.py http://localhost:9999 {wordlist} user --delay 100"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        print(f"Command: {cmd}")
        print(f"Exit code: {result.returncode}")
        if result.stdout:
            print(f"Stdout: {result.stdout.strip()}")
        if result.stderr:
            print(f"Stderr: {result.stderr.strip()}")
        
        # Accept exit code 1 (connection failed) as success
        if result.returncode == 1:
            print("✅ Command handled connection failure correctly")
        else:
            print(f"❌ Expected exit code 1, got {result.returncode}")
            return False
        print("-" * 50)
            
    finally:
        os.unlink(wordlist)
    
    print("\n🎉 All validation tests passed!")
    print("\nBrutePy is working correctly and ready for use.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)