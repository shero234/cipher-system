#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from cipher import CaesarCipher, VigenèreCipher

class CipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Encryption/Decryption System")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 18, 'bold'), foreground='#2c3e50')
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#34495e')
        style.configure('Normal.TLabel', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10))
        
        # Configure colors
        self.bg_color = '#ecf0f1'
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.create_widgets()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Title
        title_frame = tk.Frame(self.root, bg='#3498db', height=60)
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(
            title_frame, 
            text="🔐 Cipher Encryption/Decryption System",
            font=('Arial', 16, 'bold'),
            bg='#3498db',
            fg='white'
        )
        title_label.pack(pady=10)
        
        # Main content frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Cipher selection
        cipher_frame = ttk.LabelFrame(main_frame, text="Select Cipher", padding="10")
        cipher_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.cipher_var = tk.StringVar(value="caesar")
        ttk.Radiobutton(
            cipher_frame, 
            text="Caesar Cipher", 
            variable=self.cipher_var, 
            value="caesar",
            command=self.on_cipher_change
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Radiobutton(
            cipher_frame, 
            text="Vigenère Cipher", 
            variable=self.cipher_var, 
            value="vigenere",
            command=self.on_cipher_change
        ).pack(side=tk.LEFT, padx=10)
        
        # Parameters frame
        params_frame = ttk.LabelFrame(main_frame, text="Parameters", padding="10")
        params_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Caesar shift
        ttk.Label(params_frame, text="Shift Value:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.shift_var = tk.StringVar(value="3")
        self.shift_spinbox = ttk.Spinbox(
            params_frame, 
            from_=1, 
            to=25, 
            textvariable=self.shift_var,
            width=10
        )
        self.shift_spinbox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Vigenère key
        ttk.Label(params_frame, text="Key:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.key_var = tk.StringVar(value="SECRET")
        self.key_entry = ttk.Entry(params_frame, textvariable=self.key_var, width=30)
        self.key_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.key_entry.grid_remove()  # Hide initially
        
        ttk.Label(params_frame, text="(Key is hidden for Caesar)").grid(row=1, column=2, sticky=tk.W, padx=5)
        
        # Input/Output frame
        io_frame = ttk.LabelFrame(main_frame, text="Text Processing", padding="10")
        io_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Input
        ttk.Label(io_frame, text="Input Text:").pack(anchor=tk.W, pady=(0, 5))
        self.input_text = scrolledtext.ScrolledText(
            io_frame, 
            height=6, 
            width=70,
            font=('Arial', 10),
            wrap=tk.WORD
        )
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Output
        ttk.Label(io_frame, text="Output Text:").pack(anchor=tk.W, pady=(0, 5))
        self.output_text = scrolledtext.ScrolledText(
            io_frame, 
            height=6, 
            width=70,
            font=('Arial', 10),
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg='#ecf0f1'
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            button_frame,
            text="🔒 Encrypt",
            command=self.encrypt_text
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="🔓 Decrypt",
            command=self.decrypt_text
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="🔄 Clear All",
            command=self.clear_all
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="📋 Copy Output",
            command=self.copy_output
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="❌ Exit",
            command=self.root.quit
        ).pack(side=tk.RIGHT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def on_cipher_change(self):
        """Handle cipher selection change"""
        if self.cipher_var.get() == "caesar":
            self.shift_spinbox.grid()
            ttk.Label(
                self.shift_spinbox.master, 
                text="(Key is hidden for Caesar)"
            ).grid(row=1, column=2, sticky=tk.W, padx=5)
            self.key_entry.grid_remove()
        else:
            self.shift_spinbox.grid_remove()
            self.key_entry.grid()
        
        self.status_var.set("Cipher changed to " + self.cipher_var.get().upper())
    
    def encrypt_text(self):
        """Encrypt the input text"""
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to encrypt!")
            return
        
        try:
            if self.cipher_var.get() == "caesar":
                shift = int(self.shift_var.get())
                cipher = CaesarCipher(shift=shift)
                result = cipher.encrypt(input_text)
                self.status_var.set(f"✓ Caesar cipher encrypted (shift: {shift})")
            else:
                key = self.key_var.get().strip()
                if not key or not key.isalpha():
                    messagebox.showerror("Error", "Key must contain only letters!")
                    return
                cipher = VigenèreCipher(key=key)
                result = cipher.encrypt(input_text)
                self.status_var.set(f"✓ Vigenère cipher encrypted (key: {key})")
            
            self.display_output(result)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            self.status_var.set("❌ Encryption failed")
    
    def decrypt_text(self):
        """Decrypt the input text"""
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to decrypt!")
            return
        
        try:
            if self.cipher_var.get() == "caesar":
                shift = int(self.shift_var.get())
                cipher = CaesarCipher(shift=shift)
                result = cipher.decrypt(input_text)
                self.status_var.set(f"✓ Caesar cipher decrypted (shift: {shift})")
            else:
                key = self.key_var.get().strip()
                if not key or not key.isalpha():
                    messagebox.showerror("Error", "Key must contain only letters!")
                    return
                cipher = VigenèreCipher(key=key)
                result = cipher.decrypt(input_text)
                self.status_var.set(f"✓ Vigenère cipher decrypted (key: {key})")
            
            self.display_output(result)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            self.status_var.set("❌ Decryption failed")
    
    def display_output(self, text):
        """Display output text"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)
        self.output_text.config(state=tk.DISABLED)
    
    def clear_all(self):
        """Clear all text fields"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.status_var.set("All fields cleared")
    
    def copy_output(self):
        """Copy output text to clipboard"""
        output = self.output_text.get("1.0", tk.END).strip()
        if output:
            self.root.clipboard_clear()
            self.root.clipboard_append(output)
            messagebox.showinfo("Success", "Output copied to clipboard!")
            self.status_var.set("✓ Output copied to clipboard")
        else:
            messagebox.showwarning("Warning", "Nothing to copy!")

def main():
    root = tk.Tk()
    app = CipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
