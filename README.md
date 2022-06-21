# [INT3411_20 group 11: Trợ lý ảo Tiếng Việt](name)
Members: <br> **Nguyễn Văn Quang-18021052** (50%) <br>
         **Phạm Hải Thắng-18021139** (50%)
         
## [Introduction](#introduction)
**Trợ lý ảo Tiếng Việt** được lấy cảm hứng từ những assistant bots như Alexa, Siri, Google Assistant,... Hệ thống trợ lý ảo này là chương trình ứng dụng được viết hoàn toàn bằng **Python** và được thiết kế để hiểu các lệnh thoại bằng ngôn ngữ tự nhiên và thực hiện các tác vụ cho người dùng. Các tác vụ này bao gồm đọc tin nhắn văn bản hoặc địa chỉ email, tìm kiếm số điện thoại, lên lịch, đặt cuộc gọi điện và nhắc nhở người dùng cuối về các cuộc hẹn. <br> <br>
**Các chức năng chính**
- Nhận diện giọng nói (tiếng việt) <br>
- Hỏi đáp về thông tin bot <br>
- Hỏi bot về các chức năng bot có thể làm <br>
- Hỏi bot về thời gian <br>
- Hỏi bot tìm kiếm thông tin trên wikipedia <br>
- Hỏi bot để bật nhạc trên youtube <br>
- Hỏi bot để mở trang web theo yêu cầu <br>
- Đối thoại với bot <br>

## [Cài đặt](data)
**Yêu cầu:** Python 3.6 trở xuống (Python version > 3.6 có thể gặp lỗi khi cài đặt một số thư viện) <br>
**Thư viện:**
- **speech_recognition**: Nhận dạng giọng nói
- **time, datetime**: Xử lý thời gian
- **wikipedia**: Tìm kiếm trên từ điển wikipedia
- **webbrowser, selenium, webdriver_manager, urllib**: Truy cập web, trình duyệt (Chrome)
- **gTTS**: Chuyển văn bản thành âm thanh của Google (Chị Google)
- **requests**: Crawl thông tin từ web
- **smtplib**: Gửi Email bằng giao thức SMTP
- **re**: Biểu thức chính quy (Regular Expression) 
- **os, sys, ctypes**: Truy cập, xử lý file hệ thống
- **playsound**: Phát âm thanh từ file mp3
- **json**: Xử lý kiểu dữ liệu JSON
- **youtube_search**: Tìm kiếm video trên Youtube

## [Demo](demo)
**1. Import các thư viện cần thiết** <br>
![image](https://user-images.githubusercontent.com/48849879/174769290-9126649c-b1a4-4f7f-aa31-6550bfdac816.png) <br>
Với mỗi chức năng mà trợ lý ảo thực hiện sẽ đại diện bằng một hàm. Mỗi hàm có thể trả về giá trị hoặc chỉ thực hiện lệnh tùy theo chức năng của nó. <br> <br>
**2. Khai báo biến mặc định** <br>
![image](https://user-images.githubusercontent.com/48849879/174769575-a8557d7e-90db-4957-8ec5-a9401b84daf9.png) <br>
Các thư viện được sử dụng ở trên đều rất phổ thông, tích hợp nhiều hàm xử lý. <br> <br>
**3. Chức năng chuyển văn bản thành âm thanh** <br>
![image](https://user-images.githubusercontent.com/48849879/174769909-30e205c8-a6eb-4f9e-8d16-f13c82f8842d.png) <br>
Chức năng đầu tiên cần là chuyển một đoạn văn bản thành âm thanh và đọc nó lên trên máy tính. <br>
Ta sử dụng hàm gTTS (google Text To Speech) để chuyển văn bản thành âm thanh theo ngôn ngữ nhận dạng tiếng việt rồi lưu về máy tính dữ liệu âm thanh dưới file sound.mp3. <br>
Sau đó, dùng hàm playsound.playsound() để đọc file sound.mp3 trên máy tính. <br>
Sau khi đọc xong, ta phải xóa file sound.mp3 để tránh lỗi khi đọc một đoạn văn bản khác thì cũng được lưu lại dưới file sound.mp3.<br> <br>
**4. Chức năng chuyển âm thanh thành văn bản**<br>
Đây là chức năng cơ bản thứ hai cùng với chức năng chuyển văn bản thành âm thanh. <br>
Trong chức năng này, ta sử dụng 2 hàm khác hỗ trợ là get_audio() và stop(). <br>
![image](https://user-images.githubusercontent.com/48849879/174770548-fd9b30d9-b5c6-4afe-befe-18a3d2330e66.png) <br>
Ở hàm trên, ta sử dụng thư viện speech_recognition (sr) có chức năng là nhận dạng giọng nói để chuyển âm thanh thành văn bản. Âm thanh được đọc vào microphone của máy tính sau đó được xử lý qua hàm listen của sr.Recognition rồi lưu dữ liệu âm thanh vào biến audio. Dữ liệu âm thanh audio thu được sẽ được nhận dạng ở ngôn ngữ tiếng việt trong hàm r.recognize_google để chuyển thành dạng văn bản rồi lưu dữ liệu vào biến text. <br>
Nếu dữ liệu âm thanh audio không lỗi tức là hàm r.recognize_google có thể nhận dạng được audio để chuyên thành text thì hàm get_audio() sẽ được trả về giá trị là text còn nếu dữ liệu audio bị lỗi mà hàm r.recognition_google không nhận dạng được thì hàm get_audio() sẽ được trả về giá trị là 0. <br>
![image](https://user-images.githubusercontent.com/48849879/174770582-884bb3e6-9162-4a21-b3af-369b3e842492.png) <br>
Hàm stop() đơn giản là đọc đoạn text "Hẹn gặp lại bạn sau" sử dụng hàm speak() ở trên. <br>
![image](https://user-images.githubusercontent.com/48849879/174771091-7c198ba1-4c05-47f9-98bf-7f3780881fb0.png) <br>
Hàm get_text() có chức năng là máy tính sẽ cố gắng nhận dạng âm thanh của người đọc tối đa 3 lần cho đến khi máy tính hiểu. <br><br>
**5. Chức năng giao tiếp, chào hỏi**<br>
![image](https://user-images.githubusercontent.com/48849879/174771371-2bfbea76-d1c5-41fc-a4d9-f8b7e05672a4.png) <br>
Nội dung chức năng này là để giao tiếp thông thường giữa người và máy tính. Đơn cử như: chào hỏi, hỏi thăm sức khỏe hay nói về thông tin trợ lý ảo. <br>
Ở đây sử dụng biến day_time để lưu giờ hiện tại trong ngày. Sau đó, biến sẽ được so sánh với các mốc giờ trong ngày để đưa ra lời chào. <br><br>





