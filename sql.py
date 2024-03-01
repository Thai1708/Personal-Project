import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port = 3306,
    user= 'root',
    password='Pthai332277@',
    database= 'test'
)
cursor = conn.cursor()

sql = 'INSERT IGNORE INTO Stg_ThongTin_raw(Web, Nganh, Link, TenCV, CongTy, TinhThanh, Luong, LoaiHinh, KinhNghiem, CapBac, HanNopCV, YeuCau, MoTa, PhucLoi, SoLuong) VALUES (%s, %s, %s, %s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s,%s)'

sql_link = 'SELECT Link FROM Stg_ThongTin_raw where Web =\'123jobs\''