# Web-Scrabing-With-BS4
Requests ve BeautifulSoup modülleri ile webscrabing işlemi

# Uygulama
- Uygulamada örnek amaçlı elektronik sigara satan bir web sitesini kazıdım.
- Uygulamada basit mantıkla yapılmış bir scroll özelliğide bulunuyor. Benim kazıdığım web sitenin sayfa sayısı az olduğu için direk sayfa sayısını elimle girebildim. Ancak kazıdığınız sitenin sayfa sayısı eğer fazla ise(YANİ SAYFA SAYISININ SONUNU GÖREMİYORSANIZ VS.), sitenin sayfa sayılarının bulunduğu bölümü kazıyıp veriyi çektikten sonra çektiğiniz veriyi integer değere çevirip benim yaptığım işlemin aynısını yapabilirsiniz.
- Uygulamanın işlevi requests modülü ile siteye bağlanıp bs4 modülü ile html verilerini ayrıştırıyor, ardından ayrıştırılan veriler içerisinden ürün isimlerini, fiyatlarını ve linklerini alıyor.
- Pandas modülü yardımıyla bir excel dosyası oluşturup o dosya içerisine çektiğimiz verileri uygun başlıklar altına kaydediyor.
