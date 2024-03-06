# Postmortem: Ecommerce Website Outage

<img src="ss.png" />

## Issue Summary:

- Duration: 2 hours and 30 minutes, from 12:00 PM to 2:30 PM UTC
- Impact: The website was completely down, and users were unable to access any products or services. This affected 100% of users.
- Root Cause: A bug in the new payment processing system caused the website to crash.

## Timeline:

- 12:00 PM UTC: The website goes down.
- 12:05 PM UTC: The issue is detected by monitoring alerts.
- 12:10 PM UTC: Engineers begin investigating the issue.
- 12:30 PM UTC: Engineers identify the bug in the payment processing system as the root cause.
- 1:00 PM UTC: Engineers begin working on a fix.
- 2:00 PM UTC: The fix is deployed and the website is restored to full functionality.
- 2:30 PM UTC: All services are back online.

### Root Cause and Resolution:

The root cause of the outage was a bug in the new payment processing system. The bug caused the website to crash when a user attempted to make a purchase. The issue was resolved by reverting to the old payment processing system.

### Corrective and Preventative Measures:

#### Corrective Measures:

- Revert to the old payment processing system.
- Implement a more rigorous testing process for new code.

#### Preventative Measures:

- Develop a more robust payment processing system.
- Improve monitoring and alerting for the website.
- Implement a disaster recovery plan.
