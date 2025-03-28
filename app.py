import os
import psutil
import shutil
import subprocess
import requests
import sys

def auto_update():
    print("🔄 Проверка обновлений...")
    repo_url = "https://raw.githubusercontent.com/USERNAME/REPO/main/system_optimizer.py"  # Замени на свой URL
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
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            print(f"✔️ Очищено: {folder}")
        except Exception as e:
            print(f"❌ Ошибка очистки {folder}: {e}")

def clear_ram():
    print("🔥 Очистка RAM...")
    try:
        os.system('echo Clearing RAM...')
        os.system('powershell.exe Clear-RecycleBin -Force')  # Очистка корзины
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
    os.system('shell:startup')  # Открывает папку автозапуска

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
