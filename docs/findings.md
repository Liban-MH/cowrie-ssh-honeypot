## Attack Findings and Analysis

### Observation Period

The honeypot was monitored from October 28 to November 1, 2026, covering approximately 4 days and 14 hours.

The initial testing period on October 27 was excluded from the analysis to reduce the influence of setup-related activity.

### Summary of Collected Data

| Metric | Recorded Value |
|:-------|---------------:|
| Total Logged Events | 163,513 |
| SSH Connections | 19,652 |
| Unique Source IPs | 573 |
| Successful Honeypot Logins | 18,901 |
| Failed Login Attempts | 47 |
| Commands Executed | 27,204 |

Successful honeypot logins refer to authentication within Cowrie's simulated SSH environment, not successful access to the underlying VPS.

### Key Observations

**1. Automated SSH Activity**

The honeypot received thousands of SSH connections from hundreds of unique source IP addresses.

The volume and repetition of recorded activity are consistent with automated scanning and SSH attack attempts.

**2. Authentication Attempts**

Cowrie recorded attempts to authenticate using different username and password combinations.

These attempts illustrate how internet-facing SSH services are routinely targeted by automated authentication activity.

**3. System Reconnaissance**

The recorded command activity included commands used to identify operating system and system configuration details.

For example:

`uname -s -v -n -r -m`

Such commands can help attackers identify the environment they have accessed.

**4. Potential Persistence Attempts**

Some recorded commands referenced SSH configuration and authorized_keys files.

This behavior may indicate attempts to establish or maintain SSH access after authentication.

However, these commands were executed within Cowrie's simulated environment and do not demonstrate compromise of the actual VPS.

### Limitations

The findings should be interpreted with several limitations in mind:

- Source IP addresses do not necessarily identify individual attackers.
- Geographic IP information does not establish an attacker's physical location.
- Some recorded activity may originate from legitimate scanning or research systems.
- Although the initial testing day was excluded, later manual tests may still be represented in the dataset.
- Cowrie records interactions with an emulated environment rather than a fully compromised operating system.

The results therefore describe observed SSH activity and attacker-like behavior, rather than confirmed identities or successful compromises.
