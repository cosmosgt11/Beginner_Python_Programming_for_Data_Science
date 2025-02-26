# CONDA SANAL ORTAM YÖNETİCİSİ İLE
# Sanal ortamların listelenmesi:
# conda env list ---> komutu aşağıda terminal bölüme yazılır. Bu yüklenmiş olan sanal ortamları listeler.

# Sanal ortam oluşturma:
# conda create -n _vereceğinisim_ --> yeni sanal ortam oluşturur.

# Sanal ortam silme:
# conda remove -n _sileceğinisim_ --> ismini verdiğin sanal ortamı siler.

# Sanal ortamı active etme:
# conda activate _verdiğinisim_

# Sanal ortamı deactive etme:
# conda deactivate _verdiğinisim_

# yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install scipy pandas

# paket silme:
# conda remove _paketismi_

# Belirli bir versiyona göre paket yükleme (örn: numpy 1.20.2)
# conda install numpy=1.20.2

# Paket yükseltmek(upgrade) için:
# conda upgrade _paketismi_

# Tüm paketlerin yükseltilmesi:
# conda upgrade -all

# Yüklediğimiz kütüphaneleri başka bir yere aktarma
# conda env export > dosyaismi.yaml  --> .yaml file dosyası oluşturarak

# Oluşturulan dosyaları listelemek:
# dir

# dışarıdan aldığın bir .yaml dosyasını yüklemek:
# -n

# PİP SANAL ORTAM Yöneticisi İLE
# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme (örn: pandas):
# pip install pandas

# Paket yükleme versiyona göre (pandas 2.12.1 ):
# pip install pandas==2.12.1
