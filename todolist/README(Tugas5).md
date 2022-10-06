Link aplikasi Heroku: https://ririnapp.herokuapp.com/todolist/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan 
dari masing-masing style?
Inline CSS merupakan kode CSS yang ditulis langsung pada atribut elemen HTML. Internal
merupakan kode CSS yang ditulis di dalma tag <style> dan kode HTML dituliskan di bagian
atas (header) file HTML. Sedangkan untuk External CSS ditulis terpisah dengan kode HTML Eksternal
CSS ditulis di sebuah file khusus yang berekstensi .css.

# Inline CSS
  Kelebihan: berguna untuk memperbaiki kode dengan cepat, membantu untuk menguji dan melihat perubahan
  pada satu elemen, dan proses permintaan HTTP yang lebih kecil dan proses load website akan
  lebih cepat.
  Kekurangan: tidak efisien karena hanya bisa diterapkan pada satu elemen HTML.
 # Internal CSS
  Kelebihan: perubahan hanya berlaku pada satu halaman, tidak perlu melakukan upload beberapa file karena
  HTML dan CSS berada dalam satu file, dan Class dan ID bisa digunakan oleh internal stylesheet.
  Kekurangan: tidak efisien jika digunakan dalam beberapa file.
 # External CSS
  Kelebihan: ukuran file html akan menjadi lebih kecil dan struktur dari kode HTML jadi rapih
  Kekurangan: halaman akan berantakan ketika file CSS gagal dipanggil oleh file HTML. 
  
 ## Jelaskan tag HTML5 yang kamu ketahui.
  <h1> - <h6> : bisa dipakai untuk ehader
  <p> : untuk nulis teks
  <form> : untuk membuat form yang akan disubmit
  <img> : untuk import foto 
  <div> : sbg wadah atau tatakan untuk elemen yang akan dibuat didalamnya.
    
  ## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
   - "#" : untuk select id yang ingin ditambahkan pada sebuah komponen
   - "-" : untuk selector 
   - elemen selector yang biasa digunakan, seperti h1,h2,h3.
    
   ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    - Pertama, saya mengimport bootstrap pada setiap halaman HTML, yaitu pada login.html, register.html,
    add_todo.html, dan todolist.html. 
    - Selanjutnya saya mengkostumisasi template untuk halaman login, register, dan create-task
    dengan mengganti background, teks, dan menggunakan cards.
    - Setelah itu, saya mengkostumisasi template untuk halaman todolist dengan menggunakan cards pada
    masing-masing task todolist dan menerapakn hover effect pada cards.
    - Saya menambahkan pada seluruh halaman html agar menjadi responsive dengan menambahkan 
    <meta name="viewport" content="width=device-width, initial-scale=1">.
    
    
