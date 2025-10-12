import re
import customtkinter as ctk
from .assets.styles.collors import collors

class Login_View(ctk.CTkFrame):
    def __init__(self, master, on_login=None, on_cancel=None):
        super().__init__(master, fg_color=collors["NAVY"])
        self.on_login = on_login
        self.on_cancel = on_cancel
    
        self.card = ctk.CTkFrame(
            self, fg_color=collors["CARD"],
            corner_radius=16,
            border_width=1,
            border_color=collors["BORDER"]
        )
        self.card.pack(expand=True)
        self.card.propagate(False)
        self.card.configure(width=420, height=420)
        
        self.title = ctk.CTkLabel(self.card, text="Smart Financial Control", font=("Segoe UI", 20, "bold"), text_color=collors["TEXT"])
        self.title.pack(pady=(28,6))
        
        self.title = ctk.CTkLabel(self.card, text="Login", font=("Segoe UI", 16), text_color=collors["TEXT"])
        self.title.pack(pady=(0,18))
        
                # Entrada: E-mail
        self.email_entry = ctk.CTkEntry(
            self.card,
            width=320,
            height=40,
            placeholder_text="E-mail",
            fg_color=collors["ENTRY_BG"],
            text_color=collors["TEXT"],
            placeholder_text_color="#94A3B8",
            border_color=collors["BORDER"],
            border_width=1,
        )
        self.email_entry.pack(pady=8)

        # Entrada: Senha
        self.password_entry = ctk.CTkEntry(
            self.card,
            width=320,
            height=40,
            placeholder_text="Senha",
            show="*",
            fg_color=collors["ENTRY_BG"],
            text_color=collors["TEXT"],
            placeholder_text_color="#94A3B8",
            border_color=collors["BORDER"],
            border_width=1,
        )
        self.password_entry.pack(pady=8)

        # Mostrar senha
        self.show_password_var = ctk.BooleanVar(value=False)
        self.show_password = ctk.CTkCheckBox(
            self.card,
            text="Mostrar senha",
            variable=self.show_password_var,
            # command=self._toggle_password,
            text_color=collors["TEXT"],
            checkbox_height=18,
            checkbox_width=18,
            border_color=collors["BORDER"],
        )
        self.show_password.pack(pady=(2, 10), anchor="w", padx=50)

        # Label de erro
        self.error_label = ctk.CTkLabel(self.card, text="", text_color=collors["TEXT"], font=("Segoe UI", 12))
        self.error_label.pack(pady=(0, 6))

        # Botões
        self.btns_row = ctk.CTkFrame(self.card, fg_color="transparent")
        self.btns_row.pack(pady=10)

        self.login_btn = ctk.CTkButton(
            self.btns_row,
            text="Entrar",
            width=150,
            height=40,
            fg_color=collors["CONFIRM_BTN"],
            hover_color=collors["CONFIRM_BTN_HOVER"],
            text_color=collors["TEXT"],
            # command=self._attempt_login,
        )
        self.login_btn.grid(row=0, column=0, padx=8)

        self.cancel_btn = ctk.CTkButton(
            self.btns_row,
            text="Cancelar",
            width=150,
            height=40,
            fg_color=collors["CANCEL_BTN"],
            hover_color=collors["CANCEL_BTN_HOVER"],
            text_color=collors["TEXT"],
            # command=self._cancel,
        )
        self.cancel_btn.grid(row=0, column=1, padx=8)