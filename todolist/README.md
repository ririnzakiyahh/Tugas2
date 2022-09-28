Link aplikasi Heroku : https://ririnapp.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada
potongan kode tersebut pada elemen <form>?
csrf token berguna untuk membandingkan dua token yang ditemukan pada sisi user dan pada
sisi permintaan (request). Jika token tersebut tidak cocok maka permintaan pada form akan 
ditolak, sedangkan jika permintaan cocok maka form akan merespons OK.

Jika tidak terdapat potongan kode tersebut, akan terdapat beberapa route link yang bisa 
diakses oleh orang lain. Akun kita bisa saja terhapus diluar kontrol kita jika seseorang 
memiliki button ke href link tersebut.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator
seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat 
<form> secara manual.
Ya bisa. Form secara manual dapat kita buat dengan menggunakan method POST dan dengan
menggunakan csrf token. Lalu kita membuat tag table dan didalamnya terdapat tr yang 
digunakan untuk memberikan tag input beserta dengan type yang disesuaikan dengan kebutuhan. 
Setelah itu, akan dikembalikan ke fungsi yang memanggil form jika form disubmit.
Method request.POST.get(nama yg kita buat pada table) dapat digunakan untuk mengakses input.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form,
penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template
HTML.
Data yang diinput dapat diakses karena adanya penggunaan method request.POST.get(nama yg kita buat pada table).
Setalah itu, dengan menggunakan "Models".objects.create(nama = data input) sesuai dengan
nama yang kita buat di todolist/models.py. Lalu data akan tersimpan pada database django dan
diakses menggunakan "Models".objects.filter(user=request.user)--> menggunakan filter agar sesuai dengan user;
yang masuk kedalam context agar dapat ikut render ke html. Lalu object akan di for loop agar
bisa menampilkan data apa saja yang ingin ditampilkan dengan mengakses nama atributnya. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. saya membuat aplikasi bernama todolist dengan menjalankan perintah python manage.py startapp todolist
dan menambahkan aplikasi todolist ke dalam variabel INSTALLED_APPS pada settings.py.
2. membuat fungsi show_todolist dan menambahkan path('todolist/', include('todolist.urls')), 
yang ada pada urls.py di project_django
3. membuat class bernama Task pada models.py dan membuat field user, date, title, description,
dan is_finished.
4. membuat fungsi untuk login, logout, dan register pada views.py yang masing2 fungsi
terhubung dengan register.html dan login.html. Lalu menambahkan @login_required(login_url='/todolist/login/')
agar user harus selalu login dulu.
5. mengedit bagian todolist.html. agar nama user yang ditampilkan sesuai dengan username yang
dilogin maka menggunakan {{user.username}}. lalu membuat 2 button untuk logout dan tambah task dan
tabel untuk menampilkan data2 todolist.
6. membuat halaman baru yaitu todolist/add_todo untuk membuat form yang berisi task dan
description untuk todo yang ingin ditambahkan. data yang diisi akan dikirim ke fungsi
add_todo yang ada di views.py. 
7. melakukan routing terhadap fungsi views dengan membuat urls.py pada aplikasi todolist.
8. karena masih berada pada app yang sama, maka ketika melakukan push akan teromotasi terdeploy
ke heroku.
9. membuat 2 akun yang masing2 akun berisikan 3 dummy data

