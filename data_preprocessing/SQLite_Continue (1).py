import sqlite3
import pandas as pd

try:
    n = int(input("Nhập số lượng khách hàng muốn lấy (top n): "))

    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    query = """
    SELECT 
        c.CustomerId,
        c.FirstName || ' ' || c.LastName AS CustomerName,
        COUNT(i.InvoiceId) AS TotalOrders
    FROM Customer c
    JOIN Invoice i 
        ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId, CustomerName
    ORDER BY TotalOrders DESC
    LIMIT ?;
    """

    cursor.execute(query, (n,))

    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["CustomerId", "CustomerName", "TotalOrders"])
    print(df)

    cursor.close()

except sqlite3.Error as error:
    print('Error occurred - ', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
#%%

import sqlite3
import pandas as pd

try:
    # Nhập số lượng khách hàng muốn lấy
    n = int(input("Nhập số lượng khách hàng muốn lấy (top n): "))

    # Kết nối DB và tạo cursor
    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Câu truy vấn: tính tổng Total của mỗi khách hàng
    query = """
    SELECT 
        c.CustomerId,
        c.FirstName || ' ' || c.LastName AS CustomerName,
        SUM(i.Total) AS TotalAmount
    FROM Customer c
    JOIN Invoice i 
        ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId, CustomerName
    ORDER BY TotalAmount DESC
    LIMIT ?;
    """

    # Thực thi truy vấn với tham số n
    cursor.execute(query, (n,))

    # Lấy dữ liệu và chuyển thành DataFrame có tên cột
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["CustomerId", "CustomerName", "TotalAmount"])
    print(df)

    # Đóng cursor
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred - ', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
