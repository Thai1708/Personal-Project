#Phạm Văn Thái 20206303

import random

# Tao class SinhVien bao gom 6 thuoc tinh: ho_ten, mssv, lop, tc_dap_an, tc_dap_an_dung, diem
class SinhVien:
	def __init__(self, ho_ten, mssv, lop, tc_dap_an, tc_dap_an_dung, diem):
		self.ho_ten = ho_ten
		self.mssv = mssv
		self.lop = lop
		self.tc_dap_an = tc_dap_an
		self.tc_dap_an_dung = tc_dap_an_dung
		self.diem = diem

# Tao class Cau bao gom 3 thuoc tinh: cau_hoi, tat_ca_dap_an, dap_an_dung
class Cau:
	def __init__(self, cau_hoi, tat_ca_dap_an, dap_an_dung):
		self.cau_hoi = cau_hoi
		self.tat_ca_dap_an = tat_ca_dap_an
		self.dap_an_dung = dap_an_dung

# Tien hanh doc file cau_hoi.txt
# Tra ve mang cau hoi ma moi phan tu cua mang la doi tuong cua class Cau
def doc_file():
	with open("cauhoi.txt", "r", encoding="utf8") as file:
		tat_ca_cau = [] 
		so_cau_hoi = file.readline().strip()
		so_cau_hoi = int(so_cau_hoi)
		# Doc moi 6 dong, lap 1 lan, tao duoc 1 doi tuong Cau
		for i in range (so_cau_hoi):
			tat_ca_dap_an = []
			# strip() loai cac ki tu space o dau va cuoi moi dong
			cau_hoi = file.readline().strip()
			for j in range(4):
				dap_an = file.readline().strip()
				tat_ca_dap_an.append(dap_an)
			dap_an_dung = file.readline().strip()
			cau = Cau(cau_hoi, tat_ca_dap_an, dap_an_dung)
			tat_ca_cau.append(cau)
	return tat_ca_cau

# Kiem tra bo cau hoi duoc tao sau khi doc file da dung format chua
# Format: Khong 1 Cau nao duoc thieu bat ki thuoc tinh nao.
def kiem_tra_cau_hoi(tat_ca_cau):
	for i in range(len(tat_ca_cau)):
		if tat_ca_cau[i].cau_hoi == "":
			return False
		for j in range(4):
			if tat_ca_cau[i].tat_ca_dap_an[j] == "":
				return False
		if tat_ca_cau[i].dap_an_dung == "":
			return False
	return True

# Xao tron mang Cau va dap an cua tung Cau trong mang do
# In de bai duoc sinh
# Tra ve mang cac dap an dung sau khi thuc hien xao tron
def xao_tron_cau(tat_ca_cau):
	tat_ca_dap_an_dung = []
	# shuffle thuc hien xao tron
	random.shuffle(tat_ca_cau)
	for i in range(len(tat_ca_cau)):
		random.shuffle(tat_ca_cau[i].tat_ca_dap_an)
		print("Cau hoi " + str(i + 1) + ": ", end = '')
		print(tat_ca_cau[i].cau_hoi)
		for j in range(4):
			if j == 0:
				print("A. ", end = '')
			elif j == 1:
				print("B. ", end = '')
			elif j == 2:
				print("C. ", end = '')
			else:
				print("D. ", end = '')
			print(tat_ca_cau[i].tat_ca_dap_an[j])
		# Tim dap an dung cua tung Cau
		for j in range(4):
			if tat_ca_cau[i].tat_ca_dap_an[j] == tat_ca_cau[i].dap_an_dung:
				if j == 0:
					dap_an_dung = "A"
				elif j == 1:
					dap_an_dung = "B"
				elif j == 2:
					dap_an_dung = "C"
				else:
					dap_an_dung = "D"
		tat_ca_dap_an_dung.append(dap_an_dung)
	return tat_ca_dap_an_dung

# Nhap cac thong tin thi sinh: ho_ten, mssv, lop
def nhap_thong_tin_ca_nhan():
	ho_ten = input("Ho va ten sinh vien: ")
	mssv = input("Nhap ma so sinh vien: ")
	lop = input("Nhap lop: ")
	return ho_ten, mssv, lop

# Hien thi tong tin thi sinh: ho_ten, mssv, lop
def in_thong_tin_ca_nhan(sinh_vien):
	print("Ho va ten      :", end = " ")
	print(sinh_vien.ho_ten)
	print("Ma so sinh vien: ", end = " ")
	print(sinh_vien.mssv)
	print("Lop            :", end = " ")
	print(sinh_vien.lop)

# Sua thong tin thi sinh
# Bao gom 3 lua chon thay doi: ho va ten, ma so sinh vien va lop
def sua_thong_tin_ca_nhan(sinh_vien):
	print("____________________")
	print("|1: Ho va ten      |")
	print("|2: Ma so sinh vien|")
	print("|3: Lop            |")
	print("____________________")
	choice = lua_chon_so("Chon thong tin muon sua(1-3): ", 1, 3)
	if choice == 1:
		ho_ten_moi = input("Ho ten moi la: ")
		sinh_vien.ho_ten = ho_ten_moi
	elif choice == 2:
		mssv_moi = input("Ma so sinh vien moi la: ")
		sinh_vien.mssv = mssv_moi
	else:
		lop_moi = input("Lop moi la: ")
		sinh_vien.lop = lop_moi
	return sinh_vien

# Nhap input dung theo yeu cau, thuoc khong tu nho so nho nhat den lon nhat
def lua_chon_so(promp, min_, max_):
	choice = input(promp)
	# isdigit kiem tra choice co la so khong
	while not choice.isdigit() or int(choice) > max_ or int(choice) < min_:
		choice = input(promp)
	choice = int(choice)
	return choice

# Nhap input dung theo yeu cau, input phai trung voi lua chon cho truoc
def dap_an_hop_le(promp, array):
	choice = input(promp)
	while choice not in array:
		choice = input(promp)
	return choice

# Nhap dap an theo thu tu tu cau 1 den cau cuoi cung
# Tra ve dap an da nhap
def nhap_dap_an(tat_ca_cau):
	print("NHAP DAP AN CUA BAN")
	tat_ca_dap_an = []
	so_cau = len(tat_ca_cau)
	for i in range(so_cau):
		# Dap an nhap vao chi co the la A, B, C, D, ""
		dap_an = dap_an_hop_le("Cau " + str(i+1) + ": ", ["A", "B", "C", "D", ""])
		if (dap_an == ""):
			dap_an = "None"
		tat_ca_dap_an.append(dap_an)
	return tat_ca_dap_an

# Hien thi cac dap an da nhap
def hien_dap_an(tc_dap_an):
	print("DAP AN BAN DA NHAP LA:")
	tat_ca_dap_an = len(tc_dap_an)
	for i in range(tat_ca_dap_an):
		print("Cau " + str(i+1) + ": " + tc_dap_an[i])

# Sua dap an thi sinh
# Tra lai mang cac dap an moi
def sua_dap_an(tc_dap_an):
	tat_ca_cau = len(tc_dap_an)
	choice = lua_chon_so("Ban muon sua dap an cau nao???(1-" +str(tat_ca_cau) + "): ", 1, tat_ca_cau )
	dap_an_moi = dap_an_hop_le("Nhap dap an moi: ", ["A", "B", "C", "D"])
	tc_dap_an[choice - 1] = dap_an_moi
	return tc_dap_an

# Luu dap an(bai lam), bao gom ca diem bai thi cua thi sinh vao file luu_ket_qua.txt
def luu_dap_an(sinh_vien):
	with open("luu_ket_qua.txt", "a", encoding="utf8") as file:
		file.write(sinh_vien.ho_ten + "\n")
		file.write(sinh_vien.mssv + "\n")
		file.write(sinh_vien.lop + "\n")
		for i in range(len(sinh_vien.tc_dap_an)):
			if sinh_vien.tc_dap_an[i] == "None":
				file.write("-" + " ")
			else:
				file.write(sinh_vien.tc_dap_an[i] + " ")
		file.write("\n")
		for i in range(len(sinh_vien.tc_dap_an)):
			file.write(sinh_vien.tc_dap_an_dung[i] + " ")
		file.write("\n")
		file.write(str(sinh_vien.diem) + "\n")

# Thuc hien tinh diem theo dap an
# Tra ve diem cua bai lam
def tinh_diem(tc_dap_an, tc_dap_an_dung):
	diem = 0
	so_cau = len(tc_dap_an)
	# So diem duoc tinh cho moi cau dung
	don_vi = round(10/so_cau, 2)
	for i in range(len(tc_dap_an)):
		if tc_dap_an[i] == tc_dap_an_dung[i]:
			diem += don_vi

	return diem

# Hien thi ket qua bai lam thi sinh sau khi luu
def hien_thi_ket_qua(sinh_vien):
	print("-------------------------------")
	print("KET QUA BAI KIEM TRA CUA BAN:")
	print("Ho va ten      :", end = " ")
	print(sinh_vien.ho_ten)
	print("Ma so sinh vien: ", end = " ")
	print(sinh_vien.mssv)
	print("Lop            :", end = " ")
	print(sinh_vien.lop)
	print("Diem           :", end = " ")
	print(sinh_vien.diem)
	print("-------------------------------")

# Hien thi cac tinh nang thi sinh co the chon de lam bai	
def show_menu():
	print("________________________________________")
	print("|1: Hien thi bai lam 				  |")
	print("|2: Sua dap an                         |")
	print("|3: Sua thong tin sinh vien            |")
	print("|4: Luu dap an (chi duoc luu mot lan)  |")
	print("________________________________________")

# Chuong trinh chinh
def main():
	kiem_tra = None
	print("****************DE BAI****************")
	print("_____________________________________________________________________")
	# Cau lenh try except kiem tra loi doc file "cau_hoi.txt"
	try:
		tat_ca_cau = doc_file()
		kiem_tra = kiem_tra_cau_hoi(tat_ca_cau)
	except:
		print("Kiem tra lai file cau_hoi.txt")
	# De sinh ngau nhien dat yeu cau
	if kiem_tra == True:
		tat_ca_dap_an_dung = xao_tron_cau(tat_ca_cau)
		print("_____________________________________________________________________")
		print("NHAP THONG TIN SINH VIEN")
		ho_ten, mssv, lop = nhap_thong_tin_ca_nhan()
		tat_ca_dap_an = nhap_dap_an(tat_ca_cau)
		diem = tinh_diem(tat_ca_dap_an, tat_ca_dap_an_dung)
		sinh_vien = SinhVien(ho_ten, mssv, lop, tat_ca_dap_an, tat_ca_dap_an_dung, diem)

		while True:
			show_menu()
			input("Enter to continue")
			choice = lua_chon_so("Chon mot tinh nang de lam bai(1-4):", 1, 4)
			# Hien thi bai lam 
			if choice == 1:
				print("______________________________________________________________")
				in_thong_tin_ca_nhan(sinh_vien)
				hien_dap_an(tat_ca_dap_an)
				input("Enter to continue")
			# Sua dap an
			elif choice == 2:
				tat_ca_dap_an = sua_dap_an(tat_ca_dap_an)
				diem = tinh_diem(tat_ca_dap_an, tat_ca_dap_an_dung)
				sinh_vien = SinhVien(ho_ten, mssv, lop, tat_ca_dap_an, tat_ca_dap_an_dung, diem)
				print("DAP AN SAU KHI SUA")
				hien_dap_an(tat_ca_dap_an)
				input("Enter to continue")
			# Sua thong tin sinh vien
			elif choice == 3:
				sinh_vien = sua_thong_tin_ca_nhan(sinh_vien)
			# Luu dap an (chi duoc luu mot lan)
			else:
				lua_chon = dap_an_hop_le("Ban co chac chan muon luu? Yes or No(y, n, Y, N): ", ["y", "Y", "n", "N"])
				if lua_chon == "Y" or lua_chon == "y":
					luu_dap_an(sinh_vien)
					hien_thi_ket_qua(sinh_vien)
					break
				if lua_chon == "n" or lua_chon == "N":
					continue
	# De sinh ngau nhien khong dat yeu cau
	if kiem_tra == False:
		print("Kiem tra lai file cau_hoi.txt da day du thong tin de bai chua")
	
main()