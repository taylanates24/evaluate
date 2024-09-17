
# mAP50 Hesaplayıcı

Bu Python kodu, bir dizindeki birden fazla tespit (detection) dosyasını bir açıklama dosyasına (annotation file) karşı değerlendirir ve her tespit dosyasının mAP@50 (Mean Average Precision at IoU threshold 0.50) skorunu hesaplayıp sıralar.

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
    ya da,
   ```bash
    pip install pycocotools
    ```
> `requirements.txt` dosyası eval_json fonksiyonunun bağlı olduğu paketleri içermelidir.

## Kullanım

Kodu çalıştırmak için komut satırından şu adımları izleyin:

1. Terminal veya komut satırını açın.
2. Aşağıdaki komutu girin:

    ```bash
    python eval_list.py --ann_file <açıklama_dosyası_yolu> --det_dir <tespit_dizini_yolu>
    ```

### Örnek:

```bash
python eval_list.py --ann_file instances_val.json --det_dir results
```

Burada:
- `--ann_file`: Açıklama dosyasının yolunu belirtir. Varsayılan olarak `instances_val.json` kullanılır.
- `--det_dir`: Tespit dosyalarının bulunduğu dizini belirtir. Varsayılan olarak `results` kullanılır.

Eğer bu argümanları belirtmezseniz, kod varsayılan değerleri kullanır.

## Çıktı

Kod çalıştırıldığında result1.json ve result2.json adındaki dosyaları için hesaplanan **mAP@50** değerlerini şu şekilde ekrana yazdırır:

```
<tespit_dosyası_ismi>, mAP@50: <mAP50_değeri>
```

### Örnek Çıktı:

```
result1, mAP@50: 0.51234
result2, mAP@50: 0.45321
...
```

## COCO mAP@50 Hesaplayıcı

Aşağıdaki kod, COCO formatındaki bir açıklama dosyası ve bir tespit dosyası ile **mAP@50** değerini hesaplar. Bu değer, tespit (detection) doğruluğunu ölçmek için kullanılan önemli bir metriktir.

### Kodun Yapısı

1. `eval_json(ann_file, det_file)`: Bu fonksiyon, COCO kütüphanesini kullanarak bir açıklama dosyası ve tespit dosyasını alır ve mAP@50 skorunu hesaplar.
2. `main()`: Komut satırı argümanlarını işleyerek, ilgili dosyalarla `eval_json` fonksiyonunu çalıştırır.

### Kullanım

Kodu çalıştırmak için komut satırından şu adımları izleyin:

```bash
python eval.py --ann_file <açıklama_dosyası_yolu> --det_file <tespit_dosyası_yolu>
```

### Örnek:

```bash
python eval.py --ann_file instances_val.json --det_file results/result.json
```

Bu komut, `instances_val.json` açıklama dosyasını ve `results/result.json` tespit dosyasını kullanarak mAP@50 değerini hesaplayacaktır.

### Çıktı

Kod çalıştırıldığında ekrana şu formatta mAP@50 değerini yazdırır:

```
mAP@50: <mAP50_değeri>
```

### Örnek Çıktı:

```
mAP@50: 0.51234
```

Bu sonuç, tespit edilen nesnelerin doğruluk performansını gösterir.

## Tespit Dosyası Şablonu
Tespit dosyası, json dosya formatında olmalıdır. Tespit edilen her bir nesne bir python dictionary olmak üzere bütün tespitler bir liste içinde json formatında kaydedilmelidir. Örnek bir tespit dosyası şablonu şu şekildedir:
```
[
    {
        'image_id': 150,
        'category_id': 1,
        'bbox': [120.5, 135.4, 15.1, 20.2],
        'score': 0.78678989
    },
    {
        'image_id': 151,
        'category_id': 2,
        'bbox': [101.2, 105.5, 12.1, 15.7],
        'score': 0.63456732
    },
]
```

Her bir tespit nesnesini oluşturmak için kod örneği:
```
image_name = 150
label = 2
bbox = [101.2, 105.5, 12.1, 15.7]
score = 0.634567329384756

detection = {
    'image_id': image_name,
    'category_id': int(label),
    'bbox': list(bbox.astype('float64')),
    'score': float("{:.8f}".format(score.item()))
}
```
Örnek tespıt dosyası `example_detection.json` olarak oluşturuldu. 
