import requests
from bs4 import BeautifulSoup


def scrape_imdb_movie_data(url):
    # Membuat header yang lebih lengkap
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Mengambil konten HTML dari URL dengan header yang ditentukan
    response = requests.get(url, headers=headers)

    # Memastikan request berhasil
    if response.status_code == 200:
        # Parsing HTML dengan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Judul film
        title = soup.find('div', class_='title_wrapper').find('h1').get_text().strip().split('\xa0')[0]

        # Rating IMDb
        rating = soup.find('span', itemprop='ratingValue').get_text()

        # Tahun
        year = soup.find('a', title='See more release dates').get_text().split()[2]

        # Bulan
        month = soup.find('a', title='See more release dates').get_text().split()[1]

        # Certificate
        certificate = soup.find('div', class_='subtext').find('meta').get('content')

        # Durasi film
        runtime = soup.find('time', itemprop='duration').get_text().strip()

        # Director/s
        directors = [director.get_text() for director in
                     soup.find_all('div', class_='credit_summary_item')[0].find_all('a')]

        # Stars
        stars = [star.get_text() for star in soup.find_all('div', class_='credit_summary_item')[2].find_all('a')]

        # Genre/s
        genres = [genre.get_text() for genre in soup.find('div', class_='subtext').find_all('a')[:-1]]

        # Filming Location (Tidak tersedia di IMDb, Anda mungkin perlu mencari sumber data yang lain)
        filming_location = "Tidak tersedia"

        # Budget (Tidak tersedia di IMDb, Anda mungkin perlu mencari sumber data yang lain)
        budget = "Tidak tersedia"

        # Income (Tidak tersedia di IMDb, Anda mungkin perlu mencari sumber data yang lain)
        income = "Tidak tersedia"

        # Country of Origin
        country_of_origin = soup.find('a', itemprop='url').get_text()

        # Menampilkan hasil
        print("Judul:", title)
        print("Rating IMDb:", rating)
        print("Tahun:", year)
        print("Bulan:", month)
        print("Certificate:", certificate)
        print("Durasi:", runtime)
        print("Direktor:", ', '.join(directors))
        print("Bintang:", ', '.join(stars))
        print("Genre:", ', '.join(genres))
        print("Lokasi Pengambilan Gambar:", filming_location)
        print("Anggaran:", budget)
        print("Pendapatan:", income)
        print("Negara Asal:", country_of_origin)
    else:
        print("Gagal mengambil data. Kode status:", response.status_code)


# List URL yang akan di-scrape
urls = [
    "https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1",
    "https://www.imdb.com/title/tt0068646/?ref_=chttp_t_2"
]

# Loop melalui setiap URL dan scraping data film
for url in urls:
    print("Scraping data dari:", url)
    scrape_imdb_movie_data(url)
    print()  # Untuk memberikan baris kosong antara setiap output
