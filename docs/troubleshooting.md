## Challenges and Troubleshooting

Several technical challenges occurred during the implementation.

### 1. Oracle Cloud SSH Connectivity

During the setup, SSH connections occasionally timed out following changes to network access rules.

Troubleshooting involved examining Oracle Cloud security lists, firewall rules, SSH daemon configuration, and source IP allowlists.

The issue demonstrated the importance of maintaining reliable administrative access when modifying remote firewall configurations.

### 2. Docker Networking and Firewall Isolation

Implementing outbound traffic restrictions required understanding how Docker manages networking and iptables.

Standard host firewall rules alone were insufficient for confidently controlling all container traffic.

The DOCKER-USER chain was used to apply additional filtering to forwarded container traffic.

Connectivity tests and firewall counters were used to validate that the tested outbound connections were blocked.

### 3. Grafana and Loki Query Issues

Several dashboard queries initially returned errors, incorrect values, or no data.

The problems included LogQL syntax errors, query series limits, and Grafana field-selection issues.

These were addressed by adjusting queries, reviewing Loki configuration, and configuring appropriate Grafana transformations.

### 4. GeoIP Enrichment

Geographic visualization required integrating the MaxMind GeoLite2 Country database into the Alloy logging pipeline.

Initial dashboard queries did not consistently display country information.

After troubleshooting the enrichment configuration and Grafana field mappings, country labels and geographic visualizations became available.

### 5. Dashboard Visualization

Creating readable visualizations required several adjustments to Grafana panels.

These included configuring statistical aggregations, selecting appropriate fields, adjusting the dashboard time range, and improving geographic marker visibility.

The result was a dashboard showing SSH connections, authentication attempts, executed commands, top source IPs, and geographic activity.

---

## Lessons Learned

This project provided practical experience in:

- Deploying and hardening a Linux-based cloud server.
- Managing containerized security services with Docker Compose.
- Understanding the interaction between Docker networking and host firewall rules.
- Building a centralized logging pipeline using Alloy and Loki.
- Writing LogQL queries and creating security monitoring dashboards.
- Enriching security logs with geographic information.
- Troubleshooting infrastructure and monitoring issues.
- Analyzing real-world automated SSH activity.

One of the most important lessons was that deploying a security tool is only part of the challenge. Proper isolation, validation, monitoring, and documentation are equally important.
