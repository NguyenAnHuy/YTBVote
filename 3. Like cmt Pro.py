		# Like video
		# driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
		# sleep(3)

		# Like comment top
		# driver.find_elements_by_id('like-button')[1].click()
		# sleep(2)

		# Chọn kênh
		# driver.find_elements_by_id('channel-title')[2].click()
		# sleep(0.5)
		# driver.find_element_by_id('img').click()
		# sleep(0.5)
		# driver.find_elements_by_id('right-icon')[3].click()
		# sleep(0.5)
		# driver.find_elements_by_id('channel-title')[3].click()

	# for i in range(0,10):
		
	# 	random_decimal_1 = random.randint(110,130)/100
	# 	random_decimal_2 = random.randint(50,60)/100
	# 	if i ==0:
	# 		driver.find_element_by_id('img').click()
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('contentIcon')[i+1].click()		# Click vào từng acc
	# 		sleep(random_decimal_1)
	# 		driver.find_elements_by_id(key)[1].click()
	# 		sleep(random_decimal_1)
	# 	else:
	# 		driver.find_element_by_id('img').click()
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('contentIcon')[i].click()		# Click vào từng acc
	# 		sleep(random_decimal_1)
	# 		driver.find_elements_by_id(key)[1].click()
	# 		sleep(random_decimal_1)

	# user_path=""
	# # Trả về tên các thư mục trong Forder: Profile chrome
	# folders_profile_chrome = os.listdir(os.getcwd() + '\\Profile chrome\\')
	# #print(folders_profile_chrome)

from selenium import webdriver
from time import sleep
from tkinter import *
# Thư viện khai báo combobox
from tkinter import ttk
import random

# Thư viện hàm lấy đường dẫn thư mục hiện hành
# import os
# Thư viện lấy hàm đường dẫn thư mục gốc
from pathlib import Path

root = Tk()
root.wm_title("❤ Mai mông to ❤")
root.geometry('480x480')


#key=""
#user_path=""


def program():
	for i in range(9,15):
		try:
			global driver
			profile_number='Profile'+' '+str(i)
			print(profile_number)
			chrome_driver_path = str(Path().absolute()) + '\\driver offline\\chromedriver.exe'
			chrome_options = webdriver.ChromeOptions()

			#chrome_options.add_argument(r"--user-data-dir=D:\An Huy\My Project Offline\YTB comunity\User Data")
			chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data')
			chrome_options.add_argument(r'--profile-directory='+profile_number)
			#Chế độ chạy ẩn_ ko thấy like được
			#chrome_options.headless = True
			driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)

			sleep(1)
			current_url = etr_link_cmt.get()
			driver.get(etr_link_cmt.get())
			sleep(2)

			Action_cmt()
			driver.quit()
			sleep(1.5)
		except:
			driver.quit()
	lbl_link_cmt.configure(text="SUCCESS!")


def Action_cmt():
	# #chrome_driver_path = r'C:\Users\Huy\Desktop\Backup\Python\My project\driver\chromedriver.exe'
	# # Lấy đường dẫn thư mục gốc của file py
	# chrome_driver_path = str(Path().absolute()) + '\\driver\\chromedriver.exe'	# Dòng lệnh này trả về kết quả là đường dẫn chỉ có 1 dấu " \ "
	# #print(chrome_driver_path)
	# chrome_options = webdriver.ChromeOptions()
	# #prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting_values.images" : 2}	#Gộp lại để vừa tắt thông báo vừa tắt ảnh
	# #chrome_options.add_experimental_option("prefs",prefs)


	# # #chrome_options.add_argument("user-data-dir=C:\\Users\\Huy\\Desktop\\Backup\\Python\\My project\\Profile chrome\\Profile chrome 1") # ko thêm r phía trước được. Ko chọn đc profile, mở profile gần nhất
	# # chrome_driver_dir = str(Path().absolute()) + '\\Profile chrome\\Profile chrome 1'
	# # print(chrome_driver_dir)
	# # chrome_options.add_argument('user-data-dir='+chrome_driver_dir)
	# # # Ghép vào thành chuỗi "user-data-dir=C:\Users\Huy\Desktop\Backup\Python\My project\Profile chrome\Profile chrome 1"
	# # print('user-data-dir='+chrome_driver_dir)

	# #chrome_options.add_argument(user_path)
	# chrome_options.add_argument(r"--C:\Users\Huy\AppData\Local\Google\Chrome\User Data")
	# chrome_options.add_argument(r'--profile-directory='+Profile_number)



	# driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
	# current_url = etr_link_cmt.get()
	# driver.get(etr_link_cmt.get())
	# sleep(2)
	# #driver.execute_script("window.scrollTo(0, 100);")
	# #sleep(2)


	for i in range(0,10):
		random_decimal_1 = random.randint(110,130)/100
		random_decimal_2 = random.randint(50,60)/100
		random_decimal_3 = random.randint(20,30)/100
		if i ==0:
			driver.find_element_by_id('img').click()
			sleep(random_decimal_3)
			try:
				driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
				sleep(random_decimal_2)
			except:
				#print("Không hiện List account, đóng trình duyệt sau 5s")
				sleep(5)
				driver.quit()
			try:
				driver.find_elements_by_id('contentIcon')[i+1].click()		# Click vào từng acc
			except IndexError:
				sleep(3)
				driver.find_elements_by_id('contentIcon')[i+1].click()
			sleep(random_decimal_1)
			driver.find_elements_by_id(key)[1].click()
			sleep(random_decimal_3)
		else:
			driver.find_element_by_id('img').click()
			sleep(random_decimal_3)
			try:
				driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
				sleep(random_decimal_2)
			except:
				#print("Không hiện List account, đóng trình duyệt sau 5s")
				sleep(5)
				driver.quit()
			try:
				driver.find_elements_by_id('contentIcon')[i].click()		# Click vào từng acc
			except IndexError:
				sleep(3)
				driver.find_elements_by_id('contentIcon')[i].click()
			sleep(random_decimal_1)
			try:
				driver.find_elements_by_id(key)[1].click()
			except IndexError:
				sleep(3)
				driver.find_elements_by_id(key)[1].click()
			sleep(random_decimal_3)


def open_browser():
	try:
		chrome_driver_path = str(Path().absolute()) + '\\driver offline\\chromedriver.exe'
		chrome_options = webdriver.ChromeOptions()
		#chrome_options.add_argument('user-data-dir=C:\\Users\\Huy\\AppData\\Local\\Google\\Chrome\\User Data') # ko thêm r phía trước được. Ko chọn đc profile, mở profile gần nhất
		# prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting_values.images" : 2}	#Gộp lại để vừa tắt thông báo vừa tắt ảnh
		# chrome_options.add_experimental_option("prefs",prefs)
		chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data')
		chrome_options.add_argument(r'--profile-directory='+cbx_test.get())
		driver2 = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
		sleep(1)
		driver2.get("https://www.youtube.com/")
		time_value=int(etr_time_value.get())
		sleep(time_value)
		driver2.quit()
	except ValueError:
		driver2.quit()
	# else:
	# 	print("Thực hiện nếu không phát sinh lỗi trong khối try")
	# finally:
	# 	print("Luôn thực hiện dù trong khối try có phát sinh lỗi hay không")


def Like_cmt():
	global key
	key="like-button"
	program()

def Diss_cmt():
	global key
	key="dislike-button"
	program()



# Group1 Frame --------------------------------------------Tạo 1 khung chung
group1 = LabelFrame(root, text="Youtube community", padx=5, pady=5)
group1.grid(row=0, column=0, padx=10, pady=10, sticky=E+W+N+S)

lbl_link_cmt = Label(group1, text = "Link comment: ")
lbl_link_cmt.grid(row = 0, column = 0, sticky=W+E)		#Vị trí của tiêu đề và Căn lề theo phía Tây hay bên trái
etr_link_cmt = Entry(group1, width = 55)
etr_link_cmt.grid(row = 1, column = 0, sticky=W)


# Group2 Frame ----------------------------------------------------
group2 = LabelFrame(root, text="Action", padx=5, pady=5)
group2.grid(row=0, column=2, padx=10, pady=10, sticky=E+W+N+S)


btn_like = Button(group2,text="Like", command=Like_cmt, height=1)	#columnspan là độ rộng của nút
btn_like.grid(row=0, column=2, columnspan=1, sticky = W+E)			#Căn đều ra giữa

btn_diss_like = Button(group2,text="Diss Like", command=Diss_cmt, height=1)			#columnspan là độ rộng của nút
btn_diss_like.grid(row=1, column=2, columnspan=1, sticky = W+E)			#Căn đều ra giữa


# Group3 Frame --------------------------------------------Tạo 1 khung chung
group3 = LabelFrame(root, text="Open browser", padx=5, pady=5)
group3.grid(row=3, column=0, padx=10, pady=10, sticky=E+W+N+S)

list_profile = ['Profile 9', 'Profile 10', 'Profile 11','Profile 12','Profile 13','Profile 14']
cbx_test = ttk.Combobox(group3, values=list_profile, width = 20,state="readonly")		#Chỉ có thể chọn trong danh sách, ko thể điền 
cbx_test.current(0)
cbx_test.grid(row = 3, column = 0, sticky=W+N)

lbl_time_value = Label(group3, text = "Time Value: ")
lbl_time_value.grid(row = 3, column = 1, sticky=E+W+N+S)		#Vị trí của tiêu đề và Căn lề theo phía Tây hay bên trái
etr_time_value = Entry(group3, width = 10)
etr_time_value.grid(row = 3, column = 2, sticky=E)

btn_open = Button(root,text="Open", command=open_browser, width = 6, height=1)
btn_open.grid(row=3, column=2, columnspan=2)

root.mainloop()