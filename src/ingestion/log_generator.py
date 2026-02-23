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
        'Disk usage at 52% capacity',
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
        'Authentication service unavailable',
    ],
    'WebServer': [
        'GET /api/data 500 Internal Server Error',
        'Request timeout: no response after 30000ms',
        'Too many requests: rate limit exceeded',
    ]
}




