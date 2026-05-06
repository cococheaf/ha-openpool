# Security Policy

## Supported Versions

Security updates are provided for the latest public version of **ha-openpool**.

Because this project is currently in active development, only the most recent version or the current `main` branch is generally supported for security fixes.

| Version / Branch | Supported |
| ---------------- | --------- |
| `main`           | :white_check_mark: |
| Latest release   | :white_check_mark: |
| Older releases   | :x: |

If you are using an older version and discover a security issue, please update to the latest version first and check whether the issue still exists.

## Reporting a Vulnerability

If you discover a security vulnerability in **ha-openpool**, please report it responsibly.

Please do **not** open a public GitHub issue for security vulnerabilities.

Instead, report the vulnerability privately using GitHub Security Advisories if available, or contact the project maintainer directly.

When reporting a vulnerability, please include as much useful information as possible:

- a clear description of the vulnerability
- affected version, branch, or commit
- steps to reproduce the issue
- possible impact
- whether the issue can be exploited remotely or locally
- relevant logs, screenshots, or proof-of-concept details
- suggested mitigation, if known

Please avoid publicly sharing exploit details until the issue has been reviewed and, if necessary, fixed.

## What to Expect

After a vulnerability report is received, the maintainer will review the report and may ask for additional details.

If the vulnerability is accepted, the project will aim to:

- confirm the issue
- assess the severity and impact
- prepare a fix or mitigation
- publish an update when appropriate
- credit the reporter if desired

If the report is declined, the maintainer will try to explain why the issue is not considered a security vulnerability.

Response times may vary because this is a community project, but security reports will be treated with priority.

## Scope

Security reports are especially relevant for issues involving:

- unauthorized access
- unsafe Home Assistant add-on behavior
- exposure of secrets, tokens, or credentials
- command injection
- path traversal
- cross-site scripting in the web interface
- insecure network behavior
- unsafe handling of user configuration
- unexpected control of pool equipment

## Out of Scope

The following issues are usually not considered security vulnerabilities unless they create a real security impact:

- missing features
- general bugs without security impact
- configuration mistakes outside the project
- issues caused by unsupported or modified installations
- vulnerabilities in unrelated third-party systems
- physical access attacks against pool hardware
- reports without enough information to reproduce or understand the issue

## Safety Notice

ha-openpool may interact with real pool equipment such as pumps, saltwater chlorinators, heaters, and other electrical devices.

Security and safety are closely related in this project.

A security issue may also be a safety issue if it could cause equipment to run unexpectedly, ignore manual controls, or behave in a way that could damage hardware or create unsafe operating conditions.

Please report such issues responsibly and with enough detail to allow proper investigation.

## Disclosure

Please allow a reasonable amount of time for the issue to be reviewed and fixed before public disclosure.

Coordinated disclosure helps protect users while allowing the project to address the problem properly.

Thank you for helping keep **ha-openpool** safe and reliable.
