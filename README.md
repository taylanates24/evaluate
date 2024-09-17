
# mAP@50 Hesaplayıcı

Bu Python kodu, bir dizindeki birden fazla tespit (detection) dosyasını bir açıklama dosyasına (annotation file) karşı değerlendirir ve her tespit dosyasının mAP@50 (Mean Average Precision at IoU threshold 0.50) skorunu hesaplayıp sıralar.

## Gereksinimler

Bu kodu çalıştırabilmek için aşağıdaki kütüphanelere ihtiyacınız var:
- `os`: Dosya ve dizin işlemleri için kullanılır.
- `argparse`: Komut satırı argümanlarını işlemek için kullanılır.
- `eval_json`: Dışarıdan bir dosyada yer alan bir fonksiyondur. Bu fonksiyon, verilen açıklama dosyası (annotation) ve tespit dosyasına (detection) göre mAP@50 hesaplaması yapar.

> Not: `eval_json` fonksiyonunu kendiniz tanımlamalısınız veya import ettiğiniz dosyanın doğru olduğundan emin olmalısınız.

## Kodun Yapısı

Kod, aşağıdaki üç ana bölümden oluşur:
1. `evaluate_multiple_detections(ann_file, det_files)`: Bu fonksiyon, bir açıklama dosyası ve birden fazla tespit dosyasını alır. Her tespit dosyasının mAP@50 değerini hesaplar, sonuçları sıralar ve ekrana yazdırır.
2. `main()`: Bu fonksiyon, komut satırı argümanlarını işler ve dosya yollarını fonksiyonlara iletir.
3. `argparse`: Komut satırı üzerinden parametre olarak açıklama dosyasını ve tespit dosyalarının bulunduğu dizini belirtmenize olanak tanır.

## Kurulum

Bu projeyi kullanmak için şu adımları izleyin:

1. Bu projeyi bilgisayarınıza klonlayın veya indirin.
2. Gerekli Python paketlerini yüklemek için şu komutu çalıştırın:

    ```bash
    pip install -r requirements.txt
    ```

> `requirements.txt` dosyası eval_json fonksiyonunun bağlı olduğu paketleri içermelidir.

## Kullanım

Kodu çalıştırmak için komut satırından şu adımları izleyin:

1. Terminal veya komut satırını açın.
2. Aşağıdaki komutu girin:

    ```bash
    python your_script.py --ann_file <açıklama_dosyası_yolu> --det_dir <tespit_dizini_yolu>
    ```

### Örnek:

```bash
python your_script.py --ann_file instances_val.json --det_dir results
```

Burada:
- `--ann_file`: Açıklama dosyasının yolunu belirtir. Varsayılan olarak `instances_val.json` kullanılır.
- `--det_dir`: Tespit dosyalarının bulunduğu dizini belirtir. Varsayılan olarak `results` kullanılır.

Eğer bu argümanları belirtmezseniz, kod varsayılan değerleri kullanır.

## Çıktı

Kod çalıştırıldığında her bir tespit dosyası için hesaplanan **mAP@50** değerlerini şu şekilde ekrana yazdırır:

```
<tespit_dosyası_ismi>, mAP@50: <mAP50_değeri>
```

### Örnek Çıktı:

```
result1.json, mAP@50: 0.51234
result2.json, mAP@50: 0.45321
...
```

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.
