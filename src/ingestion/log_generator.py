import random
import time
import os
from datetime import datetime 
from src.config import LIVE_LOG_PATH, LOG_LEVEL_WEIGHTS, ANOMALY_PROBABILITY, LOG_DELAY

COMPONENTS = [
    'DatabaseService',
    'NetworkService',
    'DiskService',
    'SystemMonitor',
    'AuthService',
    'WebServer'
]

NORMAL_MESSAGES = {
    'DatabaseService': [
        'Query executed successfully in 12ms',
        'Connection pool status: 45% capacity used',
        'Database backup completed successfully',
    ],
    'NetworkService': [
        'Incoming request processed: 200 OK',
        'Average response time: 45ms',
        'Network throughput normal: 120 Mbps',
    ],
    'DiskService': [
        'Disk usage at 54% capacity',
        'Read operation completed in 8ms',
        'Write operation successful',
    ],
    'SystemMonitor': [
        'CPU usage: 34%',
        'Memory usage: 61%',
        'System health check passed',
    ],
    'AuthService': [
        'User login successful',
        'Session token refreshed',
        'User logout completed',
    ],
    'WebServer': [
        'GET /api/data 200 OK 23ms',
        'POST /api/submit 201 Created 45ms',
        'Cache hit ratio: 87%',
    ]
}



ANOMALY_MESSAGES = {
    'DatabaseService': [
        'Connection timeout after 30000ms - max retries exceeded',
        'Database connection pool exhausted: 100% capacity',
        'Query failed: deadlock detected',
    ],
    'NetworkService': [
        'Packet loss detected: 34% packets dropped',
        'Connection refused: remote host unreachable',
        'Network throughput critical: 2 Mbps',
    ],
    'DiskService': [
        'Disk usage CRITICAL: 98% - write operations failing',
        'Read operation failed: I/O error',
        'Write operation failed: no space left on device',
    ],
    'SystemMonitor': [
        'CPU usage CRITICAL: 99% - system unresponsive',
        'Memory usage CRITICAL: 97% - OOM killer activated',
        'Hardware failure detected: disk controller not responding',
    ],
    'AuthService': [
        'Multiple failed login attempts: 47 failures in 60 seconds',
        'Brute force attack detected from IP: 192.168.1.105',
        'Authentication service unavailable try later',
    ],
    'WebServer': [
        'GET /api/data 500 Internal Server Error',
        'Request timeout: no response after 30000ms',
        'Too many requests: rate limit exceeded',
    ]
}


def generate_log_line(force_anomaly=False):

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    component = random.choice(COMPONENTS)

    if force_anomaly:
        level = random.choice(['ERROR', 'CRITICAL'])
        message = random.choice(ANOMALY_MESSAGES[component])
    else:
        level = random.choices(
            list(LOG_LEVEL_WEIGHTS.keys()),
            weights=list(LOG_LEVEL_WEIGHTS.values()),
            k=1
        )[0]
        message = random.choice(NORMAL_MESSAGES[component])

    log_line = f"{timestamp} - {level} - {component} - {message}"

    return log_line


def stream_logs(total_lines=1000):

    os.makedirs(os.path.dirname(LIVE_LOG_PATH), exist_ok=True)

    print(f"Starting log stream...")
    print(f"Writing to: {LIVE_LOG_PATH}")
    print(f"Total lines: {total_lines}")
    print("-" * 50)

    anomaly_count = 0

    with open(LIVE_LOG_PATH, 'w') as f:

        for i in range(total_lines):

            is_anomaly = random.random() < ANOMALY_PROBABILITY

            log_line = generate_log_line(force_anomaly=is_anomaly)

            f.write(log_line + '\n')
            f.flush()

            if is_anomaly:
                anomaly_count += 1
                print(f"[ANOMALY] {log_line}")
            else:
                print(f"[NORMAL]  {log_line}")

            time.sleep(LOG_DELAY)

    print("-" * 50)
    print(f"Done. Anomalies injected: {anomaly_count} out of {total_lines}")

if __name__ == "__main__":
    stream_logs(total_lines=1000)










