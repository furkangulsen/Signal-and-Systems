import numpy as np
import matplotlib.pyplot as plt

def m_t(t):
    """Tam doğru olan m(t) fonksiyonu"""
    result = np.zeros_like(t, dtype=float)

    # -4 <= t < 0 arasında doğrusal azalan eğim
    mask_down = np.logical_and(t >= -4, t < 0)
    result[mask_down] = 3 - (3/4) * (t[mask_down] + 4)  # Lineer azalan (düzeltildi)

    # 0 <= t < 3 arasında m(t) = 0 olacak şekilde bırak

    # 3 <= t <= 7 arasında doğrusal artan eğim
    mask_up = np.logical_and(t >= 3, t <= 7)
    result[mask_up] = (3/4) * (t[mask_up] - 3)  # Lineer artan

    # t = -4 ve t = 7 noktalarını düzelt
    mask_t4 = np.isclose(t, -4, atol=0.01)
    mask_t7 = np.isclose(t, 7, atol=0.01)
    result[mask_t4] = 3
    result[mask_t7] = 3

    return result

# Zaman aralığı
t = np.linspace(-8, 10, 1000)

# Sinyalleri hesapla
mt = m_t(t)                   # m(t)
m_2t = -1 * m_t(2*t)          # -m(2t) - Genlik -3 olacak şekilde düzeltildi
m_3_t = m_t(3-t)              # m(3-t)
m_negatif_t = m_t(-t)         # m(-t)
m_eksi_2t = -1 * m_t(t)       # -m(t) - Genlik -3 olacak şekilde düzeltildi
m_eksi_2_2t = -2 * m_t(2*t)   # -2m(2t) - Orijinal çarpan (-2) ile

# Ana şekli oluştur
plt.figure(figsize=(18, 6))

# 1. Grafik: m(t)
plt.subplot(1, 3, 1)
plt.plot(t, mt, 'r-', linewidth=2)  # Ana sinyal çizgisi

# t = -4'te yatay kesikli çizgi
plt.plot(np.linspace(-4, -3, 100), np.ones(100) * 3, 'r--', linewidth=2)

# Dikey çizgiler
plt.plot([-4, -4], [0, 3], 'r-', linewidth=2)
plt.plot([7, 7], [0, 3], 'r-', linewidth=2)

# İşaretli noktalar
plt.plot([-4, 0, 3, 7], [3, 0, 0, 3], 'ro')
plt.text(-4, 3.2, "-4", ha='center', color='r', fontweight='bold')
plt.text(3, -0.3, "3", ha='center', color='r', fontweight='bold')
plt.text(7, 3.2, "7", ha='center', color='r', fontweight='bold')

# Eksen ayarları
plt.grid(True)
plt.title('m(t) Sinyali')
plt.xlabel('t')
plt.ylabel('m(t)')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.xlim(-5, 8)
plt.ylim(-0.5, 4)

# m(t) başlığını ekle
plt.text(0, 3.5, "m(t)", color='r', fontsize=14, ha='center')

# 2. Grafik: -m(2t)
plt.subplot(1, 3, 2)
plt.plot(t, m_2t, 'r-', linewidth=2)

# Eksen ayarları
plt.grid(True)
plt.title('-m(2t) Sinyali')
plt.xlabel('t')
plt.ylabel('-m(2t)')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.xlim(-5, 8)
plt.ylim(-4, 1)  # Y ekseni aralığı düzeltildi

# -m(2t) için önemli noktalar
# t=-2 için m(2t=-4)=3, böylece -m(2t=-4)=-3
# t=0 için m(2t=0)=0, böylece -m(2t=0)=0
# t=1.5 için m(2t=3)=0, böylece -m(2t=3)=0
# t=3.5 için m(2t=7)=3, böylece -m(2t=7)=-3

plt.plot([-2, 0, 1.5, 3.5], [-3, 0, 0, -3], 'ro')  # Y değerleri düzeltildi
plt.text(-2, -3.2, "-2", ha='center', color='r', fontweight='bold')
plt.text(1.5, -0.3, "1.5", ha='center', color='r', fontweight='bold')
plt.text(3.5, -3.2, "3.5", ha='center', color='r', fontweight='bold')

# Dikey çizgiler
plt.plot([-2, -2], [0, -3], 'r-', linewidth=2)  # Y değeri düzeltildi
plt.plot([3.5, 3.5], [0, -3], 'r-', linewidth=2)  # Y değeri düzeltildi

# Yatay kesikli çizgi
plt.plot(np.linspace(-2, -1.5, 100), np.ones(100) * -3, 'r--', linewidth=2)  # Y değeri düzeltildi

# -m(2t) başlığını ekle
plt.text(1.5, -0.8, "-m(2t)", color='r', fontsize=14, ha='center')  # Başlık düzeltildi

# 3. Grafik: m(3-t)
plt.subplot(1, 3, 3)
plt.plot(t, m_3_t, 'r-', linewidth=2)

# Eksen ayarları
plt.grid(True)
plt.title('m(3-t) Sinyali')
plt.xlabel('t')
plt.ylabel('m(3-t)')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.xlim(-5, 8)
plt.ylim(-0.5, 4)

# m(3-t) için önemli noktalar
# t=7 için 3-t=-4, böylece m(3-t=-4)=3
# t=3 için 3-t=0, böylece m(3-t=0)=0
# t=0 için 3-t=3, böylece m(3-t=3)=0
# t=-4 için 3-t=7, böylece m(3-t=7)=3

plt.plot([7, 3, 0, -4], [3, 0, 0, 3], 'ro')
plt.text(7, 3.2, "7", ha='center', color='r', fontweight='bold')
plt.text(3, -0.3, "3", ha='center', color='r', fontweight='bold')
plt.text(0, -0.3, "0", ha='center', color='r', fontweight='bold')
plt.text(-4, 3.2, "-4", ha='center', color='r', fontweight='bold')

# Dikey çizgiler
plt.plot([7, 7], [0, 3], 'r-', linewidth=2)
plt.plot([-4, -4], [0, 3], 'r-', linewidth=2)

# Yatay kesikli çizgi
plt.plot(np.linspace(7, 6, 100), np.ones(100) * 3, 'r--', linewidth=2)

# m(3-t) başlığını ekle
plt.text(1.5, 3.5, "m(3-t)", color='r', fontsize=14, ha='center')

plt.tight_layout()
plt.show()

# Sadece m(-t) grafiği için daha temiz bir arayüz oluştur
plt.figure(figsize=(12, 8))
plt.rcParams.update({'font.size': 14})  # Yazı boyutunu artır

# Ana sinyal çizgisi
plt.plot(t, m_negatif_t, 'r-', linewidth=3.5)  # Çizgi kalınlığını artır

# İşaretli önemli noktalar
plt.plot([-7, -3, 0, 4], [3, 0, 0, 3], 'ro', markersize=10, markeredgewidth=2, markeredgecolor='black', markerfacecolor='red')

# Kritik noktaları etiketle (daha büyük yazı boyutu)
plt.text(-7, 3.2, "-7", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(-3, -0.3, "-3", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(0, -0.3, "0", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(4, 3.2, "4", ha='center', color='r', fontweight='bold', fontsize=16)

# Dikey çizgiler
plt.plot([-7, -7], [0, 3], 'r-', linewidth=3)
plt.plot([4, 4], [0, 3], 'r-', linewidth=3)

# Yatay kesikli çizgi
plt.plot(np.linspace(-7, -6, 100), np.ones(100) * 3, 'r--', linewidth=3)

# Daha belirgin ve net grid çizgileri
plt.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)

# Eksen ayarları ve etiketler
plt.title('m(-t) Sinyali', fontsize=20, fontweight='bold')
plt.xlabel('t', fontsize=18, fontweight='bold')
plt.ylabel('m(-t)', fontsize=18, fontweight='bold')

# Eksenler
plt.axhline(y=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)

# Grafik sınırları
plt.xlim(-8, 5)
plt.ylim(-0.5, 4)

# m(-t) başlığını ekle - daha büyük ve belirgin
plt.text(-1.5, 3.5, "m(-t)", color='r', fontsize=24, ha='center', fontweight='bold')

# Grafik kenarlarını düzenle
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()

# Şimdi m(3-t) için temiz bir grafik oluştur
plt.figure(figsize=(12, 8))
plt.rcParams.update({'font.size': 14})  # Yazı boyutunu artır

# Ana sinyal çizgisi
plt.plot(t, m_3_t, 'r-', linewidth=3.5)  # Çizgi kalınlığını artır

# İşaretli önemli noktalar: m(3-t) için 7, 3, 0, -4 noktaları kritik
plt.plot([7, 3, 0, -4], [3, 0, 0, 3], 'ro', markersize=10, markeredgewidth=2, markeredgecolor='black', markerfacecolor='red')

# Kritik noktaları etiketle
plt.text(7, 3.2, "7", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(3, -0.3, "3", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(0, -0.3, "0", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(-4, 3.2, "-4", ha='center', color='r', fontweight='bold', fontsize=16)

# Dikey çizgiler
plt.plot([7, 7], [0, 3], 'r-', linewidth=3)
plt.plot([-4, -4], [0, 3], 'r-', linewidth=3)

# Yatay kesikli çizgi
plt.plot(np.linspace(7, 6, 100), np.ones(100) * 3, 'r--', linewidth=3)

# Daha belirgin ve net grid çizgileri
plt.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)

# Eksen ayarları ve etiketler
plt.title('m(3-t) Sinyali', fontsize=20, fontweight='bold')
plt.xlabel('t', fontsize=18, fontweight='bold')
plt.ylabel('m(3-t)', fontsize=18, fontweight='bold')

# Eksenler
plt.axhline(y=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)

# Grafik sınırları
plt.xlim(-5, 8)
plt.ylim(-0.5, 4)

# m(3-t) başlığını ekle - daha büyük ve belirgin
plt.text(1.5, 3.5, "m(3-t)", color='r', fontsize=24, ha='center', fontweight='bold')

# Grafik kenarlarını düzenle
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()

# m(t) için temiz bir GUI
plt.figure(figsize=(12, 8))
plt.rcParams.update({'font.size': 14})  # Yazı boyutunu artır

# Ana sinyal çizgisi
plt.plot(t, mt, 'r-', linewidth=3.5)  # Çizgi kalınlığını artır

# İşaretli önemli noktalar
plt.plot([-4, 0, 3, 7], [3, 0, 0, 3], 'ro', markersize=10, markeredgewidth=2, markeredgecolor='black', markerfacecolor='red')

# Kritik noktaları etiketle
plt.text(-4, 3.2, "-4", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(0, -0.3, "0", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(3, -0.3, "3", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(7, 3.2, "7", ha='center', color='r', fontweight='bold', fontsize=16)

# Dikey çizgiler
plt.plot([-4, -4], [0, 3], 'r-', linewidth=3)
plt.plot([7, 7], [0, 3], 'r-', linewidth=3)

# Yatay kesikli çizgi
plt.plot(np.linspace(-4, -3, 100), np.ones(100) * 3, 'r--', linewidth=3)

# Daha belirgin ve net grid çizgileri
plt.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)

# Eksen ayarları ve etiketler
plt.title('m(t) Sinyali', fontsize=20, fontweight='bold')
plt.xlabel('t', fontsize=18, fontweight='bold')
plt.ylabel('m(t)', fontsize=18, fontweight='bold')

# Eksenler
plt.axhline(y=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)

# Grafik sınırları
plt.xlim(-5, 8)
plt.ylim(-0.5, 4)

# m(t) başlığını ekle
plt.text(1.5, 3.5, "m(t)", color='r', fontsize=24, ha='center', fontweight='bold')

# Grafik kenarlarını düzenle
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()

# -m(t) için temiz bir GUI
plt.figure(figsize=(12, 8))
plt.rcParams.update({'font.size': 14})  # Yazı boyutunu artır

# Ana sinyal çizgisi
plt.plot(t, m_eksi_2t, 'r-', linewidth=3.5)  # Çizgi kalınlığını artır

# İşaretli önemli noktalar
# -m(t): t=-4 için m(t)=3, böylece -m(t)=-3
# t=0 için m(t)=0, böylece -m(t)=0
# t=3 için m(t)=0, böylece -m(t)=0
# t=7 için m(t)=3, böylece -m(t)=-3
plt.plot([-4, 0, 3, 7], [-3, 0, 0, -3], 'ro', markersize=10, markeredgewidth=2, markeredgecolor='black', markerfacecolor='red')

# Kritik noktaları etiketle
plt.text(-4, -3.2, "-4", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(0, 0.3, "0", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(3, 0.3, "3", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(7, -3.2, "7", ha='center', color='r', fontweight='bold', fontsize=16)

# Dikey çizgiler
plt.plot([-4, -4], [0, -3], 'r-', linewidth=3)
plt.plot([7, 7], [0, -3], 'r-', linewidth=3)

# Yatay kesikli çizgi
plt.plot(np.linspace(-4, -3, 100), np.ones(100) * -3, 'r--', linewidth=3)

# Daha belirgin ve net grid çizgileri
plt.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)

# Eksen ayarları ve etiketler
plt.title('-m(t) Sinyali', fontsize=20, fontweight='bold')
plt.xlabel('t', fontsize=18, fontweight='bold')
plt.ylabel('-m(t)', fontsize=18, fontweight='bold')

# Eksenler
plt.axhline(y=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)

# Grafik sınırları
plt.xlim(-5, 8)
plt.ylim(-4, 1)  # Y ekseni aralığı düzeltildi

# -m(t) başlığını ekle
plt.text(1.5, -1, "-m(t)", color='r', fontsize=24, ha='center', fontweight='bold')  # Başlık düzeltildi

# Grafik kenarlarını düzenle
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

# Mavi ok ile genliği göster
plt.annotate('Genlik = 3', xy=(0, -1.5), xytext=(1, -1.5), 
             arrowprops=dict(facecolor='blue', shrink=0.05, width=2),
             color='blue', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()

# -m(2t) için temiz bir GUI
plt.figure(figsize=(12, 8))
plt.rcParams.update({'font.size': 14})  # Yazı boyutunu artır

# Ana sinyal çizgisi
plt.plot(t, m_2t, 'r-', linewidth=3.5)  # Çizgi kalınlığını artır

# İşaretli önemli noktalar
# -m(2t): t=-2 için m(2t=-4)=3, böylece -m(2t=-4)=-3
# t=0 için m(2t=0)=0, böylece -m(2t=0)=0
# t=1.5 için m(2t=3)=0, böylece -m(2t=3)=0
# t=3.5 için m(2t=7)=3, böylece -m(2t=7)=-3
plt.plot([-2, 0, 1.5, 3.5], [-3, 0, 0, -3], 'ro', markersize=10, markeredgewidth=2, markeredgecolor='black', markerfacecolor='red')

# Kritik noktaları etiketle
plt.text(-2, -3.2, "-2", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(0, 0.3, "0", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(1.5, 0.3, "1.5", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(3.5, -3.2, "3.5", ha='center', color='r', fontweight='bold', fontsize=16)

# Dikey çizgiler
plt.plot([-2, -2], [0, -3], 'r-', linewidth=3)
plt.plot([3.5, 3.5], [0, -3], 'r-', linewidth=3)

# Yatay kesikli çizgi
plt.plot(np.linspace(-2, -1, 100), np.ones(100) * -3, 'r--', linewidth=3)  # Y değeri düzeltildi

# Daha belirgin ve net grid çizgileri
plt.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)

# Eksen ayarları ve etiketler
plt.title('-m(2t) Sinyali', fontsize=20, fontweight='bold')  # Başlık düzeltildi
plt.xlabel('t', fontsize=18, fontweight='bold')
plt.ylabel('-m(2t)', fontsize=18, fontweight='bold')  # Etiket düzeltildi

# Eksenler
plt.axhline(y=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)

# Grafik sınırları
plt.xlim(-3, 5)
plt.ylim(-4, 1)  # Y ekseni aralığı düzeltildi

# -m(2t) başlığını ekle
plt.text(1, -1, "-m(2t)", color='r', fontsize=24, ha='center', fontweight='bold')  # Başlık düzeltildi

# Grafik kenarlarını düzenle
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

# Mavi ok ile genliği göster
plt.annotate('Genlik = 3', xy=(0, -1.5), xytext=(1, -1.5), 
             arrowprops=dict(facecolor='blue', shrink=0.05, width=2),
             color='blue', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()

# -2m(2t) için temiz bir GUI
plt.figure(figsize=(12, 8))
plt.rcParams.update({'font.size': 14})  # Yazı boyutunu artır

# Ana sinyal çizgisi
plt.plot(t, m_eksi_2_2t, 'r-', linewidth=3.5)  # Çizgi kalınlığını artır

# İşaretli önemli noktalar
# -2m(2t): t=-2 için m(2t=-4)=3, böylece -2m(2t=-4)=-6
# t=0 için m(2t=0)=0, böylece -2m(2t=0)=0
# t=1.5 için m(2t=3)=0, böylece -2m(2t=3)=0
# t=3.5 için m(2t=7)=3, böylece -2m(2t=7)=-6
plt.plot([-2, 0, 1.5, 3.5], [-6, 0, 0, -6], 'ro', markersize=10, markeredgewidth=2, markeredgecolor='black', markerfacecolor='red')

# Kritik noktaları etiketle
plt.text(-2, -6.2, "-2", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(0, 0.3, "0", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(1.5, 0.3, "1.5", ha='center', color='r', fontweight='bold', fontsize=16)
plt.text(3.5, -6.2, "3.5", ha='center', color='r', fontweight='bold', fontsize=16)

# Dikey çizgiler
plt.plot([-2, -2], [0, -6], 'r-', linewidth=3)
plt.plot([3.5, 3.5], [0, -6], 'r-', linewidth=3)

# Yatay kesikli çizgi
plt.plot(np.linspace(-2, -1, 100), np.ones(100) * -6, 'r--', linewidth=3)

# Daha belirgin ve net grid çizgileri
plt.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)

# Eksen ayarları ve etiketler
plt.title('-2m(2t) Sinyali', fontsize=20, fontweight='bold')
plt.xlabel('t', fontsize=18, fontweight='bold')
plt.ylabel('-2m(2t)', fontsize=18, fontweight='bold')

# Eksenler
plt.axhline(y=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2.0, alpha=0.5)

# Grafik sınırları
plt.xlim(-3, 5)
plt.ylim(-7, 1)  # Y ekseni aralığı düzeltildi

# -2m(2t) başlığını ekle
plt.text(1, -1.5, "-2m(2t)", color='r', fontsize=24, ha='center', fontweight='bold')

# Grafik kenarlarını düzenle
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

# Mavi ok ile genliği göster
plt.annotate('Genlik = 6', xy=(0, -3), xytext=(1, -3), 
             arrowprops=dict(facecolor='blue', shrink=0.05, width=2),
             color='blue', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()
