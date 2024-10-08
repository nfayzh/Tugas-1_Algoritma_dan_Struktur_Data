# // Antrian Kendaraan di Gerbang Tol
queue = []

# Operasi enqueue (Menambahkan Jenis Kendaraan dengan Brand ke Antrian)
queue.append("Mobil Penumpang Toyota B 7840 CD")
queue.append("Mobil Penumpang Honda D 9315 EF")
queue.append("Truk Kontainer Mitsubishi G 3824 IJ")
queue.append("Mobil Sport Ferrari E 6381 GI")

print("Queue setelah operasi enqueue: ", queue)
print(f"Jumlah kendaraan dalam antrian : {len(queue)}\n")

# Operasi dequeue (Mengeluarkan Kendaraan dari Antrian)
print("Kendaraan yang keluar dari antrian (dequeue) :", queue.pop(0))
print("Sisa kendaraan dalam Antrian:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah kendaraan dalam antrian: {len(queue)}\n")

print("Kendaraan yang keluar dari antrian (dequeue) :", queue.pop(0))
print("Sisa kendaraan dalam Antrian:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah kendaraan dalam antrian: {len(queue)}\n")

print("Kendaraan yang keluar dari antrian (dequeue) :", queue.pop(0))
print("Sisa kendaraan dalam Antrian:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah kendaraan dalam antrian: {len(queue)}\n")

# Memeriksa apakah kosong
print("Apakah antrian kosong ? :", len(queue) == 0)
