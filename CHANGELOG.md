# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Binary executables for other platforms

### Changed
- Default shortcut keys remap

## [1.3.0] - 2021-07-09
### Added
- Binary executable for Windows x86
- Project icon

### Changed
- Visual overhaul of project `README.md`
- Improved installation instructions

### Removed
- Updater script `update.py`
- External version file `version.json`

## [1.2.0] - 2021-06-10
### Added
- Customise which symbols are insertable
- Define symbols and their shortcuts in `shortcuts.json`
- License (MIT)

### Fixed
- Issue with shortcuts only triggering last defined value for lambda function

## [1.1.0] - 2021-06-06
### Added
- New Symbols
  - Greek Lambda (lowercase)

### Changed
- Backend improvements to allow easier addition of shortcuts in future, using lambda functions

### Removed
- Individual character insert functions

### Fixed
- Checking for updates always fails

## [1.0.0] - 2021-06-02
Initial release build
### Added
- Update script (beta)
- New Symbols
  - Greek Delta
  - Greek Delta (lowercase)
  - Greek Lambda (lowercase)
  - Greek Pi (lowercase)
  - Multiply
  - Plus/Minus
  - Not Equal
  - Less-than or Equal to
  - Greater-than or Equal to
  - Degree
  - Reaction Arrow
  - Equilibrium
  - Therefore
