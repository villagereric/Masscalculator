import tkinter as tk
from tkinter import messagebox

def calculate_mass():
    try:
        mw = float(entry_mw.get())             # 分子量
        conc_uM = float(entry_conc.get())      # 濃度（µM）
        vol_uL = float(entry_vol.get())        # 體積（µL）

        # 單位轉換
        conc_mol_L = conc_uM * 1e-6
        vol_L = vol_uL * 1e-6

        # 計算質量（g）
        mass_g = conc_mol_L * vol_L * mw
        result.set(f"需秤取：{mass_g:.6f} g")
    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入有效的數字")

# 建立視窗
window = tk.Tk()
window.title("藥物濃度配置計算器")
window.geometry("350x250")

# 輸入欄位
tk.Label(window, text="分子量 (g/mol)").pack()
entry_mw = tk.Entry(window)
entry_mw.pack()

tk.Label(window, text="濃度 (µM)").pack()
entry_conc = tk.Entry(window)
entry_conc.pack()

tk.Label(window, text="體積 (µL)").pack()
entry_vol = tk.Entry(window)
entry_vol.pack()

# 計算按鈕
tk.Button(window, text="計算", command=calculate_mass).pack(pady=10)

# 顯示結果
result = tk.StringVar()
tk.Label(window, textvariable=result, font=("Arial", 14), fg="blue").pack()

# 啟動主程式
window.mainloop()
