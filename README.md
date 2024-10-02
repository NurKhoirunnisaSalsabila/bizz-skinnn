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
**5. Menghubungkan Model `Product` dengan `User`**
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

**8. Menjalankan Proyek Django dengan command `python manage.py runserver` dan buka `http://localhost:8000/ ` di browser untuk melihat hasilnya.** 

## Bukti 2 akun yang telah di register dengan 3 dummy data
![image](https://github.com/user-attachments/assets/07466bec-6e82-48fb-84f2-8b54b6e94a65)
![image](https://github.com/user-attachments/assets/55cecf72-9a8f-4e75-b196-4eca7b8fcc0a)

</details>


<details>
  <summary>TUGAS 5</summary>

# **TUGAS 5**

---

## 1. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

1. Inline Styles
   * CSS yang ditulis langsung dalam atribut `style` pada elemen HTML memiliki tingkat prioritas tertinggi.
   * Contoh:
     ```html
     <p style="color: pink;">This is a paragraph.</p>
     ```
     ```html
     <div style="color: red;">This text is red.</div>
     ```
2.  ID Selectors:
   * Styles yang didefinisikan menggunakan `#id`.
   * Selector yang menggunakan ID lebih prioritas dibandingkan selector dengan class, atribut, atau type (tag).
   * Contoh:
     ```html
     #header {
        background-color: blue;
      }
     ```
     ```html
     <div id="header">This background is blue.</div>
     ```
     ```html
     #myId {
        color: blue;
      }
     ```
     
3. Class, Attribute, dan Pseudo-class Selectors:
   * Class Selectors:
     - Styles yang didefinisikan menggunakan `.class`.
     - Prioritas: Class selectors memiliki prioritas lebih rendah dibandingkan ID selectors tetapi lebih tinggi daripada type selectors.
     - Setara dengan Attribute dan Pseudo-class Selectors.
     - Contoh:
       ```html
        .highlight {
          color: yellow;
        }
        ```
        ```html
        <p class="highlight">This text is yellow.</p>
        ```
        
    * Attribute Selectors:
      - Definisi: Styles yang didefinisikan menggunakan `[attribute=value]`.
      - Prioritas: Attribute selectors memiliki prioritas yang sama dengan class selectors.
      - Contoh:
        ```html
        [type="text"] {
          border: 1px solid black;
        }
        ```
        ```html
        <input type="text" />
        ```
    * Pseudo-classes:
      - Definisi: Styles yang didefinisikan menggunakan `:pseudo-class`.
      - Prioritas: Pseudo-classes memiliki prioritas yang sama dengan class selectors dan attribute selectors.
      - Contoh:
        ```html
        a:hover {
          color: green;
        }
        ```
        ```html
        <a href="#">Hover over me!</a>
        ```
4. Type Selectors dan Pseudo-element Selectors:
   * Type Selectors:
      - Definisi: Styles yang didefinisikan menggunakan nama elemen HTML.
      - Prioritas: Type selectors memiliki prioritas lebih rendah dibandingkan class selectors, attribute, atau pseudo-class selectors.
      - Contoh:
         ```html
        p {
          font-size: 16px;
        }
        ```
        ```html
        <p>This text has a font size of 16px.</p>
        ```
    * Pseudo-element Selectors:
      - Selector berdasarkan elemen HTML (tag) atau pseudo-elemen memiliki prioritas yang lebih rendah dibanding ID, class, atau atribut.
      - Contoh:
        ```html
        p {
          color: purple;
        }
        ::before {
          content: "Prefix";
        }
        ```
5. Universal Selectors:
   - Styles yang didefinisikan menggunakan `*`.
   - Universal selectors memiliki prioritas paling rendah di antara semua selector.
   - Contoh:
     ```html
     * {
        margin: 0;
        padding: 0;
      }
     ```
6. Browser Default Styles:
   - Styles yang disediakan oleh browser secara default.
   - Contoh: Default margin pada elemen `<body>`, default font pada elemen `<p>`.
   - Prioritas: Browser default styles memiliki prioritas paling rendah dan akan ditimpa oleh semua jenis selector di atas.
   
7. Important Rule:
   - Deklarasi yang menggunakan  `!important` akan mengesampingkan semua aturan lainnya, kecuali aturan lain yang juga menggunakan `!important`.
   - Contoh:
     ```python
     p {
        color: blue !important;
      }
     ```

## 2. **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**
 * **Mengapa responsive design penting?**
   1. Secara keseluruhan, responsive design adalah konsep penting karena memungkinkan tampilan website beradaptasi dengan baik pada berbagai ukuran layar, seperti desktop, tablet, dan mobile. Jika tidak menerapkan desain responsif, pengguna mungkin akan mengalami tampilan yang kurang optimal pada perangkat tertentu.
   2. Pengalaman Pengguna (User Experience):
      - Responsive design memastikan bahwa aplikasi web dapat diakses dan digunakan dengan nyaman di berbagai perangkat, termasuk desktop, tablet, dan ponsel, sehingga meningkatkan kepuasan pengguna karena mereka dapat mengakses konten dengan mudah tanpa harus melakukan zoom in atau scroll horizontal.
      - Contoh: Situs web yang responsif akan menyesuaikan tata letak, ukuran teks, dan elemen lainnya agar sesuai dengan ukuran layar perangkat yang digunakan.
    3. SEO (Search Engine Optimization)
       - Search engine seperti Google memberikan peringkat lebih tinggi pada situs web yang responsif. Hal ini karena situs web yang responsif cenderung memberikan pengalaman pengguna yang lebih baik, yang merupakan faktor penting dalam algoritma peringkat mesin pencari.
       - Contoh: Situs web yang responsif lebih mungkin muncul di halaman pertama hasil pencarian Google dibandingkan dengan situs web yang tidak responsif.
    4. Aksesibilitas
       - Dengan responsive design, konten web dapat diakses oleh lebih banyak orang, termasuk mereka yang menggunakan perangkat dengan berbagai ukuran layar dan resolusi. Sehingga, memastikan bahwa semua pengguna, terlepas dari perangkat yang mereka gunakan, dapat mengakses informasi dengan mudah.
       - Contoh: Situs web yang responsif akan menyesuaikan ukuran tombol dan teks agar mudah diakses oleh pengguna dengan kebutuhan khusus.
    5. Efisiensi Pengembangan dan Pemeliharaan
       - Dengan menggunakan responsive design, pengembang hanya perlu membuat satu versi situs web yang dapat berfungsi di berbagai perangkat, sehingga mengurangi waktu dan biaya yang diperlukan untuk mengembangkan dan memelihara beberapa versi situs web.
       - Contoh: Daripada membuat situs web terpisah untuk desktop dan mobile, pengembang dapat menggunakan responsive design untuk membuat satu situs web yang berfungsi di semua perangkat.

 * **Contoh Aplikasi yang sudah Menerapkan Responsive Design**
1. Twitter
2. Github
3. SIAKNG

## 3. **Perbedaan Margin, Border, dan Padding, serta cara mengimplementasikan ketiganya**
1. Margin
   * Margin adalah ruang di luar border elemen. Margin digunakan untuk memberikan jarak antara elemen dengan elemen lainnya (mengosongkan area di sekitar border (transparan)).
   * Contoh Implementasi:
     ```html
     .element {
        margin: 20px; /* Memberikan jarak 20px di semua sisi elemen */
      }
     ```
2. Border
   * Border adalah garis yang mengelilingi padding dan konten elemen. Border dapat memiliki warna, ketebalan, dan gaya yang berbeda (garis tepian yang membungkus konten dan padding-nya).
   * Digunakan untuk memberikan batas visual pada elemen, sehingga elemen tersebut lebih menonjol atau terpisah dari elemen lain. 
   * Contoh Implementasi:
     ```html
     .element {
        border: 2px solid black; /* Memberikan border hitam dengan ketebalan 2px di semua sisi elemen */
      }
     ```
3. Padding
   *  Padding adalah ruang di dalam border, antara border dan konten elemen. Padding digunakan untuk memberikan jarak antara konten elemen dengan border elemen.
   *  Padding tidak memiliki warna atau gaya, hanya ruang kosong. (Padding gunanya untuk mengosongkan area di sekitar konten (transparan))
   *  Contoh Implementasi:
     ```html
     .element {
        padding: 15px; /* Memberikan jarak 15px di semua sisi konten elemen */
      }
     ```

### Contoh Implementasi dalam HTML dan CSS
Misalkan kita memiliki elemen HTML berikut:
```html
<div class="box">
  Konten di dalam kotak
</div>
```
Kita dapat mengimplementasikan margin, border, dan padding menggunakan CSS sebagai berikut:
```html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Margin, Border, and Padding Example</title>
  <style>
    .box {
      margin: 20px; /* Memberikan jarak 20px di luar border elemen */
      border: 2px solid black; /* Memberikan border hitam dengan ketebalan 2px di semua sisi elemen */
      padding: 15px; /* Memberikan jarak 15px di dalam border, antara border dan konten elemen */
      background-color: lightblue; /* Memberikan warna latar belakang untuk visualisasi */
    }
  </style>
</head>
<body>
  <div class="box">
    Konten di dalam kotak
  </div>
</body>
</html>

```

## 4. **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

1. Flexbox
   * Flexbox (Flexible Box Layout) adalah model layout CSS yang dirancang untuk mengatur elemen dalam satu dimensi (baris atau kolom). Flexbox sangat berguna untuk membuat layout yang fleksibel dan responsif.
   * Kegunaan Flexbox:
     - Alignment: Mengatur alignment elemen secara horizontal dan vertikal dengan mudah.
     - Order: Mengubah urutan elemen tanpa mengubah struktur HTML.
     - Spacing: Mengatur jarak antar elemen secara dinamis.
     - Responsiveness: Membuat layout yang responsif dengan sedikit kode.
  * Contoh Implementasi Flexbox:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Flexbox Example</title>
      <style>
        .container {
          display: flex;
          justify-content: center; /* Mengatur elemen di tengah secara horizontal */
          align-items: center; /* Mengatur elemen di tengah secara vertikal */
          height: 100vh;
        }
        .item {
          background-color: lightblue;
          padding: 20px;
          margin: 10px;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="item">Item 1</div>
        <div class="item">Item 2</div>
        <div class="item">Item 3</div>
      </div>
    </body>
    </html>
    ```
2. Grid Layout
   * Grid Layout adalah model layout CSS yang dirancang untuk mengatur elemen dalam dua dimensi (baris dan kolom). Grid layout sangat berguna untuk membuat layout yang kompleks dan responsif dengan mudah.
   * Kegunaan Grid Layout:
     - Complex Layouts: Membuat layout yang kompleks dengan baris dan kolom.
     - Alignment: Mengatur alignment elemen dalam grid dengan mudah. Mengatur alignment elemen dalam grid dengan properti `align-items` dan `justify-items`.
     - Responsiveness: Membuat layout yang responsif dengan mendefinisikan grid yang fleksibel.
     - Gap Control: Mengatur jarak antar elemen dalam grid dengan properti  `grid-gap`.
    * Contoh Implementasi Grid Layout:
      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Grid Layout Example</title>
        <style>
          .container {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* Membuat 3 kolom dengan lebar yang sama */
            grid-gap: 20px; /* Mengatur jarak antar elemen dalam grid */
            padding: 20px;
          }
          .item {
            background-color: lightgreen;
            padding: 20px;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="item">Item 1</div>
          <div class="item">Item 2</div>
          <div class="item">Item 3</div>
          <div class="item">Item 4</div>
          <div class="item">Item 5</div>
          <div class="item">Item 6</div>
        </div>
      </body>
      </html>
      ```
### **Kesimpulan**
Flexbox dan Grid Layout adalah dua model layout CSS yang sangat berguna untuk membuat layout yang fleksibel, responsif, dan kompleks. Flexbox lebih cocok untuk mengatur elemen dalam satu dimensi, sementara Grid Layout lebih cocok untuk mengatur elemen dalam dua dimensi. Dengan memahami dan menggunakan kedua model layout ini, pengembang dapat membuat desain web yang lebih baik dan lebih responsif.

## 5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

1. **Menambahkan Tailwind ke Aplikasi**
   * Buka file `base.html` yang telah dibuat sebelumnya pada templates folder yang berada di root project.
   * Tambahkan tag `<meta name="viewport">` agar halaman web kamu dapat menyesuaikan ukuran dan perilaku perangkat mobile.
     ```html
      <head>
          {% block meta %}
              <meta charset="UTF-8" />
              <meta name="viewport" content="width=device-width, initial-scale=1">
          {% endblock meta %}
      </head>
     ```
     * Tambahkan script CDN (Content Delivery Network) dari Tailwind untuk diletakkan di dalam html template Django, tepatnya di bagian head file `base.html`, gunanya untuk menyambungkan template django dengan tailwind.
       ```html
       <head>
        {% block meta %}
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
        {% endblock meta %}
        <script src="https://cdn.tailwindcss.com">
        </script>
        </head>
       ```
2. **Menambahkan Fitur Edit Product pada Aplikasi**
   * Tambahkan fungsi baru di `views.py` yang ada pada subdirektori `main`, fungsi baru tersebut bernama `edit_product` yang menerima parameter `request` dan `id`.
     ```html
       def edit_product(request, id):
          # Get product entry berdasarkan id
          product = Product.objects.get(pk = id)
      
          # Set product entry sebagai instance dari form
          form = ProductForm(request.POST or None, instance=product)
      
          if form.is_valid() and request.method == "POST":
              # Simpan form dan kembali ke halaman awal
              form.save()
              return HttpResponseRedirect(reverse('main:show_main'))
      
          context = {'form': form}
          return render(request, "edit_product.html", context)

     ```
     * Tambahkan import `reverse` pada file `views.py`.
     * Membuat berkas HTML baru dengan nama `edit_product.html` pada subdirektori `main/templates`.
       ```html
        {% extends 'base.html' %}
        {% load static %}
        {% block meta %}
        <title>Edit Product</title>
        {% endblock meta %}
        
        {% block content %}
        {% include 'navbar.html' %}
        
        <div class="flex flex-col min-h-screen bg-cover bg-center" style="background-image: url('{% static 'image/landing-page.png' %}');">
          <div class="container mx-auto px-4 py-8 mt-16 max-w-xl bg-white bg-opacity-90 rounded-2xl shadow-lg">
            <h1 class="text-3xl font-bold text-center mb-8 text-maroon-700 font-cursive">Edit Product</h1>
          
            <div class="bg-white rounded-2xl p-6 shadow-lg">
              <form method="POST" class="space-y-6">
                  {% csrf_token %}
                  {% for field in form %}
                      <div class="flex flex-col">
                          <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                              {{ field.label }}
                          </label>
                          <div class="w-full">
                              {{ field }}
                          </div>
                          {% if field.help_text %}
                              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                          {% endif %}
                          {% for error in field.errors %}
                              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                          {% endfor %}
                      </div>
                  {% endfor %}
                  <div class="flex justify-center mt-6">
                      <button type="submit" class="bg-[#800000] text-white font-semibold px-6 py-3 rounded-lg hover:bg-maroon-700 transition duration-300 ease-in-out w-full">
                          Edit Product
                      </button>
                  </div>
              </form>
            </div>
          </div>
        </div>
        
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
          .font-cursive {
            font-family: 'Pacifico', cursive;
          }
        
          @media (min-width: 768px) {
            .grid-cols-1 {
              grid-template-columns: repeat(1, minmax(0, 1fr));
            }
          }
        
          @media (min-width: 1024px) {
            .grid-cols-1 {
              grid-template-columns: repeat(1, minmax(0, 1fr));
            }
          }
        </style>
        {% endblock content %}

       ```
     * Buka `urls.py` yang berada pada direktori `main` dan import fungsi `edit_product` yang sudah dibuat.
       ```
       from main.views import edit_product
       ```
     * Lakukan routing url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
       ```
       path('edit-product/<uuid:id>', edit_product, name='edit_product'),
       ```
     * Buka `card_product.html` yang berada pada subdirektori `main/templates`. Tambahkan potongan kode berikut sejajar dengan elemen `<td>` terakhir agar terlihat tombol `edit` pada setiap baris tabel.
       ```html
        <!-- Actions -->
        <div class="mt-4 flex justify-end space-x-3">
            <a href="{% url 'main:edit_product' product.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white py-2 px-4 rounded-lg transition duration-300">
                EDIT
            </a>
            ...
        </div>
       ```
     
3. **Menambahkan Fitur Delete Product pada Aplikasi**
 * Tambahkan fungsi baru di `views.py` yang ada pada subdirektori `main`, fungsi baru tersebut bernama `delete_product` yang menerima parameter `request` dan `id`.
     ```html
     def delete_product(request, id):
        # Get product berdasarkan id
        product = Product.objects.get(pk = id)
        # Hapus product
        product.delete()
        # Kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
  * Buka `urls.py` yang berada pada direktori `main` dan import fungsi `delete_product` yang sudah dibuat.
       ```
       from main.views import delete_product
       ```
  * Lakukan routing url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.
       ```
       path('delete-product/<uuid:id>', delete_product, name='delete_product'),
       ```
  * Buka `card_product.html` yang berada pada subdirektori `main/templates`. Tambahkan potongan kode berikut sejajar dengan elemen `<td>` terakhir agar terlihat tombol `delete` pada setiap baris tabel.
       ```html
       ...
           <div class="mt-4 flex justify-end space-x-3">
            <a href="{% url 'main:edit_product' product.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white py-2 px-4 rounded-lg transition duration-300">
                EDIT
            </a>
            <a href="{% url 'main:delete_product' product.pk %}" class="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded-lg transition duration-300">
                DELETE
            </a>
        </div>
       ...
      ```

4. **Menambahkan Navigation Bar pada Aplikasi**
   * Buatlah berkas HTML baru dengan nama `navbar.html` pada folder `templates/` di root directory.
     ```html
     {% load static %}
      <nav class="bg-[#800000] shadow-lg">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between h-16">
            <div class="flex">
              <div class="flex-shrink-0">
                <a href="#">
                  <img class="h-8 w-8" src="{% static 'image/bizzskin-logo.png' %}" alt="Logo">
                </a>
                <span class="text-white font-bold ml-2">BizzSkin</span>
              </div>
              <div class="hidden md:ml-6 md:flex md:space-x-8">
                <a href="#" class="text-white hover:text-gray-200 inline-flex items-center px-1 pt-1 border-b-2 border-transparent hover:border-gray-200 text-sm font-medium">Home</a>
                <a href="#" class="text-white hover:text-gray-200 inline-flex items-center px-1 pt-1 border-b-2 border-transparent hover:border-gray-200 text-sm font-medium">Products</a>
                <a href="#" class="text-white hover:text-gray-200 inline-flex items-center px-1 pt-1 border-b-2 border-transparent hover:border-gray-200 text-sm font-medium">Categories</a>
                <a href="#" class="text-white hover:text-gray-200 inline-flex items-center px-1 pt-1 border-b-2 border-transparent hover:border-gray-200 text-sm font-medium">Cart</a>
              </div>
            </div>
            <div class="hidden md:ml-6 md:flex md:items-center">
              <span class="text-white text-sm font-medium mr-4">Welcome, {{ user.username }}!</span>
              <a href="{% url 'main:logout' %}" class="text-white hover:text-gray-200 border border-white hover:bg-gray-200 hover:text-[#800000] text-sm font-bold py-2 px-4 rounded transition duration-300">
                Logout
              </a>
            </div>
            <div class="-mr-2 flex items-center md:hidden">
              <button class="mobile-menu-button inline-flex items-center justify-center p-2 rounded-md text-white hover:text-gray-200 hover:bg-gray-200 focus:outline-none focus:bg-gray-200 focus:text-[#800000]">
                <svg class="w-6 h-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
      
        <!-- Mobile Menu -->
        <div class="mobile-menu hidden md:hidden px-4 w-full bg-[#800000]">
          <div class="py-2 space-y-1">
            <a href="#" class="block text-white hover:text-gray-200 py-2">Home</a>
            <a href="#" class="block text-white hover:text-gray-200 py-2">Products</a>
            <a href="#" class="block text-white hover:text-gray-200 py-2">Categories</a>
            <a href="#" class="block text-white hover:text-gray-200 py-2">Cart</a>
      
            <!-- Welcome Message and Logout Button for Mobile -->
            <div class="block text-center text-white font-medium py-2">Welcome, {{ user.username }}!</div>
            <a href="{% url 'main:logout' %}" class="block text-center border border-white hover:bg-gray-200 hover:text-[#800000] text-white font-bold py-2 px-4 rounded transition duration-300 mt-2">
              Logout
            </a>
          </div>
        </div>
      </nav>
      
      <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
      
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
      </script>
     ```
  * Kemudian, tautkan navbar tersebut ke dalam `main.html`, `create_product.html`, dan `edit_product.html` yang berada di subdirektori `main/templates/` dengan menggunakan tags `include:`
    ```
    {% include 'navbar.html' %}
    ```

5. **Konfigurasi Static Files pada Aplikasi**
   * Pada `settings.py`, tambahkan middleware WhiteNoise.
   ```
     ...
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
        ...
    ]
    ...
   ```
    * Pada `settings.py`, pastikan variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` dikonfigurasikan seperti ini:
      ```
      ...
      STATIC_URL = '/static/'
      if DEBUG:
          STATICFILES_DIRS = [
              BASE_DIR / 'static' # merujuk ke /static root project pada mode development
          ]
      else:
          STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
      ...
      ```
6. **Menambahkan Styles pada Aplikasi dengan Tailwind dan External CSS**
   * Tambahkan `global.css`
     - Buatlah file `global.css` di `/static/css` pada root directory.
     -  Pada file global.css ini isi dengan kode berikut untuk custom styling:
       ```css
             .form-style form input, form textarea, form select {
          width: 100%;
          padding: 0.5rem;
          border: 2px solid #bcbcbc;
          border-radius: 0.375rem;
      }
      .form-style form input:focus, form textarea:focus, form select:focus {
          outline: none;
          border-color: #674ea7;
          box-shadow: 0 0 0 3px #674ea7;
      }
      @keyframes shine {
          0% { background-position: -200% 0; }
          100% { background-position: 200% 0; }
      }
      .animate-shine {
          background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
          background-size: 200% 100%;
          animation: shine 3s infinite;
      }
      ```
   * Hubungkan `global.css` dan script Tailwind ke `base.html`.
     - Agar style CSS yang ditambahkan di `global.css` dapat digunakan dalam template Django, kamu perlu menambahkan file tersebut ke `base.html`. Modifikasi file `base.html` seperti berikut:
       ```html
       {% load static %}
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            {% block meta %} {% endblock meta %}
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
          </head>
          <body>
            {% block content %} {% endblock content %}
          </body>
        </html>
       ```
       
   * Menambahkan styling di page lainnya:
     
     - login.html
     - register.html
     - main.html
     - navbar.html
     - footer.html
     - card_product.html
     - add_product.html
     - edit_product.html


7. **Menambahkan Footer**
   - Membuat `footer.html` di folder main/templates:
     ```html
           {% load static %}
      
      <footer class="bg-[#800000] text-white py-6 sm:py-8 md:py-10 text-xs sm:text-sm md:text-base">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex flex-col space-y-4 sm:space-y-6 md:space-y-8">
      
            <!-- Logo -->
            <div class="flex justify-start">
              <img src="{% static 'image/bizzskin-logo.png' %}" alt="glowify logo" class="h-4 sm:h-5 md:h-6">
            </div>
      
            <!-- Divider -->
            <div class="w-full border-t border-white"></div>
      
            <!-- Links and Copyright -->
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center w-full space-y-2 sm:space-y-0">
      
              <!-- Copyright -->
              <div class="text-left">
                <p class="text-xs sm:text-sm md:text-base">&copy; 2024, chachamarica.</p>
              </div>
      
              <!-- Links -->
              <div class="flex flex-col sm:flex-row space-y-1 sm:space-y-0 sm:space-x-3 md:space-x-4 text-left sm:text-right">
                <a href="#" class="hover:underline text-xs sm:text-sm md:text-base">Privacy Policy</a>
                <a href="#" class="hover:underline text-xs sm:text-sm md:text-base">Terms of Service</a>
              </div>
            </div>
          </div>
        </div>
      </footer>
     ```
8. **Menambahkan Card untuk Produk dan Card Info**
   * Membuat `card_product.html` di folder main/templates:
     ```html
     {% load humanize %}

      <div class="bg-white p-4 sm:p-6 md:p-8 rounded-lg shadow-lg transition-transform transform hover:scale-105 duration-300">
          <!-- Product Details -->
          <div class="text-left">
              <h3 class="text-lg sm:text-xl md:text-2xl font-bold text-gray-800 mb-2">{{ product.name }}</h3>
              <p class="text-sm sm:text-base md:text-lg text-gray-600 mb-4">{{ product.description }}</p>
              <p class="text-xl sm:text-2xl md:text-3xl font-bold text-indigo-600 mb-2">Rp{{ product.price|intcomma }}</p>
              <p class="text-sm sm:text-base md:text-lg text-gray-500">Skin Type: {{ product.skin_type }}</p>
          </div>
      
          <!-- Actions -->
          <div class="mt-4 flex justify-end space-x-3">
              <a href="{% url 'main:edit_product' product.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white py-2 px-4 rounded-lg transition duration-300">
                  EDIT
              </a>
              <a href="{% url 'main:delete_product' product.pk %}" class="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded-lg transition duration-300">
                  DELETE
              </a>
          </div>
      </div>
     ```
     * Membuat `card_info.html` di folder main/templates:
       ```html
       <!-- <div class="bg-indigo-700 rounded-xl overflow-hidden border-2 border-indigo-800">
            <div class="p-4 animate-shine">
              <h5 class="text-lg font-semibold text-gray-200">{{ title }}</h5>
              <p class="text-white">{{ value }}</p>
            </div>
        </div> -->
        
        <div class="bg-pink-100 rounded-xl overflow-hidden border-2 border-maroon-800 shadow-lg transform transition duration-300 hover:scale-105">
          <div class="p-6">
            <h5 class="text-lg font-semibold text-maroon-700">{{ title }}</h5>
            <p class="text-maroon-600">{{ value }}</p>
          </div>
        </div>
       ```

9. **Menambahkan Halaman Register**
   * Membuat `register.html` di folder templates:
     ```html
     {% extends 'base.html' %}
      {% load static %}
      
      {% block meta %}
      <title>Register</title>
      {% endblock meta %}
      
      {% block content %}
      <div class="min-h-screen flex items-center justify-center bg-pink-100 py-12 px-4 sm:px-6 lg:px-8" style="background-image: url('{% static 'image/background-pattern.png' %}'); background-size: cover; background-position: center;">
        <div class="max-w-md w-full space-y-8 form-style bg-white p-8 rounded-lg shadow-lg">
          <div>
            <h2 class="mt-6 text-center text-3xl font-extrabold" style="color: #800000;">
              Create your account
            </h2>
          </div>
          <form class="mt-8 space-y-6" method="POST">
            {% csrf_token %}
            <input type="hidden" name="remember" value="true">
            <div class="rounded-md shadow-sm -space-y-px">
              {% for field in form %}
                <div class="{% if not forloop.first %}mt-4{% endif %}">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold" style="color: #800000;">
                    {{ field.label }}
                  </label>
                  <div class="relative">
                    {{ field }}
                    <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                      {% if field.errors %}
                        <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                        </svg>
                      {% endif %}
                    </div>
                  </div>
                  {% if field.errors %}
                    {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                  {% endif %}
                </div>
              {% endfor %}
            </div>
            <div>
              <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-maroon-600 hover:bg-maroon-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-maroon-500" style="background-color: #800000;">
                Register
              </button>
            </div>
            <div class="text-center mt-4">
              <p class="text-sm" style="color: #800000;">
                Already have an account?
                <a href="{% url 'main:login' %}" class="font-bold hover:opacity-80" style="color: #800000;">Login here</a>
              </p>
            </div>
          </form>
        </div>
      </div>
      {% endblock content %}

   
10. **Menambahkan Halaman Tambah Produk**
    * Membuat `create_product.html` di folder main/templates:
    ```html
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Create Product</title>
    {% endblock meta %}
    
    {% block content %}
    {% include 'navbar.html' %}
    
    <div class="flex flex-col min-h-screen bg-cover bg-center" style="background-image: url('{% static 'image/landing-page.png' %}');">
      <div class="container mx-auto px-4 py-8 mt-16 max-w-xl bg-white bg-opacity-90 rounded-2xl shadow-lg">
        <h1 class="text-3xl font-bold text-center mb-8 text-maroon-700 font-cursive">Create Product</h1>
      
        <div class="bg-white shadow-md rounded-lg p-6 form-style">
          <form method="POST" class="space-y-6">
            {% csrf_token %}
            {% for field in form %}
              <div class="flex flex-col">
                <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                  {{ field.label }}
                </label>
                <div class="w-full">
                  {{ field }}
                </div>
                {% if field.help_text %}
                  <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                {% endif %}
                {% for error in field.errors %}
                  <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
              </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
              <button type="submit" class="bg-[#800000] text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                Create Product
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
      .font-cursive {
        font-family: 'Pacifico', cursive;
      }
    
      @media (min-width: 768px) {
        .grid-cols-1 {
          grid-template-columns: repeat(1, minmax(0, 1fr));
        }
      }
    
      @media (min-width: 1024px) {
        .grid-cols-1 {
          grid-template-columns: repeat(1, minmax(0, 1fr));
        }
      }
    </style>
    {% endblock content %}
    ```
11. **Melakukan add, commit, dan push ke github dan pws**
</details>
