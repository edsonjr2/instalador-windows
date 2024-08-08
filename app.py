import os
import requests
import subprocess
from tqdm import tqdm
from colorama import init, Fore, Back
import platform
import ctypes

init(autoreset=True)

def main():
    while True:
        print_menu()
        choice = input("Digite o número da opção desejada: ").strip()

        if choice == "1":
            install_anydesk()
        elif choice == "2":
            install_google_chrome()
        elif choice == "3":
            install_mozilla_firefox()
        elif choice == "4":
            install_zoom()
        elif choice == "5":
            install_vlc_media_player()
        elif choice == "6":
            install_microsoft_office()
        elif choice == "7":
            install_visual_studio_code()
        elif choice == "8":
            install_discord()
        elif choice == "9":
            install_winrar()
        elif choice == "10":
            install_notepad_plus_plus()
        elif choice == "11":
            install_dropbox()
        elif choice == "12":
            install_adobe_cc()
        elif choice == "13":
            print(Back.BLACK + Fore.GREEN + "Saindo do programa.")
            break
        else:
            print(Back.BLACK + Fore.RED + "Opção inválida. Por favor, digite novamente.")

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
    print(Back.BLACK + Fore.GREEN + "========== Menu Principal ==========")
    print(Back.BLACK + Fore.GREEN + "Escolha uma opção:")
    print(Back.BLACK + Fore.YELLOW + "1. Instalar AnyDesk para Windows")
    print(Back.BLACK + Fore.YELLOW + "2. Instalar Google Chrome")
    print(Back.BLACK + Fore.YELLOW + "3. Instalar Mozilla Firefox")
    print(Back.BLACK + Fore.YELLOW + "4. Instalar Zoom")
    print(Back.BLACK + Fore.YELLOW + "5. Instalar VLC Media Player")
    print(Back.BLACK + Fore.YELLOW + "6. Instalar Microsoft Office (versão online)")
    print(Back.BLACK + Fore.YELLOW + "7. Instalar Visual Studio Code")
    print(Back.BLACK + Fore.YELLOW + "8. Instalar Discord")
    print(Back.BLACK + Fore.YELLOW + "9. Instalar WinRAR")
    print(Back.BLACK + Fore.YELLOW + "10. Instalar Notepad++")
    print(Back.BLACK + Fore.YELLOW + "11. Instalar Dropbox")
    print(Back.BLACK + Fore.YELLOW + "12. Instalar Adobe Creative Cloud (versão de avaliação)")
    print(Back.BLACK + Fore.GREEN + "13. Sair")
    print(Back.BLACK + Fore.GREEN + "====================================")

def install_anydesk():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do AnyDesk para Windows...")
    anydesk_download_url = "https://download.anydesk.com/AnyDesk.exe"
    installer_filename = "AnyDesk.exe"
    try:
        download_with_progress(anydesk_download_url, installer_filename)
        run_installer(installer_filename, "AnyDesk")
        print(Back.BLACK + Fore.GREEN + "AnyDesk foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do AnyDesk: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_google_chrome():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Google Chrome para Windows...")
    chrome_download_url = "https://www.google.com/intl/pt-BR/chrome/"
    installer_filename = "ChromeStandaloneSetup64.exe"
    try:
        download_with_progress(chrome_download_url, installer_filename)
        run_installer(installer_filename, "Google Chrome")
        print(Back.BLACK + Fore.GREEN + "Google Chrome foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Google Chrome: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_mozilla_firefox():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Mozilla Firefox para Windows...")
    firefox_download_url = "https://download.mozilla.org/?product=firefox-latest&os=win&lang=pt-BR"
    installer_filename = "FirefoxSetup.exe"
    try:
        download_with_progress(firefox_download_url, installer_filename)
        run_installer(installer_filename, "Mozilla Firefox")
        print(Back.BLACK + Fore.GREEN + "Mozilla Firefox foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Mozilla Firefox: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_zoom():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Zoom para Windows...")
    zoom_download_url = "https://zoom.us/client/latest/ZoomInstaller.exe"
    installer_filename = "ZoomInstaller.exe"
    try:
        download_with_progress(zoom_download_url, installer_filename)
        run_installer(installer_filename, "Zoom")
        print(Back.BLACK + Fore.GREEN + "Zoom foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Zoom: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_vlc_media_player():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do VLC Media Player para Windows...")
    system_architecture = platform.architecture()[0]
    arch_suffix = "64" if system_architecture == "64bit" else "32"
    vlc_download_url = f"https://get.videolan.org/vlc/last/win{arch_suffix}/vlc-{arch_suffix}.0.16-win{arch_suffix}.exe"
    installer_filename = f"vlc-{arch_suffix}.0.16-win{arch_suffix}.exe"
    try:
        download_with_progress(vlc_download_url, installer_filename)
        run_installer(installer_filename, "VLC Media Player")
        print(Back.BLACK + Fore.GREEN + "VLC Media Player foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do VLC Media Player: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_microsoft_office():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Microsoft Office (versão online) para Windows...")
    office_download_url = "https://www.office.com/"
    installer_filename = "OfficeInstaller.exe"
    try:
        download_with_progress(office_download_url, installer_filename)
        run_installer(installer_filename, "Microsoft Office (versão online)")
        print(Back.BLACK + Fore.GREEN + "Microsoft Office (versão online) foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Microsoft Office: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_visual_studio_code():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Visual Studio Code para Windows...")
    system_architecture = platform.architecture()[0]
    vscode_download_url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64" if system_architecture == "64bit" else "https://code.visualstudio.com/sha/download?build=stable&os=win32"
    installer_filename = "VSCodeSetup.exe"
    try:
        download_with_progress(vscode_download_url, installer_filename)
        run_installer(installer_filename, "Visual Studio Code")
        print(Back.BLACK + Fore.GREEN + "Visual Studio Code foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Visual Studio Code: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_discord():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Discord para Windows...")
    system_architecture = platform.architecture()[0]
    arch_suffix = "x64" if system_architecture == "64bit" else "ia32"
    discord_download_url = f"https://discord.com/api/download?platform=win&arch={arch_suffix}"
    installer_filename = f"DiscordSetup-{arch_suffix}.exe"
    try:
        download_with_progress(discord_download_url, installer_filename)
        run_installer(installer_filename, "Discord")
        print(Back.BLACK + Fore.GREEN + "Discord foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Discord: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_winrar():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do WinRAR para Windows...")
    system_architecture = platform.architecture()[0]
    arch_suffix = "x64" if system_architecture == "64bit" else "x86"
    winrar_download_url = f"https://www.win-rar.com/fileadmin/winrar-versions/{arch_suffix}/wrar641.exe"
    installer_filename = f"winrar-{arch_suffix}.exe"
    try:
        download_with_progress(winrar_download_url, installer_filename)
        run_installer(installer_filename, "WinRAR")
        print(Back.BLACK + Fore.GREEN + "WinRAR foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do WinRAR: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_notepad_plus_plus():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Notepad++ para Windows...")
    npp_download_url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.3.1/npp.8.3.1.Installer.exe"
    installer_filename = "npp.8.3.1.Installer.exe"
    try:
        download_with_progress(npp_download_url, installer_filename)
        run_installer(installer_filename, "Notepad++")
        print(Back.BLACK + Fore.GREEN + "Notepad++ foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Notepad++: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_dropbox():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Dropbox para Windows...")
    dropbox_download_url = "https://www.dropbox.com/download?plat=win"
    installer_filename = "DropboxInstaller.exe"
    try:
        download_with_progress(dropbox_download_url, installer_filename)
        run_installer(installer_filename, "Dropbox")
        print(Back.BLACK + Fore.GREEN + "Dropbox foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Dropbox: {e}")
    finally:
        input("Pressione Enter para continuar...")

def install_adobe_cc():
    print(Back.BLACK + Fore.GREEN + "Iniciando o download do Adobe Creative Cloud (versão de avaliação) para Windows...")
    adobe_cc_download_url = "https://www.adobe.com/creativecloud/desktop-app.html"
    installer_filename = "AdobeCreativeCloud.exe"
    try:
        download_with_progress(adobe_cc_download_url, installer_filename)
        run_installer(installer_filename, "Adobe Creative Cloud (versão de avaliação)")
        print(Back.BLACK + Fore.GREEN + "Adobe Creative Cloud (versão de avaliação) foi instalado com sucesso!")
    except Exception as e:
        print(Back.BLACK + Fore.RED + f"Erro durante a instalação do Adobe Creative Cloud: {e}")
    finally:
        input("Pressione Enter para continuar...")

def download_with_progress(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        with open(filename, 'wb') as f, tqdm(
            desc=f"Baixando {filename}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            colour='green'
        ) as progress_bar:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                progress_bar.update(len(chunk))

def run_installer(filename, app_name):
    print(Back.BLACK + Fore.YELLOW + f"Iniciando a instalação de {app_name}...")
    try:
        # Executa o instalador com privilégios elevados
        if platform.system() == "Windows":
            ctypes.windll.shell32.ShellExecuteW(None, "runas", filename, None, None, 1)
        else:
            subprocess.run(["sudo", filename], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Erro durante a instalação de {app_name}: {e}")

def clean_up():
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    print(Back.BLACK + Fore.RED + "Esse sistema foi desenvolvido por Edson.")
    main()