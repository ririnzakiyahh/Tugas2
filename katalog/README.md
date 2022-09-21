Link aplikasi Heroku : https://ririnapp.herokuapp.com/katalog/

## 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya 
dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![messageImage_1663123482575](https://user-images.githubusercontent.com/103397457/190047042-74d920b7-931d-4a92-a33a-bb93ac2b4f6a.jpg)

Client akan memberikan sebuah request yang nantinya akan diterima oleh url (urls.py) dan akan dilanjutkan ke view (views.py) yang akan melakukan
pemrosesan terhadap permintaan yang masuk. Jika nanti terdapat proses yang membutuhkan database, maka akan memanggil query ke models yang nantinya
database akan mengembalikan hasilnya ke views. Jika permintaan sudah selesai diproses, maka hasilnya akan dipetakan ke templates (berkas html) yang akan 
diperlihatkan ke client.

## 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual envinronment kita gunakan agar kita tidak bertabrakan dengan versi lain yang ada pada komputer kita. Venv akan mengisolasi package dan dependecies
dari aplikasi. Jika kita tidak menggunakan env dalam membuat aplikasi web berbasis Django, maka update packages dan dependancies dari aplikasi otomatis
akan mengubah data pada local storage dan akan terjadinya perbedaan dari data2 tersebut.

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
### views.py
Pada bagian ini, views akan mengambil semua data yang ada di database. Selain itu juga menambahkan variabel seperti nama dan npm yang akan disimpan dalam
variabel context dan akan ikut di-render dengan memanggil function show_katalog sehingga dapat dimunculkan datanya pada halaman HTML.

### urls.py
Pada urls.py akan melakukan routing terhadap fungsi show_katalog sehingga halaman HTML dapat ditampilkan lewat browser. Pada bagian ini, saya mendaftarkan
path aplikasi katalog ke dalam urls.py yang ada pada folder project_django.

### katalog.html
Pada poin ini, saya menggunakan for loop untuk mengambil data2 pada database yang akan disimpan  kedalma variabel list_barang.

### deploy
Pada tahap ini, saya menyambungkan repo github saya ke heroku dan melakukan deploy. Diperlukan HEROKU_APP_NAME dan HEROKU_API_KEY di github secret. 
Hal ini bertujuan agar dapat terhubung secara langsung.

