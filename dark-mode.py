import winreg
import sys

REG_APPS_USE_LIGHT_THEME = "AppsUseLightTheme"
REG_SYSTEM_USE_LIGHT_THEME = "SystemUsesLightTheme"
REG_KEY_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if (
            "on" in arg or arg == "0"
        ):  # turn on dark mode by setting 'use light theme' to false.
            set_reg(REG_APPS_USE_LIGHT_THEME, 0)
        elif "off" in arg or arg == "1":
            set_reg(REG_APPS_USE_LIGHT_THEME, 1)


def set_reg(key, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_KEY_PATH)
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, REG_KEY_PATH, 0, winreg.KEY_WRITE
        )
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(registry_key)
    except WindowsError:
        pass


if __name__ == "__main__":
    main()
