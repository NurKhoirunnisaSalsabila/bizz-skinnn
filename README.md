# TUGAS PBP Nur Khoirunnisa Salsabila

## Link Menuju Web PWS: http://nur-khoirunnisa-bizzskinnn.pbp.cs.ui.ac.id/


Nama: Nur Khoirunnisa Salsabila

NPM: 2306165534

Kelas: PBP A

<details>
  <summary>TUGAS 2</summary>
 
 # **TUGAS 2**

Link Menuju Web PWS: http://nur-khoirunnisa-bizzskinnn.pbp.cs.ui.ac.id/

Nama: Nur Khoirunnisa Salsabila

NPM: 2306165534

Kelas: PBP A
  

### **No.1 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Proses Pembuatan Proyek Django dan Inisiasi Proyek Django
1. Membuat direktori baru dengan nama ```happy-skin``` pada dekstop.
2. Membuka folder happy-skin dalam VSCode, kemudian membuka terminal shell (unix) atau git bash.
3. Buat virtual environment dengan menjalankan _command_ berikut:
 
   ```python -m venv env```
4. Mengaktifkan atau menyalakan virtual environment Python baru dengan _command_:
   
   ```env\Scripts\activate```
5. Mempersiapkan _Dependencies_ dengan cara membuat ```requirements.txt``` pada direktori ```happy-skin``` kemudian menambahkan isi _dependencies_
  ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
  ```
6. Lanjutkan dengan melakukan instalasi ```requirements``` dengan _command_ berikut:

   ```pip install -r requirements.txt```
7. Membuat Proyek Django dengan nama ```happy_skin``` dengan _command_ berikut:

   ```django-admin startproject happy_skin .```
8. Menambahkan string ```ALLOWED_HOSTS = ["localhost", "127.0.0.1"]``` pada ```ALLOWED_HOSTS``` di
    ```settings.py```
9. Membuat aplikasi ```main``` dengan _command_:
    ```python manage.py startapp main```
10. Menambahkan nama aplikasi ke ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```happy-skin```
11. Me-_routing_ url pada file ```urls.py``` di direktori ```happy-skin``` sehingga isi file ```urls.py``` sekarang menjadi:
    ```
    from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
12. Mengubah models.py menjadi:
     ```
    from django.db import models

    class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    ```
13. Melakukan migrasi dengan command:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
14. Membuat direktori templates dan template ``html`` untuk laman ``main``:
    ```
      <h1>{{ app_name }} Happy Skin </h1>
      <h5>Name: </h5>
      <p>{{ name }}<p>
      <h5>NPM: </h5>
      <p>{{ npm }}<p>  
      <h5>Class: </h5>
      <p>{{ class }}<p>
    ```
15. Menambahkan fungsi untuk me-_render_ laman main pada file ``views.py`` di direktori ``main``:
    ```
      from django.shortcuts import render

      def show_main(request):
          context = {
              'app name': 'Happy Skin',
              'name': 'Nur Khoirunnisa Salsabila',
              'npm' : '2306165534',
              'class': 'PBP A'
          }

          return render(request, "main.html", context)
    ```
16. Melakukan _routing_ pada aplikasi ``main`` pada file ``urls.py`` di direktori ``main``:
    ```
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
17. Mencoba menjalankan aplikasi pada _localhost_ dengan _command_:
    ```python manage.py runserver```
18. Membuat repository GitHub baru dengan nama ```icha-ecommerce``` dan visibilitas publik.
19. Menginisiasi direktori lokal ```happy-skin``` sebagai repositori Git
20. Menambahkan berkas ``.gitignore`` dan mengisinya dengan teks berikut:

```
  # Django
  *.log
  *.pot
  *.pyc
  __pycache__
  db.sqlite3
  media
  
  # Backup files
  *.bak
  
  # If you are using PyCharm
  # User-specific stuff
  .idea/**/workspace.xml
  .idea/**/tasks.xml
  .idea/**/usage.statistics.xml
  .idea/**/dictionaries
  .idea/**/shelf
  
  # AWS User-specific
  .idea/**/aws.xml
  
  # Generated files
  .idea/**/contentModel.xml
  .DS_Store
  
  # Sensitive or high-churn files
  .idea/**/dataSources/
  .idea/**/dataSources.ids
  .idea/**/dataSources.local.xml
  .idea/**/sqlDataSources.xml
  .idea/**/dynamic.xml
  .idea/**/uiDesigner.xml
  .idea/**/dbnavigator.xml
  
  # Gradle
  .idea/**/gradle.xml
  .idea/**/libraries
  
  # File-based project format
  *.iws
  
  # IntelliJ
  out/
  
  # JIRA plugin
  atlassian-ide-plugin.xml
  
  # Python
  *.py[cod]
  *$py.class
  
  # Distribution / packaging
  .Python build/
  develop-eggs/
  dist/
  downloads/
  eggs/
  .eggs/
  lib/
  lib64/
  parts/
  sdist/
  var/
  wheels/
  *.egg-info/
  .installed.cfg
  *.egg
  *.manifest
  *.spec
  
  # Installer logs
  pip-log.txt
  pip-delete-this-directory.txt
  
  # Unit test / coverage reports
  htmlcov/
  .tox/
  .coverage
  .coverage.*
  .cache
  .pytest_cache/
  nosetests.xml
  coverage.xml
  *.cover
  .hypothesis/
  
  # Jupyter Notebook
  .ipynb_checkpoints
  
  # pyenv
  .python-version
  
  # celery
  celerybeat-schedule.*
  
  # SageMath parsed files
  *.sage.py
  
  # Environments
  .env
  .venv
  env/
  venv/
  ENV/
  env.bak/
  venv.bak/
  
  # mkdocs documentation
  /site
  
  # mypy
  .mypy_cache/
  
  # Sublime Text
  *.tmlanguage.cache
  *.tmPreferences.cache
  *.stTheme.cache
  *.sublime-workspace
  *.sublime-project
  
  # sftp configuration file
  sftp-config.json
  
  # Package control specific files Package
  Control.last-run
  Control.ca-list
  Control.ca-bundle
  Control.system-ca-bundle
  GitHub.sublime-settings
  
  # Visual Studio Code
  .vscode/*
  !.vscode/settings.json
  !.vscode/tasks.json
  !.vscode/launch.json
  !.vscode/extensions.json
  .history
```
21. Melakukan ``add``, ``commit``, dan ``push`` dari direktori repositori lokal.
22. Mengakses halaman PWS dan membuat proyek baru dengan menekan tombol ```Create New Project```. Kemudian, isi ``Project Name`` dengan ``bizzskinnn``, lalu tekan ``Create New Project`` yang ada di bawahnya.
23. Menambahkan URL _deployment_ PWS pada file ``settings.py`` dan bagian ``ALLOWED_HOSTS`` sehingga menjadi:
    ```ALLOWED_HOSTS = ["localhost", "127.0.0.1", "nur-khoirunnisa-bizzskinnn.pbp.cs.ui.ac.id"]```
24. Menjalankan 3 perintah ini untuk push ke PWS:
    ```
    git remote add pws http://pbp.cs.ui.ac.id/nur.khoirunnisa/bizzskinnn
    git branch -M master
    git push pws master
    ```

### **No. 2 Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ``urls.py``, ``views.py``, ``models.py``, dan berkas ``html``.**
![Untitled](https://github.com/user-attachments/assets/2ae76eab-89fe-4ce8-9b79-954e93050457)



### **No. 3 Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git adalah alat yang membantu pengembang perangkat lunak mengelola dan melacak perubahan kode secara efisien. Dalam sebuah tim, Git memungkinkan setiap anggota untuk bekerja secara mandiri pada berbagai bagian proyek tanpa saling mengganggu. Dengan sistem ini, setiap perubahan yang dilakukan akan tersimpan dalam catatan yang jelas, sehingga memudahkan untuk kembali ke versi sebelumnya jika diperlukan. Git juga mendukung pengembangan paralel dengan fitur _branching_, yang memungkinkan pengembangan fitur baru secara terpisah sebelum digabungkan kembali ke proyek utama (_merge_). Git juga sering digunakan bersama dengan alat CI/CD (_Continuous Integration_/_Continuous Deployment_) untuk mengotomatisasi pengujian dan penyebaran kode. Setiap kali kode di-_commit_, CI/CD dapat otomatis menjalankan tes dan menyebarkan versi terbaru aplikasi ke server.
Kemudian, jika terjadi kesalahan atau _bug_ Git memungkinkan pengembang untuk kembali ke versi sebelumnya dari kode yang diketahui berfungsi dengan baik, sehingga dapat mengurangi risiko kehilangan kode atau waktu ketika menghadapi masalah. Lalu, Git adalah sistem kontrol versi terdistribusi, artinya setiap pengembang memiliki salinan lengkap dari seluruh riwayat proyek. Pada Git, setiap perubahan pada kode disertai dengan pesan _commit_ yang mendokumentasikan apa yang telah dilakukan, sehingga memudahkan untuk melacak histori pengembangan proyek dan memahami alasan di balik perubahan tertentu.

### **No. 4 Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Menurut saya mengapa _framework_ Django yang dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah karena pertama Django punya banyak fitur _built-in _yang siap pakai ('_batteries included_'), sehingga memungkinkan para pemula untuk langsung fokus pada pengembangan aplikasi tanpa perlu menghabiskan banyak waktu untuk mengatur hal-hal dasar. Kedua, Django dikenal memiliki dokumentasi yang sangat lengkap dan mudah dipahami, sehingga akan sangat membantu pemula yang sedang belajar karena mereka bisa dengan cepat menemukan panduan atau contoh penggunaan fitur-fitur yang ada. Ketiga, Django punya pola arsitektur MVT (_Model-View-Template_) yang membantu pemula memahami konsep dasar dalam pengembangan aplikasi web. Keempat, Django digunakan oleh banyak perusahaan besar dan proyek _open-source_, yang berarti belajar Django memberi pemula pengalaman langsung dengan teknologi yang relevan di industri. Kelima, Django memiliki komunitas yang besar dan aktif, sehingga memudahkan pemula untuk mendapatkan bantuan, menemukan tutorial, atau mengakses berbagai pustaka tambahan yang bisa mempercepat proses belajar.

### **No. 5 Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM (_Object-Relational Mapping_) karena Django menggunakan teknik pemetaan objek relasional untuk menghubungkan antara tabel dalam basis data relasional (seperti MySQL, PostgreSQL, SQLite, dll.) dengan objek-objek dalam bahasa pemrograman Python. ORM memungkinkan pengembang untuk bekerja dengan data menggunakan objek Python daripada menulis query SQL secara langsung. Sederhananya, ORM Django hanyalah cara untuk membuat SQL secara _pythonic_ untuk mengambil dan memanipulasi data dari database. Kemudian mendapatkan hasil dengan gaya pemrograman Python yang mudah dipahami. 

</details>

<details>
  <summary>TUGAS 3</summary>

# **TUGAS 3**

Link Menuju Web PWS: http://nur-khoirunnisa-bizzskinnn.pbp.cs.ui.ac.id/

Nama: Nur Khoirunnisa Salsabila

NPM: 2306165534

Kelas: PBP A

### **1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery sangat penting dalam pengembangan platform, terutama yang berbasis web atau aplikasi. Data tidak hanya disimpan, tetapi juga perlu dikirim dan diterima antara server dan client (baik itu browser maupun aplikasi). Sebagai contoh, ketika user melakukan request untuk melihat produk, server akan mengirimkan data produk tersebut ke client untuk ditampilkan. Tanpa data delivery yang efisien, interaksi antara user dan platform akan terganggu, yang dapat berdampak buruk pada pengalaman pengguna.

Data tidak hanya disajikan secara visual dalam bentuk HTML, tetapi juga perlu diantarkan (dikirim dan diterima) dalam format yang sesuai. Pada platform modern, JSON dan XML menjadi format yang umum digunakan untuk mengirim data dalam bentuk yang mudah dipahami oleh berbagai aplikasi dan sistem, terutama selama interaksi antara client dan server.

Kaitan data delivery dalam pengembangan platform dapat dijelaskan sebagai berikut:

* Dalam pengembangan platform seperti aplikasi e-commerce, setiap kali user menambahkan produk ke keranjang atau mengecek daftar produk, platform harus mengirimkan data tersebut dari server ke client (browser atau aplikasi mobile).
* Data ini bisa dikirim dalam bentuk JSON atau XML, tergantung kebutuhan, untuk menyampaikan informasi seperti harga, deskripsi, atau rating produk.
* Penggunaan XML dan JSON dalam proses data delivery memastikan bahwa data yang dikirimkan dari server dapat diinterpretasikan dengan benar oleh client, begitu juga sebaliknya.

Oleh karena itu, hubungan data delivery dengan pengembangan platform adalah memastikan informasi dapat disampaikan dengan tepat dari satu bagian sistem ke bagian lainnya (misalnya dari server ke browser) menggunakan format data yang efisien seperti JSON atau XML.


### **2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

| Kriteria         | XML (Extensible Markup Language)                                   | JSON (JavaScript Object Notation)                                |
|------------------|--------------------------------------------------------------------|-----------------------------------------------------------------|
| Struktur         | Berbasis tag mirip dengan HTML, lebih verbose karena setiap data ditutup dengan tag. | Berbasis key-value pairs, lebih sederhana dan mudah dibaca manusia. |
| Ukuran           | Lebih besar karena adanya penutup tag untuk setiap elemen.         | Lebih kecil dan ringan dibandingkan XML karena tidak ada tag penutup. |
| Kecepatan Parsing| Parsing cenderung lebih lambat karena struktur yang lebih kompleks. | Parsing lebih cepat, terutama dalam aplikasi berbasis JavaScript. |
| Dukungan         | Banyak digunakan di sistem enterprise dan lama.                    | Lebih banyak digunakan di aplikasi modern dan web service.        |
| Ekstensi         | Mendukung skema yang lebih kompleks, dapat menampung data terstruktur yang lebih dalam. | Terbatas pada data yang lebih sederhana. Namun, mudah dikombinasikan dengan format lain. |
| Penggunaan       | Cocok untuk dokumen besar dan data yang memerlukan validasi skema. | Lebih cocok untuk data ringan dan komunikasi antara client-server. |
| Keamanan         | Cenderung lebih rentan terhadap serangan XML External Entity (XXE) dan parsing lebih rumit. | Lebih aman secara default, namun masih perlu validasi untuk memastikan keamanan. |
| Populer untuk    | Aplikasi legacy dan enterprise systems.                            | Aplikasi web modern, API, dan mobile apps.                        |

### Kesimpulan: Mana yang Lebih Baik antara XML dan JSON?

Sebenarnya hal ini kembali lagi ke kebutuhan masing-masing.

   * Jika bekerja dengan aplikasi web modern, terutama yang melibatkan banyak interaksi client-server dan JavaScript, JSON adalah opsi yang lebih baik dibandingkan XML. Mengapa? Hal ini dikarenakan JSON lebih ringkas, cepat, dan mudah  digunakan di banyak platform.
   * Namun, jika perlu mengelola dokumen yang sangat terstruktur dan kompleks dengan banyak validasi skema, XML mungkin lebih cocok karena XML mendukung lebih banyak fitur yang dibutuhkan untuk dokumen yang lebih rumit.
   * Akan tetapi, JSON lebih baik dalam hal kecepatan, kesederhanaan, dan efisiensi, sehingga bisa disimpulkan JSON lebih baik dibandingkan XML.

### Mengapa JSON Lebih Populer Dibandingkan XML?

   * JSON memiliki sintaks yang lebih sederhana dan lebih ringan dibandingkan dengan format lain seperti XML. Hal ini membuatnya lebih efisien.
   * JSON lebih mudah dibaca sehingga sangat membantu saat debugging
   * Hampir semua bahasa pemrograman modern memiliki dukungan bawaan untuk parsing dan menghasilkan JSON.
   * JSON dapat di-parse dengan mudah oleh JavaScript, bahasa yang digunakan di mayoritas webapp.


### **3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

Method `is_valid()` di Django digunakan untuk memastikan data yang diinput oleh pengguna sesuai dengan aturan yang sudah ditetapkan di form. Kalau data yang dimasukkan benar/data yang dimasukkan valid, method ini akan mengembalikan `True`, dan kita bisa lanjut menyimpan datanya ke database. Tapi kalau ada yang salah/data tidak valid, Django akan kasih pesan error yang relevan supaya pengguna tahu apa yang perlu diperbaiki. Fungsi ini sangat penting supaya data yang masuk selalu sesuai (integritas data terjamin) dan memastikan bahwa data yang masuk ke database sesuai dengan aturan yang telah ditentukan, sehingga pengembang tidak perlu menulis validasi secara manual untuk setiap input pengguna. Jadi, semuanya lebih aman dan terkontrol.

### **4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

`csrf_token` adalah nilai unik yang dihasilkan secara acak dan disematkan ke dalam form sebagai lapisan keamanan tambahan. Token ini melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery) dengan memastikan bahwa setiap permintaan yang dikirim berasal dari pengguna yang sah, bukan dari penyerang yang mencoba mengeksploitasi sesi pengguna yang telah diautentikasi. Ketika server menerima permintaan, token yang dikirim akan diperiksa apakah sesuai dengan token yang disimpan di sesi pengguna. Jika token tidak valid atau tidak ada, permintaan akan ditolak, sehingga mencegah tindakan berbahaya yang mungkin dilakukan oleh penyerang. Tanpa `csrf_token`, seorang penyerang bisa memanfaatkan sesi pengguna yang valid untuk menjalankan aksi yang tidak diinginkan, seperti mengubah data atau melakukan transaksi tanpa sepengetahuan pengguna, dengan memanfaatkan link jahat.

### **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. **Membuat Forms**
   * Membuat file ``forms.py`` pada direktori ``main`` 
   * Tambahkan fields dari ``forms`` yang berasal dari class ``Product`` yang telah dideklarasikan di models.py.
   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ["name", "price", "description", "skin_type", "stock", "rating"]
  
2. Membuat method/fungsi baru di ``views.py`` dengan nama ``create_product``untuk menambah entri database pada direktori ``main``
   ```
   def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    else:
        print(form.errors)

    context = {'form': form}
    return render(request, "create_product.html", context)


  Fungsi ini nantinya akan merender tampilan dari form pada sebuah template HTML.
   
3. Membuat template HTML untuk ``create_product`` sebagai template untuk form yang akan dirender oleh fungsi ``create_product``
   ```
   {% extends 'base.html' %} 
   {% block content %}
   <h1>Add New Product</h1>
   
   <form method="POST">
     {% csrf_token %}
     <table>
       {{ form.as_table }}
       <tr>
         <td></td>
         <td>
           <input type="submit" value="Add Product" />
         </td>
       </tr>
     </table>
   </form>
   
   {% endblock %}
   

4. Menambahkan folder ``templates`` di direktori utama dan ``base.html`` sebagai basis dari laman-laman lain
   
5. Menambahkan lokasi folder ``templates`` tersebut ke ``settings.py`` di direktori ``happyskin``
   ```
   ...
   'DIRS': [BASE_DIR / 'templates'],
   ...

6. Mengimplementasikan database ke dalam laman utama ``main.html`` dan juga menjadi perpanjangan dari ``base.html`` di direktori utama
   ```
   ...
       <table>
            <tr>
                <th class="nama-produk">Nama Produk</th>
                <th class="harga-produk">Harga Produk</th>
                <th class="deskripsi-produk">Deskripsi Produk</th>
                <th class="tipe-kulit">Tipe Kulit</th>
                <th class="stok-produk">Stok Produk</th>
                <th class="rating-produk">Rating Produk</th>
            </tr>
            {% for product in products %}
            <tr>
                <td class="nama-produk">{{ product.name }}</td>
                <td class="harga-produk">{{ product.price }}</td>
                <td class="deskripsi-produk">{{ product.description }}</td>
                <td class="tipe-kulit">{{ product.skin_type }}</td>
                <td class="stok-produk">{{ product.stock }}</td>
                <td class="rating-produk">{{ product.rating }}</td>
            </tr>
            {% endfor %}
        </table>
        ...
   
7. Menambahkan Button pada ``main.html``
   ```
   <a href="{% url 'main:create_product' %}">
            <button>Tambah Produk Baru</button>
        </a>
  tombol pada halaman ``main.html`` nantinya akan mengarahkan pengguna ke halaman yang berisi form untuk menambahkan produk. 
  
8. Menambahkan Fungsi/Method Tampilan dalam Format XML, JSON, XML id, dan JSON id pada file di ``views.py`` pada direktori ``main``
   ```
   def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  Fungsi ini akan mengambil data dari database menggunakan serializer dan mengubahnya menjadi format XML atau JSON.
   
9. Merouting URL yang bersangkutan di file ``urls.py`` pada direktori ``main``
   ```
   urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
   ]
   
10. Menjalankan aplikasi pada localhost dengan command:
    ```
    pyhthon manage.py runserver

11. Membuka ``http://localhost:8000/`` di browser dan juga di POSTMAN 


## **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**

### Postman XML
![image](https://github.com/user-attachments/assets/93a6cd2b-8914-44a4-98d8-78a50ea878d9)
### Postman JSON
![image](https://github.com/user-attachments/assets/ac237e68-77c0-40f7-ac2d-98b492b7b623)
### Postman XML By ID
![image](https://github.com/user-attachments/assets/9faf96b0-0957-4ee1-a8ad-ada2f2667c3e)
### Postman JSON By ID
![image](https://github.com/user-attachments/assets/5ccd6173-73ba-408d-8a44-dc5d1b7c5ca6)



</details>


<details>
  <summary>TUGAS 4</summary>
 
 # **TUGAS 4**



---

## 1. **Perbedaan antara `HttpResponseRedirect()` dan `redirect()`**

* ``HttpResponseRedirect():``
  - Kelas yang digunakan untuk mengembalikan respons HTTP yang mengarahkan pengguna ke URL tertentu.
  - Membutuhkan URL sebagai argumen.
  - Penggunaan kelas ini memberikan kontrol lebih terhadap respons HTTP, terutama jika ada kebutuhan untuk menjalankan mekanisme tambahan sebelum mengirimkan respons. Dengan demikian, fungsinya lebih dari sekadar pengalihan halaman.
  - Pada fungsi ``login_user``, ``HttpResponseRedirect()`` digunakan karena saya ingin menambahkan cookie ke dalam respons sebelum mengembalikannya. Sehingga, respons dapat dimodifikasi terlebih dahulu sebelum dikirimkan kembali ke pengguna (dialihkan ke halaman ``show_main``), seperti terlihat dari cara kelas tersebut dipanggil dan disimpan dalam variabel response terlebih dahulu.
      ```python
      def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
              user = form.get_user()
              login(request, user)
              response = HttpResponseRedirect(reverse("main:show_main"))
              response.set_cookie('last_login', str(datetime.datetime.now()))
              return response
            ...
      ```

- ``redirect()``: 
  - Fungsi shortcut yang lebih fleksibel dibanding ``HttpResponseRedirect()``.
  - Bisa menerima URL, nama view, atau objek model sebagai argumen, dan Django akan mengatur detail pengarahannya secara otomatis. Dengan demikian dapat dikatakan sebagai fungsi di Django yang membantu routing menjadi lebih sederhana.
  - Pada fungsi ``register``, saya menggunakan ``redirect()`` karena tujuannya hanya untuk langsung mengarahkan pengguna ke halaman login setelah selesai mendaftar. Saya tidak perlu menentukan URL secara spesifik atau menambahkan mekanisme tambahan. Penggunaan ``redirect()`` membuat kode lebih sederhana dan mudah dibaca, karena hanya perlu melakukan pengalihan halaman tanpa fungsionalitas tambahan.
      ```python
      def register(request):
        form = UserCreationForm()
    
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
            ...
      ```

## 2. **Cara Kerja Penghubungan Model Product dengan User**

- Model `Product` memiliki field `user` yang merupakan `ForeignKey` ke model `User`. Artinya, setiap instance `Product` terkait dengan satu instance `User`.
- ForeignKey memungkinkan terjadinya hubungan banyak-ke-satu (many-to-one), yang artinya beberapa produk (Product) bisa dimiliki oleh satu pengguna (User).
- Django menyediakan mekanisme `on_delete=models.CASCADE`, yang berarti jika pengguna dihapus, semua produk terkait juga akan dihapus dari database.
  ```python
    import uuid
    from django.db import models
    from django.contrib.auth.models import User
    
    # Create your models here.
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
  ```

- Salah satu praktik terbaik dalam web e-commerce adalah menampilkan produk sesuai dengan pengguna yang sedang login (terpersonalisasi). Oleh karena itu, di bagian `view`, produk harus difilter agar hanya produk milik pengguna yang terautentikasi yang ditampilkan. Pada fungsi `show_main`, lakukan filter produk berdasarkan `request.user`.
- Ketika pengguna membuat produk baru, produk tersebut secara otomatis akan terhubung dengan pengguna yang sedang login, karena properti user telah ditambahkan ke instance produk sebelum disimpan.
    ```python
    @login_required(login_url='/login')
    def show_main(request):
        products = Product.objects.filter(user=request.user)
    ...
  ```
    ```python
    def create_product(request):
      form = ProductForm(request.POST or None)
  
      if form.is_valid() and request.method == "POST":
          product = form.save(commit=False)
          product.user = request.user
          product.save()
          return redirect('main:show_main')
  
      context = {'form': form}
      return render(request, "create_product.html", context)
  ```

## 3. **Perbedaan antara Authentication dan Authorization & Implementasi Authentication dan Authorization di Django**

- **Authentication**
  * Proses verifikasi identitas pengguna, biasanya melalui username dan password.
- **Authorization**
  * Proses menentukan hak akses pengguna setelah mereka terautentikasi, yaitu menentukan apa yang dapat dan tidak dapat dilakukan oleh pengguna.
- **Implementasi Authentication dan Authorization di Django**
  * Contoh alurnya: Setelah pengguna login (authentication), aplikasi menentukan apa yang bisa diakses pengguna tersebut (authorization).
  * Misalnya, saya pernah mendaftar ke BizzSkin dengan username Chacha. Proses authentication akan mengecek, 'apakah ini benar-benar akun Chacha?'. Lalu, authorization akan mempertanyakan, 'apakah username Chacha memiliki izin untuk mengakses halaman admin e-commerce atau mengedit data produk?'.
  * **Authentication:**
    Django menggunakan sistem autentikasi bawaan untuk memverifikasi kredensial pengguna.
    ```python
    from django.contrib.auth import authenticate, login
    
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
    ```
  * **Authorization:**
    Authorization di Django menggunakan decorators dan mixins untuk mengatur hak akses pengguna. Contoh menggunakan `@login_required` decorator:
    ```python
    from django.contrib.auth.decorators import login_required
    
     @login_required(login_url='/login')
     def show_main(request):
    ```

## 4. **Bagaimana Django Mengingat Pengguna yang Telah Login, Kegunaan lain dari cookies, dan apakah semua cookies aman digunakan?**

**Cara Django Mengingat Pengguna yang Telah Login**
- Django menggunakan **sessions** dan **cookies** untuk mengingat pengguna yang telah login.

  Penjelasan:
  Setelah pengguna berhasil login, Django menggunakan mekanisme sesi (session) untuk mengidentifikasi mereka. Data sesi sebenarnya disimpan di server, sedangkan browser pengguna hanya menyimpan session ID dalam bentuk cookie. Ketika pengguna membuat permintaan (request) ke server, browser akan mengirimkan session ID tersebut, dan Django akan mencocokkannya dengan informasi di server untuk mengidentifikasi pengguna yang sedang login. Proses ini dilakukan setiap kali pengguna mengakses halaman baru tanpa perlu login ulang. 
- Saat pengguna berhasil login, Django membuat sesi baru dan menyimpan ID sesi di dalam cookie pengguna.

  Penjelasan:
  Setelah login, Django mengirimkan cookie yang berisi session ID ke browser pengguna. Django kemudian menggunakan cookie ini untuk mengakses informasi sesi. Ketika pengguna membuka halaman lain di situs web, browser secara otomatis mengirimkan cookie tersebut dalam setiap request, memungkinkan Django untuk mengenali pengguna yang telah login.
- Setiap kali pengguna membuat permintaan baru, cookie ini dikirimkan kembali ke server, dan server menggunakan ID sesi untuk mengidentifikasi pengguna tersebut.

  Penjelasan:
  Defaultnya, Django mengingat pengguna selama sesi berjalan. Jika pengguna menutup browser atau durasi sesi habis, mereka harus login kembali. Namun, Django bisa dikonfigurasi untuk memperpanjang waktu login pengguna, misalnya dengan fitur "remember me" yang memperpanjang masa aktif sesi.
  

**Kegunaan Lain dari Cookies:**

Selain digunakan untuk mengingat pengguna yang telah login, cookies memiliki berbagai kegunaan lain, antara lain:

- **Menyimpan Preferensi Pengguna:** Cookies dapat digunakan untuk menyimpan preferensi pengguna seperti tema, bahasa, atau pengaturan tampilan lainnya.
- **Pelacakan dan Analitik:** Cookies sering digunakan untuk melacak aktivitas pengguna di situs web untuk tujuan analitik dan pemasaran. Cookies bisa digunakan untuk mengumpulkan data statistik tentang pengunjung, yang kemudian dianalisis untuk mengukur performa dan meningkatkan pengalaman pengguna di situs.
- **Keranjang Belanja:** Dalam aplikasi e-commerce, cookies dapat digunakan untuk menyimpan item yang ditambahkan ke keranjang belanja oleh pengguna.
- **Personalisasi Konten:** Cookies dapat digunakan untuk menyajikan konten yang dipersonalisasi berdasarkan aktivitas dan preferensi pengguna sebelumnya. Selain itu, third-party cookies sering digunakan oleh layanan iklan untuk menampilkan iklan yang dipersonalisasi berdasarkan perilaku pengguna di berbagai situs web. 
- **Otentikasi Sesi**: Cookies digunakan untuk menyimpan token sesi yang memungkinkan pengguna tetap login saat mereka menavigasi situs web.

**Apakah Semua Cookies Aman Digunakan?**

Tidak semua cookies aman digunakan, terutama jika tidak dikonfigurasi dengan benar. Ada beberapa risiko keamanan yang terkait dengan penggunaan cookies:

- XSS (Cross-Site Scripting): Jika situs web rentan terhadap serangan XSS, penyerang dapat menyuntikkan skrip berbahaya yang mencuri cookies pengguna.
- CSRF (Cross-Site Request Forgery): Cookies dapat digunakan dalam serangan CSRF di mana penyerang membuat permintaan berbahaya atas nama pengguna yang terautentikasi.
- Penyadapan Data: Jika cookies tidak dienkripsi dan dikirim melalui koneksi HTTP yang tidak aman, mereka dapat disadap oleh penyerang.
  
**Cara Mengamankan Cookies**
Django menyediakan beberapa pengaturan untuk membuat cookies lebih aman:

- HttpOnly: Mengatur cookie sebagai HttpOnly mencegah akses cookie melalui JavaScript, mengurangi risiko XSS.
  ``SESSION_COOKIE_HTTPONLY = True``
- Secure: Mengatur cookie sebagai Secure memastikan bahwa cookie hanya dikirim melalui koneksi HTTPS, mengurangi risiko penyadapan data.
  ``SESSION_COOKIE_SECURE = True``
- SameSite: Mengatur atribut SameSite pada cookie membantu mencegah serangan CSRF dengan membatasi pengiriman cookie ke permintaan lintas situs.
  ``SESSION_COOKIE_SAMESITE = 'Lax'``

*Kesimpulan:*
Cookies yang mengandung informasi sensitif, seperti session ID, sebaiknya diberi atribut HttpOnly, sehingga tidak bisa diakses oleh JavaScript dan mengurangi risiko serangan cross-site scripting (XSS). Selain itu, cookies yang dikirim melalui koneksi aman (HTTPS) harus memiliki atribut Secure, untuk memastikan cookies hanya dikirim melalui koneksi yang terenkripsi. Atribut SameSite juga penting, karena mencegah cookies dikirimkan dalam permintaan lintas situs, melindungi dari serangan cross-site request forgery (CSRF). Cookies pihak ketiga yang digunakan untuk iklan atau pelacakan bisa dianggap mengganggu privasi, dan beberapa browser kini memblokir cookies ini secara otomatis.

## 5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

**1. Membuat Fungsi dan Form Registrasi**
- Membuat fungsi `register` ke dalam `views.py` yang ada pada subdirektori `main`. Tujuannya untuk membuat formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
  ```python
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib import messages

  ...
  def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
  ...
  ```
- Membuat file `register.html` pada direktori `main/templates`.
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Register</title>
  {% endblock meta %}
  
  {% block content %}
  
  <div class="login">
    <h1>Register</h1>
  
    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td><input type="submit" name="submit" value="Daftar" /></td>
        </tr>
      </table>
    </form>
  
    {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>
  
  {% endblock content %}
  ```
- Melakukan routing untuk `register` di `urls.py` yang ada pada subdirektori `main`
  ```python
  from main.views import register

  urlpatterns = [
     ...
     path('register/', register, name='register'),
   ]
  ```

**2. Membuat Fungsi Login**
- Buat fungsi `login_user` di `views.py` yang ada pada subdirektori `main`.
- Tambahkan import `authenticate`, `login`, dan `AuthenticationForm` pada bagian paling atas.
  ```python
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  from django.contrib.auth import authenticate, login
  ...
  def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
  ...
  ```
  - Setelah berhasil login, set cookie `last_login.` dan fungsi `login_user` menjadi seperti berikut:
    ```python
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import authenticate, login
    import datetime
    
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    ```
- Membuat file `login.html` pada direktori `main/templates`.
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Login</title>
  {% endblock meta %}
  
  {% block content %}
  <div class="login">
    <h1>Login</h1>
  
    <form method="POST" action="">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
      </table>
    </form>
  
    {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
  </div>
  
  {% endblock content %}
  ```
-Melakukan routing untuk `login` di `urls.py` yang ada pada subdirektori `main`
  ```python
  from main.views import login_user

  urlpatterns = [
    ...
    path('login/', login_user, name='login'),
  ]
  ```

**3. Membuat Fungsi Logout**
- Buat fungsi `logout_user` di `views.py` yang ada pada subdirektori `main`.
- Tambahkan import `logout` pada bagian paling atas.
  ```python
  from django.contrib.auth import logout
  ...
  def logout_user(request):
    logout(request)
    return redirect('main:login')
  ```
- Menambahkan potongan kode berikut pada file `main.html` pada direktori `main/templates`.
  ```html
    ...
    <a href="{% url 'main:logout' %}">
      <button>Logout</button>
    </a>
    ...
  ```
-Melakukan routing untuk `logout` di `urls.py` yang ada pada subdirektori `main`
  ```python
  from main.views import logout_user

  urlpatterns = [
    ...
    path('logout/', logout_user, name='logout'),
  ]
  ```

**4. Merestriksi Akses Halaman Main**
- Menambahkan import decorator `login_required` pada bagian paling atas di `views.py` yang ada pada subdirektori `main`.
- Menambahkan potongan kode `@login_required(login_url='/login')` di atas fungsi `show_main` agar halaman `main` hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
  ```python
  from django.contrib.auth.decorators import login_required
  
  ...
  @login_required(login_url='/login')
  def show_main(request):
  ...
  ```
**4. Menghubungkan Model `Product` dengan `User`**
- Menambahkan kode berikut di `models.py` yang ada pada subdirektori `main.
  ```python
  ...
  from django.contrib.auth.models import User
  ...
  
  class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
  ...
  ```
Potongan kode di atas mendefinisikan model `Product` yang memiliki relasi banyak-ke-satu (many-to-one) dengan model `User` dari Django. Yang berarti setiap instance `Product` terkait dengan satu instance `User`. Relasi ini diimplementasikan menggunakan ForeignKey.

- Mengubah potongan kode pada fungsi `create_product` menjadi kode berikut:
  ```python
  def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
    ...
    ```
-Mengubah value dari `product` dan `context` pada fungsi `show_main` menjadi seperti berikut:
  ```python
  @login_required(login_url='/login')
  def show_main(request):
      products = Product.objects.filter(user=request.user)
  
      context = {
          'name': request.user.username,
          ...
  ```
**6. Melakukan Migrasi**
- Simpan semua perubahan, dan lakukan migrasi model dengan  `python manage.py makemigrations`.
- Lakukan `python manage.py migrate `untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.

**7. Import OS dan ganti variabel DEBUG dari berkas `settings.py`.**
```python
import os
...
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
....
```

*8. Menjalankan Proyek Django dengan command `python manage.py runserver` dan buka  http://localhost:8000/ di browser favoritmu untuk melihat hasilnya. 

## Bukti 2 akun yang telah di register dengan 3 dummy data
![image](https://github.com/user-attachments/assets/07466bec-6e82-48fb-84f2-8b54b6e94a65)
![image](https://github.com/user-attachments/assets/55cecf72-9a8f-4e75-b196-4eca7b8fcc0a)

</details>

