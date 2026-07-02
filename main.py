import pandas as pd
import matplotlib.pyplot as plt

# مسیر فایل
file_path = r'C:\Users\Mahsa\Heat_Treatment_4140.xlsx'

try:
    # خواندن داده‌ها
    df = pd.read_excel(file_path)
    
    # رسم نمودار با نام دقیق ستون‌ها (دقیقاً مطابق لیست تو)
    plt.figure(figsize=(10, 6))
    plt.plot(df['Temp_Tempering (°C)'], df['Hardness (HRC)'], marker='o', linestyle='-', color='b', linewidth=2)

    # افزودن عنوان و برچسب‌ها
    plt.title('AISI 4140 Steel: Hardness vs Tempering Temperature', fontsize=14)
    plt.xlabel('Tempering Temperature (°C)', fontsize=12)
    plt.ylabel('Hardness (HRC)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # نمایش نمودار
    plt.show()

except Exception as e:
    print(f"یک خطا رخ داد! متن خطا: {e}")