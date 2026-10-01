import platform
import sys
from datetime import datetime

print("Cybersecurity Learning Toolkit")
print("=" * 32)
print(f"Time: {datetime.now().isoformat(timespec='seconds')}")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Architecture: {platform.machine()}")
print(f"Python: {sys.version.split()[0]}")
print(f"Hostname: {platform.node()}")
