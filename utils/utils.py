# CONSTANTS
import inspect

URL = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"


def whoami():
    return inspect.stack()[1][3]