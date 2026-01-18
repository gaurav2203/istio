import requests
import time
from collections import Counter

HEALTH_URL = "http://payment:8080/health"
PAYMENT_URL = "http://payment:8080/payment/process"
TOKEN = "fake-jwt-token"
AMOUNT = 100

TOTAL_REQUESTS = 50
DELAY = 0.05  # small delay to avoid connection reuse

pod_hits_health = Counter()
pod_hits_payment = Counter()
errors_health = 0
errors_payment = 0

def check_payment_health():
    print("Checking payment /health ...")
    for i in range(TOTAL_REQUESTS):
        try:
            r = requests.get(HEALTH_URL, timeout=2)
            if r.status_code == 200:
                data = r.json()
                pod_ip = data.get("pod_ip", "unknown")
                pod_hits_health[pod_ip] += 1

                print(
                    f"[{i+1}] "
                    f"pod_ip={pod_ip} "
                    f"version={data.get('version')}"
                )
            else:
                errors_health += 1
                print(f"[{i+1}] ERROR status={r.status_code}")

        except Exception as e:
            errors_health += 1
            print(f"[{i+1}] EXCEPTION {e}")

        time.sleep(DELAY)

def check_payment_process():
    print("Checking payment /process ...")
    for i in range(TOTAL_REQUESTS):
        try:
            r = requests.post(
                PAYMENT_URL,
                params={"token": TOKEN, "amount": AMOUNT},
                timeout=3
            )

            if r.status_code == 200:
                data = r.json()
                pod_ip = data.get("pod_ip", "unknown")
                pod_hits_payment[pod_ip] += 1

                print(
                    f"[{i+1}] "
                    f"pod_ip={pod_ip} "
                    f"version={data.get('version')}"
                )
            else:
                errors_payment += 1
                print(f"[{i+1}] ERROR status={r.status_code}")

        except Exception as e:
            errors_payment += 1
            print(f"[{i+1}] EXCEPTION {e}")

        time.sleep(DELAY)


print("=== Starting Load Balancing Test ===\n")

check_payment_health()
check_payment_process()



print("\n=== LOAD BALANCING RESULT HEALTH===")
for ip, count in pod_hits_health.items():
    print(f"{ip}: {count} requests")

print(f"\nErrors: {errors_health}")
print("=== Test Finished ===")


print("\n=== LOAD BALANCING RESULT PROCESS===")
for ip, count in pod_hits_payment.items():
    print(f"{ip}: {count} requests")

print(f"\nErrors: {errors_payment}")
print("=== Test Finished ===")
