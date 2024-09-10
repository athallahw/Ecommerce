Untuk tautan PWS belum ada karena ada masalah dari server,

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. saya instalasi, inisialisi, menyiapkan dependencies, konfigurasi, menjalankan server django
    b. membuat aplikasi main sebagai unit modular yang menjalankan tugas tugas spesifik nantinya
    c. melakukan routing URL agar aplikasi main dapat diakses melalui peramban web
    d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut.
        - nama produk dengan charfield
        - harga produk dengan decimalfield
        - deskripsi produk dengan textfield
        - kuantitas produk dengan positive interger field
    e. membuat fungsi def_main yang berisi penjelasan product pada views.py
    f. melakukan routing pada urls.py dengan main untuk memetakan views.py


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ![alt text](image.png)
    penjelasan alur kerja
    1. Pengguna meminta halaman: Pengguna mengetik alamat website di browser.
    2. Django mencari URL: Django mencari URL yang sesuai di file urls.py.
    3. Django menjalankan view: Django menjalankan fungsi view yang terkait dengan URL tersebut.
    4. View mengambil data: Jika diperlukan, view akan mengambil data dari database menggunakan model.
    5. View memilih template: View memilih template HTML yang sesuai untuk menampilkan data.
    6. Django merender template: Django mengisi template dengan data yang diambil dari database.
    7. Halaman ditampilkan: Browser menampilkan halaman HTML yang sudah jadi kepada pengguna.

Jelaskan fungsi git dalam pengembangan perangkat lunak!
Dalam pembuatan perangkat lunak, tentu saja banyak hal yang terjadi. mulai dari perkerjaan yang membutuhkan backup, pekerjaan tim, perlunya mengetahui riwayat perubahan kode, dan mungkin juga bereksperimen sehinga dibutuhkan branch-branch lain. Hal ini dapat dipenuhi oleh git sebagai sebuah sistem.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 
Django mengadopsi arsitektur MVT(Model View Template) yang mudah dipahami, selain itu django menggunakan bahasa python yang mudah dipahami. Django juga dilengkapi oleh ORM(Object Relational Mapper) yang membuat coding lebih cepat tanpa perlu menulis query SQL yang kompleks, admin interface, dan lain-lain.

Mengapa model pada Django disebut sebagai ORM
ORM(Object Relational Mapper) memungkinkan kita untuk berinteraksi dengan database dengan cara yang simple. Bayangkan sebuah buku alamat. Di dalam buku alamat, terdapat data seperti nama, alamat, nomor telepon, dan sebagainya. Setiap orang di buku alamat bisa dianggap sebagai sebuah "objek". Dalam konteks Django, model itu seperti buku alamat. Setiap model yang dibuat merepresentasikan sebuah "tabel" di dalam database.
Pada intinya =
    -Setiap model yang didefinisikan dalam Python (yang merupakan objek) akan dipetakan secara otomatis ke sebuah tabel dalam database.
    - Saat membuat objek baru, memperbarui, atau menghapus data, Django secara otomatis akan menerjemahkan tindakanmu menjadi query SQL yang sesuai dan menjalankannya pada database.
