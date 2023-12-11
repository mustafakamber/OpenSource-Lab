import json
import requests

# API URL
api_url = "http://universities.hipolabs.com/search"

# Sorgu parametreleri
params = {
    "country": "turkey",
    "name": "istanbul"
}

# API'ye GET isteği gönderme
response = requests.get(api_url, params=params)

# İsteğin başarılı olup olmadığını kontrol etme
if response.status_code == 200:

    # JSON formatındaki cevabı çözme
    data = response.json()

    # Çıktıyı JSON formatında ekrana yazdırma
    formatted_data = json.dumps(data, indent=2, ensure_ascii=False)
    print(formatted_data)
    #Hata çıktısı
else:
    print("API'ye yapılan istek başarısız. HTTP Hata Kodu:", response.status_code)
    print("Hata Mesajı:", response.text)