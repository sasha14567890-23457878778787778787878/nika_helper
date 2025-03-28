import os
import psutil
import shutil
import subprocess
import requests
import sys

def auto_update():
    print("🔄 Проверка обновлений...")
    repo_url = "https://raw.githubusercontent.com/sasha14567890-23457878778787778787878/nika_helper/refs/heads/main/app.py"  # Замени на свой URL
    try:
        response = requests.get(repo_url)
        if response.status_code == 200:
            with open(__file__, 'wb') as f:
                f.write(response.content)
            print("✔️ Утилита обновлена! Перезапуск...")
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            print("⚠️ Обновлений нет или ошибка загрузки.")
    except Exception as e:
        print(f"❌ Ошибка обновления: {e}")

def open_folders():
    print("📂 Открытие папок для очистки...")
    folders = ["%temp%", "C:\\Windows\\Temp", os.path.expanduser("~\\AppData\\Local\\Temp")]
    for folder in folders:
        print(f"Открываю: {folder}")
        os.system(f'start {folder}')

def clear_temp():
    print("🗑️ Очистка временных файлов...")
    folders = [os.getenv('TEMP'), os.getenv('TMP'), 'C:\\Windows\\Temp']
    for folder in folders:
        try:
            for root, dirs, files in os.walk(folder):
                for name in files:
                    file_path = os.path.join(root, name)
                    try:
                        os.unlink(file_path)
                    except PermissionError:
                        print(f"⚠️ Пропущен занятой файл: {file_path}")
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    try:
                        shutil.rmtree(dir_path)
                    except PermissionError:
                        print(f"⚠️ Пропущена занятая папка: {dir_path}")
            print(f"✔️ Очищено: {folder}")
        except Exception as e:
            print(f"❌ Ошибка очистки {folder}: {e}")

def clear_ram():
    print("🔥 Очистка RAM...")
    try:
        os.system('echo Clearing RAM...')
        # Проверка перед очисткой корзины
        recycle_bin = subprocess.check_output('powershell.exe Get-ChildItem C:\\$Recycle.Bin', shell=True)
        if recycle_bin:
            os.system('powershell.exe Clear-RecycleBin -Force')  # Очистка корзины, если она не пуста
        print("✔️ RAM очищена!")
    except Exception as e:
        print(f"❌ Ошибка очистки RAM: {e}")

def monitor():
    print("📊 Мониторинг системы...")
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"RAM: {psutil.virtual_memory().percent}%")
    print(f"Диск: {psutil.disk_usage('/').percent}%")

def manage_autorun():
    print("⚙️ Автозапуск программ...")
    try:
        subprocess.run(['powershell', 'explorer.exe', 'shell:startup'], check=True)
    except Exception as e:
        print(f"❌ Ошибка открытия автозапуска: {e}")

def main():
    auto_update()  # Автоматическое обновление при запуске
    
    while True:
        print("\n🔧 Утилита для оптимизации ПК")
        if input("📂 Открыть папки для очистки? (y/n): ").lower() == 'y':
            open_folders()
        if input("🗑️ Очистить мусор? (y/n): ").lower() == 'y':
            clear_temp()
        if input("🔥 Очистить RAM? (y/n): ").lower() == 'y':
            clear_ram()
        if input("📊 Запустить мониторинг? (y/n): ").lower() == 'y':
            monitor()
        if input("⚙️ Открыть автозапуск? (y/n): ").lower() == 'y':
            manage_autorun()
        
        if input("🔌 Выйти? (y/n): ").lower() == 'y':
            print("👋 Завершение работы...")
            break

if __name__ == '__main__':
    main()
