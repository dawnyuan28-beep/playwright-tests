import sys
import subprocess

def run_install():
    # sys.executable 会自动抓取你右下角选中的那个 Python 3.12.9 的准确位置
    python_exe = sys.executable
    print(f"检测到正确的 Python 位置：{python_exe}")
    
    # 1. 安装 playwright 库
    print("正在安装 Playwright 库...")
    subprocess.check_call([python_exe, "-m", "pip", "install", "playwright", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    
    # 2. 安装浏览器驱动
    print("正在安装内置浏览器（请耐心等待）...")
    # 找到 Scripts 目录下的 playwright.exe
    playwright_exe = python_exe.replace("python.exe", r"Scripts\playwright.exe")
    subprocess.check_call([playwright_exe, "install"])
    
    print("\n🎉 恭喜！Playwright 已经彻底装好了！")

if __name__ == "__main__":
    run_install()