class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListCircular:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, node_data, new_data):
        new_node = Node(new_data)
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_data:
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                if current_node == self.tail:
                    self.tail = new_node
                break
            current_node = current_node.next
            if current_node == self.head:
                break

    def delete_first(self):
        if self.is_empty():
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            del temp

    def delete_last(self):
        if self.is_empty():
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            current_node = self.head
            prev_node = None
            while current_node.next is not self.head:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = self.head
            self.tail = prev_node

    def delete_after(self, node_data):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.data == node_data:
                next_node = current_node.next
                if next_node == self.head:
                    self.tail = prev_node
                prev_node.next = next_node
                break
            prev_node = current_node
            current_node = current_node.next
            if current_node == self.head:
                break

    def search(self, nama):
        current_node = self.head
        while current_node is not None:
            if current_node.data.nama == nama:
                return current_node.data
            current_node = current_node.next
        return None

    def print_list(self):
        if self.is_empty():
            print("Daftar produk kosong.")
        else:
            current_node = self.head
            while True:
                print(current_node.data)
                current_node = current_node.next
                if current_node == self.head:
                    break

class Produk:
    def __init__(self, nama, harga, stok, merek, kategori):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.merek = merek
        self.kategori = kategori

    def __str__(self):
        return f"Nama: {self.nama}\nHarga: Rp{self.harga:,}\nStok: {self.stok}\nMerek: {self.merek}\nKategori: {self.kategori} \n"

class KatalogProduk:
    def __init__(self):
        self.produk = LinkedListCircular()

    def create(self, produk):
        self.produk.add_last(produk)

    def read(self):
        print("\n--- Toko Komputer ---")
        self.produk.print_list()

    def update(self, nama, produk_baru):
            current_node = self.produk.head
            while current_node is not None:
                if current_node.data.nama == nama:
                    current_node.data = produk_baru
                    break
                current_node = current_node.next

            if current_node is None:
                print(f"Produk dengan nama '{nama}' tidak ditemukan.")

    def delete(self, nama):
        current_node = self.produk.head
        prev_node = None
        while current_node is not None:
            if current_node.data.nama == nama:
                if prev_node is None:  
                    self.produk.delete_first()
                else:
                    prev_node.next = current_node.next
                    if current_node == self.produk.tail:  
                        self.produk.tail = prev_node
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"Produk dengan nama '{nama}' tidak ditemukan.")

def main():
    katalog = KatalogProduk()

    produk_baru = [
        Produk("AOC 27G4 Gaming Monitor", 2678000, 5, "AOC", "Monitor Gaming"),
        Produk("Intel Core i5 13400F", 3500000, 3, "INTEL", "Processor"),
        Produk("LENOVO Legion 9i 16IRX8", 76999000, 2, "LENOVO", "Laptop Gaming"),
        Produk("ASUS ROG Zephyrus G16 GU603ZU", 24199000, 4, "ASUS", "Laptop Gaming"),
        Produk("NVIDIA GeForce RTX 3060", 4475000, 4, "GIGABYTE", "Vga Card"),
        Produk("AMD Ryzen 5 5600G", 2179000, 5, "AMD", "Processor"),
        Produk("MSI PRO B660M-A DDR4", 1800000, 7, "MSI", "Motherboard"),
        Produk("DDR4 32GB (2x16GB) Corsair Vengeance LPX", 1350000, 6, "CORSAIR", "RAM"),
        Produk("NVMe M.2 1TB Samsung 980 Pro", 3200000, 4, "Samsung", "SSD"),
        Produk("ASUS Vivobook Pro 14 OLED M3401Q1-KM043W", 13000000, 2, "ASUS", "Laptop"),
        Produk("AMD Ryzen 9 7950X", 14000000, 6, "AMD", "Processor"),
        Produk("NVIDIA GeForce RTX 4070 Ti", 10000000, 2, "COLORFUL", "Vga Card"),
    ]

    for produk in produk_baru:
        katalog.create(produk)

    while True:
        print("\n--- Toko Komputer ---")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Keluar")

        pilihan = int(input("\nMasukkan pilihan: "))

        if pilihan == 1:
            nama_produk = input("Masukkan nama produk: ")
            harga_produk = int(input("Masukkan harga produk: "))
            stok_produk = int(input("Masukkan stok produk: "))
            merek_produk = input("Masukkan merek produk: ")
            kategori_produk = input("Masukkan kategori produk: ")

            produk_baru = Produk(nama_produk, harga_produk, stok_produk, merek_produk, kategori_produk)
            katalog.create(produk_baru)

        elif pilihan == 2:
            katalog.read()

        elif pilihan == 3:
            nama_produk = input("Masukkan nama produk yang ingin diubah: ")

            nama_baru = input("Masukkan nama baru: ")
            harga_baru = int(input("Masukkan harga baru: "))
            stok_baru = int(input("Masukkan stok baru: "))
            merek_baru = input("Masukkan merek baru: ")
            kategori_baru = input("Masukkan kategori baru: ")

            produk_baru = Produk(nama_baru, harga_baru, stok_baru, merek_baru, kategori_baru)
            katalog.update(nama_produk, produk_baru)

        elif pilihan == 4:
            nama_produk = input("Masukkan nama produk yang ingin dihapus: ")
            katalog.delete(nama_produk)

        elif pilihan == 5:
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
