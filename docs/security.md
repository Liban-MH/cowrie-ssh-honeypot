## Security Measures

Since the honeypot was intentionally exposed to the internet, securing the underlying infrastructure was an important part of the project.

The following security measures were implemented:

### 1. SSH Hardening

Administrative SSH access was separated from the public honeypot service.

Password-based authentication was disabled, and administrative access was configured to use SSH keys.

Access was further restricted using source IP allowlisting, reducing exposure to unauthorized remote connections.

### 2. Docker Network Isolation

Cowrie and the monitoring services were deployed using separate Docker networks.

This separation was intended to limit direct communication between the attacker-facing honeypot and the internal monitoring infrastructure.

Only the honeypot service was intentionally exposed to incoming internet traffic.

### 3. Firewall Configuration

UFW, iptables, and Oracle Cloud network security rules were used to control network access.

Additional filtering rules were implemented through the DOCKER-USER chain to restrict outbound traffic originating from the honeypot network.

Basic connectivity tests confirmed that the tested outbound connection was blocked.

However, these tests did not establish that every possible outbound communication path was restricted.

### 4. Restricted Monitoring Access

Grafana and Loki were configured to bind to the loopback interface rather than being directly exposed to the internet.

Grafana was accessed through an encrypted SSH tunnel from the administrator's laptop.

This reduced the public attack surface of the monitoring infrastructure.

### 5. Persistent Logging

Docker volumes were used to preserve Cowrie logs and monitoring data independently of container lifecycles.

The collected JSON logs were exported and backed up for offline analysis.

---
