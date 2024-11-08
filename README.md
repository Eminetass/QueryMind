QueryMind
QueryMind, Milvus vektör veritabanının ve OpenAI'nin Büyük Dil Modelleri'nin (LLM) yeteneklerini kullanmak üzere tasarlanmış, yapay zeka destekli akıllı bir arama ve yanıt sistemidir. Proje, kullanıcıların büyük metin verilerinden içgörüler çıkarmasını, verimli vektör tabanlı aramalar gerçekleştirmesini ve gelişmiş derin öğrenme modelleri kullanarak doğru, bağlam farkında yanıtlar üretmesini sağlar.


İçindekiler :
Genel bakış ,
Özellikler ,
Proje Yapısı ,
Gereksinimler , 
Kurulum ,
Kullanım , 
API Uç Noktaları ,
Yapılandırma ,
Katkıda bulunmak ,


GENEL BAKIŞ

QueryMind, hızlı, ölçeklenebilir ve doğru yanıtlar sunmak için metin yerleştirmeleri ve vektör araması için makine öğrenimi tekniklerinden yararlanır. Verimli benzerlik araması için Milvus vektör veritabanını ve doğal dil yanıtları oluşturmak için OpenAI'nin GPT modellerini entegre eder. Bu çözüm, sohbet robotları, soru-cevap sistemleri ve kişiselleştirilmiş içerik dağıtımı gibi akıllı arama yetenekleri gerektiren uygulamalar için idealdir.

ÖZELLİKLER

Verimli Metin Gömme : Metni yüksek boyutlu gömmelere dönüştürmek için Transformer modellerini kullanır.
Milvus ile Vektör Arama : Milvus vektör veritabanında gömülü verileri depolar ve geri alır, böylece hızlı ve ölçeklenebilir benzerlik aramaları sağlar.
Doğal Dil Tepkileri : Tutarlı ve bağlamsal olarak doğru yanıtlar üretmek için OpenAI'nin GPT modellerini kullanır.
Kolay Entegrasyon : Diğer uygulamalara sorunsuz entegrasyon için RESTful API sağlar.
Esnek Yapılandırma : Özelleştirilebilir ayarlar için ortam değişkenlerini destekler.

PROJE YAPISI

QueryMind/
├── api/
│   ├── routers/
│   │   └── QueryMind_router.py
│   ├── services/
│   │   ├── llm_service.py
│   │   ├── milvus_service.py
│   │   └── log_service.py
├── models/
│   └── models.py
├── configs/
│   ├── settings.py
│   └── log_config.py
├── data/
│   └── AL.txt
├── tests/
│   ├── test_blog.py
│   ├── test_query.py
│   └── test_milvus.py
├── .env
├── requirements.txt
├── docker-compose.yml
├── main.py
└── README.md


GEREKSİNİMLER

Python 3.8+
Docker ve Docker Oluşturma
Milvus (Docker üzerinden yüklendi)
PostgreSQL (kullanıcı sorgularını kaydetmek için)
Anaconda (sanal ortam yönetimi için önerilir)

KURULUM

1. Depoyu Klonlayın
git clone https://github.com/your-username/QueryMind.git
cd QueryMind
2. Sanal Ortamı Kurun git clone https://github.com/your-username/QueryMind.git
cd QueryMind

3. Bağımlılıkları Yükleyin  git clone https://github.com/your-username/QueryMind.git
cd QueryMind

4. Ortam Değişkenlerini Yapılandırın
.env kök dizininde bir dosya oluşturun:
MILVUS_HOST=localhost
MILVUS_PORT=19530
DATABASE_URL=postgresql://username:password@localhost:5432/querymind_db
AZURE_OPENAI_API_KEY=your_openai_api_key
AZURE_OPENAI_LLM_MODEL=text-davinci-003

5. Milvus ve PostgreSQL Hizmetlerini Başlatın docker-compose up -d

6. Uygulamayı çalıştırın python main.py



KULLANIM

1.Swagger kullanıcı arayüzüne erişmek için http://127.0.0.1 :8080 /docs adresine gidin .

2. /querySorularınızı göndermek için uç noktayı kullanın .

3. Sistem, indekslenen içeriğe göre doğal dil yanıtı döndürecektir.




API UÇ NOKTALARI

POST /query/- Bir sorgu dizesini kabul eder, bir vektör araması gerçekleştirir ve bir yanıt üretir.
Talep Gövdesi :
json

Kodu kopyala
{
  "query": "Your question here"
}
Cevap :
json

Kodu kopyala
{
  "response": "Generated answer based on search results"
}


YAPILANDIRMA

Milvus Bağlantısı : milvus_service.pyOrtam değişkenleri kullanılarak tanımlanır.
LLM Yapılandırması.env : ve aracılığıyla yapılandırılmış OpenAI GPT modellerini kullanır settings.py.
Veritabanı Yapılandırması : PostgreSQL için kurulum .env.


Katkıda bulunmak
Katkılarınız memnuniyetle karşılanır! Lütfen şu adımları izleyin:

1. Projeyi çatallandırın.
2. Bir özellik dalı oluşturun ( git checkout -b feature-branch).
3. Değişikliklerinizi kaydedin ( git commit -m "Add new feature").
4. Şubeye doğru itin ( git push origin feature-branch).
5. Bir Çekme İsteği açın.



