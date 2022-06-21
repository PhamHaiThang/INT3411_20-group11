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
Ở đây sử dụng biến day_time để lưu giờ hiện tại trong ngày. Sau đó, biến sẽ được so sánh với các mốc giờ trong ngày để đưa ra lời chào. <br>



https://user-images.githubusercontent.com/48849879/174858550-247ea182-0526-472e-bf69-3f00302fb1f9.mp4


 <br>


**6. Chức năng hiển thị các khả năng của trợ lý ảo**<br>
![image](https://user-images.githubusercontent.com/48849879/174855360-f6946758-d6ed-4559-ac7b-9b9c28fbf45d.png)<br>
Hàm đọc lại 6 chức năng mà trợ lý ảo có thể thực hiện được phòng khi người sử dụng chưa biết công dụng của trợ lý ảo.<br>



https://user-images.githubusercontent.com/48849879/174858714-441c4536-26fe-4453-9949-dee57f5fb21d.mp4


 <br>


**7. Chức năng cảm ơn + kết thúc**<br>
Đây là hàm sử dụng để giao tiếp cơ bản với bot. <br>


https://user-images.githubusercontent.com/48849879/174857019-b8b7e6ac-efd1-46a5-90ed-4ec1cc7bd115.mp4


**8. Chức năng hiển thị thời gian**<br>
![image](https://user-images.githubusercontent.com/48849879/174854854-fb413df9-1060-43fa-a286-4c2e8350e97a.png)<br>
 Sử dụng thư viện datetime để lưu thông tin thời gian tại thời điểm hiện tại trong ngày rồi lưu vào biến now.


https://user-images.githubusercontent.com/48849879/174858870-030b45d2-0400-43fa-b730-3c31a24fca90.mp4



 <br>


**9. Chức năng mở ứng dụng hệ thống, website và chức năng tìm kiếm từ khóa trên Google**<br>
![image](https://user-images.githubusercontent.com/48849879/174857474-c83ad097-c0a7-4686-9dfc-e1c74e314337.png)<br>
Khi xuất hiện các từ khóa đặc biệt như google hay word hay excel trong text thì dùng hàm os.startfile() để mở các file ứng dụng từ hệ thống. <br>
Chỉ kiểm tra từ google hay word hay excel trong text là chưa đủ. Cần giới hạn ngữ nghĩa của text ở trong hàm assistant để bot có thể hiểu là mở chương trình Google Chrome, Word, Excel chứ không nhầm lẫn với các chức năng khác.<br>
![image](https://user-images.githubusercontent.com/48849879/174857577-9b5ad4a6-c311-4810-a411-a8fe13fd69c2.png)<br>
Sử dụng hàm re.search() (Hàm tìm kiếm trong biểu thức chính quy Regular Expression) để tách phần domain sau chữ "mở" trong text rồi ghép với phần tiền tố "https://www." để tạo thành đường dẫn url của web. Sau đó, sử dụng webbroser.open(url) để mở trang web mình yêu cầu.<br>
Nếu domain được hàm re.search() tìm thấy thì sẽ thực hiện chức năng mở website và hàm open_website được trả về giá trị là True, còn nếu domain không được tìm thấy thì sẽ không thực hiện chức năng gì cả và hàm open_website trả về giá trị là False.<br>


https://user-images.githubusercontent.com/48849879/174858895-018dd46c-d8ae-40e7-a406-2f325d26463d.mp4



 <br>


**10. Chức năng tìm định nghĩa trên từ điển wikipedia**<br>
![image](https://user-images.githubusercontent.com/48849879/174859053-3b5711cd-6bb9-4dff-b4be-841aed782e76.png)<br>
Hàm tìm kiếm của thư viện wikipedia sẽ tìm kiếm chủ đề được yêu cầu và trích xuất 500 ký tự đầu tiên (nếu không chỉ định giới hạn, bot sẽ đọc toàn bộ trang). Wikipedia là một thư viện Python giúp dễ dàng truy cập và phân tích dữ liệu từ Wikipedia.<br>

Đầu tiên sử dụng hàm get_text() để lấy thông tin về thứ mình muốn định nghĩa rồi lưu vào biến text.<br>

Sau đó, gọi hàm wikipedia.summary(text).split('\n') để lưu lại thành một list các đoạn nội dung mà wikipedia tìm kiếm được.<br>

Tiếp theo, đọc đoạn định nghĩa đầu tiên. Nếu có yêu cầu đọc thêm các nội dung sau thì mình phải yêu cầu là "có" còn nếu không yêu cầu thì trợ lý ảo sẽ dừng đọc nội dung trong phần contents.<br>


https://user-images.githubusercontent.com/48849879/174859262-d10936a7-310e-43fe-b558-b96323985bce.mp4


<br>

**11. Chức năng phát nhạc trên Youtube**<br>
![image](https://user-images.githubusercontent.com/48849879/174859378-b69db1f5-594b-48b8-b3fa-40676f4d563c.png)<br>
Gọi hàm get_text() để lấy thông tin tên bài hát muốn phát rồi lưu vào biến mysong.<br>

Gọi vòng While là vì thực hiện tìm kiếm sử dụng mạng Internet nên sẽ có lúc kết nối yếu không tìm thấy. Chạy While True khi nào tìm thấy thì thôi.<br>

Biến url lưu đường dẫn đến kết quả đầu tiên khi tìm kiếm trên Youtube. Dùng hàm webbrowser.open(url) mở đường dẫn url đến video vừa được tìm kiếm trên Google Chrome để phát nhạc.<br>


https://user-images.githubusercontent.com/48849879/174859554-59815228-f76d-4cc9-b4e4-4bbb7d4fe2f9.mp4


<br>





