import tkinter as tk
from tkinter import ttk
from main import VoxelEngine
import signals
import inspect


class DevPannel:
    def __init__(self, app: VoxelEngine):
        self.app = app
        self.root = tk.Tk()
        self.root.wm_geometry("270x600+1620+50")

        self.button1 = tk.Button(self.root, text="Заморозить обновления",
                                 command=lambda s=self: exec("s.app.is_paused = not s.app.is_paused"))
        self.button1.pack()

        # Разделительная полоса
        ttk.Separator(self.root, orient='horizontal').pack(fill='x', pady=10)

        self.signal_classes = self.get_signal_classes()
        self.selected_signal_class = tk.StringVar()

        tk.Label(self.root, text="Select Signal:").pack(pady=5)

        signal_select = ttk.Combobox(self.root, textvariable=self.selected_signal_class, state="readonly")
        signal_select['values'] = list(self.signal_classes.keys())
        signal_select.pack(pady=5)
        signal_select.bind("<<ComboboxSelected>>", self.on_signal_selected)

        self.param_frame = tk.Frame(self.root)
        self.param_frame.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Signal to Queue", command=self.add_signal_to_queue)
        self.add_button.pack(pady=5)

    @staticmethod
    def get_signal_classes():
        signal_classes = {}
        for name, obj in inspect.getmembers(signals):
            if inspect.isclass(obj) and issubclass(obj, signals.Signal) and obj is not signals.Signal:
                signal_classes[name] = obj
        return signal_classes

    def on_signal_selected(self, event):
        for widget in self.param_frame.winfo_children():
            widget.destroy()

        signal_class_name = self.selected_signal_class.get()
        signal_class = self.signal_classes[signal_class_name]

        self.param_vars = {}
        init_signature = inspect.signature(signal_class.__init__)

        for param_name, param in init_signature.parameters.items():
            if param_name == 'self':
                continue

            param_type = param.annotation if param.annotation != inspect.Parameter.empty else str
            param_type_str = self.get_type_str(param_type)

            tk.Label(self.param_frame, text=f"{param_name} ({param_type_str}):").pack()
            param_var = tk.StringVar()
            self.param_vars[param_name] = (param_var, param_type)
            tk.Entry(self.param_frame, textvariable=param_var).pack()

    @staticmethod
    def get_type_str(param_type):
        if hasattr(param_type, '__origin__') and param_type.__origin__ is tuple:
            return f"tuple[{', '.join(t.__name__ for t in param_type.__args__)}]"
        return param_type.__name__

    def add_signal_to_queue(self):
        signal_class_name = self.selected_signal_class.get()
        signal_class = self.signal_classes[signal_class_name]

        kwargs = {}
        for param_name, (param_var, param_type) in self.param_vars.items():
            param_value = param_var.get()
            if param_type == int:
                param_value = int(param_value)
            elif param_type == float:
                param_value = float(param_value)
            elif hasattr(param_type, '__origin__') and param_type.__origin__ is tuple:
                param_value = eval(param_value)  # Преобразуем строку в кортеж
            kwargs[param_name] = param_value

        signal_instance = signal_class(**kwargs)
        self.app.add_signal(signal_instance)
        print(f"Added signal: {signal_instance}")

    def update(self):
        self.root.update()