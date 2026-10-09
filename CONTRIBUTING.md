# Contributing to ITB Study Programs Directory

Thank you for your interest in contributing to the Institut Teknologi Bandung (ITB) Study Programs, Schools, and Faculties Directory. This project provides transparent, accurate, and accessible educational and admission data for prospective students, researchers, and academic counselors.

To maintain dataset integrity, reliability, and code quality, please adhere to the following contribution guidelines.

---

## Code of Conduct

We are committed to providing a welcoming, productive, and harassment-free environment. All contributors and participants are expected to maintain professional, constructive, and respectful communication in all issues, discussions, and pull requests.

---

## Ways to Contribute

1. **Reporting Data Corrections:** Report outdated daya tampung, changes in national (BAN-PT/LAM Teknik/LAM Infokom) or international accreditations (ASIIN, ABET, KAAB, IABEE), or missing program details.
2. **Proposing Feature Enhancements:** Suggest UI improvements, new filter categories, analytical visualizations, or campus location filters.
3. **Submitting Code Changes:** Fix bugs, optimize client-side rendering performance, or enhance mobile accessibility.

---

## Local Development Workflow

### 1. Prerequisites
- Python 3.9 or higher (standard library only; no third-party packages required).
- A modern web browser (Chrome, Firefox, Safari, or Edge).
- Git installed and configured.

### 2. Setup
Clone the repository and inspect the directory structure:
```bash
git clone https://github.com/lunizura/itb-prodi-directory.git
cd itb-prodi-directory
```

### 3. File Organization
- `data/itb_prodi.json`: Raw structured dataset of all 52 study programs.
- `data/itb_prodi.js`: Client-ready JavaScript data bundle for the static interface.
- `data/itb_prodi.csv`: Tabular CSV export.
- `data/metadata.json`: Dataset metadata, totals, and verification metrics.
- `index.html`: Responsive bilingual web directory application.
- `scripts/build_itb_dataset.py`: Generator script for dataset compilation and quota balancing.
- `tests/test_itb_directory.py`: Automated end-to-end regression validation suite.

---

## Data Verification & Mathematical Parity

If you submit changes to the dataset, your edits must satisfy the following strict rules:

1. **Mathematical Quota Equality:**
   For every study program, the total seat allocation must strictly equal the sum of its admission tracks:
   ```
   daya_tampung == dt_snbp + dt_snbt + dt_smitb
   ```
2. **Bilingual Parity:**
   Every study program entry must provide complete content in both Bahasa Indonesia and English (`deskripsi`, `fokus`, and `karir`).
3. **Official Sourcing:**
   All quota and accreditation changes must be accompanied by an official verification reference (e.g. `admission.itb.ac.id`, BAN-PT, LAM, ASIIN, or ABET).

---

## Running the Automated Test Suite

Before committing or pushing any changes, execute the test suite locally:
```bash
python -m unittest tests/test_itb_directory.py -v
```
All 10 tests must pass with 100% success rate (`OK`).

---

## Strict Zero-Emoji Policy

This repository strictly enforces a zero-emoji policy across all files, code, comments, commit messages, issue templates, and documentation. Automated test suites will fail if any emoji codepoint is detected.

---

## Commit Message Guidelines

We follow Conventional Commits formatting:
- `feat:` for new features or substantial additions
- `fix:` for bug fixes or data corrections
- `docs:` for documentation updates
- `test:` for test additions or modifications
- `chore:` for repository maintenance or workflow updates

Example:
```
feat: add sub-quota breakdown for international undergraduate program
```

---

## Pull Request Process

1. Create a descriptive branch from `main`:
   ```bash
   git checkout -b fix/correct-stei-accreditation
   ```
2. Make your atomic changes and verify tests locally.
3. Push your branch to GitHub and open a Pull Request using the repository template.
4. Ensure your PR description references the relevant issue (e.g. `Closes #3`).
