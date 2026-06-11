# Topic: Lambda with Data Streams

# Simulation: HTTP Status Codes from a server log
status_codes = [200, 404, 500, 201, 403, 502, 200]

# Lambda for Security Filter: Capture only error codes (>= 400)
# This is a common pattern in AI Security monitoring
is_error = lambda code: code >= 400

# Use filter() to apply the lambda across the data stream
security_alerts = list(filter(is_error, status_codes))

# Multi-argument Lambda: Financial calculation for "Supra Tier" costs
# formula: base + tax + shipping
total_cost = lambda base, tax, ship: base + (base * tax) + ship

print(f"Security Alerts Detected: {security_alerts}")
print(f"Final Part Cost (₹): {total_cost(50000, 0.18, 2000)}")