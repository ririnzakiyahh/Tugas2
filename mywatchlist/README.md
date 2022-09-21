Link aplikasi Heroku : https://ririnapp.herokuapp.com/mywatchlist/html/

## 1.Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON (JavaScript Object Notation) biasanya digunakan untuk menyimpan dan mengirimkan data pada aplikasi web ataupun mobile. JSON merupakan format dalam bentuk JavaScript yang terdiri dari key dan value. JSON lebih cepat untuk pengaksesan dan mudah dibaca oleh mesin karena tidak seperti XML dan HTML yang menggunakan tag. 

XML (Extensice Markup Language) digunakan untuk menyimpan dan mengirimkan data pada aplikasi web ataupun mobile. Informasi pada XML dibungkus di dalam tag sehingga lebih mudah dibaca. Kita dapat mengerti informasi yang disampaikan dari data yang tertulis dengan membaca XML.

HTML (Hypertext Markup Language) merupakan sebuah bahasa yang digunakan untuk membuat halaman pada website dan aplikasi web. Isi dalam website terdiri dari berbagai kode yang tersusun struktur untuk membuat suatu website.

## 2.Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementsian sebuah platform agar mudah dalam melakukan pengiriman data. Agar suatu data dapat diterima dengan baik dan mudah dipahami, biasanya pengiriman data menggunakan format HTML, XML, atau JSON.

## 3.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat aplikasi mywatchlist dengan menjalankan perintah pythin manage.py startapp mywatchlist pada folder main. Lalu menambahkan aplikasi ke dalam installed_apps. Lalu yang terakhir mempersiapkan migrasi skema model ke dalam database Django lokal. 

2. Melakukan routing dengan menambahkan path('mywatchlist/', include('mywatchlist.urls')) ke dalam urls.py dan pada variabel urlpatterns yang ada pada folder projecr_django agar halaman HTML dapat ditampilkan lewat browser. 

3. Membuat model MyWatchList pada mywatchlist/models.py dengan field: watched_movie, movie_title, movie_rate, release_date, dan movie_review. Setelah itu melakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

## POSTMAN
<img width="1440" alt="Screen Shot 2022-09-21 at 23 59 06" src="https://user-images.githubusercontent.com/103397457/191586413-6b5f7402-bdf0-4be6-b756-e68ff92d6824.png">

<img width="1440" alt="Screen Shot 2022-09-22 at 00 01 56" src="https://user-images.githubusercontent.com/103397457/191586556-438a74dd-6a6b-45bb-830f-39542d0c886d.png">

<img width="1440" alt="Screen Shot 2022-09-22 at 00 00 13" src="https://user-images.githubusercontent.com/103397457/191586568-46c2578a-5524-4591-8be4-3cd12e9e9c52.png">