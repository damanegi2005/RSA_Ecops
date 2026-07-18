# RSA Security Analysis

This repository contains an educational project exploring the mathematical foundations, security assumptions, and limitations of the RSA cryptosystem.

## Overview

The goal of this project is to understand why RSA is secure, under which conditions it becomes vulnerable, and how common attacks can recover the private key when its assumptions are violated.

## Topics Covered

- RSA key generation
- Raw RSA implementation
- Encryption and decryption
- Deterministic encryption
- Codebook attack
- Integer factorization
- Pollard's Rho algorithm
- Weak key generation
- RSA key size and security

## Project Structure

- `rsa.py` – Raw RSA implementation
- `attack.py` – Basic attacks on RSA
- `pollards_rho.py` – Pollard's Rho factorization
- `experiment.py` – Performance comparison and experiments

## Technologies

- Python
- Math
- SymPy

## Notes

This project was developed for educational purposes to study RSA and its security assumptions.

The implementation uses small prime numbers for demonstration and should **not** be used in real-world cryptographic applications.
