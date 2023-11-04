Program ini adalah API untuk suatu media sosial. Pengguna media sosial ini dapat membuat
post, namun hanya dalam bentuk tulisan. Pengguna dapat juga mengedit atau menghapus
post yang dibuatnya sendiri. Pengguna dapat berinteraksi dengan post yang dibuat orang
lain dengan memberi votes(like)

Framework yang digunakan adalah `FastAPI`. Sistem database yang digunakan adalah
`PostgreSQL`. Koneksi API ke database menggunakan `SQLAlchemy`. Migrasi database menggunakan `alembic`. Terdapat path operation yang mengharuskan pengguna dalam keadaan logged in. Sistem autentikasi yang digunakan adalah JSON Web Token

Aplikasi fastapi akan dibuat pada file app/main.py(folder app menjadi suatu paket). Dengan menggunakan APIRouter, path operation yang ada dikelompokkan dalam 4 file.
- auth.py: tentang login(mendapat json web token)
- post.py: tentang operasi CRUD terhadap post(data post di tabel `posts`)
- user.py: tentang mendapat suatu user dari tabel `users`, membuat user baru(data baru di tabel `users`)  
- vote.py: tentang vote(user vote suatu post)


Argumen yang diterima pada suatu fungsi path operation terdapat query parameter, body request(jika ada, sesuai dengan metode dari path operation), path parameter, dependency injection.

Dependency injection yang digunakan pada aplikasi ini
- `db:Session = Depends(get_db)`: Membuat database session untuk mengakses database
- `current_user=Depends(oauth2.get_current_user)`: Mengambil user dari tabel `users` dengan `id` yang berasal dari payload token
- `token:str=Depends(oauth2_scheme)`: Mengambil token dari request headers

Body request yang diterima suatu path operation diterima oleh argumen yang mendapat validasi model `Pydantic`. 

Terdapat validasi struktur dari request yang masuk ke suatu path operation dan respon dari path operation, dengan model `Pydantic` yang ada di `schemas.py`

Tabel yang digunakan aplikasi ini
- `users`: Tabel pengguna media sosial. Primary key `id`
- `posts` Tabel post yang ada di media sosial. Memliki relationship dengan tabel `users`, yaitu setiap post dimiliki oleh suatu user. Primary key `id` dan foreign key `owner_id` yang menghubungkan ke pemilik post(`id` dari pemilik post di tabel `users`)
- `votes`: Memiliki relatioinship dengan tabel `users` dan `posts`. Terdapat foreign key `user_id`(ke tabel `users`) dan `post_id`(ke tabel `posts`). Primary key dibentuk dari `user_id` dan `post_id`



## Sumber video
https://youtu.be/0sOvCWFmrtA?si=5l0DKeAZIOfVMA-k