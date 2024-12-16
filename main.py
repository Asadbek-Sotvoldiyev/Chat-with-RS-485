import serial
import threading

def read_from_port(port):
    while True:
        if port.in_waiting:
            data = port.read_until().decode('utf-8').strip()
            print(f"\nXabar keldi: {data}")

def write_to_port(port):
    while True:
        message = input("Xabar kiriting: ")
        port.write(f"{message}\n".encode('utf-8'))

def main():
    port_name = input("Port nomini kiriting: (/dev/pts/1): ")
    try:
        port = serial.Serial(port_name, baudrate=9600, timeout=1)
        print(f"{port_name} portiga ulandi")

        read_thread = threading.Thread(target=read_from_port, args=(port,))
        read_thread.daemon = True
        read_thread.start()

        write_to_port(port)

    except serial.SerialException as e:
        print(f"Xatolik: {e}")
    except KeyboardInterrupt:
        print("Mavjud...")
    finally:
        if 'port' in locals() and port.is_open:
            port.close()

if __name__ == "__main__":
    main()
