import subprocess
from datetime import datetime

class ResourceMonitor:
    def report(self):
        try:
            cpu = subprocess.check_output(["sysctl", "-n", "vm.loadavg"], text=True).strip()
            mem = subprocess.check_output(["ps", "-caxm", "-o", "%cpu,%mem"], text=True).splitlines()[:5]
            disk = subprocess.check_output(["df", "-h", "/"], text=True).splitlines()[-1]
            return {"time": datetime.now().isoformat(), "system_load": cpu, "top_processes_snapshot": "\n".join(mem), "disk_space_root": disk.strip()}
        except Exception as e:
            return {"error": str(e)}
