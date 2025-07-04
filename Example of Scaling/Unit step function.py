import numpy as np
import matplotlib.pyplot as plt

def unit_step(t):
    return np.where(t >= 0, 1, 0)

# Daha geniş zaman aralığı
t = np.linspace(-8, 8, 1000)

# Orijinal fonksiyon x(t) = 2t/5 [u(t) - u(t-6)]
def x_t(t):
    return (2*t/5) * (unit_step(t) - unit_step(t-6))

# Ölçeklendirilmiş fonksiyonlar
def x_2t(t):  # x(2t) - Zamansal sıkıştırma
    return x_t(2*t)

def x_3t(t):  # 3x(t) - Genlik artırma
    return 3 * x_t(t)

def x_2_minus_t(t):  # x(2-t) - Zamansal tersine çevirme ve kaydırma
    return x_t(2-t)

# 2x2 grafik oluştur
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# Ortak stil ayarları
def setup_axis(ax, title, explanation=""):
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.set_title(title, fontsize=14)
    if explanation:
        ax.text(0.5, -0.15, explanation, transform=ax.transAxes, ha='center', 
                fontsize=11, bbox={"facecolor":"lightgray", "alpha":0.5, "pad":5})
    ax.set_xlabel('t', fontsize=12)
    ax.set_ylabel('f(t)', fontsize=12)
    ax.legend(fontsize=10)

# 1) Orijinal fonksiyon: x(t) = 2t/5 [u(t) - u(t-6)]
signal = x_t(t)
ax1.plot(t, signal, 'b-', label='x(t) = 2t/5 [u(t) - u(t-6)]', linewidth=2)
setup_axis(ax1, 'Orijinal Fonksiyon: x(t)', 
           't=0\'da başlar, t=6\'ya kadar doğrusal artar,\nt=6\'da sıfıra düşer. Max değer: 2.4')
ax1.set_ylim([-0.5, 3])
ax1.set_xlim([-2, 8])

# 2) x(2t) - Zamansal sıkıştırma
signal_2t = x_2t(t)
ax2.plot(t, signal_2t, 'r-', label='x(2t)', linewidth=2)
setup_axis(ax2, 'Zamansal Sıkıştırma: x(2t)', 
           'Orijinal sinyalin zaman ekseni 1/2 kat sıkıştırılmış.\nt=3\'te sıfıra düşer.')
ax2.set_ylim([-0.5, 3])
ax2.set_xlim([-2, 8])

# 3) 3x(t) - Genlik artırma
signal_3t = x_3t(t)
ax3.plot(t, signal_3t, 'g-', label='3x(t)', linewidth=2)
setup_axis(ax3, 'Genlik Artırma: 3x(t)', 
           'Orijinal sinyalin genliği 3 kat artırılmış.\nMax değer: 7.2')
ax3.set_ylim([-0.5, 8])
ax3.set_xlim([-2, 8])

# 4) x(2-t) - Zamansal tersine çevirme ve kaydırma
signal_2_minus_t = x_2_minus_t(t)
ax4.plot(t, signal_2_minus_t, 'm-', label='x(2-t)', linewidth=2)
setup_axis(ax4, 'Zamansal Tersine Çevirme ve Kaydırma: x(2-t)', 
           't=2\'de sıfırdan başlar ve sola doğru artar.\nt=-4\'te max değere ulaşır ve sonra sıfıra düşer.')
ax4.set_ylim([-0.5, 3])
ax4.set_xlim([-6, 4])

# Doğrulama amaçlı: Orijinal ve x(2-t) fonksiyonlarını karşılaştırmak için küçük işaretler ekleyelim
# Orijinal fonksiyonda t=0 ve t=6 noktalarını işaretleyelim
ax1.plot(0, 0, 'ro', markersize=6)
ax1.plot(6, 2.4, 'ro', markersize=6)
ax1.text(0, 0.2, 't=0', fontsize=10)
ax1.text(6, 2.6, 't=6', fontsize=10)

# x(2-t) fonksiyonunda t=2 ve t=-4 noktalarını işaretleyelim
ax4.plot(2, 0, 'ro', markersize=6)
ax4.plot(-4, 2.4, 'ro', markersize=6)
ax4.text(2, 0.2, 't=2', fontsize=10)
ax4.text(-4, 2.6, 't=-4', fontsize=10)

plt.tight_layout()
plt.show()
