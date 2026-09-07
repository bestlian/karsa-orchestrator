# Gemini Spark Fullstack Skills

Panduan ringkas untuk suite full stack greenfield berbasis delapan skill yang sudah dikurasi per fase. Suite ini tidak menyalin framework upstream secara utuh, hanya mengambil subset yang relevan untuk alur kerja di repositori ini, termasuk alur anti-keserupaan visual yang dipimpin kontrak visual.

Sumber upstream yang dipin: anti-slop `v3.2.4`, commit `44be68777e96d53d113edad33dbc4ab380f5d054`, lisensi MIT. Suite ini bukan afiliasi atau dukungan dari proyek upstream.

## Catatan Kurasi Anti-Slop

Yang dipakai hanya aturan anti-fabrikasi, anti-template visual, dan peran fase yang dibutuhkan di sini. Upstream menyumbang filter anti-template visual yang dipilih; suite ini menambahkan kontrak VDC/VIS lokal, traceability, fidelity implementasi, dan quality blocking yang terverifikasi. CLI, plugin, script, tooling MCP, dan seluruh rule set upstream tetap tidak diimpor.

Prinsip bukti dan anti-fabrikasi yang dipakai lintas fase:

- klaim harus bisa dirujuk ke bukti, keputusan, atau artefak yang nyata;
- bila data nyata belum tersedia, tulis `[REAL DATA NEEDED]` dan sebutkan apa yang masih kurang;
- jangan mengisi celah dengan angka, kutipan, hasil, atau status yang belum ada buktinya;
- simpan bukti di artefak, jangan disamarkan di narasi.

Ringkasan pemeriksaan per fase:

- `discover-product`: discovery berbasis bukti, anti-fabrikasi, dan brief yang siap disetujui;
- `design-experience`: owner kontrak visual yang disetujui di `experience-spec.md`, dengan state nyata dan traceability ke requirement;
- `define-architecture`: blueprint netral framework, ownership dan contract jelas, tanpa coupling ke patch script;
- `plan-delivery`: propagasi referensi visual, acceptance visual, dan proof yang diminta ke backlog;
- `implement-feature`: fidelity kontrak visual, kontrol dan state harus nyata, tidak ada interaksi palsu atau tombol mati;
- `verify-quality`: real browser, click-through, build, run, console, keyboard, contrast, mobile reflow, theme, state loading, empty, error, disabled, serta blocking untuk drift terverifikasi atau proof yang hilang;
- `review-security`: klaim berbasis bukti saja, hasil yang belum pasti tetap ditulis sebagai ketidakpastian;
- `prepare-release`: keputusan akhir `PASS` atau `FAIL`, plus penjagaan notice dan atribusi.

## Kontrak Visual

- `VDC-NNN` adalah revisi Visual Direction Contract yang disetujui di `experience-spec.md`.
- `VIS-NNN` adalah keputusan visual bernomor di dalam revisi itu.
- Referensi kanonik memakai bentuk `experience-spec@VDC-NNN#VIS-NNN`, misalnya `experience-spec@VDC-001#VIS-001`.
- `direction_mode` bisa `restrained` atau `expressive`, dipilih sesuai tujuan produk, bukan selera estetika. Gradien, glass, animasi, atau imitasi brand tidak wajib.
- Referensi visual hanya dipakai sebagai provenance dan pembanding. Referensi itu tidak memberi izin untuk menyalin brand, aset yang dilindungi, atau materi tanpa lisensi dan persetujuan yang sesuai.
- Validasi visual real browser memakai lebar yang disetujui, atau fallback 375, 768, dan 1280 CSS px bila produk tidak menetapkannya. Screenshot saja tidak cukup untuk lulus.
- Mismatch kontrak yang terverifikasi, default generik yang sudah tertulis di kontrak, signature moment yang hilang, atau proof wajib yang tidak ada akan membuat quality gagal dan harus lewat remediasi di siklus hidup yang sudah ada.

## Delapan skill

1. `discover-product`
2. `design-experience`
3. `define-architecture`
4. `plan-delivery`
5. `implement-feature`
6. `verify-quality`
7. `review-security`
8. `prepare-release`

## Siklus pakai

Alur dasarnya:

1. `discover-product`
2. `design-experience` dan `define-architecture` dapat jalan paralel setelah kebutuhan awal cukup jelas
3. `plan-delivery`
4. `implement-feature` mengerjakan satu item siap pakai dalam satu waktu dan memperbarui `artifacts/implementation/<release-slice-id>-increment-manifest.md`
5. Selama item wajib dalam release slice masih tersisa, skill berikutnya tetap `implement-feature`
6. Setelah semua laporan item wajib selesai dan disetujui secara eksplisit, manifest increment dipindah ke `awaiting-approval`, lalu manusia menyetujuinya, lalu increment yang sudah disetujui masuk ke `verify-quality` dan `review-security` secara paralel
7. Jika `verify-quality` menghasilkan `fail` atau `conditional`, atau `review-security` menghasilkan `block` dengan temuan yang bisa diperbaiki, buat item remediasi yang dapat ditelusuri, minta persetujuan manusia, jalankan lagi `implement-feature`, lalu ulangi kedua review
8. Hanya laporan yang sudah disetujui dan tidak memblokir yang boleh lanjut ke `prepare-release`

Setiap tahap menghasilkan artefak yang harus lewat persetujuan manusia sebelum lanjut. Kalau `define-architecture` dibuat ulang, blueprint baru selalu mulai dari `awaiting-approval`, walau arahan sebelumnya sudah pernah disetujui.

## Kontrak handoff

Gunakan format `fullstack-skill-handoff/v1` untuk artefak antar tahap. Status yang dipakai:

- `draft`, masih dikerjakan
- `awaiting-approval`, siap ditinjau manusia
- `approved`, sudah disetujui manusia
- `rejected`, perlu revisi
- `blocked`, tertahan karena dependensi atau keputusan belum ada

Referensi VDC/VIS yang sudah disetujui tetap dibawa di `decision_refs`, sementara provenance dan bukti visual tetap dibawa di `validation_evidence`. `fullstack-skill-handoff/v1` dan model field tingkat atasnya tidak berubah.

Persetujuan harus eksplisit dari manusia. Jangan lanjut hanya karena artefak sudah selesai ditulis.

`implement-feature` memakai `technical_verdict: complete | partial | blocked` di laporan kerja. Laporan quality dan security memakai verdict teknis sendiri, terpisah dari status artefak.

## Upload ke Gemini Spark

Setiap skill diunggah sendiri, bukan sekaligus.

Langkah umum:

1. Pastikan folder skill hanya berisi paket skill itu sendiri.
2. Simpan `SKILL.md` di root folder skill.
3. Bungkus folder skill menjadi ZIP terpisah.
4. Unggah ZIP tersebut satu per satu ke Gemini Spark.
5. Ulangi untuk semua delapan skill.

## Contoh penggunaan

Panggil skill dengan bentuk:

```text
/discover-product
/design-experience
/define-architecture
/plan-delivery
/implement-feature
/verify-quality
/review-security
/prepare-release
```

Contoh alur singkat:

```text
/discover-product
```

Lalu, setelah artefak awal disetujui:

```text
/design-experience
/define-architecture
```

Setelah implementasi selesai:

```text
/verify-quality
/review-security
```

## ZIP usage

ZIP dipakai sebagai kemasan transfer untuk satu skill per arsip. Isi ZIP harus mewakili satu paket skill saja, agar impor tetap jelas dan nama skill tetap konsisten dengan format kebab-case.

Setiap ZIP yang didistribusikan harus berisi `SKILL.md` di root dan `THIRD_PARTY_NOTICES.md` di root. Notice di file itu harus tetap ada dan tidak boleh dihapus saat paket dipindah, disalin, atau dibungkus ulang.
