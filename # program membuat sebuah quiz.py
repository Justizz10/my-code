# program membuat sebuah quiz
print("Selamat Datang di Quiz Faizul Kamil!!")
print("Berikut adalah pertanyaannya\n1. Siapa bapak Proklamator Indonesia?\n2. Siapa Presiden kedua Indonesia?\n3. Indonesia merupakan benua apa?\n4. Apa semboyan negara kita?\n5. Negara Indonesia diamput oleh dua benua, Benua Asia dan Benua?")

while True:
    try:
        jawaban = str(input("Apakah anda siap?(ya/tidak): "))

        if jawaban == "ya":
            print("Quiz telah siap")

            jawaban_soal1 = str(input("Soal No 1\nSiapa bapak Proklamator Indonesia? "))
            if jawaban_soal1 == "Ir Soekarno":
                print("Jawaban anda benar")
                nilai1 = 20
            elif jawaban_soal1 == "Soekarno":
                print("Jawaban anda benar namun kurang tepat")
                nilai1 = 10
            else:
                print("Jawaban anda salah")
                nilai1 = 0
                
            jawaban_soal2 = str(input("Soal No 2\nSiapa Presiden kedua Indonesia? "))
            if jawaban_soal2 == "Soeharto":
                print("Jawaban anda benar")
                nilai2 = 20
            else:
                print("Jawaban anda salah")
                nilai2 = 0

            jawaban_soal3 = str(input("Soal No 3\nIndonesia merupakan benua apa? "))
            if jawaban_soal3 == "Asia Tenggara":
                print("Jawaban anda benar")
                nilai3 = 20
            elif jawaban_soal3 == "Asia":
                print("Jawaban benar namun kurang lengkap:>")
                nilai3 = 10
            else:
                print("Jawaban anda salah")
                nilai3 = 0

            jawaban_soal4 = str(input("Soal No 4\nApa semboyan negara kita? "))
            if jawaban_soal4 == "Bhineka Tunggal Ika":
                print("Jawaban anda benar")
                nilai4 = 20
            else:
                print("Jawaban anda salah")
                nilai4 = 0
            
            jawaban_soal5 = str(input("Soal no 5\nNegara Indonesia diamput oleh dua benua, Benua Asia dan Benua? "))
            if jawaban_soal5 == "Australia":
                print("Jawaban anda benar\n====================================================")
                nilai5 = 20
            else:
                print("Jawaban anda salah\n====================================================")
                nilai5 = 0
            
            nilai_total = nilai1+nilai2+nilai3+nilai4+nilai5
            while True:
                konfirmasi_nilai = str(input('Ketik "Konfirmasi" untuk melihat nilai: '))
                if konfirmasi_nilai == "Konfirmasi":
                    print("\n=============================================")
                    print("SELAMAT KAMU TELAH MENYELESAIKAN QUIZ INI\n============================================\nNilai kamu adalah:",nilai_total)
                    if nilai_total == 100:
                        print("Predikat: Sempurna\n")
                        break
                    elif nilai_total >= 90:
                        print("Predikat: Mantap\n")
                        break
                    elif nilai_total >= 80:
                        print("Predikat: Bagus\n")
                        break
                    elif nilai_total >= 70:
                        print("Predikat: Lumayan\n")
                        break
                    elif nilai_total >= 20:
                        print("Predikat: Remedial\n")
                        break
                    elif nilai_total <= 20:
                        print("Predikat: Belajar Lagi ya:>\n")
                        break
                else:
                    print('Tolong ketik "Konfirmasi" untuk melanjutkan')


                    

# apabila quiz tidak siap
        elif jawaban == "tidak":
            print("Quiz tidak tersedia")
            break
        else:
            print("Silahkan tulis sesuai dengan perintah")
    except ValueError:
        print("Tolong masukkan sebuah kata")