langkah 0:
https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py
    python get-pipenv.py

pip install --user pipenv

untuk pastikan bisa jalan, ketik pipenv di terminal

https://docs.djangoproject.com/en/2.2/intro/

tambahkan c:\python37\scripts ke environment variable PATH

pasang git

# bahasan (dengan contoh project nya workshop-django)
1. buat directory kerja misalnya di c:\src\workshop-django
    mkdir workshop-django
2. pindah ke directory keja c:\src\workshop-django
    cd workshop-django
3. (optional) buat repo git baru, git init
4. install django pakai pipenv
    pipenv install django
5. aktifkan virtual environment
    pipenv shell
6. (optional) tambahkan perubahan ke repo baru, git add .
7. (optional) simpan perubahan, git commit -m "first commit"
8. start project django baru
    django-admin startproject workshopdjango .
9. jalankan aplikasi django
    python manage.py runserver

# langkah-langkah menambahkan view (tampilan web)
1. edit file views.py di app yang akan digunakan untuk menampilkan view
    misalnya di app hello, berarti di hello/views.py
2. tambahkan/edit function baru
    def namafunction(request):
        return HttpResponse('apa yang mau ditampilkan')
3. pasangkan routing di urls.py project, misalnya di workshopdjango/urls.py
    from hello import views
    urlpatterns = [
        ...
        path('namapath', namaview, name='nama_halaman'),
        ...
    ]


# langkah buat template django
1. daftarkan nama app di settings.py project (workshopdjango) apabila belum ada
    di INSTALLED_APPS
    INSTALLED_APPS = [
    ...,
    'hello',
    ]
2. buat folder di app hello templates/hello
3. buat file template di folder langkah 2 misalnya templates/hello/index.html
4. render di view yang bersangkutan
    def index(request):
        #return HttpResponse('Hello World')
        return render(request, 'hello/index.html', {})
