# Contributing to ha-openpool

Thank you for your interest in contributing to **ha-openpool**.

ha-openpool is a Home Assistant add-on project for monitoring and controlling pool-related equipment such as filtration pumps, saltwater chlorinators, heat pumps, and PV-aware pool operation logic.

Contributions are welcome, whether they are bug reports, feature ideas, documentation improvements, code changes, UI improvements, or testing feedback.

## Project Goals

The goal of ha-openpool is to provide a practical and reliable pool automation solution for Home Assistant.

The project aims to:

- integrate pool equipment into Home Assistant
- support safe and transparent automation logic
- provide a simple and useful web interface
- allow manual override where needed
- make pool operation more efficient by considering weather, temperature, PV production, and operating modes
- keep the system understandable and maintainable for users

## How to Contribute

You can contribute in several ways:

- report bugs
- suggest improvements
- improve documentation
- test the add-on with your own pool setup
- improve the user interface
- add support for additional hardware
- improve Home Assistant integration
- review pull requests
- share configuration examples

## Reporting Bugs

When reporting a bug, please include as much useful information as possible.

A good bug report should include:

- a clear description of the problem
- steps to reproduce the issue
- what you expected to happen
- what actually happened
- relevant logs or error messages
- your Home Assistant version
- your add-on version or Git commit
- information about your pool hardware, if relevant
- screenshots, if they help explain the issue

Please avoid reports like “it does not work” without additional context. The more details you provide, the easier it is to reproduce and fix the issue.

## Suggesting Features

Feature requests are welcome.

Before opening a feature request, please consider whether the idea fits the project goals.

Good feature requests should explain:

- what problem the feature solves
- why the feature would be useful
- how you imagine it should work
- whether it should be optional or configurable
- if there are any safety-related concerns

For automation-related features, please also describe the desired behavior clearly, especially when pumps, chlorinators, heating, or electrical devices are involved.

## Pull Requests

Pull requests are welcome.

Before opening a pull request, please make sure that:

- your change has a clear purpose
- the code is understandable and maintainable
- existing functionality is not broken
- documentation is updated where needed
- configuration changes are explained
- UI changes are tested in a realistic browser environment
- Home Assistant add-on behavior is tested where possible

Small, focused pull requests are preferred over large, mixed changes.

## Development Guidelines

Please try to follow these general guidelines:

- keep the code simple and readable
- avoid unnecessary complexity
- prefer explicit logic over hidden behavior
- use meaningful variable and function names
- document non-obvious decisions
- keep user-facing text clear and understandable
- avoid breaking existing configurations without a good reason
- keep safety in mind when controlling pool hardware

## Safety Considerations

ha-openpool may control real pool equipment such as pumps, saltwater chlorinators, heaters, and other electrical devices.

Please be careful when contributing automation logic.

Changes should avoid:

- running equipment in unsafe conditions
- disabling important manual controls
- creating automation loops
- ignoring equipment cooldown or delay requirements
- assuming that all users have identical hardware
- hardcoding values that should be configurable
- causing pumps or heaters to run unexpectedly

Where possible, automation behavior should be transparent and predictable.

## Home Assistant Add-on Notes

When working on the Home Assistant add-on, please check relevant files such as:

- `openpool/config.yaml`
- `openpool/Dockerfile`
- `openpool/run.sh`
- `openpool/www/index.html`

Depending on the change, you may need to test:

- add-on startup
- add-on logs
- web UI availability
- Home Assistant Ingress behavior
- configuration handling
- sensor or entity interaction
- restart behavior

## Documentation

Documentation improvements are very welcome.

Helpful documentation includes:

- installation instructions
- example configurations
- troubleshooting steps
- explanations of operating modes
- screenshots
- hardware compatibility notes
- Home Assistant automation examples

Please keep documentation practical and easy to follow.

## Commit Messages

Please use clear commit messages.

Examples:

```text
fix: correct pump state handling
feat: add weather-based operating mode
docs: improve installation instructions
ui: simplify status card layout
refactor: clean up timer logic
```

## Branches

For larger changes, please create a feature branch.

Example:

```bash
git checkout -b feature/weather-based-mode
```

Then open a pull request against the main development branch of the repository.

## Testing

Please test your changes before opening a pull request.

Depending on the type of change, testing may include:

- running the add-on locally
- checking Home Assistant add-on logs
- testing the web interface
- validating configuration changes
- checking behavior after restart
- testing manual override buttons
- verifying automation behavior with realistic values

When opening a pull request, please describe how you tested the change.

## Code Style

There is currently no strict formal code style requirement.

Please keep contributions consistent with the existing project style.

In general:

- use consistent formatting
- keep files readable
- avoid unrelated formatting changes
- avoid large rewrites unless necessary
- keep comments helpful and limited to useful explanations

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

This project is licensed under the **GNU General Public License v3.0**.

## Community Conduct

Please be respectful and constructive.

This project is built to help Home Assistant users operate their pool systems more efficiently and reliably. Discussions should stay friendly, practical, and focused on improving the project.

## Questions

If you are unsure whether a change fits the project, open an issue first and describe your idea.

Thank you for helping improve **ha-openpool**.
