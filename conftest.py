import os
from webdriver_manager.firefox import GeckoDriverManager

driver_path = GeckoDriverManager().install()
os.environ["PATH"] = os.path.dirname(driver_path) + os.pathsep + os.environ.get("PATH", "")
