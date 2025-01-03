import tkinter as tk
import pyautogui
import time
import threading

class AutoClicker:
    def init(self, master):
        self.master = master
        self.master.title("Автокликер")
        
        self.is_running = False

        # Метки и поля для ввода
        tk.Label(master, text="Время автоклика (в секундах):").grid(row=0, column=0)
        self.click_time_entry = tk.Entry(master)
        self.click_time_entry.grid(row=0, column=1)

        tk.Label(master, text="Время до начала (в секундах):").grid(row=1, column=0)
        self.start_delay_entry = tk.Entry(master)
        self.start_delay_entry.grid(row=1, column=1)

        tk.Label(master, text="Интервал между нажатиями (в секундах):").grid(row=2, column=0)
        self.interval_entry = tk.Entry(master)
        self.interval_entry.grid(row=2, column=1)

        tk.Label(master, text="Координаты клика (x, y):").grid(row=3, column=0)
        self.position_entry = tk.Entry(master)
        self.position_entry.grid(row=3, column=1)

        # Кнопки
        self.start_button = tk.Button(master, text="Запустить", command=self.start_clicking)
        self.start_button.grid(row=4, column=0)

        self.stop_button = tk.Button(master, text="Остановить", command=self.stop_clicking)
        self.stop_button.grid(row=4, column=1)

    def start_clicking(self):
        if not self.is_running:
            self.is_running = True
            thread = threading.Thread(target=self.autoclicker)
            thread.daemon = True
            thread.start()

    def stop_clicking(self):
        self.is_running = False

    def autoclicker(self):
        click_time = float(self.click_time_entry.get())
        start_delay = float(self.start_delay_entry.get())
        interval = float(self.interval_entry.get())
        positions = [tuple(map(int, pos.split(','))) for pos in self.position_entry.get().strip().split(';')]

        time.sleep(start_delay)

        start_time = time.time()
        while self.is_running and (time.time() - start_time < click_time):
            for pos in positions:
                if not self.is_running:
                    break
                pyautogui.click(pos)
                print(f"Кликнул в {pos}")
                time.sleep(interval)

        self.is_running = False

if name == "main":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()
