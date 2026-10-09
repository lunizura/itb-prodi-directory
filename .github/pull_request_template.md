## Summary of Changes

Please provide a concise description of what this pull request introduces or fixes.

- **Related Issue:** Fixes # (or Closes #)
- **Component Affected:** (e.g. Data JSON / Table Grid / Modal View / Documentation)

---

## Type of Change

- [ ] Data Correction (Updating quotas, accreditation status, or program details)
- [ ] Feature Enhancement (UI components, filters, exports, accessibility)
- [ ] Bug Fix (Resolving broken links, rendering issues, or filter behavior)
- [ ] Documentation Update (README, CONTRIBUTING, or code comments)
- [ ] CI/CD & Testing (GitHub Actions, test cases, build scripts)

---

## Verification & Quality Checklist

Before submitting this pull request, please verify that you have satisfied each requirement:

- [ ] **Mathematical Quota Parity:** `daya_tampung == dt_snbp + dt_snbt + dt_smitb` verified for all modified entries.
- [ ] **Bilingual Parity:** Both Indonesian and English fields are fully populated (`deskripsi`, `fokus`, `karir`).
- [ ] **Automated Test Suite:** `python -m unittest tests/test_itb_directory.py -v` passes with 10/10 tests green.
- [ ] **Strict Zero-Emoji Policy:** Checked and verified that no emoji characters are included in code, comments, or documentation.
- [ ] **Official Documentation:** Sourced from `admission.itb.ac.id`, BAN-PT, or accredited agencies.
- [ ] **Conventional Commits:** Commit messages adhere to the conventional format (e.g. `feat:`, `fix:`, `docs:`).
