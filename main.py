import numpy as np
import matplotlib.pyplot as plt

# المعاملات
principal = 1000  # الاستثمار الأولي
rates = [0.03, 0.05, 0.07]  # معدلات الفائدة السنوية
years = 20  # عدد السنوات
times_compounded = [1, 2, 4]  # عدد مرات تركيب الفائدة سنوياً

# إنشاء الرسوم البيانية
plt.figure(figsize=(14, 8))

# حساب ورسم الفائدة المركبة لكل معدل فائدة وعدد مرات تركيب
for rate in rates:
    for n in times_compounded:
        # النقاط الزمنية
        t = np.arange(0, years + 1, 1)
        # صيغة الفائدة المركبة
        amount = principal * (1 + rate / n) ** (n * t)
        # تسمية الخطوط
        label = f'Rate: {rate*100}%, Compounded {n} times/year'
        # رسم الخطوط
        plt.plot(t, amount, marker='o', label=label)

# تخصيص الرسم البياني
plt.title('نمو الفائدة المركبة لمعدلات وأوقات تركيب مختلفة')
plt.xlabel('السنوات')
plt.ylabel('المبلغ ($)')
plt.legend()
plt.grid(True)
plt.show()
