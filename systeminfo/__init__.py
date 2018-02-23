from systeminfo import main
import platform

__all__ = ['get_platform_info', 'platform'] 

def get_platform_info():
    return platform.platform()
