# Antigravity Fullstack Skills

Repositori ini adalah paket orkestrasi Antigravity Fullstack Skills untuk membangun aplikasi full-stack greenfield end to end. `fullstack-orchestrator` adalah control plane berbasis bahasa natural. Delapan skill lain adalah skill spesialis fase. Alurnya memandu kerja dari ide dan discovery, ke UX, arsitektur, perencanaan, implementasi, QA, security, lalu persiapan rilis.

## Tentang Proyek

`fullstack-orchestrator` membaca artefak yang terlihat dan merekomendasikan skill berikutnya yang paling tepat. Ia adalah lapisan kontrol, bukan pekerja.

Ia tidak menjalankan skill spesialis secara langsung, tidak merangkai pekerjaan secara otomatis, tidak menyimpan state lintas chat, tidak self-approve, tidak membuat artefak orchestrator baru, tidak deploy, dan tidak menggantikan kontrak skill spesialis. Ia juga tidak mengklaim Antigravity akan menjalankan routing otomatis yang pasti. Semua skill tetap dipasang sebagai direktori terpisah di workspace yang sama.

## Siklus Hidup

Urutan resminya adalah `discover-product -> (design-experience + define-architecture) -> plan-delivery -> one-item implement-feature loop -> (verify-quality + review-security) -> prepare-release`.

Aturan intinya:

- `discover-product` dimulai dari bukti yang tampak, lalu menghasilkan product brief yang siap dimintakan persetujuan manusia.
- `design-experience` dan `define-architecture` baru berjalan paralel setelah product brief disetujui secara eksplisit. Keduanya adalah join, jadi dua output yang sudah disetujui harus ada sebelum lanjut.
- `plan-delivery` hanya jalan setelah brief, experience spec, dan blueprint sudah disetujui.
- `implement-feature` berjalan satu item siap kerja per putaran, bukan batch.
- `verify-quality` dan `review-security` baru berjalan paralel setelah seluruh item wajib dan increment manifest sudah disetujui. Ini juga join, jadi kedua report harus ada dan disetujui sebelum lanjut.
- `prepare-release` hanya boleh dipilih setelah quality dan security lulus sesuai aturan yang berlaku.

## Persetujuan Dan Join

Setiap transisi ke fase berikutnya memerlukan persetujuan manusia yang eksplisit pada artefak upstream yang dipakai fase itu. Status artefak, verdict teknis, PASS gate, `next_skills`, dan persetujuan manusia adalah hal yang berbeda.

- `awaiting-approval` bukan persetujuan.
- `PASS`, `pass`, `pass-with-findings`, `complete`, atau `technical_verdict` yang baik tidak otomatis berarti disetujui manusia.
- `next_skills` hanya arahan hilir. Itu bukan bukti bahwa skill sudah dipanggil, pekerjaan sudah berjalan, atau persetujuan sudah diberikan.
- Saat dua skill diparalelkan, kedua branch harus selesai dan disetujui sebelum join dibuka.

Jika `verify-quality` gagal, `conditional`, atau `review-security` `block` dengan temuan yang bisa diperbaiki, jalurnya adalah remediation. Buat satu item remediasi yang dapat ditelusuri, mintakan persetujuan manusia, jalankan `implement-feature` untuk satu item itu, lalu ulangi kedua verifikasi sampai syarat rilis terpenuhi.

## Handoff Dan Artefak

Gunakan `fullstack-skill-handoff/v1` untuk handoff antar tahap. Struktur ini tetap dipakai apa adanya.

Status yang sah:

- `draft`
- `awaiting-approval`
- `approved`
- `rejected`
- `blocked`

`implement-feature` memakai `technical_verdict: complete | partial | blocked` pada laporan kerja. `verify-quality` dan `review-security` punya verdict teknis mereka sendiri, terpisah dari status artefak.

Referensi visual kanonik selalu memakai bentuk `experience-spec@VDC-NNN#VIS-NNN`. Contoh: `experience-spec@VDC-001#VIS-001`.

Resume harus dimulai dari artefak yang terlihat, bukan dari ingatan chat. Kalau pindah chat, bawa artefak terbaru dan handoff terbaru, lalu lanjut dari sana. Memori percakapan bukan sumber otoritatif.

## Keterbacaan Dan Daya Rawat

Keterbacaan berarti source code lebih mudah dipahami dan diubah oleh developer yang menerima dan memelihara aplikasi hasil generasi ini.

- Arsitektur menetapkan tanggung jawab modul, kontrak publik, dan arah dependensi.
- Perencanaan menurunkan keputusan itu ke acceptance criteria, test, quality gate, dan proof yang wajib ada.
- Implementasi memakai TDD, konvensi repository, modularitas yang didukung bukti, dan evidence Design And Maintainability.
- Quality memverifikasi secara independen dan memblokir kegagalan material atau evidence wajib yang belum terselesaikan.
- Checks yang dikonfigurasi repository diprioritaskan. Tooling opsional yang tidak tersedia dicatat sebagai evidence gap, bukan dipalsukan menjadi pass dan bukan syarat otomatis untuk instalasi.
- Tidak ada line limit universal, mandat framework universal, kebijakan SOLID universal, atau preferensi gaya subjektif yang dipakai sebagai release gate.

## Sembilan Paket

1. `fullstack-orchestrator`, control plane natural-language
2. `discover-product`
3. `design-experience`
4. `define-architecture`
5. `plan-delivery`
6. `implement-feature`
7. `verify-quality`
8. `review-security`
9. `prepare-release`

## Instalasi Dan Format Paket

Setiap ZIP adalah artefak distribusi portabel. Satu ZIP hanya boleh berisi satu skill.

Langkahnya:

1. Ekstrak tiap paket ke `.agents/skills/<skill-name>/`.
2. Setelah diekstrak, setiap direktori skill harus punya `SKILL.md` dan `THIRD_PARTY_NOTICES.md` di root-nya.
3. Instal semua sembilan direktori skill di workspace Antigravity yang sama.
4. Nama skill yang sudah ada tetap tidak berubah.

## Cara Pakai

Contoh mulai dengan bahasa natural:

```text
Bangun aplikasi inventori baru, gunakan artefak yang terlihat.
```

Contoh resume:

```text
Lanjutkan dari product brief yang sudah approved, lalu cek handoff terbaru untuk branch design dan architecture.
```

Contoh slash command opsional:

```text
/fullstack-orchestrator
/discover-product
/design-experience
/define-architecture
/plan-delivery
/implement-feature
/verify-quality
/review-security
/prepare-release
```

## Kontrak Visual

- `VDC-NNN` adalah revisi Visual Direction Contract yang disetujui di `experience-spec.md`.
- `VIS-NNN` adalah keputusan visual bernomor di dalam revisi itu.
- `direction_mode` bisa `restrained` atau `expressive`, dipilih sesuai tujuan produk, bukan selera estetika.
- Referensi visual hanya dipakai sebagai provenance dan pembanding. Itu tidak memberi izin untuk menyalin brand, aset yang dilindungi, atau materi tanpa lisensi dan persetujuan yang sesuai.
- Validasi visual di browser nyata memakai lebar yang disetujui, atau fallback 375, 768, dan 1280 CSS px bila produk tidak menetapkannya. Screenshot saja tidak cukup.
- Default generik yang tertulis di kontrak, signature moment yang hilang, mismatch yang terverifikasi, atau proof wajib yang tidak ada akan membuat quality gagal dan harus lewat remediation di siklus hidup yang sama.

## Kurasi Anti-Slop

Anti-slop hanya berfungsi sebagai guardrail mutu tambahan. Anti-slop bukan mesin orkestrasi, bukan framework utama proyek ini, dan tidak diimpor secara utuh.

Yang dipakai dari upstream hanya kurasi yang membantu mengurangi output aplikasi generik atau terlalu mirip template, visual sameness atau keserupaan visual, bukti yang direkayasa, interaksi palsu, dan klaim mutu yang belum diverifikasi.

Sumber upstream yang dipin: anti-slop `v3.2.4`, commit `44be68777e96d53d113edad33dbc4ab380f5d054`, lisensi MIT. Referensi sumber upstream adalah [anti-slop](https://github.com/miqdadbadjuber/anti-slop). Proyek ini tidak berafiliasi dengan, tidak didukung oleh, dan tidak mewakili proyek upstream.

Prinsip yang dipakai lintas fase:

- klaim harus bisa dirujuk ke bukti, keputusan, atau artefak yang nyata;
- kalau data nyata belum ada, tulis `[REAL DATA NEEDED]` dan sebutkan apa yang kurang;
- jangan mengisi celah dengan angka, kutipan, hasil, atau status yang belum terbukti;
- simpan bukti di artefak, bukan di narasi.

`THIRD_PARTY_NOTICES.md` harus tetap ikut di root setiap ZIP yang didistribusikan. Notice itu tidak boleh dihapus saat paket dipindah, disalin, atau dibungkus ulang.
