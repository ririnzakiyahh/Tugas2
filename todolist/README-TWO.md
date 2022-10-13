Link aplikasi Heroku : https://ririnapp.herokuapp.com/todolist/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
### Synchronus Web Communication
Komunikasi web yang sifatnya sinkronus, setiap ada event atau permintaan request dari user ke server maka user akan menunggu respon dari server untuk mengenerate request. misalnya user click trus dia wait kemudian akan refresh

### Asynchronus Web Communication
Digunakan AJAX (async javasript and xml)
Komunikasi web yang sifatnya asyncronus dan parsial. Misalnya ingin ubah data di baris kelima kemudian server mengenerate dan mengirimkan partial page saja jadi tidak melakukan refresh secara keseluruhan. Jadi tetap bisa berinteraksi ketika loading data. User dapat berinteraksi tanpa perlu untuk menunggu respon

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming merupakan  paradigma pemrograman di mana aliran program ditentukan oleh peristiwa seperti tindakan pengguna (klik mouse, penekanan tombol), output sensor, atau pesan yang lewat dari program atau utas lain. Contoh penerapannya pada tugas ini yaitu pembuat tombol create. Ketika di click, dia akan menjalankan fungsi yg ditetapkan untuk membuat suatu task. 

## Jelaskan penerapan asynchronous programming pada AJAX.
Akan terjadi sebuah event seperti tombol create task ada tugas 6 ini. Ketika terjadi sebuah event, maka fungsionalitas AJAX akan dijalankan. AJAX dilakukan untuk mengambil data dan menangani sebuah response dalam bentuk JSON. Pada tugas 6 ini, ketika kita mencet tombol create maka akan dilakukan AJAX POST untuk mengirim data ke server yang nantinya akan diolah. Data yang ditangkap akan dikirimkan ke server tanpa melalui browser reload sehingga memberikan pengalaman browsing lebih baik. Disini menggunakan JQUERY jadi hanya perlu menambahkan library JQUERY pada todolist.html sehingga response handling dapat dilakukan secara langsung dengan memanggil function.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
AJAX GET
1. Pertama-tama membuat fungsi baru pada views.py yaitu show_json yang bakal digunain buat ngembaliin seluruh data task dalam bentuk JSON dan memetakannya dengan routing /todolist/json di urls.py
2. Membuat function untuk get data dengan menggunakan ajax pada todolist.html. AJAX GET akan terpanggil untuk mendapatkan task dalam bentuk JSON.

AJAX POST
1. Buat button untuk create task dan ubah link pemetaannya agar dapat memunculkan modal ketika tombol dipencet
2 Membuat function baru pada views.py untuk menambahkan task dan melakukan routing pada urls.py.
3. Membuat function untuk post data dengan menggunakan ajax pada todolist.hmtl untuk mengirim data ke server dan diproses. Akan dilakukan pemanggilan callback function dari AJAX POST dan menutup modal ketika berhasil membuat task baru. 
4. Terdapat async programming pada function agar taskn akan terupdate tanpa reload website. 
