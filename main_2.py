import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\Mahsa\Heat_Treatment_4140.xlsx'

try:
    df = pd.read_excel(file_path)
    
    plt.figure(figsize=(10, 6))

    # رسم خطوط بر اساس دسته‌بندی محیط کوئنچ
    for medium, group_data in df.groupby('Quench_Medium (Code)'):
        plt.plot(group_data['Temp_Tempering (°C)'], 
                 group_data['Hardness (HRC)'], 
                 marker='o', 
                 label=f'Medium: {medium}', 
                 linewidth=2)

    # تنظیمات حرفه‌ای نمودار
    plt.title('AISI 4140: Hardness vs Tempering Temperature by Quench Medium', fontsize=14)
    plt.xlabel('Tempering Temperature (°C)', fontsize=12)
    plt.ylabel('Hardness (HRC)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title="Quenching Media") # این دستور راهنمای رنگ‌ها رو اضافه می‌کنه

    plt.show()

except Exception as e:
    print(f"خطایی رخ داد: {e}")