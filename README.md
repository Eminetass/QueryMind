QueryMind

QueryMind, bir metin veritabanı üzerinde anlamsal arama yeteneklerini etkinleştirmek için tasarlanmış FastAPI tabanlı bir uygulamadır. Metin verilerinin yerleştirmelerini depolamak için bir vektör veritabanı olan Milvus'u kullanır ve arama sonuçlarına göre insan benzeri yanıtlar üretmek için OpenAI'nin dil modelini kullanır. Bu proje, vektör veritabanında depolanan ilgili içeriği sorgulayarak soruları yanıtlamayı ve bağlamsal olarak ilgili bilgilerle yanıt kalitesini artırmayı amaçlamaktadır.


İçindekiler
Proje Genel Bakışı
Özellikler
Kurulum
Yapılandırma
Kullanım
API Belgeleri
Proje Yapısı
Katkıda bulunmak
Lisans



Proje Genel Bakışı
QueryMind, kullanıcıların Milvus'ta depolanan ilgili metin yerleştirmeleriyle bağlamsal olarak zenginleştirilmiş sorular girmesine ve AI tarafından oluşturulan yanıtlar almasına olanak tanır. Proje aşağıdaki adımlarda çalışır:

Veri Hazırlama : Metin verilerini yükleyin ve bunları gömülü verilere dönüştürün.
Milvus'ta Depolama : Gömülü verileri Milvus vektör veritabanında saklayın.
Sorgu İşleme : Bir kullanıcı sorgusunu kabul edin, onu bir yerleştirmeye dönüştürün ve Milvus'tan ilgili içeriği alın.
LLM Üretimi : Alınan içeriğe dayalı bir yanıt üretmek için OpenAI'nin dil modelini kullanın.


Özellikler
Vektör Veritabanı Entegrasyonu : Milvus kullanarak metin yerleştirmelerini depolar ve geri alır.
Doğal Dil İşleme : İnsan benzeri yanıtlar sağlamak için OpenAI'nin GPT modelini kullanır.
FastAPI Arayüzü : Sistemle sorgu yapmak ve etkileşim kurmak için RESTful API'leri kullanıma sunar.
Docker Desteği : Milvus kurulumu için Docker Compose ile dağıtıma hazır.


Kurulum
Ön koşullar

Python 3.8+
Docker
Docker Compose
Milvus v2.4.13


Adımlar
Depoyu Klonlayın :git clone https://github.com/yourusername/QueryMind.git
cd QueryMind


Bağımlılıkları Kurun : Sanal ortam kullanılması önerilir.

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Docker Compose Kullanarak Milvus'u Kurun : Docker'ın çalıştığından emin olun, ardından Milvus'u başlatın:




Yapılandırma
Çevre Değişkenleri
.envKök dizinde bir dosya oluşturun ve aşağıdaki ortam değişkenlerini yapılandırın:

DATABASE_HOST=localhost
DATABASE_PORT=5432
AZURE_OPENAI_API_KEY=your_openai_api_key
AZURE_OPENAI_ENDPOINT=your_openai_endpoint
AZURE_OPENAI_LLM_MODEL=gpt-4
AZURE_OPENAI_EMBEDDING_MODEL=text-embedding-ada-002
settings.pyGerekirse uygun yapılandırmaya işaret edecek şekilde güncelleyin


Milvus Yapılandırması
Milvus yapılandırması milvus-standalone-docker-compose.yml. 19530 (Milvus) ve 9000 (MinIO) portlarının açık olduğundan ve diğer hizmetlerle çakışmadığından emin olun.


Veri Hazırlama : Metin verilerini yükleyin ve bunları gömülü verilere dönüştürün.
Milvus'ta Depolama : Gömülü verileri Milvus vektör veritabanında saklayın.
Sorgu İşleme : Bir kullanıcı sorgusunu kabul edin, onu bir yerleştirmeye dönüştürün ve Milvus'tan ilgili içeriği alın.
LLM Üretimi : Alınan içeriğe dayalı bir yanıt üretmek için OpenAI'nin dil modelini kullanın.
Özellikler
Vektör Veritabanı Entegrasyonu : Milvus kullanarak metin yerleştirmelerini depolar ve geri alır.
Doğal Dil İşleme : İnsan benzeri yanıtlar sağlamak için OpenAI'nin GPT modelini kullanır.
FastAPI Arayüzü : Sistemle sorgu yapmak ve etkileşim kurmak için RESTful API'leri kullanıma sunar.
Docker Desteği : Milvus kurulumu için Docker Compose ile dağıtıma hazır.


Depoyu Klonlayın :

git clone https://github.com/yourusername/QueryMind.git
cd QueryMind
Bağımlılıkları Kurun : Sanal ortam kullanılması önerilir.
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Docker Compose Kullanarak Milvus'u Kurun : Docker'ın çalıştığından emin olun, ardından Milvus'u başlatın:

docker-compose -f milvus-standalone-docker-compose.yml up -d
Yapılandırma
Çevre Değişkenleri
.envKök dizinde bir dosya oluşturun ve aşağıdaki ortam değişkenlerini yapılandırın:

DATABASE_HOST=localhost
DATABASE_PORT=5432
AZURE_OPENAI_API_KEY=your_openai_api_key
AZURE_OPENAI_ENDPOINT=your_openai_endpoint
AZURE_OPENAI_LLM_MODEL=gpt-4
AZURE_OPENAI_EMBEDDING_MODEL=text-embedding-ada-002
settings.pyGerekirse uygun yapılandırmaya işaret edecek şekilde güncelleyin .

Milvus Yapılandırması
Milvus yapılandırması milvus-standalone-docker-compose.yml. 19530 (Milvus) ve 9000 (MinIO) portlarının açık olduğundan ve diğer hizmetlerle çakışmadığından emin olun.

Kullanım
FastAPI Sunucusunu Başlatın :

uvicorn wsgi:app --host 127.0.0.1 --port 8080 --reload
Swagger Kullanıcı Arayüzüne Erişim : API dokümantasyonu ve test için Swagger kullanıcı arayüzüne erişmek üzere tarayıcınızda http://127.0.0.1 :8080 /docs adresini açın.

Metin Verilerini Yükle : Metin verilerinizi dosyaya yerleştirin data/AL.txt. Bu veriler sunucu başlatıldığında Milvus'ta işlenecek ve saklanacaktır.




API Belgeleri
Uç Noktalar
POST /query/- Sorgu Rotası

Açıklama : Bir sorgu dizesi kabul eder, Milvus'tan ilgili içeriği alır ve OpenAI kullanarak bir yanıt oluşturur.
Talep Gövdesi :
json

{
  "query": "string"
}
Cevap :
json

{
  "response": "Generated answer based on relevant context"
}


QueryMind/
├── api/
│   ├── routers/
│   │   └── QueryMind_router.py         
│   ├── services/
│   │   ├── milvus_service.py        
│   │   ├── llm_service.py            
│   │   └── log_service.py             
├── configs/
│   ├── settings.py                   
│   └── log_config.py                
├── data/
│   └── AL.txt                          
├── models/
│   └── models.py                      
├── .env                               
├── main.py                             
├── wsgi.py                             
└── milvus-standalone-docker-compose.yml 




Katkıda bulunmak
Katkılarınız memnuniyetle karşılanır! Lütfen standart GitHub iş akışını takip edin:

Depoyu çatallandırın.
Bir özellik dalı oluşturun ( git checkout -b feature/new-feature).
Değişikliklerinizi kaydedin ( git commit -am 'Add new feature').
Şubeye doğru itin ( git push origin feature/new-feature).
Bir Çekme İsteği açın.




Lisans
Bu proje MIT Lisansı altında lisanslanmıştır

