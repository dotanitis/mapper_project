import tkinter as tk
from tkinter import ttk, messagebox
import math

class HexMapper:
    def __init__(self, root):
        self.root = root
        self.root.title("Hex Number Mapper - 8bit to 10bit to 16bit")
        self.root.geometry("600x500")
        
        # Configuration variables
        self.bit8_min = tk.DoubleVar(value=0)
        self.bit8_max = tk.DoubleVar(value=255)
        self.bit10_min = tk.DoubleVar(value=0)
        self.bit10_max = tk.DoubleVar(value=1023)
        self.bit16_min = tk.DoubleVar(value=0)
        self.bit16_max = tk.DoubleVar(value=65535)
        self.bit12_min = tk.DoubleVar(value=0)
        self.bit12_max = tk.DoubleVar(value=4095)

        # Value variables
        self.hex8_var = tk.StringVar(value="80")
        self.dec8_var = tk.StringVar()
        self.bin8_var = tk.StringVar()
        self.hex10_var = tk.StringVar()
        self.dec10_var = tk.StringVar()
        self.bin10_var = tk.StringVar()
        self.hex12_var = tk.StringVar()
        self.dec12_var = tk.StringVar()
        self.bin12_var = tk.StringVar()
        self.hex16_var = tk.StringVar()
        self.dec16_var = tk.StringVar()
        self.bin16_var = tk.StringVar()

        self.setup_ui()
        self.update_values()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuration section
        config_frame = ttk.LabelFrame(main_frame, text="Configuration", padding="10")
        config_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # 8-bit config
        ttk.Label(config_frame, text="8-bit range:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(config_frame, textvariable=self.bit8_min, width=8).grid(row=0, column=1, padx=5)
        ttk.Label(config_frame, text="to").grid(row=0, column=2, padx=5)
        ttk.Entry(config_frame, textvariable=self.bit8_max, width=8).grid(row=0, column=3, padx=5)
        
        # 10-bit config
        ttk.Label(config_frame, text="10-bit range:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(config_frame, textvariable=self.bit10_min, width=8).grid(row=1, column=1, padx=5)
        ttk.Label(config_frame, text="to").grid(row=1, column=2, padx=5)
        ttk.Entry(config_frame, textvariable=self.bit10_max, width=8).grid(row=1, column=3, padx=5)
        
        # 12-bit config
        ttk.Label(config_frame, text="12-bit range:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(config_frame, textvariable=self.bit12_min, width=8).grid(row=2, column=1, padx=5)
        ttk.Label(config_frame, text="to").grid(row=2, column=2, padx=5)
        ttk.Entry(config_frame, textvariable=self.bit12_max, width=8).grid(row=2, column=3, padx=5)

        # 16-bit config
        ttk.Label(config_frame, text="16-bit range:").grid(row=3, column=0, sticky=tk.W)
        ttk.Entry(config_frame, textvariable=self.bit16_min, width=8).grid(row=3, column=1, padx=5)
        ttk.Label(config_frame, text="to").grid(row=3, column=2, padx=5)
        ttk.Entry(config_frame, textvariable=self.bit16_max, width=8).grid(row=3, column=3, padx=5)
        
        # Values section
        values_frame = ttk.LabelFrame(main_frame, text="Values", padding="10")
        values_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # 8-bit section
        ttk.Label(values_frame, text="8-bit Input:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Label(values_frame, text="Hex:").grid(row=1, column=0, sticky=tk.W, padx=20)
        hex8_entry = ttk.Entry(values_frame, textvariable=self.hex8_var, width=10)
        hex8_entry.grid(row=1, column=1, padx=5)
        hex8_entry.bind('<KeyRelease>', self.on_hex8_change)

        ttk.Label(values_frame, text="Dec:").grid(row=1, column=2, sticky=tk.W, padx=20)
        dec8_entry = ttk.Entry(values_frame, textvariable=self.dec8_var, width=10)
        dec8_entry.grid(row=1, column=3, padx=5)
        dec8_entry.bind('<KeyRelease>', self.on_dec8_change)

        ttk.Label(values_frame, text="Bin:").grid(row=1, column=4, sticky=tk.W, padx=20)
        bin8_entry = ttk.Entry(values_frame, textvariable=self.bin8_var, width=10, state='readonly')
        bin8_entry.grid(row=1, column=5, padx=5)
        
        # 10-bit section
        ttk.Label(values_frame, text="10-bit Mapped:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=(15, 5))
        ttk.Label(values_frame, text="Hex:").grid(row=3, column=0, sticky=tk.W, padx=20)
        hex10_entry = ttk.Entry(values_frame, textvariable=self.hex10_var, width=10)
        hex10_entry.grid(row=3, column=1, padx=5)
        hex10_entry.bind('<KeyRelease>', self.on_hex10_change)

        ttk.Label(values_frame, text="Dec:").grid(row=3, column=2, sticky=tk.W, padx=20)
        dec10_entry = ttk.Entry(values_frame, textvariable=self.dec10_var, width=10)
        dec10_entry.grid(row=3, column=3, padx=5)
        dec10_entry.bind('<KeyRelease>', self.on_dec10_change)

        ttk.Label(values_frame, text="Bin:").grid(row=3, column=4, sticky=tk.W, padx=20)
        bin10_entry = ttk.Entry(values_frame, textvariable=self.bin10_var, width=14, state='readonly')
        bin10_entry.grid(row=3, column=5, padx=5)

        # 12-bit section
        ttk.Label(values_frame, text="12-bit Mapped:", font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky=tk.W, pady=(15, 5))
        ttk.Label(values_frame, text="Hex:").grid(row=5, column=0, sticky=tk.W, padx=20)
        hex12_entry = ttk.Entry(values_frame, textvariable=self.hex12_var, width=10)
        hex12_entry.grid(row=5, column=1, padx=5)
        hex12_entry.bind('<KeyRelease>', self.on_hex12_change)

        ttk.Label(values_frame, text="Dec:").grid(row=5, column=2, sticky=tk.W, padx=20)
        dec12_entry = ttk.Entry(values_frame, textvariable=self.dec12_var, width=10)
        dec12_entry.grid(row=5, column=3, padx=5)
        dec12_entry.bind('<KeyRelease>', self.on_dec12_change)

        ttk.Label(values_frame, text="Bin:").grid(row=5, column=4, sticky=tk.W, padx=20)
        # Use a Text widget for color highlighting
        self.bin12_text = tk.Text(values_frame, width=18, height=1, font=('TkDefaultFont', 9))
        self.bin12_text.grid(row=5, column=5, padx=5)
        self.bin12_text.config(state='disabled')
        # Label for 10MSB hex value
        self.msb10_hex_label = ttk.Label(values_frame, text="")
        self.msb10_hex_label.grid(row=5, column=6, padx=5, sticky=tk.W)
        
        # 16-bit section
        ttk.Label(values_frame, text="16-bit Mapped:", font=('Arial', 10, 'bold')).grid(row=6, column=0, sticky=tk.W, pady=(15, 5))
        ttk.Label(values_frame, text="Hex:").grid(row=7, column=0, sticky=tk.W, padx=20)
        hex16_entry = ttk.Entry(values_frame, textvariable=self.hex16_var, width=10)
        hex16_entry.grid(row=7, column=1, padx=5)
        hex16_entry.bind('<KeyRelease>', self.on_hex16_change)

        ttk.Label(values_frame, text="Dec:").grid(row=7, column=2, sticky=tk.W, padx=20)
        dec16_entry = ttk.Entry(values_frame, textvariable=self.dec16_var, width=10)
        dec16_entry.grid(row=7, column=3, padx=5)
        dec16_entry.bind('<KeyRelease>', self.on_dec16_change)

        ttk.Label(values_frame, text="Bin:").grid(row=7, column=4, sticky=tk.W, padx=20)
        bin16_entry = ttk.Entry(values_frame, textvariable=self.bin16_var, width=18, state='readonly')
        bin16_entry.grid(row=7, column=5, padx=5)
    def on_hex12_change(self, event=None):
        try:
            hex_val = self.hex12_var.get().strip()
            if hex_val:
                dec_val = int(hex_val, 16)
                self.dec12_var.set(str(dec_val))
                self.update_from_12bit(dec_val)
        except ValueError:
            pass

    def on_dec12_change(self, event=None):
        try:
            dec_val = int(self.dec12_var.get())
            hex_val = hex(dec_val)[2:].upper()
            self.hex12_var.set(hex_val)
            self.update_from_12bit(dec_val)
        except ValueError:
            pass

        
        # Process explanation
        process_frame = ttk.LabelFrame(main_frame, text="Process Explanation", padding="10")
        process_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.process_text = tk.Text(process_frame, height=8, width=70, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(process_frame, orient="vertical", command=self.process_text.yview)
        self.process_text.configure(yscrollcommand=scrollbar.set)
        self.process_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind configuration changes
        for var in [self.bit8_min, self.bit8_max, self.bit10_min, self.bit10_max, self.bit16_min, self.bit16_max]:
            var.trace('w', self.on_config_change)
    
    def linear_interpolate(self, value, in_min, in_max, out_min, out_max):
        if in_max == in_min:
            return out_min
        normalized = (value - in_min) / (in_max - in_min)
        return out_min + normalized * (out_max - out_min)
    
    def on_hex8_change(self, event=None):
        try:
            hex_val = self.hex8_var.get().strip()
            if hex_val:
                dec_val = int(hex_val, 16)
                self.dec8_var.set(str(dec_val))
                self.update_mapped_values()
        except ValueError:
            pass
    
    def on_dec8_change(self, event=None):
        try:
            dec_val = int(self.dec8_var.get())
            hex_val = hex(dec_val)[2:].upper()
            self.hex8_var.set(hex_val)
            self.update_mapped_values()
        except ValueError:
            pass
    
    def on_hex10_change(self, event=None):
        try:
            hex_val = self.hex10_var.get().strip()
            if hex_val:
                dec_val = int(hex_val, 16)
                self.dec10_var.set(str(dec_val))
                self.update_from_10bit(dec_val)
        except ValueError:
            pass
    
    def on_dec10_change(self, event=None):
        try:
            dec_val = int(self.dec10_var.get())
            hex_val = hex(dec_val)[2:].upper()
            self.hex10_var.set(hex_val)
            self.update_from_10bit(dec_val)
        except ValueError:
            pass
    
    def on_hex16_change(self, event=None):
        try:
            hex_val = self.hex16_var.get().strip()
            if hex_val:
                dec_val = int(hex_val, 16)
                self.dec16_var.set(str(dec_val))
                self.update_from_16bit(dec_val)
        except ValueError:
            pass
    
    def on_dec16_change(self, event=None):
        try:
            dec_val = int(self.dec16_var.get())
            hex_val = hex(dec_val)[2:].upper()
            self.hex16_var.set(hex_val)
            self.update_from_16bit(dec_val)
        except ValueError:
            pass
    
    def on_config_change(self, *args):
        self.update_values()
    
    def update_mapped_values(self):
        try:
            dec8 = int(self.dec8_var.get())

            # Map 8-bit to 10-bit
            dec10 = self.linear_interpolate(
                dec8,
                self.bit8_min.get(), self.bit8_max.get(),
                self.bit10_min.get(), self.bit10_max.get()
            )
            dec10 = int(round(dec10))

            # Map 10-bit to 12-bit
            dec12 = self.linear_interpolate(
                dec10,
                self.bit10_min.get(), self.bit10_max.get(),
                self.bit12_min.get(), self.bit12_max.get()
            )
            dec12 = int(round(dec12))

            # Map 12-bit to 16-bit
            dec16 = self.linear_interpolate(
                dec12,
                self.bit12_min.get(), self.bit12_max.get(),
                self.bit16_min.get(), self.bit16_max.get()
            )
            dec16 = int(round(dec16))

            self.dec10_var.set(str(dec10))
            self.hex10_var.set(hex(dec10)[2:].upper())
            self.bin10_var.set(format(dec10, '010b'))

            self.dec12_var.set(str(dec12))
            self.hex12_var.set(hex(dec12)[2:].upper())
            self.bin12_var.set(format(dec12, '012b'))

            self.dec16_var.set(str(dec16))
            self.hex16_var.set(hex(dec16)[2:].upper())
            self.bin16_var.set(format(dec16, '016b'))

            self.bin8_var.set(format(int(self.dec8_var.get()), '08b'))
            self._update_bin12_text()

            self.update_process_explanation(dec8, dec10, dec12, dec16)

        except (ValueError, ZeroDivisionError):
            pass
    def _update_bin12_text(self):
        # Show 12 bits, mark 10 MSB in red, and show their hex value
        bin12 = self.bin12_var.get()
        if len(bin12) < 12:
            bin12 = bin12.zfill(12)
        msb10 = bin12[:10]
        lsb2 = bin12[10:]
        self.bin12_text.config(state='normal')
        self.bin12_text.delete('1.0', tk.END)
        self.bin12_text.insert(tk.END, msb10, 'red')
        self.bin12_text.insert(tk.END, lsb2)
        self.bin12_text.tag_configure('red', foreground='red')
        self.bin12_text.config(state='disabled')

        # Show the value of the 10 MSB in hex
        msb10_val = int(msb10, 2)
        msb10_hex = hex(msb10_val)[2:].upper()
        self.msb10_hex_label.config(text=f"10MSB: 0x{msb10_hex}")
    
    def update_from_10bit(self, dec10):
        try:
            # Reverse map 10-bit to 8-bit
            dec8 = self.linear_interpolate(
                dec10,
                self.bit10_min.get(), self.bit10_max.get(),
                self.bit8_min.get(), self.bit8_max.get()
            )
            dec8 = int(round(dec8))

            # Map 10-bit to 12-bit
            dec12 = self.linear_interpolate(
                dec10,
                self.bit10_min.get(), self.bit10_max.get(),
                self.bit12_min.get(), self.bit12_max.get()
            )
            dec12 = int(round(dec12))

            # Map 12-bit to 16-bit
            dec16 = self.linear_interpolate(
                dec12,
                self.bit12_min.get(), self.bit12_max.get(),
                self.bit16_min.get(), self.bit16_max.get()
            )
            dec16 = int(round(dec16))

            self.dec8_var.set(str(dec8))
            self.hex8_var.set(hex(dec8)[2:].upper())
            self.bin8_var.set(format(dec8, '08b'))

            self.dec12_var.set(str(dec12))
            self.hex12_var.set(hex(dec12)[2:].upper())
            self.bin12_var.set(format(dec12, '012b'))

            self.dec16_var.set(str(dec16))
            self.hex16_var.set(hex(dec16)[2:].upper())
            self.bin16_var.set(format(dec16, '016b'))

            self.bin10_var.set(format(dec10, '010b'))
            self._update_bin12_text()

            self.update_process_explanation(dec8, dec10, dec12, dec16)

        except (ValueError, ZeroDivisionError):
            pass
    
    def update_from_16bit(self, dec16):
        try:
            # Reverse map 16-bit to 12-bit
            dec12 = self.linear_interpolate(
                dec16,
                self.bit16_min.get(), self.bit16_max.get(),
                self.bit12_min.get(), self.bit12_max.get()
            )
            dec12 = int(round(dec12))

            # Reverse map 12-bit to 10-bit
            dec10 = self.linear_interpolate(
                dec12,
                self.bit12_min.get(), self.bit12_max.get(),
                self.bit10_min.get(), self.bit10_max.get()
            )
            dec10 = int(round(dec10))

            # Reverse map 10-bit to 8-bit
            dec8 = self.linear_interpolate(
                dec10,
                self.bit10_min.get(), self.bit10_max.get(),
                self.bit8_min.get(), self.bit8_max.get()
            )
            dec8 = int(round(dec8))

            self.dec8_var.set(str(dec8))
            self.hex8_var.set(hex(dec8)[2:].upper())
            self.bin8_var.set(format(dec8, '08b'))

            self.dec10_var.set(str(dec10))
            self.hex10_var.set(hex(dec10)[2:].upper())
            self.bin10_var.set(format(dec10, '010b'))

            self.dec12_var.set(str(dec12))
            self.hex12_var.set(hex(dec12)[2:].upper())
            self.bin12_var.set(format(dec12, '012b'))

            self.bin16_var.set(format(dec16, '016b'))
            self.dec16_var.set(str(dec16))
            self.hex16_var.set(hex(dec16)[2:].upper())

            self._update_bin12_text()

            self.update_process_explanation(dec8, dec10, dec12, dec16)

        except (ValueError, ZeroDivisionError):
            pass
    def update_from_12bit(self, dec12):
        try:
            # Reverse map 12-bit to 10-bit
            dec10 = self.linear_interpolate(
                dec12,
                self.bit12_min.get(), self.bit12_max.get(),
                self.bit10_min.get(), self.bit10_max.get()
            )
            dec10 = int(round(dec10))

            # Reverse map 10-bit to 8-bit
            dec8 = self.linear_interpolate(
                dec10,
                self.bit10_min.get(), self.bit10_max.get(),
                self.bit8_min.get(), self.bit8_max.get()
            )
            dec8 = int(round(dec8))

            # Map 12-bit to 16-bit
            dec16 = self.linear_interpolate(
                dec12,
                self.bit12_min.get(), self.bit12_max.get(),
                self.bit16_min.get(), self.bit16_max.get()
            )
            dec16 = int(round(dec16))

            self.dec8_var.set(str(dec8))
            self.hex8_var.set(hex(dec8)[2:].upper())
            self.bin8_var.set(format(dec8, '08b'))

            self.dec10_var.set(str(dec10))
            self.hex10_var.set(hex(dec10)[2:].upper())
            self.bin10_var.set(format(dec10, '010b'))

            self.bin12_var.set(format(dec12, '012b'))
            self._update_bin12_text()

            self.dec16_var.set(str(dec16))
            self.hex16_var.set(hex(dec16)[2:].upper())
            self.bin16_var.set(format(dec16, '016b'))

            self.update_process_explanation(dec8, dec10, dec12, dec16)

        except (ValueError, ZeroDivisionError):
            pass
    
    def update_values(self):
        self.update_mapped_values()
    
    def update_process_explanation(self, dec8, dec10, dec12, dec16):
        explanation = f"""Linear Interpolation Process (8-bit → 10-bit → 12-bit → 16-bit):

Step 1: 8-bit to 10-bit mapping
Input: {dec8} (0x{hex(dec8)[2:].upper()})
Range: [{self.bit8_min.get():.0f}, {self.bit8_max.get():.0f}] → [{self.bit10_min.get():.0f}, {self.bit10_max.get():.0f}]
Formula: ({dec8} - {self.bit8_min.get():.0f}) / ({self.bit8_max.get():.0f} - {self.bit8_min.get():.0f}) * ({self.bit10_max.get():.0f} - {self.bit10_min.get():.0f}) + {self.bit10_min.get():.0f}
Result: {dec10} (0x{hex(dec10)[2:].upper()}) (bin: {format(dec10, '010b')})

Step 2: 10-bit to 12-bit mapping
Input: {dec10} (0x{hex(dec10)[2:].upper()})
Range: [{self.bit10_min.get():.0f}, {self.bit10_max.get():.0f}] → [{self.bit12_min.get():.0f}, {self.bit12_max.get():.0f}]
Formula: ({dec10} - {self.bit10_min.get():.0f}) / ({self.bit10_max.get():.0f} - {self.bit10_min.get():.0f}) * ({self.bit12_max.get():.0f} - {self.bit12_min.get():.0f}) + {self.bit12_min.get():.0f}
Result: {dec12} (0x{hex(dec12)[2:].upper()})

Step 3: 12-bit to 16-bit mapping
Input: {dec12} (0x{hex(dec12)[2:].upper()})
Range: [{self.bit12_min.get():.0f}, {self.bit12_max.get():.0f}] → [{self.bit16_min.get():.0f}, {self.bit16_max.get():.0f}]
Formula: ({dec12} - {self.bit12_min.get():.0f}) / ({self.bit12_max.get():.0f} - {self.bit12_min.get():.0f}) * ({self.bit16_max.get():.0f} - {self.bit16_min.get():.0f}) + {self.bit16_min.get():.0f}
Result: {dec16} (0x{hex(dec16)[2:].upper()})

Final mapping: 0x{hex(dec8)[2:].upper()} → 0x{hex(dec10)[2:].upper()} → 0x{hex(dec12)[2:].upper()} → 0x{hex(dec16)[2:].upper()}
"""
        self.process_text.delete(1.0, tk.END)
        self.process_text.insert(1.0, explanation)

if __name__ == "__main__":
    root = tk.Tk()
    app = HexMapper(root)
    root.mainloop()