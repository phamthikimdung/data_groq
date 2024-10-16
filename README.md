# Xây Dựng Công Cụ Trợ Giúp Phân Tích Dữ Liệu VÀ CHAT PDF (DA_GROQ)

## Giới Thiệu

Tôi sẽ xây dựng một công cụ phân tích và chat với dữ liệu hữu ích và tiện lợi tên là **DA_GROQ** (Data Analysis GROQ). Công cụ này sử dụng các mô hình ngôn ngữ lớn (LLMs) để hỗ trợ việc thao tác và phân tích dữ liệu thông qua giao diện đàm thoại. Dự án này sử dụng Python, Langchain, Streamlit, PyGWalker, và GROQ API để tạo ra một ứng dụng web tương tác, cho phép người dùng tải lên dữ liệu, đặt câu hỏi, khám phá dữ liệu và nhận được các phân tích chi tiết.
## TỔNG QUAN
## Data Visualization
![vs_data](https://github.com/user-attachments/assets/92c93ff9-50b9-4721-b913-2d35db037a98)

![data](https://github.com/user-attachments/assets/e90b2d4a-24c5-46b7-ae0f-a99d1e58bdb7)
## Data Analysis 
![data_csv](https://github.com/user-attachments/assets/a5a38a31-ec36-45fc-b440-709c1f0c189b)
## Chat_PDF
![chat_pdf](https://github.com/user-attachments/assets/9b33c9f1-56eb-47e9-910b-ba4afd8d0893)
## VIDEO DEMO
https://github.com/user-attachments/assets/0d269c1f-67d4-45dc-8ce2-1e4e0dadfb66
## Nội Dung

### 1. Giới Thiệu về DA_GROQ

**Tổng quan:**  
DA_GROQ là một công cụ phân tích dữ liệu sử dụng các mô hình ngôn ngữ lớn để hỗ trợ các tác vụ phân tích và thao tác dữ liệu qua giao diện đàm thoại.

**Tính năng:**
- **Tải lên tệp CSV và PDF:** Dễ dàng tải lên dữ liệu CSV và PDF qua thanh bên.
- **Phân tích dữ liệu:** Nhập các truy vấn về dữ liệu và nhận phản hồi được hỗ trợ bởi LLMs.
- **Trực quan hóa dữ liệu:** Tạo và hiển thị các biểu đồ dựa trên các truy vấn dữ liệu.
- **Công cụ trực quan hóa tương tác:** Khám phá dữ liệu một cách tương tác bằng cách sử dụng các biểu đồ tùy chỉnh.

### 2. Công Cụ và Gói Cần Thiết

- **Python 3.9 hoặc cao hơn:** Ngôn ngữ lập trình chính để phát triển ứng dụng.
- **Langchain:** Khung phát triển ứng dụng sử dụng các mô hình ngôn ngữ lớn.
- **Streamlit:** Khung ứng dụng mã nguồn mở cho các dự án Machine Learning và Khoa học dữ liệu.
- **Pygwalker:** Công cụ tạo trực quan hóa tương tác.
- **GROQ API (tùy chọn):** Sử dụng để truy cập các mô hình ngôn ngữ tiên tiến.

### 3. Hướng Dẫn Chi Tiết

#### Bước 1: Thiết Lập Cơ Bản
1. Xây dựng cấu trúc dự án.
2. Thiết lập môi trường ảo.
3. Cài đặt các gói cần thiết.
4. Thiết lập kho lưu trữ Git để lưu trữ mã nguồn dự án.

#### Bước 2: Xây Dựng Công Cụ "Chat Với Dữ Liệu"
1. Sử dụng Streamlit để xây dựng giao diện người dùng.
2. Sử dụng các bộ công cụ của Langchain để xây dựng công cụ phân tích dữ liệu.
3. Sử dụng mô hình GPT của GROQ.

#### Bước 3: Xây Dựng Công Cụ Trực Quan Hóa Tương Tác
1. Nhúng Pygwalker vào giao diện Streamlit để xây dựng công cụ trực quan hóa tương tác.

### 4. Kết Luận

Với khả năng của LLMs, việc viết một ứng dụng thực hiện các tác vụ phân tích dữ liệu phức tạp hàng ngày trở nên rất dễ dàng.  
Sử dụng Streamlit giúp dễ dàng xây dựng giao diện đàm thoại và các khả năng trực quan hóa mạnh mẽ, làm cho việc phân tích dữ liệu trở nên dễ tiếp cận hơn với mọi người.  
Pygwalker là một công cụ miễn phí và hữu ích thay thế cho Tableau và có thể được nhúng vào ứng dụng của chúng ta.  
Bằng cách làm theo hướng dẫn này, mọi người có thể tự xây dựng công cụ phân tích dữ liệu của riêng mình, tận dụng sức mạnh của LLMs và Streamlit.

## Liên Hệ

Nếu có bất kỳ câu hỏi hoặc góp ý nào, liên hệ với mình qua email: [phamthikimdung.it@gmail.com](mailto:phamthikimdung.it@gmail.com).

## Liên Kết Hữu Ích

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Langchain Documentation](https://langchain.readthedocs.io/)
- [Pygwalker Documentation](https://pygwalker.github.io/)
- [HuggingFace Embeddings](https://huggingface.co/docs/transformers/embeddings)
- [PyPDFLoader](https://pypdfloader.readthedocs.io/)
- [FAISS](https://faiss.ai/)
- [GROQ API](https://groq.com/docs/api)

## Phụ Lục: Cách Thiết Lập Khóa API của GROQ

### Đăng Ký / Đăng Nhập vào GROQ

1. Truy cập trang web [GROQ](https://groq.com/) và tạo tài khoản hoặc đăng nhập nếu bạn đã có tài khoản.

### Đi tới API Keys

1. Sau khi đăng nhập, vào phần **API** trong bảng điều khiển tài khoản của bạn. Thường phần này nằm dưới tab "API Keys".

### Tạo Khóa API Mới

1. Nhấn vào nút **"Create new secret key"**. Hệ thống sẽ tạo một khóa API mới cho bạn.

### Sao Chép Khóa API

1. Sau khi khóa được tạo, hãy sao chép nó và thay thế khóa API trong tệp `.env` của dự án.

Để biết thêm chi tiết, hãy truy cập [GROQ](https://groq.com/docs/api).
